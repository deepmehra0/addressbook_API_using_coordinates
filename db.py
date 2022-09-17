import sqlite3
import apiendpoint as api


'''This function is used prevent code failure at the starting of application run,
and also create table if it doses not exist'''
def start_db():
    connection = sqlite3.connect('data.db', check_same_thread=False)
    cursor = connection.cursor()
    item_c = 'CREATE TABLE IF NOT EXISTS address("Place_Name" text,"Latitude" float,"Longitude" float,"City" text,"Area" text,"country" text)'
    result =cursor.execute(item_c).fetchall()
    connection.commit()
    if result:
        return True

#This function is used to add records in database
def insert_item(v1,v2):
    if fetch_by(v1,v2): # this will prevent duplication of records in database
        return {"message" :"Record already present in database"}
    else:
        data =api.by_cod(v1,v2) # this will provide the data from coordinates API which we will insert in DB
        data =data['data'][0]
        connection = sqlite3.connect('data.db', check_same_thread=False)
        cursor = connection.cursor()
        item_ins_c = f'''INSERT INTO address VALUES("{data.get('name')}",'{data.get('latitude')}','{data.get('longitude')}','{data.get('region')}', '{data.get('neighbourhood')}','{data.get('country')}')'''
        cursor.execute(item_ins_c)
        connection.commit()
        # this is for the response of our request and in this same pattern we will store data in DB
        x = {
            'Place_name': data.get('name'),
             'Latitude': data.get('latitude'),
             'Longitude': data.get('longitude'),
             'City': data.get('region'),
             'Area': data.get('neighbourhood'),
             'country': data.get('country')
             }
        if cursor.execute(item_ins_c):
            connection.close()
            return {"Message":"Record is created and saved in database",
                "record":x}
        else:
            connection.close()
            return False

def diplay_records():# this function is used to display all records from DB
    if start_db():#if we will request for data from table before table creation this will pervent this issue.
        return False
    else:
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        Selcet_c = "SELECT * FROM address"
        result = cursor.execute(Selcet_c).fetchall()
        connection.close()
        if result:
            values =[]# this used to display all records in below format
            for i in result:
                x={
                    'Place_name': i[0],
                    'Latitude': i[1],
                    'Longitude': i[2],
                    'City': i[3],
                    'Area': i[4],
                    'Country': i[5]
                }
                values.append(x)
            return ({'Records': values})
        return {'MESSAGE': 'No Records To Show -Empty DATABASE'}

def delete_record(v1,v2):# this will allow us to delete records on the bases of Latitude and Longitude from DB
    connection = sqlite3.connect('data.db', check_same_thread=False)
    cursor = connection.cursor()
    select_c = f"DELETE FROM address where ( Latitude ={v1} and Longitude ={v2} )"
    cursor.execute(select_c)
    connection.commit()
    connection.close()

def fetch_by(v1,v2,): #this will allow us to fetch records on the bases of Latitude and Longitude from DB
     if start_db():#if we will request for data from table before table creation this will pervent this issue.
        return False
     else:
        connection = sqlite3.connect('data.db', check_same_thread=False)
        cursor = connection.cursor()
        select_c = f"SELECT * FROM address where latitude= {v1} and longitude= { v2}"
        result = cursor.execute(select_c).fetchone()
        connection.commit()
        connection.close()
        if result !=None:
            # x used to display  records in below format
            x={     'Place_name': result[0],
                    'Latitude': result[1],
                    'Longitude': result[2],
                    'City': result[3],
                    'Area': result[4],
                    'Country': result[5]
                }
            return x
        return False

def update_by(data,v1,v2):#this will allow us to upadte records on the bases of Latitude and Longitude from DB
    if fetch_by(v1,v2) :#this will check the record which we want to upadte is presnet in db or not
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        for key, values in data.items():
            query_c = f"UPDATE address SET {key} = '{values}' where latitude= {v1} and longitude= { v2} "
            result = cursor.execute(query_c)
            connection.commit()
        connection.close()
        if result:
            return ({"Message ": "Record Updated Sucessfully."})
        return {{"Message ": "Having Technical Issues."}}
    return {"Message ": f"No Record Found For This Given Latitude = {v1} and Longitude = {v2}."}
