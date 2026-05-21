## Plantilla de README

### 1) Objetivo
- Analizar y visualizar un dataset de demostración para entender el proceso de limpieza de datos, construcción de características y generación de visualizaciones.

### 2) Dataset
- Fuente: vehicles_dataset.csv (kaggle)
- Nº filas/columnas: 1002/18
- Variables clave:
  - `price`: precio del vehículo
  - `make`: marca del vehículo
  - `model`: modelo del vehículo
  - `year`: año del vehículo
  - `mileage`: kilometraje
  - `fuel`: tipo de combustible
  - `transmission`: tipo de transmisión
  - `body`: tipo de carrocería

### 3) Preguntas
- Q1: ¿Cómo se distribuyen los precios de los vehículos?
- Q2: ¿Qué marcas tienen más vehículos en el dataset?
- Q3: ¿Qué marcas tienen el precio medio más alto?
- Q4: ¿Existe relación entre el kilometraje y el precio del vehículo?
- Q5: ¿Cómo cambia el precio medio según la edad del vehículo?
- Q6: ¿Qué tipos de combustible son más habituales en el dataset?

### 4) Data issues & fixess
Durante la limpieza se han corregigo varios problemas:

- Valores duplicados → Se eliminan filas repetidas.
- Valores faltantes → Se revisan las columnas con datos nulos.
- Precios incorrectos o igual a 0 → Se eliminan o filtran para no afectar al análisis.
- Formatos de texto inconsistentes → Se limpian columnas categóricas como marca, combustible o transmisión.
- Valores extremos → En algunos gráficos se limita el análisis al percentil 95 para evitar que valores muy altos deformen la visualización.
- Tipos de datos → Se revisan columnas numéricas como `price`, `mileage` y `year`.

### 5) Pipeline

- raw → clean → features → viz → export a `data/processed/`

1. Se carga el dataset original desde data/raw/.
2. Se limpian los datos.
3. Se crean nuevas variables.
4. Se generan gráficos.
5. Se guardan los resultados en data/processed/ y figures/.

### 6) Hallazgos
- Insight 1: En el gráfico de distribución de precios se observa que la mayoría de vehículos se concentran en precios bajos y medios.
- Insight 2: En el gráfico de marcas con más vehículos se ve que algunas marcas aparecen mucho más que otras dentro del dataset.
- Insight 3: El gráfico de la relación entre kilometraje y precio muestra que, en general, los vehículos con más kilómetros tienden a tener precios más bajos.
- Insight 4: El precio medio suele disminuir conforme aumenta la edad del vehículo.
- Insight 5: El gráfico de combustible permite ver cuáles son los tipos de combustible más frecuentes en el dataset.

### 7) Estructura del proyecto
```text
project/
├── main.py
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── eda.ipynb
├── src/
│   ├── __init__.py
│   ├── io.py
│   ├── cleaning.py
│   ├── config.py
│   ├── features.py
│   ├── viz.py
│   └── utils.py
├── README.md
├── .gitignore
└── requirements.txt
```

### 8) Cómo ejecutar
- `pip install -r requirements.txt`
- Ejecutar pipeline: `python main.py`
- (Opcional) Abrir y ejecutar: `notebooks/eda.ipynb`


