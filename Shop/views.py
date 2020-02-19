from Shop import app
from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/basket")
def basket():
    return render_template("basket.html")

@app.route("/about_us")
def about():
    return render_template("about.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/reviews")
def reviews():
    return render_template("reviews.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

@app.route("/delivery")
def delivery():
    return render_template("delivery.html")
""" 
змінити від
"""
@app.route("/top_diсk")
def top_diсk():
    return render_template("top_diсk.html")

@app.route("/red_diсk")
def red_diсk():
    return render_template("red_diсk.html")

@app.route("/blaсk_diсk")
def blak_diсk():
    return render_template("blak_diсk.html")
""" 
змінити до
"""
