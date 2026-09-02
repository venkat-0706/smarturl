
# 🔗 SmartURL — URL Shortener

SmartURL is a full-stack URL shortening application built with **Django REST Framework**, **PostgreSQL**, and **React (Vite)**.

It converts long URLs into short, shareable links and tracks basic usage such as click counts and expiration.

---

## 🚀 Features

- 🔗 Shorten long URLs
- ⚡ Generate unique short codes
- ↗️ Redirect short URLs to original URLs
- 📊 Track click count
- ⏳ Automatically expire URLs after 24 hours
- ✅ Validate submitted URLs
- 🔐 JWT authentication
- 👤 User registration
- 🗄️ PostgreSQL database
- 🌐 REST API
- 📱 Responsive React frontend
- 📋 Copy shortened URLs easily

---

## 🛠️ Tech Stack

### Backend

- Python
- Django
- Django REST Framework
- Simple JWT
- PostgreSQL
- Gunicorn
- django-cors-headers
- dj-database-url

### Frontend

- React
- Vite
- JavaScript
- HTML
- CSS

### Tools

- Git
- GitHub
- Postman
- VS Code

---

## 📁 Project Structure

```text
smarturl/
│
├── backend/
│   └── shortner/
│       ├── manage.py
│       ├── requirements.txt
│       │
│       ├── myapp/
│       │   ├── models.py
│       │   ├── serializers.py
│       │   ├── views.py
│       │   ├── urls.py
│       │   └── utils.py
│       │
│       └── shortner/
│           ├── settings.py
│           ├── urls.py
│           ├── wsgi.py
│           └── asgi.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
└── README.md
````

---

# ⚙️ Backend Setup

## 1. Clone the repository

```bash
git clone https://github.com/venkat-0706/smarturl.git
cd smarturl
```

## 2. Go to the backend directory

```bash
cd backend/shortner
```

## 3. Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 5. Configure environment variables

Create a `.env` file inside the backend directory.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgresql://postgres:password@localhost:5432/shortner_db
```

> ⚠️ Never commit `.env` or production secrets to GitHub.

## 6. Run migrations

```bash
python manage.py migrate
```

## 7. Start the Django server

```bash
python manage.py runserver
```

Backend will be available at:

```text
http://127.0.0.1:8000/
```

---

# 🎨 Frontend Setup

Open a new terminal.

## 1. Go to the frontend directory

```bash
cd frontend
```

## 2. Install dependencies

```bash
npm install
```

## 3. Start the React application

```bash
npm run dev
```

Frontend will be available at:

```text
http://localhost:5173/
```

---

# 🔌 API Endpoints

## Register User

```http
POST /api/auth/register/
```

Example request:

```json
{
    "username": "chandu",
    "email": "chandu@example.com",
    "password": "yourpassword"
}
```

Example response:

```json
{
    "message": "User Registered Successfully...",
    "username": "chandu"
}
```

---

## Login

```http
POST /api/auth/login/
```

Example request:

```json
{
    "username": "chandu",
    "password": "yourpassword"
}
```

Example response:

```json
{
    "refresh": "your-refresh-token",
    "access": "your-access-token"
}
```

---

## Refresh Token

```http
POST /api/auth/refresh/
```

Example request:

```json
{
    "refresh": "your-refresh-token"
}
```

---

## Create Short URL

```http
POST /api/shorten/
```

Example request:

```json
{
    "original_url": "https://www.youtube.com/"
}
```

Example response:

```json
{
    "id": 1,
    "original_url": "https://www.youtube.com/",
    "short_code": "aB72xK",
    "short_url": "http://127.0.0.1:8000/aB72xK/",
    "expires_at": "2026-09-03T08:00:00Z"
}
```

---

## Redirect Short URL

```http
GET /<short_code>/
```

Example:

```text
http://127.0.0.1:8000/aB72xK/
```

The user will be redirected to the original URL.

Every successful redirect also increases the `click_count`.

