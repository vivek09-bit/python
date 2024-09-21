import requests
import pprint
def get_weather(city):
    api_key = 'Api_key'  # Replace with your actual API key of weatherapi.com
    base_url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'

    response = requests.get(base_url)
    
    if response.status_code == 200:
        weather_data = response.json()
        # pprint.pprint(weather_data)
        location = weather_data['location']
        current = weather_data['current']
        print(location['country'])
        print(current['condition'])
        # pprint.pprint(response.json())
        print(f"Weather in {location['name']}, {location['region']}, {location['country']}:")
        print(f"Temperature: {current['temp_c']}°C")
        print(f"Condition: {current['condition']['text']}")
        print(f"Humidity: {current['humidity']}%")
        print(f"Wind Speed: {current['wind_kph']} km/h")
    else:
        print(f"Error: {response.json().get('error', {}).get('message', 'An error occurred.')}")

if __name__ == "__main__":
    city = input('Enter city name: ')
    get_weather(city)
