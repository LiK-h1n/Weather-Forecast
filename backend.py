from requests import get

API_KEY = "eb803fd0e96ff09195f9dc981a0ecba8"


def get_data(place, forecast_days, kind):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = get(url)
    data = response.json()
    return data


if __name__ == "__main__":
    print(get_data("Bahrain", None, None))
