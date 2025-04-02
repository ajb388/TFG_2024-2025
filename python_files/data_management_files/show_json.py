import pandas as pd
import matplotlib.pyplot as plt
import json
from datetime import datetime

# Cargar archivo JSON (formato lista completa)
with open("/app/json/central/cafeteria_central_smooth.json", "r", encoding="utf-8") as f:
    data = json.load(f)  # Not json.loads(line) — esto carga toda la lista a la vez

# Crear DataFrame
df = pd.DataFrame(data)

# Corregir secuencia de escape en fechas si es necesario
df['date'] = df['date'].str.replace('\\/', '/', regex=False)

# Crear datetime y filtrar entre 13:00 y 16:00
df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'], dayfirst=True)
df.set_index('datetime', inplace=True)
df_filtered = df.between_time("07:30", "19:50")

# Agrupar por hora:minuto y calcular la media
df_filtered['time_only'] = df_filtered.index.time
avg_volume = df_filtered.groupby('time_only')['volume'].mean()

# Graficar
plt.figure(figsize=(12, 6))
plt.plot([t.strftime("%H:%M") for t in avg_volume.index], avg_volume.values, marker='o')
plt.title('Media de volumen entre las 07:30 y las 19:50')
plt.xlabel('Hora')
plt.ylabel('Volumen medio')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("cafeteria_central.jpg")  # Guarda la gráfica
plt.show()
