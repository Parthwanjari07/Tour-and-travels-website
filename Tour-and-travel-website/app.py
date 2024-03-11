from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/places')
def places():
    return render_template('places.html')

@app.route('/toggle_menu')
def toggle_menu():
    # Code to handle menu toggle action goes here
    return 'Menu toggled'

if __name__ == '__main__':
    app.run(debug=True)

