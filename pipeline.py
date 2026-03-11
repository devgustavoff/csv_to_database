import pandas as pd
import numpy as np
from sqlalchemy import create_engine

df = pd.read_csv("datas/dirty_datas.csv", on_bad_lines="skip")

def clean_strings(df):
    # nome
    df["nome"] = df["nome"].str.strip().str.title()
    df["nome"] = df["nome"].str.replace(";","")

    # email
    df["email"] = df["email"].str.lower()

    # status
    df["status"] = df["status"].str.capitalize()

    # pais
    df["pais"] = df["pais"].replace("BR", "Brasil")
    df["pais"] = df["pais"].ffill()

    # Coluna: observacao
    df["observacao"] = df["observacao"].fillna("No Note")
    df["observacao"] = df["observacao"].str.strip()

    return df

def clean_numerics(df):
    # idade
    df["idade"] = pd.to_numeric(df["idade"], errors="coerce")
    df["idade"] = df["idade"].fillna(df["idade"].mean())
    df["idade"] = df["idade"].astype("int")

    # valor_compra
    df["valor_compra"] = df["valor_compra"].str.replace("-", "")
    df["valor_compra"] = df["valor_compra"].str.replace(",", ".")
    df["valor_compra"] = pd.to_numeric(df["valor_compra"], errors="coerce")
    df["valor_compra"] = df["valor_compra"].where(df["valor_compra"] < 1_000_000, np.nan)

    return df

def clean_dates(df):
    # data_cadastro
    df["data_cadastro"] = pd.to_datetime(df["data_cadastro"], errors="coerce", format="mixed")
    df = df.dropna(subset="data_cadastro")

    return df


def run_pipeline(df):
    df_clean = clean_strings(df)
    df_clean = clean_numerics(df_clean)
    df_clean = clean_dates(df_clean)


    df_clean = df_clean[df_clean["status"] != "Inativo"]
    df_clean = df_clean.drop_duplicates()

    return df_clean

df_clean = run_pipeline(df)

engine = create_engine("postgresql://postgres:hakkjj97@localhost:5432/mydb")
df_clean.to_sql("clientes", engine, if_exists="replace", index=False)