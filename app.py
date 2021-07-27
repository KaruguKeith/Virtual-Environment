from flask import Flask #importing flask
#create an instance for flask
app = Flask(__name__)

#create our routes end points . We create a route then put a function at the end point
@app.route('/')
# it will land on the route folder of yoour application
# when using a framework we use / to create our own index path
def index():
    return 'Hello world'

#we now run our application
#this is the code that runs our application
if __name__ == '__main__':
    app.run(debug=True)