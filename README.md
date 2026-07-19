# 💰 Expense Tracker

A modern Expense Tracker web application built using **Python, Flask, SQLite, HTML, CSS, and Bootstrap**.

This application allows users to securely register, log in, and manage their personal expenses with a clean and responsive dashboard.

---

## 🚀 Features

- 👤 User Registration
- 🔐 Secure Login & Logout
- 🔑 Password Hashing using Werkzeug
- 🍪 Session-based Authentication
- 👥 User-specific Expense Management
- ➕ Add Expenses
- ✏️ Edit Expenses
- 🗑️ Delete Expenses
- 📂 Expense Categories
- 📅 Expense Date Tracking
- 📊 Dashboard Statistics
  - Total Expenses
  - Total Number of Expenses
  - Average Expense
- 📱 Responsive Bootstrap UI
- 🚫 Empty Dashboard State for New Users

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- SQLite

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- Jinja2 Templates

### Authentication
- Flask Sessions
- Werkzeug Password Hashing

---

## 📁 Project Structure

```text
expense-tracker/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── add_expense.html
│   └── edit_expense.html
│
├── static/
│   └── style.css
│
└── expenses.db
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/ummayhanee/expense-tracker.git
```

Move into the project directory

```bash
cd expense-tracker
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 📷 Screenshots

### Dashboard

*(Add screenshot after uploading to GitHub)*

### Login Page

*(Add screenshot)*

### Registration Page

*(Add screenshot)*

### Add Expense

*(Add screenshot)*

---

## 🔒 Security Features

- Passwords are securely hashed before being stored.
- User authentication is handled using Flask Sessions.
- Each user can only access and manage their own expenses.
- Protected routes require authentication before access.

---

## 🎯 Future Enhancements

- 📈 Expense Charts & Analytics
- 📅 Monthly Reports
- 💸 Budget Management
- 📄 Export to CSV/PDF
- 📧 Email Verification
- 🔁 Password Reset
- ☁️ AWS EC2 Deployment
- 🐳 Docker Support
- 🤖 AI-powered Expense Insights

---

## 👨‍💻 Author

**Ummay Hanee**

Python Backend Developer | AI & ML Enthusiast

---

## 📜 License

This project is for educational and portfolio purposes.