@"
# 📰 News Portal (Django)

A simple **Django-based Blog/News Portal** with categories, search, and an admin panel to post articles. Frontend uses **Bootstrap**.

## 🚀 Features
- Create, edit, delete posts from Django Admin
- Category filtering and keyword search
- Responsive Bootstrap templates
- (Optional) Pagination and featured posts

## 🛠️ Tech Stack
Python 3 · Django 5 · SQLite · Bootstrap

## 📂 Typical Structure
news_portal/
├─ news_portal/           # Project settings (urls.py, settings.py)
├─ blog/                  # App with models, views, templates
├─ templates/             # Base and page templates
├─ static/                # CSS/JS if any
├─ manage.py
└─ README.md

## ⚡ Setup
git clone https://github.com/sujal1702/news_portal.git
cd news_portal
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
# Open http://127.0.0.1:8000/

## 🎯 Usage
- Visit the site to browse posts by category or search.
- Login to /admin to add or manage posts.
