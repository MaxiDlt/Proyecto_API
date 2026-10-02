

# Extraer informacion de una API
import requests
import pandas as pd

# url de api
url = "https://dummyjson.com/products"

# Pido respuesta
response = requests.get(url)

# Si el codigo es 200 estamos ok
print(response.status_code)

#Extraigo la data en json
data = response.json()

# Veo la data
print(data)


df = pd.DataFrame(data['products'])

print(df)


# También se pueden poner parametros
params = {
    "q": "phone"
}

response = requests.get( "https://dummyjson.com/products/search", 
                        params = params)


# Extraigo los datos en JSON
data = response.json()
print(data)

# Convierto a DataFrame
df = pd.DataFrame(data['products'])

print(df)
