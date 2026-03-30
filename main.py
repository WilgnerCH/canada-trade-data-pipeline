import pandas as pd
from src.extract import download_data
from src.transform import process_data
from src.load import save_files, upload_to_drive


def main():

    print("Starting pipeline...")

    # EXTRACT
    df = download_data()

    # TRANSFORM
    df = process_data(df)

    # SAVE
    parquet_path, csv_path = save_files(df)

    # LOAD → GOOGLE DRIVE
    upload_to_drive(parquet_path, "canada_trade_full.parquet")
    upload_to_drive(csv_path, "canada_trade_full.csv")

    print("Pipeline finished successfully!")


if __name__ == "__main__":
    main()
