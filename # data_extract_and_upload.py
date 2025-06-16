import requests
import json
import time
import os
from datetime import datetime
from azure.storage.blob import BlobServiceClient

# === CONFIGURATION ===
API_URL = "https://api.beta.runwei.io/api/v1/opportunity/via/api-key"
USERNAME = "DfdakEbR"
PASSWORD = "TJsds2dgNl2iecdRRk"

AZURE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=opportunity2025;AccountKey=Hp8VDbs2jy8BaaYTbIu6SB4b1O5loFPuyZcStFYOvGJLlQEWrfY9P1Bzx5fCP1vVoUItNNHtmLIz+AStjf//uw==;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "runweidata"

# Save path and logging path
SAVE_DIR = r"C:\Users\wyp01\Desktop\Runwei\runwei_update"
LOG_FILE = os.path.join(SAVE_DIR, "runwei_upload_log.txt")

# === Ensure save directory exists ===
os.makedirs(SAVE_DIR, exist_ok=True)

# === Logging Helper ===
def log(message):
    with open(LOG_FILE, "a") as logf:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logf.write(f"[{timestamp}] {message}\n")

# === Azure Setup ===
try:
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)
    if not container_client.exists():
        container_client.create_container()
    log("Azure Blob container initialized.")
except Exception as e:
    log(f"Failed to initialize Azure Blob: {e}")
    raise

# === API Fetch ===
def fetch_opportunities(page=1, size=50):
    auth = (USERNAME, PASSWORD)
    all_opportunities = []

    while True:
        try:
            response = requests.get(f"{API_URL}?page={page}&size={size}", auth=auth, timeout=10)
            if response.status_code == 200:
                data = response.json()
                items = data.get("data", {}).get("items", [])
                if not items:
                    break
                all_opportunities.extend(items)
                log(f"Fetched page {page} with {len(items)} items.")
                page += 1
            elif response.status_code == 429:
                log("Rate limit exceeded. Retrying in 60s.")
                time.sleep(60)
            else:
                log(f"Error {response.status_code}: {response.text}")
                break
        except Exception as e:
            log(f"Exception during fetch: {e}")
            time.sleep(10)

    return all_opportunities

# === Main Flow ===
try:
    data = fetch_opportunities()
    if not data:
        log("No opportunity data fetched. Ending script.")
    else:
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        filename = f"runwei_opportunities_{timestamp}.json"
        filepath = os.path.join(SAVE_DIR, filename)

        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
        log(f"Data saved to {filepath}")

        blob_client = container_client.get_blob_client(filename)
        with open(filepath, "rb") as data_file:
            blob_client.upload_blob(data_file, overwrite=True)
        log(f"Uploaded file to Azure as {filename}")

except Exception as e:
    log(f"Fatal error: {e}")

print(f"Data extraction successful. Uploaded as {filename}")