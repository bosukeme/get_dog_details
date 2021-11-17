from flask_restful import Resource, reqparse
from get_dogs import get_dog_details, get_dog_details_csv
from flask import request


class DogDetails(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('num_dog_beds_sold', type=int, help="The number of dogs to be sold")
            parser.add_argument('avg_bed_weight', type=float, help="The average weight of the dogs")
            parser.add_argument('lea_lea_sold', type=int, help="The lea lea sold")
            parser.add_argument('lea_col_sold', type=int, help="The lea col sold")
            

            args = parser.parse_args()


            result = get_dog_details(args['num_dog_beds_sold'], args['avg_bed_weight'], args['lea_lea_sold'], args['lea_col_sold'])
            return {
                'status': 'success',
                'data': result, 
                'message': 'Dog Details successful.'
            }, 200

        except Exception as e:
            return {
                'status': 'failed',
                'data': None,
                'message': str(e)
            }, 500




class DogDetailsCSV(Resource):

    def post(self):
        try:
            csv_file = request.files["csv_file"]
            if not csv_file:
                return "No CSV file attached"

            result = get_dog_details_csv(csv_file)
            return {
                'status': 'success',
                'data': result, 
                'message': 'Dog Details successful.'
            }, 200

        except Exception as e:
            return {
                'status': 'failed',
                'data': None,
                'message': str(e)
            }, 500