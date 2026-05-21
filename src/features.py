import pandas as pd


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    
    df_features = df.copy()

    # Se añade la edad aproximada del vehículo (Teniendo en cuenta que estamos en 2026)
    df_features["vehicle_age"] = 2026 - df_features["year"]

    # Se añade el kilometraje por año. Se añade un 1 para evitar divisiones entre 0
    df_features["mileage_per_year"] = df_features["mileage"] / (df_features["vehicle_age"] + 1)

    # Se añade una categoría de precio: bajo, medio o alto
    low_limit = df_features["price"].quantile(0.33)
    high_limit = df_features["price"].quantile(0.66)

    def price_group(price):
        if price <= low_limit:
            return "Bajo"
        elif price <= high_limit:
            return "Medio"
        else:
            return "Alto"

    df_features["price_level"] = df_features["price"].apply(price_group)

    return df_features