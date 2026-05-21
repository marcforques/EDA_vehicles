import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def plot_graph(df: pd.DataFrame) -> None:
    
    df_plot = df.copy()

    # Se guardan los gráficos en la carpeta figures
    figures_path = Path(__file__).resolve().parent.parent / "figures"
    figures_path.mkdir(exist_ok=True)

    # GRÁFICO 1: distribución de precios
    if "price" in df_plot.columns:
        prices = df_plot[df_plot["price"].notna() & (df_plot["price"] > 0)]
        prices = prices[prices["price"] <= prices["price"].quantile(0.95)]

        plt.figure(figsize=(8, 5))
        plt.hist(prices["price"], bins=25)
        plt.title("Distribución de precios")
        plt.xlabel("Precio")
        plt.ylabel("Número de vehículos")
        plt.tight_layout()
        plt.savefig(figures_path / "01_distribucion_precios.png", dpi=120)
        plt.show()


    # GRÁFICO 2: marcas con más vehículos
    if "make" in df_plot.columns:
        top_marcas = df_plot["make"].value_counts().head(10).sort_values()

        plt.figure(figsize=(8, 5))
        plt.barh(top_marcas.index, top_marcas.values)
        plt.title("Top 10 marcas con más vehículos")
        plt.xlabel("Número de vehículos")
        plt.ylabel("Marca")
        plt.tight_layout()
        plt.savefig(figures_path / "02_top_marcas.png", dpi=120)
        plt.show()
        

    # GRÁFICO 3: precio medio por marca
    if "make" in df_plot.columns and "price" in df_plot.columns:
        precio_marca = (
            df_plot.groupby("make")["price"]
            .mean()
            .sort_values(ascending=False)
            .head(10)
            .sort_values()
        )

        plt.figure(figsize=(8, 5))
        plt.barh(precio_marca.index, precio_marca.values)
        plt.title("Top 10 marcas con mayor precio medio")
        plt.xlabel("Precio medio")
        plt.ylabel("Marca")
        plt.tight_layout()
        plt.savefig(figures_path / "03_precio_medio_marca.png", dpi=120)
        plt.show()
        

    # GRÁFICO 4: relación entre kilometros y precio
    if "mileage" in df_plot.columns and "price" in df_plot.columns:
        temp = df_plot[["mileage", "price"]].dropna()
        temp = temp[(temp["mileage"] <= temp["mileage"].quantile(0.95)) & (temp["price"] <= temp["price"].quantile(0.95))]

        plt.figure(figsize=(8, 5))
        plt.scatter(temp["mileage"], temp["price"], alpha=0.6)
        plt.title("Relación entre kilometraje y precio")
        plt.xlabel("Kilometraje")
        plt.ylabel("Precio")
        plt.tight_layout()
        plt.savefig(figures_path / "04_kilometraje_precio.png", dpi=120)
        plt.show()
        

    # GRÁFICO 5: precio medio según la edad del vehículo
    if "vehicle_age" in df_plot.columns and "price" in df_plot.columns:
        precio_edad = (
            df_plot.groupby("vehicle_age")["price"]
            .mean()
            .sort_index()
        )
        precio_edad = precio_edad[precio_edad.index <= 30]

        plt.figure(figsize=(8, 5))
        plt.plot(precio_edad.index, precio_edad.values, marker="o")
        plt.title("Precio medio según la edad del vehículo")
        plt.xlabel("Edad del vehículo")
        plt.ylabel("Precio medio")
        plt.tight_layout()
        plt.savefig(figures_path / "05_precio_edad.png", dpi=120)
        plt.show()


    # GRÁFICO 6: tipo de combustible
    if "fuel" in df_plot.columns:
        combustibles = df_plot["fuel"].value_counts().head(8).sort_values()

        plt.figure(figsize=(8, 5))
        plt.barh(combustibles.index, combustibles.values)
        plt.title("Vehículos por tipo de combustible")
        plt.xlabel("Número de vehículos")
        plt.ylabel("Combustible")
        plt.tight_layout()
        plt.savefig(figures_path / "06_combustible.png", dpi=120)
        plt.show()
        
    
