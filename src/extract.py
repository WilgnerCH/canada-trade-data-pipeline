import pandas as pd

def download_data():

    print("Loading sample dataset...")

    data = {
        "YearMonth/AnnéeMois": ["202401", "202401"],
        "HS10": ["0101210010", None],
        "HS8": [None, "01012100"],
        "Value/Valeur": [1000, 2000],
        "Quantity/Quantité": [10, 20],
        "Country/Pays": ["US", "CN"]
    }

    df = pd.DataFrame(data)

    return df
