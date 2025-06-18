import requests

def infos_pays(nom_pays):
    url = f"https://restcountries.com/v3.1/name/{nom_pays}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()  # Liste de résultats
        pays = data[0]          # Premier résultat (le plus pertinent)
        capitale = pays.get("capital", ["Aucune capitale"])[0]
        population = pays.get("population", "Inconnue")
        print(f"Pays : {nom_pays.capitalize()}")
        print(f"Capitale : {capitale}")
        print(f"Population : {population}")
    else:
        print(f"Erreur lors de la requête : {response.status_code}")

# info sur pays en testant la fonction
infos_pays("france")