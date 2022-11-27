from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
 return 'Hello World'

@app.route('/')
def index():
 return render_template("index.html")

@app.route('/namaste')
def namaste():
 return 'Namaste'

@app.route('/add')
def add():
 n1 = int(request.args.get("num1"))
 n2 = int(request.args.get("num2"))
 result = n1+n2
 op = "+"
 return render_template("output.html",op=op,result=result,num1=n1,num2=n2)

@app.route('/mul')
def mul():
 n1 = int(request.args.get("num1"))
 n2 = int(request.args.get("num2"))
 result = n1*n2
 op = "*"
 return render_template("output.html",op=op,result=result,num1=n1,num2=n2)

@app.route('/sub')
def sub():
 n1 = int(request.args.get("num1"))
 n2 = int(request.args.get("num2"))
 result = n1-n2
 op = "-"
 return render_template("output.html",op=op,result=result,num1=n1,num2=n2)

if __name__ == "__main__":
 app.run() #debug=False,port=5001