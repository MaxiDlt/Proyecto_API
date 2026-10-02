import pandas as pd

from src.extract import extract
from src.transform import transform
from src.load import save_data


# Extract
data = extract()

# Transform
df = transform(data)

# Load
save_data(df)