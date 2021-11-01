from flask import Flask
from flask_restful import Api
from dog_resources import DogDetails

app=Flask(__name__)

api=Api(app)


@app.route("/")
def home():
    return "<h1 style='color:blue'>This is the DOG Details  pipeline!</h1>"


api.add_resource(DogDetails, '/dog_details')

if __name__=='__main__':
    app.run(port= 5000, debug=True)