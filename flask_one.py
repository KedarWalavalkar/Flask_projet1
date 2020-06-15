from flask import *
f=Flask(__name__)

@f.route("/home")
def home():
    return "<h1>Hello World</h1>"
    
@f.route("/f/<name>")
def name():
    return "<h1>hello "+name+"</h1>"
    
if __name__=='__main__':
    f.run(debug=True)
    

    