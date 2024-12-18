
# Weather Web Application

This web application allows users to view current weather conditions and forecasts for a given city. The project was developed using **Django** and leverages the **MeteoConcept API** to retrieve real-time weather data.

## Features

- Displays current weather conditions for a specified city.
- Short-term weather forecasts (e.g., for the next 3 days).
- Simple and intuitive user interface.

## Technologies Used

- **Django**: Python web framework for backend development.
- **MeteoConcept API**: External service for fetching real-time weather data.
- **HTML/CSS**: For structuring and styling the user interface.
- **JavaScript**: For client-side interactions, such as form submissions without page reload.

## Installation

### Prerequisites

- Python 3.x
- pip (to install dependencies)

### Installation Steps

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Dany-py/Meteo.git
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Linux/Mac
   venv\Scripts\activate  # On Windows
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the MeteoConcept API by obtaining an API key from [MeteoConcept](https://www.meteo-concept.com/), and add it to your Django `settings.py` file:
   ```python
   METEO_API_KEY = 'your_api_key'
   ```

5. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Open the application in your browser at the following address:
   ```
   http://127.0.0.1:8000/
   ```

## Project Structure

- `django_project/`: Contains the main Django configuration.
- `Meteo/`: The Django app that handles weather-related features.
- `templates/`: Contains HTML files for displaying weather information.
- `static/`: Contains CSS and JavaScript files for frontend design.

## Contribution

Feel free to fork this repository and submit a pull request if you'd like to contribute.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
