import pymysql

db = pymysql.connect("server", "username", "password", "database")


# creates a new user
def new_login(user, pas):
    if user == "":
        return "Enter a Username."
    if pas == "":
        return "Enter a Password."
    p = search_for(user)
    if not p:
        cursor = db.cursor()
        cursor.execute(f"INSERT INTO logins (username, password) VALUES ('{user}', '{pas}');")
        db.commit()
        return
    return "Username is Taken."


# checks if user exists and returns password
def search_for(user):
    cursor = db.cursor()
    cursor.execute(f"SELECT password FROM logins WHERE username='{user}';")
    p = cursor.fetchone()
    if p is None:
        return False
    return "" + p[0]
