import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


def save_files(df):

    print("Saving files...")

    os.makedirs("data_processed", exist_ok=True)

    parquet_path = "data_processed/canada_trade_full.parquet"
    csv_path = "data_processed/canada_trade_full.csv"

    df.to_parquet(parquet_path, index=False)
    df.to_csv(csv_path, index=False)

    return parquet_path, csv_path


def upload_to_drive(file_path, filename):

    print(f"Uploading {filename} to Google Drive...")

    credentials_json = os.environ.get("GOOGLE_CREDENTIALS")

    if not credentials_json:
        raise ValueError("GOOGLE_CREDENTIALS not found")

    creds_dict = json.loads(credentials_json)

    creds = service_account.Credentials.from_service_account_info(
        creds_dict,
        scopes=["https://www.googleapis.com/auth/drive"]
    )

    service = build("drive", "v3", credentials=creds)

    file_metadata = {
        "name": filename,
        "parents": ["1ylnUllISklTnJW7CFfdn9Xk9buzRVkuk"]  # seu folder ID
    }

    media = MediaFileUpload(file_path, resumable=True)

    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id",
        supportsAllDrives=True
    ).execute()

    print("Upload complete. File ID:", file.get("id"))
