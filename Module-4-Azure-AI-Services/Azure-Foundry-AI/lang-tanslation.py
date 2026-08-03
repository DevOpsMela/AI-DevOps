import requests
 
ENDPOINT = "https://devops-openai-fdry.cognitiveservices.azure.com/"
API_VERSION = "2025-10-01-preview"

SUBSCRIPTION_KEY = "9MjzZS2KoHWBWXjLCBrK1hkC4q5ynFiwgrVMMzM4sxE7UzyjSuvlJQQJ99CFACYeBjFXJ3w3AAAAACOGr8QP"

def translate_text(text, targets, source_language):
    headers = {
        "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY,
        "Content-Type": "application/json"
    }
    url = f"{ENDPOINT}/translator/text/translate?api-version={API_VERSION}"
    body = {
        "inputs": [
            {
                "Text": text,
                "language": source_language,
                "targets": targets
            }
        ]
    }

    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()
    return response.json()
 
def main():
    text = "Doctor is available next Monday. Do you want to schedule an appointment?"
    targets = [
        {"language": "es",},
        {"language": "hi", }
    ]
    source_language = "en"
    try:
        result = translate_text(text, targets,source_language)

        for t in result["value"][0]["translations"]:
            print(f"Translation ({t['language']}): {t['text']}")
    except Exception as e:
        print(f"Translation failed: {e}")
 
if __name__ == "__main__":
    main()