from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# Carbon footprint data
carbon_footprint = {
    'beef': 20, 
    'chicken': 6,
    'milk': 1,
    'lamp': 39,
    'eggs': 4,
    'pork': 7,
    'fish': 6,
}

# Routes for main pages
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/meal-plans")
def meal_plans():
    return render_template("meal-plans.html")

@app.route("/calculator")
def calculator():
    return render_template("calculator.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# Routes for meal planner subpages
@app.route("/meal-plans/breakfast")
def breakfast():
    return render_template("breakfast.html")

@app.route("/meal-plans/lunch")
def lunch():
    return render_template("lunch.html")

@app.route("/meal-plans/dinner")
def dinner():
    return render_template("dinner.html")

@app.route("/meal-plans/brunch")
def brunch():
    return render_template("brunch.html")

@app.route("/meal-plans/baby-foods")
def baby_foods():
    return render_template("baby_foods.html")

@app.route("/meal-plans/others")
def others():
    return render_template("others.html")

# Route to handle carbon footprint calculation
@app.route('/calculate', methods=['POST'])
def calculate():
    product = request.form.get('product')
    quantity = request.form.get('quantity', type=float)
    
    if product is None or quantity is None:
        # Handle missing form data
        error_message = "Please provide both product and quantity."
        return render_template('calculator.html', error=error_message)
    
    footprint_per_kg = carbon_footprint.get(product.lower(), 0)
    total_footprint = quantity * footprint_per_kg
    
    return render_template('calculator.html', product=product, quantity=quantity, total_footprint=total_footprint)

if __name__ == '__main__':
    app.run(debug=True)
