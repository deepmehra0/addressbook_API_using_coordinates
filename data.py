from flask_restful import Resource
from flask import request
import db


class Insert_data(Resource): # this Class is used to add data in DATABASE
    def post(self):
        DATA = request.get_json()
        result = db.insert_item(DATA['Latitude'], DATA['Longitude'])
        if result:
            return (result)
        return {'MESSAGE': 'No Record Found '}


class Display_data(Resource): # this Class is used to display all records from the DATABASE
    def get(self):
        return db.diplay_records()


class Delete_data(Resource): # this Class is used to delete records from the DATABASE on the bases of Latitude and Longitude
    def delete(self):
        DATA = request.get_json()
        value = db.fetch_by(DATA['Latitude'], DATA['Longitude'])
        result = db.delete_record(DATA['Latitude'], DATA['Longitude'])
        if value:
            return {'MESSAGE': 'Successful Deleted'}
        return ({'MESSAGE': 'No record to Deleted'})


class Fetch_data(Resource): # this Class is used to display records from the DATABASE on the bases of Latitude and Longitude
    def get(self):
        DATA = request.get_json()
        result = db.fetch_by(DATA['Latitude'], DATA['Longitude'])
        if result:
            return ({'records': result})
        return {'MESSAGE': f"No Record Found For These Given Latitude = {DATA['Latitude']} and Longitude = {DATA['Longitude']}"}


class Update_data(Resource): # this Class is used to update records from the DATABASE on the bases of Latitude and Longitude
    def put(self):
        DATA = request.get_json()
        result = db.update_by(DATA, DATA['Latitude'], DATA['Longitude'])
        return result