# Weather Visualization Project

## Overview

The Weather Visualization Project is a Python application that fetches weather data for a specified city using the OpenWeatherMap API. It visualizes the 5-day temperature forecast using Matplotlib, allowing users to see temperature trends and identify the hottest and coldest days. In case of an error (e.g., invalid city name or API key), the application displays a humorous sad face GIF.

## Features

- **Fetch Weather Data**: Retrieves weather forecast data for a given city and country code using the OpenWeatherMap API.
- **Data Parsing**: Extracts relevant temperature and date information from the API response.
- **Temperature Visualization**: Plots a line graph showing temperature trends over the next five days, highlighting the highest and lowest temperatures with markers and annotations.
- **Error Handling**: Displays a sad face GIF when a request fails due to a bad response, enhancing user experience.

## Requirements

To run this project, you will need:

- Python 3.x
- The following Python libraries:
  - `requests`
  - `matplotlib`
  - `numpy`

You can install the required libraries using pip:

```bash
pip install requests matplotlib numpy
```

## Setup

1. **Clone the Repository**: 
   Clone this repository to your local machine using:
   ```bash
   git clone https://github.com/YourUsername/Weather-Visualization.git
   ```

2. **Obtain an API Key**:
   Sign up for an API key at [OpenWeatherMap](https://openweathermap.org/api) and replace the placeholder API key in the `main()` function.

3. **Run the Application**:
   Navigate to the project directory and run the script:
   ```bash
   python weather_visualization.py
   ```

4. **Input City and Country Code**:
   When prompted, enter the city name and the country code (e.g., 'CA' for Canada).

## Running on Google Colab

You can also run this project on Google Colab by clicking the following link:

[Run on Google Colab](https://colab.research.google.com/drive/1DdmIXvD17Q-IEI_Zk3gSjwArA2MPgjNR)

When prompted, enter the city name and country code to see the forecast.

## How It Works

- **fetch_weather_data(city, country_code, api_key)**:
  This function constructs the API request URL and fetches the weather data from the OpenWeatherMap API. It raises an error for any bad responses.

- **parse_weather_data(data)**:
  This function processes the JSON response from the API, extracting dates and temperatures for the upcoming 5 days.

- **plot_weather_data(dates, temperatures, city)**:
  This function uses Matplotlib to create a visually appealing temperature forecast graph, using color gradients to represent temperature variations.

- **show_error_gif()**:
  Displays a sad face GIF when an error occurs during the data fetching process.

## Example Output

Upon successful execution, the program will generate a plot similar to the one shown below:

![Example Weather Plot](img/project/weather_plot.png)

In case of an error, the program will show the following GIF:

![Error GIF](https://github.com/HardikPatel-DX/Analytics-Portfolio/edit/main/projects/weathervisual/giphy.gif)

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. You can also open issues to discuss improvements or report bugs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [OpenWeatherMap](https://openweathermap.org/api) for providing the weather data API.
- [Matplotlib](https://matplotlib.org/) for creating visualizations.
- [NumPy](https://numpy.org/) for numerical operations.
