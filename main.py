from streamlit import title, text_input, slider, selectbox, subheader, plotly_chart
from plotly.express import line

title("Weather Forecast for the Next Days")
place = text_input("Place")
forecast_days = slider("Forecast Days", 1, 5)
data_type = selectbox("Data to view", ["Temperature", "Sky"])
subheader(f"Temperature for the next {forecast_days} {'day' if forecast_days == 1 else 'days'} in {place}")
dates = ["2023-05-31", "2023-06-01", "2023-06-02"]
temperatures = [3, 10, 4]
figure = line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
plotly_chart(figure)
