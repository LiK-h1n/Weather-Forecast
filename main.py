from streamlit import title, text_input, slider, selectbox, subheader

title("Weather Forecast for the Next Days")
place = text_input("Place")
forecast_days = slider("Forecast Days", 1, 5)
data_type = selectbox("Data to view", ["Temperature", "Sky"])
subheader(f"Temperature for the next {forecast_days} {'day' if forecast_days == 1 else 'days'} in {place}")
