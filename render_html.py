from flask import Flask, render_template
import calendar

app = Flask(__name__, template_folder="templates")

# Render page
def render_page():
    template = render_template('base_planner.html')
    return template

# Route Decorator 
@app.route('/')
def home():
    template_out = render_page()
    return template_out

if __name__ == '__main__':
    app.run()