from flask import Flask
app = Flask(__name__)
@app.route('/')
def project_home():
    return "Hello DevOps Enthusiasts! Welcome to this project"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
