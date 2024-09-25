import requests
import matplotlib.pyplot as plt
import datetime
import numpy as np

def fetch_weather_data(city, api_key):
    url = ('http://api.openweathermap.org/data/2.5/forecast'
           f'?q={city}&units=metric&appid={api_key}')
    response = requests.get(url)
    data = response.json()
    return data

def parse_weather_data(data):
    dates = []
    temperatures = []
    for entry in data['list']:
        date = datetime.datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S')
        temp = entry['main']['temp']
        dates.append(date)
        temperatures.append(temp)
    return dates, temperatures

def plot_weather_data(dates, temperatures, city):
    plt.style.use('dark_background')  # Set dark background
    plt.figure(figsize=(12, 6))

    # Normalize temperatures for colormap
    norm = plt.Normalize(min(temperatures), max(temperatures))
    colors = plt.cm.coolwarm(norm(temperatures))  # Use coolwarm colormap

    # Create the line plot
    plt.plot(dates, temperatures, marker='o', color='white')  # Base line color
    for i in range(len(dates) - 1):
        plt.plot(dates[i:i + 2], temperatures[i:i + 2], color=colors[i])  # Segment line color based on temperature

    # Get unique days
    unique_days = {date.date() for date in dates}

    # Annotate hottest and coldest points per day
    for day in unique_days:
        day_indices = [i for i, date in enumerate(dates) if date.date() == day]
        daily_temps = [temperatures[i] for i in day_indices]
        daily_dates = [dates[i] for i in day_indices]

        hottest_index = day_indices[np.argmax(daily_temps)]
        coldest_index = day_indices[np.argmin(daily_temps)]

        # Annotate the hottest point
        plt.annotate(f'{daily_temps[np.argmax(daily_temps)]:.1f}°C',
                     xy=(dates[hottest_index], temperatures[hottest_index]),
                     xytext=(5, 5), textcoords='offset points',
                     bbox=dict(boxstyle='round,pad=0.3', edgecolor='none', facecolor='gray'),
                     arrowprops=dict(arrowstyle='->', color='orange'),
                     fontsize=10, fontweight='bold', color='orange')

        # Annotate the coldest point
        plt.annotate(f'{daily_temps[np.argmin(daily_temps)]:.1f}°C',
                     xy=(dates[coldest_index], temperatures[coldest_index]),
                     xytext=(5, -15), textcoords='offset points',
                     bbox=dict(boxstyle='round,pad=0.3', edgecolor='none', facecolor='gray'),
                     arrowprops=dict(arrowstyle='->', color='blue'),
                     fontsize=10, fontweight='bold', color='blue')

    plt.title(f'5-Day Temperature Forecast for {city}', fontsize=14)
    plt.xlabel('Date and Time', fontsize=12)
    plt.ylabel('Temperature (°C)', fontsize=12)
    plt.grid(True, color='gray')
    plt.tight_layout()
    plt.savefig('weather_plot.png')
    plt.show()

def main():
    city = 'Edmonton'  # You can change the city
    api_key = 'dbedd922e0ab39f9e9d6dbd8251e9f18'  # Replace with your OpenWeatherMap API key
    data = fetch_weather_data(city, api_key)
    dates, temperatures = parse_weather_data(data)
    plot_weather_data(dates, temperatures, city)

if __name__ == '__main__':
    main()
