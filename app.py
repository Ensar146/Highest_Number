from flask import Flask, render_template, request
import sqlite3

server=sqlite3.connect("data.db", check_same_thread=False)

cursor=server.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, names TEXT NOT NULL, numbers INTEGER NOT NULL)")
server.commit()

app=Flask(__name__)

x=0
y=""

@app.route("/", methods=["GET","POST"])
def Home():
    global x,y


    if request.method=="POST":
        number=int(request.form["number"])
        name=request.form["name"]
        if number>x:
            x=number
            y=name
        cursor.execute("INSERT INTO users (numbers,names) VALUES (?,?)", (x,y))
        server.commit()


    return render_template("index.html",x=x,y=y)



if __name__=="__main__":
    app.run(debug=True)
