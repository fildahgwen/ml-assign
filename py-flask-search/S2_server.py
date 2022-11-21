# (A) INIT
# (A1) LOAD MODULES
from flask import Flask, render_template, request, make_response
import sqlite3

# (A2) FLASK SETTINGS + INIT
HOST_NAME = "localhost"
HOST_PORT = 80
DBFILE = "users.db"
app = Flask(__name__)
# app.debug = True

# (B) HELPER FUNCTION - SEARCH USERS
def getusers(search):
  conn = sqlite3.connect(DBFILE)
  cursor = conn.cursor()
  cursor.execute(
    "SELECT * FROM `users` WHERE `name` LIKE ? OR `email` LIKE ?",
    ("%"+search+"%", "%"+search+"%",)
  )
  results = cursor.fetchall()
  conn.close()
  return results

# (C) DEMO SEARCH PAGE
@app.route("/", methods=["GET", "POST"])
def index():
  # (C1) SEARCH FOR USERS
  if request.method == "POST":
    data = dict(request.form)
    users = getusers(data["search"])
  else:
    users = []

  # (C2) RENDER HTML PAGE
  return render_template("S3_users.html", usr=users)

# (D) START
if __name__ == "__main__":
  app.run(HOST_NAME, HOST_PORT)