# API Pipeline - E-commerce Products

Pipeline de Data Engineering que consume datos de una API de e-commerce, los transforma con Python y Pandas, y los almacena en formato Parquet.

## Tecnologías

* Python
* Requests
* Pandas
* python-dotenv
* PyArrow
* DummyJSON API

## Estructura del proyecto

```text
Proyecto_API/
├── src/
│   ├── config.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
├── data/
│   └── products.parquet
├── .env
├── .gitignore
└── requirements.txt
```

## Setup

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd Proyecto_API
```

### 2. Crear el archivo `.env`

Crear un archivo `.env` en la raíz del proyecto:

```text
API_BASE_URL=https://dummyjson.com
```

### 3. Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

## Uso

Ejecutar el pipeline desde la raíz del proyecto:

```bash
python -m src.main
```

El pipeline realiza las siguientes etapas:

```text
API
 ↓
Extract
 ↓
Transform
 ↓
Load
 ↓
Parquet
```

### Extract

Obtiene los productos desde la API mediante una solicitud HTTP `GET`.

### Transform

Convierte los datos obtenidos en un DataFrame y realiza transformaciones sobre los productos.

Entre ellas:

* Conversión de `price` a formato numérico.
* Cálculo de `price_after_discount`.

### Load

Guarda los datos transformados en formato Parquet:

```text
data/products.parquet
```

## Output

Luego de ejecutar el pipeline, se genera:

```text
data/
└── products.parquet
```

El archivo contiene los productos obtenidos de la API junto con las transformaciones realizadas.

## Autor

Maxi
