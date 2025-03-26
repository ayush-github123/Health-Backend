# Health API 🩺

Welcome to the **Health API**, a backend service for managing authentication, user health data, and AI-powered chat assistance.

## 🌟 Features
- **User Authentication** (Registration, Login, Logout, OTP Verification)
- **Health Form Management** (Submit, Update, Retrieve User Health Data)
- **JWT Authentication** for secure API access

## Prerequisites
Before you begin, make sure you have the following installed:
- **Python** (recommended version 3.8 or higher)
- **Git**
- A code editor (like Visual Studio Code, PyCharm, or Sublime Text)

## 📌 Step-by-Step Setup Guide

### 1. Clone the Repository 📂
1. Open your terminal or command prompt
2. Clone the repository:
   ```bash
   git clone https://github.com/ayush-github123/Health-Backend.git
   cd Health-Backend
   ```

### 2. Set Up a Virtual Environment 🌐
Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### 3. Install Project Dependencies 📦
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables 🔐
1. Create a `.env` file in the root directory
2. Add the following variables:
   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True  # Set to False in production
   DATABASE_URL=your_database_connection_string
   GEMINI_API_KEY=your_gemini_api_key
   EMAIL_HOST_USER=your_host_gmail_id
   EMAIL_HOST_PASSWORD=your_email_host_password
   ```

   🚨 **Important Notes**:
   - Keep your `.env` file private
   - Never commit it to version control
   - Use app passwords for Gmail if using 2-factor authentication

### 5. Database Setup 💾
Apply database migrations:
```bash
python manage.py migrate
```

### 6. Collect Static Files 📁
```bash
python manage.py collectstatic --noinput
```

### 7. Running the Server 🖥️

#### Option 1: Django Development Server
For basic development:
```bash
python manage.py runserver
```

#### Option 2: Daphne (Recommended for WebSocket Support) 🌐
```bash
# Install Daphne if not already installed
pip install daphne

# Run the server
daphne your_project_name.asgi:application
```

🎉 The API will be accessible at `http://127.0.0.1:8000/`

## 🔐 Authentication
- Uses **JWT (JSON Web Token) Authentication**
- Include token in requests:
  ```
  Authorization: Bearer <your-access-token>
  ```

## 📌 API Endpoints

### Authentication Routes (`/auth/`)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/auth/register/` | Register a new user |
| POST   | `/auth/login/` | Login and get JWT tokens |
| POST   | `/auth/logout/` | Logout user |
| POST   | `/auth/refresh/` | Refresh JWT token |
| POST   | `/auth/verify-otp/` | Verify user OTP |
| POST   | `/auth/resend-otp/` | Resend OTP |

### Health Form Routes (`/healthcare/`)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/healthcare/form/submit/` | Submit health form |
| GET    | `/healthcare/form/me/` | Retrieve health form |
| PUT    | `/healthcare/form/me/update/` | Update health form |

## 📖 API Documentation
- **Swagger UI**: `/docs/swagger/`
- **ReDoc UI**: `/docs/redoc/`
- **OpenAPI Schema**: `/api/schema/`

## 📌 Example Requests

### User Registration
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "SecurePass123",
  "confirm_password": "SecurePass123"
}
```

### Login
```json
{
  "username": "john_doe",
  "password": "SecurePass123"
}
```

### Submit Health Form
```json
 {
    "name": "User1",
    "age": 6,
    "gender": "Female",
    "contact_details": "9873443240",
    "chronic_conditions": "Arthritis, High Cholesterol",
    "past_surgeries": "Hip Replacement",
    "allergies": "Penicillin",
    "medications": "Atorvastatin, Ibuprofen",
    "symptoms": "Joint pain and stiffness",
    "symptom_severity": "Moderate",
    "symptom_duration": "Chronic",
    "mental_health_stress": false,
    "mental_health_anxiety": false,
    "mental_health_depression": false,
    "vaccination_history": "Covid-19, Pneumonia",
    "accessibility_needs": "Hearing aid support",
    "pregnancy_status": "Not Applicable",
    "emergency_contact": {
      "name": "Emma Green",
      "relationship": "Daughter",
      "number": "4376543241"
    },
    "health_insurance_provider": "WellCare",
    "health_insurance_policy": "MN123456",
    "preferred_language": "English",
    "research_participation": false
  }
```

## 🚀 Deployment (Using Render)
1. Push code to GitHub/GitLab
2. Connect Render account
3. Set environment variables
4. Build Command:
   ```bash
   pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
   ```
5. Deploy!

## Troubleshooting 🛠️
- Verify Python and dependency versions
- Check environment variables
- Ensure WebSocket configuration is correct
- Consult project issues on GitHub

## 🤝 Contributing
1. Fork the repository
2. Create a new branch
3. Make changes
4. Submit a pull request

## 📃 License
MIT License

## 📧 Contact
- Ayush Rai: [ayushrai31593@gmail.com](mailto:ayushrai31593@gmail.com)
- Project Repository: [GitHub Link](https://github.com/ayush-github123/Health-Backend)