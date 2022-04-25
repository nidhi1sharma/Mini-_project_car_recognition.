#importing mysql.connector
import mysql.connector as c
#connecting to the database.......
host_name   = input("ENTER THE HOSTNAME:")
user_       = input("ENTER USER NAME:")
passwd_     = input("ENTER THE PASSWORD:")
database_   = input("ENTER THE NAME OF THE DATABASE:")
connect_sql = c.connect(host = host_name, user= user_, passwd = passwd_, database = database_)
cursor = connect_sql.cursor()
if connect_sql.is_connected():
    print("DATABASE SUCCESSFULLY CONNECTED....")
#taking input to select whether to fetch, update, insert .......
input_1 = int(input("ENTER 1 TO FETCH DATA \nENTER 2 TO UPDATE DATA \nENTER 3 TO INSERT DATA\n"))
#query to fetch data....
if input_1 == 1:
    while True :
        car_no      = input("ENTER CAR NUMBER:")
        query       = "select * from data_sample where car_no = '{}'".format(car_no)
        cursor.execute(query)
        data = cursor.fetchall()
        print (data)
        x = int(input("ENTER 1 : TO FETCH MORE \n ENTER 2 : TO EXIT"))
        if x == 2:
            break
#query to update data....
elif input_1 == 2:
    while True :
        house_no    = int(input("ENTER HOUSE NUMBER:"))
        car_no      = input("ENTER CAR NUMBER:")
        query       = "update data_sample set car_no = '{}' where house_no ={}".format(car_no,house_no)
        cursor.execute(query)
        connect_sql.commit()
        print("Data updated successfully.")
        x = int(input("ENTER 1 : TO ADD MORE \n ENTER 2 : TO EXIT"))
        if x == 2:
            break
#query to insert into database....
elif input_1 == 3:
    while True :
        house_no    = int (input("ENTER HOUSE NUMBER:"))
        name        = input("ENTER NAME:")
        car_no      = input("ENTER CAR NUMBER:")
        car_name    = input("ENTER CAR NAME:")
        query       = "insert into data_sample values({},'{}','{}','{}')".format(house_no,name,car_no,car_name)
        cursor.execute(query)
        connect_sql.commit()
        print("Data inserted successfully.")
        x = int (input("ENTER 1 : TO ADD MORE RECORDS \n ENTER 2 : TO EXIT"))
        if x == 2:
            break
#query for deletion of a particular data
elif input_1 == 4:
    while True :
        car_no      = input("ENTER CAR NUMBER:")
        query       = "delete from data_sample where car_no = '{}'".format(car_no)
        cursor.execute(query)
        connect_sql.commit()
        print ("Data deleted successfully.")
        x = int (input("ENTER 1 : TO ADD DELETE MORE RECORDS \n ENTER 2 : TO EXIT"))
        if x == 2:
            break
        
else :
    print("incorrect input given ....")     

