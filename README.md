# Quora Clone
## Setup
### 1. Create a Virtual Environment with python3.10
```
python3.10 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```
### 3. Apply Migrations
```
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser (for admin access)
```
python manage.py createsuperuser
```
Follow the prompts to set username, email, and password.

### 5. Run the Development Server
```
python manage.py runserver
```
Open your browser and go to:
```
http://127.0.0.1:8000/
```

### 6.Features
- Post and view Questions

- Submit Answers

- Like/Unlike Answers

- Admin interface to manage all models

## Administration
### Admin Panel
Access the admin interface:
```
http://127.0.0.1:8000/admin/
```
Log in using the superuser credentials you created.

## Contact
For any queries, contact sridhar562345@gmail.com