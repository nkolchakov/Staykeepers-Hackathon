from flask import (
    Flask,
    render_template,
    jsonify
)

# Create the application instance
app = Flask(__name__, template_folder="templates")

class Kotka:
    def __init__(self,name, age):
        self.name = name
        self.age = age

# Create a URL route in our application for "/"
@app.route('/katze')
def home():
    k = Kotka("kotka",12)
    return jsonify(k.__dict__)

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)