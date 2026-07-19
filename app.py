from flask import Flask, render_template, request, url_for, redirect
import sqlite3
from datetime import datetime
from werkzeug.security import generate_password_hash
from flask import session
from werkzeug.security import check_password_hash
import os
print(os.path.abspath("expenses.db"))

app = Flask(__name__)
app.secret_key =  os.environ.get("SECRET_KEY","dev_secret_key")   # Later we'll move this to an environment variable

# expenses = []

@app.route("/")
def home():
    
    if "user_id" not in session:
        return redirect(url_for("login"))

    user_id = session["user_id"]
    today = datetime.now().strftime("%A, %d %B %Y")
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses where user_id =?",(user_id,))
    expenses = cursor.fetchall()

    cursor.execute("SELECT SUM(amount) FROM expenses where user_id = ?",(user_id,))
    total = cursor.fetchone()[0] or 0

    cursor.execute("SELECT COUNT(*) FROM expenses where user_id=?",(user_id,))
    count = cursor.fetchone()[0]

    average = total / count if count else 0
    
    conn.close()

    return render_template("index.html", expenses=expenses, sum_expenses = total, today = today, count = count, average = average)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = sqlite3.connect("expenses.db")
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, username, password_hash from users where username = ?",(username,))
        user = cursor.fetchone()
        conn.close()
        if user:
            stored_hash = user[2]

            if check_password_hash(stored_hash,password):

                session["user_id"] = user[0]
                session["username"] = user[1]
                print(session)
                return redirect(url_for("home"))

        return render_template("login.html",error = "Invalid Username or Password")
    return render_template("login.html")    

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        hashed_password = generate_password_hash(password)
        conn = sqlite3.connect("expenses.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email=?", (email,))
        existing_user = cursor.fetchone()
        if existing_user:
            conn.close()
            return render_template("register.html", error="Email already exists!")
       
        cursor.execute("INSERT INTO users(username,email,password_hash) values (?,?,?)",(username,email,hashed_password))
        conn.commit()
        conn.close() 
      #  return redirect(url_for("home"))
        return redirect(url_for("login"))   
    return render_template("register.html")

@app.route("/add_expense", methods=["GET","POST"])
def add_expense():

    if "user_id" not in session:
        return redirect(url_for("login")) 

    if request.method == "POST":

        expense = request.form["expense"]
        amount = request.form["amount"]
        date = request.form["date"]
        category = request.form["category"]
        user_id = session["user_id"]
        conn = sqlite3.connect("expenses.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses(expense,amount,date,category,user_id) VALUES (?,?,?,?,?)",(expense,amount,date,category,user_id))
        conn.commit()
        conn.close()
        return redirect(url_for("home"))
    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()
    user_id = session["user_id"]
    cursor.execute("SELECT * FROM expenses where user_id = ?",(user_id,))

    expenses = cursor.fetchall()
    conn.close()

    return render_template("add_expense.html", expenses=expenses)        
#        expenses.append({
#            "expense":expense,
#            "amount":amount
#            })
#        print(expenses)
#        return "Expense saved successfully!"
   
   #         return f"Expense: {expense}, Amount: {amount}"
  #  return render_template("add_expense.html")

@app.route("/delete/<int:id>")
def delete_expense(id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    user_id = session["user_id"]
    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id=? AND user_id = ?", (id,user_id,))

    conn.commit()

    conn.close()
    return redirect(url_for("home"))

@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit_expense(id):
    
    if "user_id" not in session:
        return redirect(url_for("login"))
    user_id = session["user_id"]
    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()
    if request.method == "POST":
        expense = request.form["expense"]
        amount = request.form["amount"]
        date = request.form["date"]
        category = request.form["category"]
        cursor.execute("""UPDATE expenses SET expense=?, amount=?, date=?, category=? WHERE id=? and user_id = ?""",(expense,amount,date,category,id,user_id))
        conn.commit()
        conn.close()
        return redirect(url_for("home"))       

    cursor.execute("SELECT * FROM expenses WHERE id=? AND user_id=?",(id, user_id))

    expense = cursor.fetchone()
    if expense is None:
        return redirect(url_for("home"))
    conn.close()
    return render_template("edit_expense.html",expense=expense)

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)