from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Kaixo mundua!"

if __name__ == "__main__":
    app.run()
    
    //additional comments
        //additional comments
            //additional comments