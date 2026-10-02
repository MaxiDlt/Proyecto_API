import requests
# Sirve para que el codigo "duerma" y no saturar la API
import time

from src.config import API_BASE_URL



def extract():
    
    url = f"{API_BASE_URL}/products"
    
    for intento in range(3):
    
        try:
            
            # Hacemos la consulta a la API
            response = requests.get(url)
            
            # Si tira un error usamos esto para guardarlo
            response.raise_for_status()

            # Si la consulta a la API esta ok, arma el JSON
            return response.json()
        
         # Capturamos errores producidos por requests
        except requests.exceptions.RequestException:

            # Si ya estamos en el intento 3 volvemos a lanzar error
            if intento == 2:
                raise
        
            # Calculamos el tiempo de espera usando un exponencial
            espera = 2 ** (intento + 1)
        
            # Mostramos cuanto se va a esperar para intentar de nuevo
            print(f"Error. Reintentando en {espera} segundos...")
            
            time.sleep(espera)
            
            