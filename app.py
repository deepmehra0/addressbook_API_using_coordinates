from flask import Flask
from flask_restful import Api
from data import Insert_data,Display_data,Delete_data,Fetch_data,Update_data
app = Flask('__name__')
api =Api(app)

# end point for our API
api.add_resource(Insert_data,'/add_address') # this end point will allow use to enter address in DB
api.add_resource(Display_data,'/view_all_address')# this end point will allow use to view all address from the DB
api.add_resource(Delete_data,'/delete_address')# this end point will allow use to delete address in DB
api.add_resource(Fetch_data,'/view_by_lon_lat')# this end point will allow use to fetch  address on the bases of Latitude and Longitude in DB
api.add_resource(Update_data,'/update_record')# this end point will allow use to update address in DB on the bases of Latitude and Longitude


if __name__==('__main__'):
    app.run(debug='on')
