import os
import requests

GAFFA_API_KEY = os.getenv("GAFFA_API_KEY")
HEADERS = {
    "x-api-key": GAFFA_API_KEY,
    "Content-Type": "application/json"
}

def download_file(url):
    payload = {
        "url": url,
        "async": False,
        "settings": {
            "actions": [{"type": "download_file", "timeout": 30000}],
            "time_limit": 60000
        }
    }
    print(f"Retrieving download URL for: {url}")
    response = requests.post("https://api.gaffa.dev/v1/browser/requests", json=payload, headers=HEADERS)
    response.raise_for_status()
    download_url = next((act["output"] for act in response.json()["data"]["actions"] if act["type"] == "download_file"), None)

    print("Downloading file.")
    file_data = requests.get(download_url).content
    filename = os.path.basename(download_url)
    with open(filename, "wb") as f:
        f.write(file_data)
    print(f"Saved: {filename}")

def main():
    # Direct file download: the file downloads straight to disk.
    download_file("https://demo.gaffa.dev/simulate/download?fileName=ReasoningAboutActionAndChange.pdf")

    # Browser-rendered file: the file opens inline in the browser instead of downloading automatically.
    download_file("https://demo.gaffa.dev/simulate/pdf/ReasoningAboutActionAndChange.pdf")

    # Same download_file action, same code path, both patterns handled identically.

if __name__ == "__main__":
    main()
