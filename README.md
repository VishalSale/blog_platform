# Blog Platform Assessment

A Django + DRF + Channels project providing:

✅ RESTful CRUD APIs for **Authors** and **Posts**  
✅ JWT token authentication  
✅ Filter posts by author name & creation date  
✅ Real-time WebSocket notifications when a new post is added  
✅ Pagination & basic error handling

---

## Local Setup Instructions

Follow these steps to run the project locally:

1. **Clone the repository**
   ```bash
   git clone https://github.com/VishalSale/blog_platform.git
   cd blog_platform
   ```

2. **Create & activate a virtual environment**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **If you already have a Postgres account (user):**
   
   Just create the database and grant permissions to your existing Postgres user.
   
   In psql shell:
   
   ```
   CREATE DATABASE blog_post_db;
   GRANT ALL PRIVILEGES ON DATABASE blog_post_db TO your_existing_user;
   ```
   **Then update your blog_platform_assessment/settings.py or set environment variables with your existing user’s credentials:**
   ```
   export DATABASE_NAME=blog_post_db
   export DATABASE_USER=your_existing_user
   export DATABASE_PASSWORD=your_password
   export DATABASE_HOST=localhost
   export DATABASE_PORT=5432
   ```
6. **If you do NOT have a Postgres account:**
   
   Create the database and a new user with the same credentials used in this assessment.
   
   In psql shell:
   
   ```
   CREATE DATABASE blog_post_db;
   CREATE USER vishal WITH PASSWORD 'vishalsale';
   GRANT ALL PRIVILEGES ON DATABASE blog_post_db TO vishal;
   ```
   **No Need to change in blog_platform_assessment/settings.py**
   
8. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

9. **Create a superuser (for admin access & testing)**
   ```bash
   python manage.py createsuperuser
   ```

10. **Start the development server**
   ```bash
   python manage.py runserver
   ```
---

## 🔗 Endpoints & URLs

- **Admin UI:** http://127.0.0.1:8000/admin/  
- **API root:** http://127.0.0.1:8000/api/  
- **Authors List:** http://127.0.0.1:8000/api/authors/
- **Posts CRUD:** http://127.0.0.1:8000/api/posts/
- **Filter by date:** `?date=YYYY-MM-DD`  
- **Search by author:** `?search=AuthorName`  
- **JWT token endpoints:**  
  - Obtain token: `POST /api/token/` with JSON  
  - Refresh token: `POST /api/token/refresh/`  
- **WebSocket:** `ws://127.0.0.1:8000/ws/posts/` – broadcasts new post messages  
---

**Everything you need is in this one file.**
