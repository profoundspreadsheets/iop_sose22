from flask import Flask, jsonify, request

# fix because conda flask-restul is only 0.3.8 TODO fix when 0.3.9
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

from flask_restful import Api, Resource

import xml.etree.ElementTree as ET

app = Flask(__name__)

api = Api(app)

xmlpath = "../xmls/1_data.xml"

class Hello(Resource):
  
    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
  
        tree = ET.parse(xmlpath)
        root = tree.getroot()
        teams = root.findall(".//Team[@teamid=609]")

        return jsonify({'message': teams})
  
    # Corresponds to POST request
    def post(self):
          
        data = request.get_json()     # status code
        return jsonify({'data': data})
  
  
# another resource to calculate the square of a number
class Square(Resource):
  
    def get(self, num):
  
        return jsonify({'square': num**2})
  
  
# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')

if __name__ == '__main__':
    app.run(debug = True)