
import pandas as pd

def transform(raw_data: dict) -> pd.DataFrame:
    
    # Extraemos la lista de productos
    products = raw_data.get("products", [])
    
    # Convertimos los productos en un dataframe
    df = pd.DataFrame(products)
    
    # Si no hay datos devolvemos un dataframe vacio
    if df.empty:
        return df
    
    # Convertimos los precios a numerico
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    
    # Creamos una columna con el precio despues del descuento
    df["price_after_discount"] = (
        df["price"] * (1 - df["discountPercentage"] / 100)
        )

    return df