---

## List URLs

```http
GET /api/urls/
```

Returns the available shortened URLs.

---

## URL Details

```http
GET /api/urls/<id>/
```

Returns details for a specific shortened URL.

---

## Delete URL

```http
DELETE /api/urls/<id>/
```

Deletes a shortened URL.

---

# 🔐 Authentication

SmartURL uses **JWT (JSON Web Tokens)** for authentication.

Send the access token using:

```http
Authorization: Bearer <access_token>
```

Example:

```text
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

---

# ⏳ URL Expiration

Every generated short URL is valid for **24 hours**.

After expiration, the API returns:

```http
410 Gone
```

Example response:

```json
{
    "error": "This short URL has been expired.."
}
```

---

# 📊 Click Tracking

Every successful visit to a shortened URL increases its click count.

For example:

```text
Initial click_count = 0

User opens short URL
        ↓
click_count = 1

User opens it again
        ↓
click_count = 2
```

---

# 🧪 Testing

Run Django tests using:

```bash
python manage.py test
```

The project includes tests for:

* ✅ Creating a short URL
* ✅ Redirecting a short URL
* ✅ Click count
* ✅ Expired URLs
* ✅ Invalid URLs

---

# 🌐 Deployment

The planned production architecture is:

```text
                ┌─────────────────┐
                │     Vercel      │
                │      React      │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │     Render      │
                │ Django / DRF    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   PostgreSQL    │
                │     Render      │
                └─────────────────┘
```

---

# 🚀 Backend Deployment — Render

## Root Directory

```text
backend/shortner
```

## Build Command

```bash
pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
```

## Start Command

```bash
gunicorn shortner.wsgi:application
```

### Production Environment Variables

Configure these inside Render:

```env
SECRET_KEY=your-production-secret-key
DEBUG=False
DATABASE_URL=your-render-postgresql-url
```

---

# ⚡ Frontend Deployment — Vercel

After deploying the Django backend, update the React API URL.

Create a frontend environment variable:

```env
VITE_API_URL=https://your-backend.onrender.com
```

Then use it in your React application instead of:

```javascript
http://127.0.0.1:8000
```

Example:

```javascript
const API_URL = import.meta.env.VITE_API_URL;
```

Then:

```javascript
fetch(`${API_URL}/api/shorten/`, {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        original_url: url
    })
});
```

---

# 🔒 Security

* Keep `SECRET_KEY` outside source control.
* Never commit `.env`.
* Set `DEBUG=False` in production.
* Configure `ALLOWED_HOSTS`.
* Configure CORS for the deployed frontend.
* Store production database credentials in environment variables.
* Never expose sensitive credentials in source code.

---

# 📌 Future Improvements

The following features can be added later:

* 👤 User-specific URL ownership
* 📊 Analytics dashboard
* 📈 Detailed click analytics
* 🔐 More granular permissions
* ⚡ Redis caching
* 🚦 API rate limiting
* 📅 Custom expiration periods
* 🔗 Custom short codes
* 📱 Improved mobile experience

---

# 🎯 Learning Outcomes

This project demonstrates practical experience with:

* Django REST API development
* PostgreSQL
* JWT authentication
* Database modeling
* URL redirection
* API validation
* Backend testing
* CORS
* Environment variables
* React development
* Full-stack integration
* Production deployment

---

# 👨‍💻 Author

## Chandu

**Computer Science Engineering | Python Full Stack Developer**

### GitHub

```text
https://github.com/venkat-0706
```

### LinkedIn

```text
Add your LinkedIn profile here
```

---

⭐ If you find this project useful, consider giving it a star!

````

### One important correction before you commit

Your actual GitHub repository URL may be different from:

```text
https://github.com/venkat-0706/smarturl.git
````

So replace that line with your **actual SmartURL repository URL** before pushing the README.

Then commit it:

```bash
git add README.md
git commit -m "Add project documentation"
git push

