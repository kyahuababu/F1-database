<<<<<<< HEAD
# F1-database
=======
# Formula 1 Database Application

A Flask-based Formula 1 database application with Firebase authentication and Firestore integration for managing drivers and teams data.

## Features

- Firebase Authentication with Google Sign-in
- CRUD operations for F1 drivers and teams
- Query and comparison functionality
- Responsive UI with Bootstrap dark theme

## Prerequisites

- Python 3.11
- Firebase project with Google Authentication enabled
- Required Python packages (see requirements.txt)

## Environment Variables

The following environment variables are required:

```
FIREBASE_API_KEY=your_api_key
FIREBASE_PROJECT_ID=your_project_id
FIREBASE_PRIVATE_KEY=your_private_key
FIREBASE_CLIENT_EMAIL=your_client_email
FIREBASE_APP_ID=your_app_id
SESSION_SECRET=your_session_secret
```

## Firebase Setup Instructions

1. Go to the [Firebase Console](https://console.firebase.google.com/) and create a new project
2. Enable Google Authentication:
   - Go to Authentication > Sign-in methods
   - Enable Google sign-in
   - Add your domain to the authorized domains list
3. Get Firebase Configuration:
   - Go to Project Settings > General
   - Register a new web app if you haven't already
   - Copy the configuration values (API Key, Project ID, App ID)
4. Generate Service Account Key:
   - Go to Project Settings > Service Accounts
   - Click "Generate New Private Key"
   - Save the JSON file securely

## Local Development Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd formula1-database
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your Firebase configuration:
```
FIREBASE_API_KEY=your_api_key
FIREBASE_PROJECT_ID=your_project_id
FIREBASE_PRIVATE_KEY=your_private_key
FIREBASE_CLIENT_EMAIL=your_client_email
FIREBASE_APP_ID=your_app_id
SESSION_SECRET=your_session_secret
```

4. Run the application:
```bash
python main.py
```

## Project Structure

```
├── app.py                 # Main application configuration
├── main.py               # Application entry point
├── models.py             # Data models
├── static/
│   └── js/
│       ├── auth.js       # Authentication logic
│       ├── firebase-init.js  # Firebase initialization
│       └── validation.js # Form validation
├── templates/
│   ├── base.html        # Base template
│   ├── index.html       # Home page
│   ├── drivers/         # Driver-related templates
│   └── teams/           # Team-related templates
└── .gitignore           # Git ignore configuration
```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
>>>>>>> dc724ec (Initial commit: Setup Flask F1 database application with Firebase authentication and Firestore integration. Includes CRUD operations for drivers and teams, query functionality, and responsive UI.)
