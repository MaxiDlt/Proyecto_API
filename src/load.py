import os
import pandas as pd

def save_data(df: pd.DataFrame, output_dir: str = "data"):
    
    # Creamos la carpeta si no existe
    os.makedirs(output_dir, exist_ok=True)
        
    # Guardamos los datos en un archivo parquet
    df.to_parquet(
        f"{output_dir}/products.parquet",
        index=False
        )
     
    # Mostramos cuantos productos guardamos
    print(f"Guardamos {len(df)} productos en {output_dir}/products.parquet")
    
    
    