import pandas as pd


def format_hs(code):

    if pd.isna(code):
        return None

    code = str(code).strip()

    if not code.isdigit():
        return None

    # HS8
    if len(code) == 8:
        return f"{code[:4]}.{code[4:6]}.{code[6:8]}"

    # HS10
    elif len(code) == 10:
        return f"{code[:4]}.{code[4:6]}.{code[6:8]} {code[8:10]}"

    return None


def process_data(df):

    print("Transforming dataset...")

    # Criar data YYYY-MM
    ym = df["YearMonth/AnnéeMois"].astype(str)
    df["date"] = ym.str[:4] + "-" + ym.str[4:6]

    # Unificar HS
    df["HS_raw"] = df["HS10"].fillna(df["HS8"])

    # remover vazios
    df = df[df["HS_raw"].notna()]

    df["HS_raw"] = df["HS_raw"].astype(str)

    # manter só números
    df = df[df["HS_raw"].str.match(r"^\d+$")]

    # formatar HS
    df["HS"] = df["HS_raw"].apply(format_hs)

    # criar HS6 (PADRÃO GLOBAL)
    df["HS6"] = df["HS_raw"].str[:6]

    # remover inválidos
    df = df[df["HS"].notna()]

    return df
