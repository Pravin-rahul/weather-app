import requests

# Get your API key from OpenWeatherMap
API_KEY = "4caeac3dec7d893123147d6b1b5efb64"

# Function to get weather data
def get_weather(city):
    # URL for the weather API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    # Sending the GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        
        # Extracting required data
        temperature = main['temp']
        humidity = main['humidity']
        description = weather['description']
        
        # Display the weather information
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
    else:
        print(f"Error {response.status_code}: {response.json()['message']}")
        print(f"City '{city}' not found. Please check the spelling or try a different city!")

# Input from the user
city = input("Enter city name: ")
get_weather(city)
