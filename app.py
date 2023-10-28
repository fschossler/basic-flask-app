from flask import Flask, render_template

app = Flask(__name__)

# Add a /hello route
@app.route('/hello')
def hello():
    # Return the index.html inside the templates folder, this is a pattern in Flask
    return render_template('index.html')

if __name__ == '__main__':
    # Start the app in the 8080 port
    app.run(port=8080)
