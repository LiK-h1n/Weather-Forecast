from streamlit import title, text_input, slider, selectbox, subheader, plotly_chart, image, info
from plotly.express import line
from backend import get_data

title("Weather Forecast for the Next Days")
place = text_input("Place")
forecast_days = slider("Forecast Days", 1, 5)
kind = selectbox("Data to view", ["Temperature", "Sky"])

if place:
    try:
        subheader(f"{kind} for the next {forecast_days if forecast_days > 1 else ''} "
                  f"{'day' if forecast_days == 1 else 'days'} in {place}")

        filtered_data = get_data(place, forecast_days)
        if kind == "Temperature":
            temperatures = [value["main"]["temp"] for value in filtered_data]
            dates = [value["dt_txt"] for value in filtered_data]
            figure = line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            plotly_chart(figure)
        elif kind == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}
            sky_conditions = [value["weather"][0]["main"] for value in filtered_data]
            image_paths = [images[sky_condition] for sky_condition in sky_conditions]
            image(image_paths, width=115)
    except KeyError:
        info("Place does not exist / Place not found")
