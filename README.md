# Job Application Tracker (Django)

A simple and efficient **Job Application Tracker** built with **Django** that helps users manage and track their job applications.
Users can add, update, and delete job applications through a clean and responsive web interface.

---

## 🚀 Features

* Add new job applications
* Edit existing job applications
* Delete job applications
* View all applications in a structured table
* Bootstrap-based responsive UI
* SQLite database integration
* Full **CRUD (Create, Read, Update, Delete)** functionality

---

## 🛠️ Tech Stack

* **Python**
* **Django**
* **HTML**
* **Bootstrap**
* **SQLite**
* **Git & GitHub**

---

## 📂 Project Structure

```
job_tracker/
│
├── applications/
│   ├── migrations/
│   ├── templates/
│   │   └── applications/
│   │       ├── job_list.html
│   │       ├── job_form.html
│   │       └── job_confirm_delete.html
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── job_tracker/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/YOUR_USERNAME/job-application-tracker-django.git
```

### 2️⃣ Navigate to project folder

```
cd job_tracker
```

### 3️⃣ Install dependencies

```
pip install django
```

### 4️⃣ Apply migrations

```
python manage.py migrate
```

### 5️⃣ Run the development server

```
python manage.py runserver
```

---

## 🌐 Access the Application

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

## 📸 Application Preview

The dashboard displays a list of job applications with options to:

* Add Job Application
* Edit Job Application
* Delete Job Application

---

## 👨‍💻 Author

**Ranjith**

GitHub:
https://github.com/mummadiranjithkumar

---

## 📌 Future Improvements

* User authentication (login/register)
* Dashboard statistics
* Search and filter job applications
* File upload for resumes
* Email notifications


