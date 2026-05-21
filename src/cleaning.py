import pandas as pd


def clean(df: pd.DataFrame) -> pd.DataFrame:
    
    df_cleaned = df.copy()
    
    # Se quitan posibles espacios en str
    text_columns = df_cleaned.select_dtypes(include="object").columns
    for col in text_columns:
        df_cleaned[col] = df_cleaned[col].astype("string").str.strip()
        df_cleaned[col] = df_cleaned[col].replace("", pd.NA)

    # Se fuerza que las columnas seleccionadas sean numéricas
    numeric_columns = ["year", "price", "mileage", "cylinders", "doors"]
    for col in numeric_columns:
        df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors="coerce")

    # Se eliminan los valores de precio negativos o sin precio ya que no nos servirá para el análisis
    df_cleaned = df_cleaned.dropna(subset=["price"])
    df_cleaned = df_cleaned[df_cleaned["price"] > 0]

    # Rellenar valores faltantes con el valor que más se repite 
    df_cleaned["mileage"] = df_cleaned["mileage"].fillna(df_cleaned["mileage"].median())
    df_cleaned["cylinders"] = df_cleaned["cylinders"].fillna(df_cleaned["cylinders"].median())
    df_cleaned["doors"] = df_cleaned["doors"].fillna(df_cleaned["doors"].median())

    # En texto, si falta algo, ponemos Unknown
    text_columns = df_cleaned.select_dtypes(include=["object", "string"]).columns
    for col in text_columns:
        df_cleaned[col] = df_cleaned[col].fillna("Unknown")

    return df_cleaned





