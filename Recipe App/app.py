from flask import Flask, render_template, request
import requests

app = Flask(__name__)

Recipe_API = "https://www.themealdb.com/api/json/v1/1/search.php"

@app.route("/", methods=["GET", "POST"])
def index():
    recipes = []  # Store recipe list
    if request.method == "POST":
        query = request.form.get("recipe")  # Get search input
        if query:
            response = requests.get(Recipe_API, params={"s": query})
            if response.status_code == 200:
                data = response.json()
                if data["meals"]:
                    recipes = data["meals"]  # Store recipe results

    return render_template("index.html", recipes=recipes)

@app.route("/recipe/<recipe_id>")
def recipe_detail(recipe_id):
    response = requests.get("https://www.themealdb.com/api/json/v1/1/lookup.php", params={"i": recipe_id})
    
    if response.status_code == 200:
        data = response.json()
        if data["meals"]:
            recipe = data["meals"][0]
            return render_template("recipe.html", recipe=recipe)
    return "Recipe not found", 404
if __name__ == "__main__":
    app.run(debug=True)
