import requests

api_url = "https://api.openweathermap.org/data/2.5/weather?q=Florianopolis&appid=4ecdccc255f44763b561436f22654748"

def fetch_data():
    print("Coletando dados meteorológicos de openweather.org.")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("Informações coletadas com sucesso de openweather.org.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição em openweather.org: {e}")
        raise