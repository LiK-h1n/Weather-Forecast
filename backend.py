from requests import get

API_KEY = "eb803fd0e96ff09195f9dc981a0ecba8"


def get_data(place, forecast_days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&units=metric&appid={API_KEY}"
    response = get(url)
    data = response.json()
    filtered_data = data["list"]
    no_values = 8 * forecast_days
    filtered_data = filtered_data[:no_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data("Bahrain", None, None))
