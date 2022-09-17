import requests as rq

access_key='b65b7efe03240b2925b76422e002fa21'
# this function is used to fetch location details on the bases of Latitude and Longitude for this API
def by_cod(value1,value2):
    end =f'http://api.positionstack.com/v1/reverse?access_key={access_key}&query={value1},{value2}'
    data=rq.get(url=end).json()
    return data




