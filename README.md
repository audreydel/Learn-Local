## Learn Local Booking System

This application is a simple booking system built using Flask for the backend and React for the frontend. It allows users to book times and dates, specify the number of people, and view existing bookings.

## Setup

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3 or higher
- Flask
- Flask-SQLAlchemy
- React
- npm (Node Package Manager)

### Backend Setup

The backend is a Flask application that handles bookings and stores them in a SQLite database.

1. Navigate to the `flask-app` directory (backend).
2. Create a virtual environment:
   - Windows: `python -m venv <path>`
   - Mac/Linux: `python3 -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install the required packages:
   - Windows/Mac/Linux: `pip install Flask Flask-SQLAlchemy`
5. Run the application:
   - Windows: `python app.py`
   - Mac/Linux: `python3 app.py`
6. The backend will be running on `http://localhost:5000`.

### Frontend Setup

The frontend is a React application that provides a user interface for the booking system.

1. Navigate to the frontend directory: `cd learn-local/frontend`.
2. Install the necessary packages: `npm install`.
3. Start the frontend on a local server: `npm start`.
4. The frontend should be running on `http://localhost:3000`.

### Features

1. **Booking Form**: Users can book a time and date through a form, specifying the number of people (up to 24). Navigate to `/book` to access the form.

2. **View Bookings**: To view all bookings, navigate to `/info`.

3. **Database Integration**: Bookings are stored in a SQLite database. The backend manages the creation and retrieval of booking records.

4. **Validation**: The system checks for already booked slots and validates the number of people
