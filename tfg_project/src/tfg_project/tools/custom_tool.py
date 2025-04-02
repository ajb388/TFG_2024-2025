import os
import requests
from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool

class GoogleMapsRouteInput(BaseModel):
    """Input schema for GoogleMapsRouteTool."""
    origin: str = Field(..., description="Lugar de origen dentro del campus")
    destination: str = Field(..., description="Lugar de destino dentro del campus")

class GoogleMapsRouteTool(BaseTool):
    name: str = "Google Maps Walking Directions Tool"
    description: str = (
        "Dada una pregunta del usuario sobre cómo llegar de un sitio a otro dentro del campus de la Universidad de Almería",
        "usa la API de Google Maps para obtener direcciones a pie entre dos ubicaciones dentro del campus de la Universidad de Almería. "
        "Devuelve duración, distancia, pasos clave de la ruta y un enlace directo a Google Maps."
    )
    args_schema: Type[BaseModel] = GoogleMapsRouteInput

    def _run(self, origin: str, destination: str) -> str:
        api_key = os.getenv("GOOGLE_MAPS_API_KEY")
        if not api_key:
            return "ERROR: Falta la variable de entorno GOOGLE_MAPS_API_KEY"

        # Aseguramos que se entienda el contexto del campus
        campus_suffix = "Universidad+de+Almería,+Almería,+España"
        # Reemplazamos espacios en blanco por "+"
        origin_formatted = origin.replace(" ", "+")
        destination_formatted = destination.replace(" ", "+")
        origin_full = f"{origin_formatted}" + f"+{campus_suffix}"
        destination_full = f"{destination_formatted}" + f"+{campus_suffix}"

        endpoint = "https://maps.googleapis.com/maps/api/directions/json"
        params = {
            "origin": origin_full,
            "destination": destination_full,
            "key": api_key,
            "mode": "walking",
            "language": "es",
            "units": "metric"
        }

        response = requests.get(endpoint, params=params)
        if response.status_code != 200:
            return f"ERROR: La solicitud falló con código {response.status_code}"

        data = response.json()
        if not data.get("routes"):
            return "No se encontró ninguna ruta a pie entre esos puntos del campus."

        route = data["routes"][0]
        leg = route["legs"][0]

        duration = leg["duration"]["text"]
        distance = leg["distance"]["text"]

        steps = []
        for step in leg["steps"]:
            instruction = step["html_instructions"].replace("<b>", "").replace("</b>", "")
            steps.append(f"- {instruction} ({step['distance']['text']})")

        # Enlace a Google Maps (con travelmode walking y en español)
        gmaps_url = (
            f"https://www.google.com/maps/dir/?api=1"
            f"&origin={origin_full}&destination={destination_full}&hl=es&travelmode=walking"
        )

        return (
            f"🚶 **Ruta a pie desde {origin} hasta {destination} (Campus UAL)**\n"
            f"- ⏱️ Tiempo estimado: {duration}\n"
            f"- 📏 Distancia total: {distance}\n\n"
            f"📍 **Pasos sugeridos:**\n" +
            "\n".join(steps) +
            f"\n\n🔗 Ver en Google Maps: {gmaps_url}"
        )

class GoogleMapsPlaceSearchInput(BaseModel):
    """Input schema for GoogleMapsPlaceSearchTool."""
    place_name: str = Field(..., description="Nombre del lugar a buscar dentro del campus")

class GoogleMapsPlaceSearchTool(BaseTool):
    name: str = "Google Maps Place Search Tool"
    description: str = (
        "Busca un lugar concreto dentro del campus de la Universidad de Almería usando la API Places de Google Maps."
        "Devuelve el nombre oficial, dirección, coordenadas y un enlace directo a Google Maps."
    )
    args_schema: Type[BaseModel] = GoogleMapsPlaceSearchInput

    def _run(self, place_name: str) -> str:
        api_key = os.getenv("GOOGLE_MAPS_API_KEY")
        if not api_key:
            return "❌ ERROR: Falta la variable de entorno GOOGLE_MAPS_API_KEY"

        url = "https://places.googleapis.com/v1/places:searchText"

        headers = {
            "Content-Type": "application/json",
            "X-Goog-Api-Key": api_key,
            "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.location,places.id"
        }
        place_name_replace = place_name.replace(" ", "+")
        # Contexto de búsqueda dentro del campus
        data = {
            "textQuery": f"{place_name_replace}, Universidad+de+Almería,+España",
            "languageCode": "es"
        }

        response = requests.post(url, headers=headers, json=data)
        if response.status_code != 200:
            return f"❌ ERROR {response.status_code}: {response.text}"

        resultado = response.json()
        lugares = resultado.get("places", [])

        if not lugares:
            return "⚠️ No se encontró ningún lugar con ese nombre dentro del campus."

        lugar = lugares[0]
        nombre = lugar["displayName"]["text"]
        direccion = lugar.get("formattedAddress", "Sin dirección disponible")
        lat = lugar["location"]["latitude"]
        lng = lugar["location"]["longitude"]
        maps_link = f"https://www.google.com/maps/search/?api=1&query={lat},{lng}"

        return (
            f"📍 **Lugar encontrado:** {nombre}\n"
            f"📫 Dirección: {direccion}\n"
            f"🌐 Coordenadas: {lat}, {lng}\n"
            f"🔗 [Ver en Google Maps]({maps_link})"
        )
