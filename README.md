📰 Django News Portal

A **News Portal Web Application** built with Django where admins can post news articles, and users can browse, search, and filter news by categories.  
The portal provides a clean and responsive UI using **Bootstrap**.

---

## 🚀 Features

- 📝 **Admin Panel** – Admin can add, edit, and delete news articles.
- 🗂 **Categories** – News can be filtered by category (e.g., Sports, Politics, Tech).
- 🔍 **Search Functionality** – Search news articles by title or content.
- 📅 **Date & Time** – Each article shows its published date.
- 📱 **Responsive UI** – Works on mobile, tablet, and desktop (Bootstrap).
- 👤 **User Authentication (Optional)** – Allow users to sign up and comment (future scope).

---

## 🛠️ Tech Stack

- **Backend**: Django 5.x (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (default) / PostgreSQL / MySQL
- **Admin**: Django’s built-in Admin Panel

---

## 📂 Project Structure

news_portal/
│── blog/ # Main app
│ ├── migrations/ # Database migrations
│ ├── templates/ # HTML templates
│ │ ├── base.html
│ │ ├── home.html
│ │ ├── category.html
│ │ ├── search.html
│ │ └── detail.html
│ ├── static/ # CSS, JS, images
│ ├── models.py # News model
│ ├── views.py # Logic for displaying articles
│ ├── urls.py # App URLs
│ └── admin.py # Register models for admin
│
│── news_portal/ # Project settings
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py / asgi.py
│
│── manage.py # Django entry point
│── db.sqlite3 # Local DB (ignored in GitHub)
