from flask import Flask, render_template, request, redirect, url_for
import json, os

app = Flask(__name__)
DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

@app.route("/")
def index():
    items = load_data()
    return render_template("index.html", items=items)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        items = load_data()
        new_item = request.form["item"]
        items.append(new_item)
        save_data(items)
        return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/edit/<int:item_id>", methods=["GET", "POST"])
def edit(item_id):
    items = load_data()
    if request.method == "POST":
        items[item_id] = request.form["item"]
        save_data(items)
        return redirect(url_for("index"))
    return render_template("edit.html", item=items[item_id], item_id=item_id)

@app.route("/delete/<int:item_id>")
def delete(item_id):
    items = load_data()
    items.pop(item_id)
    save_data(items)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
