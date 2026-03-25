# Verum

**Verum** is a personal blog project built to showcase backend skills and full-stack development capabilities. While primarily created as a portfolio project, it’s fully functional and can be used in production with minor adjustments.

---

## 🔹 Features

* Create, edit, and delete blog posts
* Commenting system for posts
* Categories and tags support
* Powerful search and pagination
* Admin authentication for managing content
* Beautiful and unique design
* Secure backend architecture

---

## 🔹 Technologies Used

* **Backend:** Django 5
* **Database:** PostgreSQL
* **Frontend:** Typeright template by Styleshout (HTML/CSS/JS)
* **ORM:** Django Models
* **Admin:** Full-featured Django Admin
* **Authentication:** Admin-only login

---

## 🔹 Project Structure

* `blog/` — main Django app with models, views, and templates
* `static/` — static files (CSS, JS, images)
* `media/` — uploaded files
* `Verum/` — Main project directory

All code is written with clean architecture principles and modular backend design.

---

## 🔹 Setup & Running Locally

1. Clone the repository:

```bash
git clone https://github.com/kryptxnite/Verum.git
cd Verum
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with the following variables:

```
SECRET_KEY='REDACTED'
DEBUG=True
DB_NAME=REDACTED
DB_USER=REDACTED
DB_PASSWORD=REDACTED
DB_HOST=localhost
DB_PORT=5432
```

5. Apply migrations and create superuser:

```bash
python manage.py migrate
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

---

## 🔹 Screenshots

<img width="1920" height="1080" alt="Screenshot from 2026-03-25 12-44-48" src="https://github.com/user-attachments/assets/42ea0303-70ca-4bb4-831b-6afbbbcaf3e8" />
<img width="1920" height="1080" alt="Screenshot from 2026-03-25 12-45-02" src="https://github.com/user-attachments/assets/37ab4c40-e3df-4268-a5fa-5c4b4a6c28d0" />
<img width="1920" height="1080" alt="Screenshot from 2026-03-25 12-46-47" src="https://github.com/user-attachments/assets/f9fb12f0-239b-405c-bb22-fa932499f81d" />

---

## 🔹 Notes

* Project is fully functional and ready to use after basic configuration
* Admin authentication only; no public registration implemented
* All backend code written from scratch (except frontend template)
* Clean code and structured architecture

---

