import json

# Cargar el JSON original
with open("/app/tfg_project/knowledge/volumen_cafeteria_completo.json", "r") as f:
    data = json.load(f)

# Convertir cada `content` en texto plano
for doc in data["documents"]:
    if not isinstance(doc["content"], str):
        doc["content"] = json.dumps(doc["content"])  # Convertir JSON a string si no lo es

# Guardar el nuevo archivo corregido
with open("volumen_cafeteria_fixed.json", "w") as f:
    json.dump(data, f, indent=4)

print("Archivo corregido guardado como volumen_cafeteria_fixed.json")
