from flask import Flask
#WSGI application
app = Flask(__name__)
@app.route('/')
def Home():
    return "Welcome to my youtube channel"
if __name__=='__main__':
    app.run(debug=True)