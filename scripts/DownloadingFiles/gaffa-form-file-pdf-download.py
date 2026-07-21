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
        "max_cache_age": 0,
        "settings": {
            "actions": [
                {"type": "type", "selector": "#email", "text": "johndoe@example.com", "timeout": 20000},
                {"type": "type", "selector": "#state", "text": "Brent", "timeout": 20000},
                {"type": "type", "selector": "#zipCode", "text": "12345", "timeout": 20000},
                {"type": "click", "selector": ".inline-flex", "timeout": 1000},
                {"type": "wait", "selector": "div.flex:nth-child(1)", "timeout": 1000, "continue_on_fail": True, "time": 1000},
                {"type": "download_file", "timeout": 1000}
            ]
        }
    }
    print("Submitting form.")
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
    download_file("https://demo.gaffa.dev/simulate/form?loadTime=3&showModal=false&modalDelay=0&formType=address&firstName=John&lastName=Doe&address1=123%20Main%20Street&city=London&country=UK&pdfExport=true")

if __name__ == "__main__":
    main()
