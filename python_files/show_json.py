import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_cafeteria_volume(json_file, selected_date):
    """
    Lee un archivo JSON con datos de la cafetería y genera una gráfica que muestra los picos de volumen para un día específico.

    :param json_file: Ruta al archivo JSON con los datos de la cafetería.
    :param selected_date: Fecha seleccionada para generar la gráfica (formato: dd/mm/yyyy).
    """
    try:
        # Verificar si el archivo existe y no está vacío
        if not os.path.exists(json_file):
            raise FileNotFoundError(f"El archivo {json_file} no fue encontrado. Verifica la ruta.")
        if os.path.getsize(json_file) == 0:
            raise ValueError(f"El archivo {json_file} está vacío.")

        # Cargar los datos desde el archivo JSON
        data = pd.read_json(json_file)

        # Validar que las columnas necesarias estén presentes
        required_columns = {'date', 'time', 'volume'}
        if not required_columns.issubset(data.columns):
            raise ValueError(f"El archivo JSON debe contener las columnas: {', '.join(required_columns)}.")

        # Filtrar los datos por la fecha seleccionada
        data = data[data['date'] == selected_date]
        if data.empty:
            raise ValueError(f"No hay datos disponibles para la fecha {selected_date}.")

        # Ordenar los datos por tiempo (por si no están ordenados)
        data.sort_values(by='time', inplace=True)

        # Crear la gráfica
        plt.figure(figsize=(12, 6))
        plt.plot(data['time'], data['volume'], label='Volumen de personas', linewidth=1.5)
        
        # Añadir títulos y etiquetas
        plt.title(f'Picos de Volumen en la Cafetería de Humanidades - {selected_date}', fontsize=14)
        plt.xlabel('Hora', fontsize=12)
        plt.ylabel('Volumen de Personas', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend()

        # Ocultar etiquetas del eje X
        plt.xticks([])

        # Mostrar la gráfica
        plt.tight_layout()
        plt.show()

    except ValueError as e:
        print(f"Error al procesar los datos del JSON: {e}")
    except FileNotFoundError as e:
        print(e)

def show_volume_plot():
    """
    Solicita al usuario un archivo JSON y una fecha, y muestra una gráfica con los datos.
    """
    json_file = input("Introduce la ruta al archivo JSON con los datos: ")
    selected_date = input("Introduce la fecha para generar la gráfica (formato: dd/mm/yyyy): ")
    plot_cafeteria_volume(json_file, selected_date)

# Ejemplo de uso
if __name__ == "__main__":
    show_volume_plot()
