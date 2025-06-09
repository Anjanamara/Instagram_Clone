"# Instagram Clone Backend"

# Instagram Clone Backend

This repository contains the backend code for the Instagram Clone project.  
The backend is built using Python with the Flask framework, providing REST API endpoints to support the web and mobile frontend apps.

---

## Features

- User authentication and authorization
- Fetch Instagram-like feed using Instagram API
- Basic user profile management
- Post creation, update, and deletion (planned)
- Secure API with token-based authentication

---

## Tech Stack

- Python 3.12
- Flask
- Flask-RESTful
- Instagram API integration
- Virtual environment for dependency management

---

## Project Structure

backend/
├── app.py # Main Flask app entry point
├── requirements.txt # Python dependencies
└── routes/
└── instagram.py # Instagram API routes and logic

yaml
Copy
Edit

---

## Setup Instructions

1. Clone the repository  
   git clone https://github.com/Anjanamara/Instagram_Clone.git

css
Copy
Edit

2. Navigate to the backend folder  
   cd Instagram_Clone/backend

r
Copy
Edit

3. Create and activate a virtual environment

- Windows:
  ```
  python -m venv venv
  venv\Scripts\activate
  ```
- Linux/macOS:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

4. Install dependencies  
   pip install -r requirements.txt

markdown
Copy
Edit

5. Run the Flask app  
   flask run

yaml
Copy
Edit

---

## Usage

- The backend will be running at `http://localhost:5000`
- API routes are available under `/api/...`

---

## Future Work

- Implement user registration and login
- Add more detailed API endpoints for posts and comments
- Integrate database (e.g., PostgreSQL) for persistent storage
- Add unit and integration tests

---

## Contributing

Feel free to open issues or pull requests to improve the project.

---

## License

This project is open source and available under the MIT License.
