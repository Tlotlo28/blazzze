# Blazzze 🍃

The Internet's Couch — a parody cannabis-themed community site built with Django + HTMX.

🔗 **Live demo:** https://blazzze.onrender.com  
⏱ *First load may take ~30s — free Render tier spins down after 15 mins of inactivity.*

## Stack
- Django 6 + HTMX
- Python 3.13
- Postgres (Neon)
- WhiteNoise for static files
- Deployed on Render

## Features
- Custom middleware (age verification gate)
- Custom template tags (random mascot quotes anywhere)
- HTMX-driven dynamic UX (chat, modals, product cards)
- Pattern-matching response engine with regex word boundaries
- Pure CSS smoke animations
- Image upload with emoji fallback
- Multi-app architecture (core, munchies, buy, chat)
- Custom 404 page

## Local setup
\`\`\`bash
git clone https://github.com/Tlotlo28/blazzze
cd blazzze
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
cp .env.example .env  # then edit with your values
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
\`\`\`