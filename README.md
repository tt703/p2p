# Peer2Peer Tutoring Platform 🎓

**Peer2Peer** is a Django-based web application designed to connect students with peer tutors. It facilitates learning by allowing high-performing students to register as tutors for specific subjects, while other students can book tutoring sessions, chat in real-time, and track their learning progress.

![Python](https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Framework-Django-092E20?logo=django&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## ✨ Key Features

### 🍎 For Tutors
- **Registration Validation:** Users can register as tutors only if they achieved a specific mark (e.g., ≥ 80%) in their subject.
- **Session Management:** View upcoming tutoring sessions and student details.
- **Performance Tracking:** Tutors are ranked by a performance rating system.

### 📚 For Students
- **Find Tutors:** Browse a list of available tutors filtered by subject and rating.
- **Book Sessions:** Schedule tutoring sessions with specific descriptions and dates.
- **Dashboard:** Access a personalized dashboard showing available subjects and active chats.

### 💬 Communication & Tools
- **Real-Time Chat:** Integrated messaging system allowing students and tutors to communicate directly before or after sessions.
- **Google Calendar Integration:** (Optional) Support for syncing sessions with Google Calendar.
- **Online Status:** Real-time visibility of user online status.

---

## 🛠️ Tech Stack

- **Backend:** Python 3, Django 5
- **Real-Time:** Django Channels (ASGI)
- **Database:** SQLite (Default)
- **Frontend:** HTML5, CSS3, Django Templates
- **Authentication:** Django Auth System (Extended User Model)

---

## 🚀 Getting Started

Follow these instructions to set up the project locally.

### Prerequisites
- Python 3.8+ installed.
- `pip` package manager.

### Installation

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/tt703/p2p-tutoring.git](https://github.com/tt703/p2p-tutoring.git)
    cd p2p-tutoring
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Database Migration**
    Initialize the database tables:
    ```bash
    cd myp2p
    python manage.py migrate
    ```

5.  **Run the Server**
    ```bash
    python manage.py runserver
    ```
    Access the application at `http://127.0.0.1:8000/`.

---

## ⚙️ Configuration

### Google Calendar API
To enable calendar features, place your Google Cloud credentials JSON file in:
`myp2p/credentials/credentials.json`

### Email Settings
Update the `EMAIL_HOST` settings in `myp2p/settings.py` or use a `.env` file to configure SMTP for notifications.


