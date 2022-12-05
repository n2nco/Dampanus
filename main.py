import os

from flask import Flask, render_template 
from flask import request, jsonify
from flask_cors import CORS
import func

app = Flask(__name__, static_url_path='')
CORS(app)


@app.route("/")

def hello_world():
    # name = os.environ.get("NAME", "World")
    #print(userInput)
    return render_template('index.html')
   
    # return "Hello {}!".format(func.hello_world())
    # return render_template("index.html")
    # return '<html> <body> <h1 contenteditable=true> Hello World palakesh 1</h1> </body> </html>'


@app.route('/index/')
def root():
    return app.send_static_file('index.html')

@app.route("/objective")

def objective():
    # name = os.environ.get("NAME", "World")
    if request.args.get('userinput') is not None:
        userInput = request.args.get('userinput') 

    print("request data - ob")
    print(userInput)
    objective = userInput
    # response.headers.add('Access-Control-Allow-Origin', '*')
    r = func.runFile(objective) 

    print("response:")
    print(r)
    response = jsonify({"status":"OK", 'result': str(r)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


    #return func.runFile(objective)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))