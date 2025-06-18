import re
import requests
from tenacity import retry, stop_after_attempt, wait_fixed

# utils.py for all of the functions which are usefull

def en_majuscule(texte):
    return texte.upper()




def mock_reverse(text):
    emails = re.findall(r'\S+@\S+\.\S+', text)
    placeholders = [f"__EMAIL{i}__" for i in range(len(emails))]
    for email, placeholder in zip(emails, placeholders):
        text = text.replace(email, placeholder)
    reversed_text = text[::-1]
    for placeholder, email in zip(placeholders, emails):
        reversed_text = reversed_text.replace(placeholder[::-1], email)
    return reversed_text

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def appel_api_libretranslate(texte):
    response = requests.post(
        "https://libretranslate.de/translate",
        data={"q": texte, "source": "en", "target": "ar", "format": "text"},
        timeout=10
    )
    response.raise_for_status()
    return response.json()["translatedText"]

def traduire_texte(texte, use_mock=True):
    if not texte.strip():
        return ""
    if use_mock:
        return mock_reverse(texte)
    try:
        return appel_api_libretranslate(texte)
    except Exception as e:
        print("Translation error after retries:", e)
        return texte

