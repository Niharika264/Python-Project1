from werkzeug.wrappers import Request,Response
from flask import Flask,request,jsonify
from datetime import datetime
import pyodbc
name = str
def Patientdb(name):
    #building connection
    connection = pyodbc.connect('Driver={SQL Server};'
    'Server=DESKTOP-L846VMO\SQLEXPRESS;'
    'Database=myTable;'
    'username=niharika;'
    'password=niharika;'
    'Trusted_Connection=True;')
    
    #building curosor object from established connection
    cur = connection.cursor()
    
    #creating the table
    '''Table = "create table Patient(date DATE NOT NULL,name varchar(20) NOT NULL, age int , gender varchar(10) , diagnosis         varchar(30) NOT NULL, treatment varchar(30) NOT NULL)"
    cur.execute(Table)
    cur.commit()'''
    
    #opening file to read contents and insert the read data into table
    files = open("EyeRecords.txt","r")
    files.seek(0)
    
    #the description of data stored in database
    describe=files.readline()
    
    # reading values from file that has to be inserted into SQL
    data = []
    record=[]
    for i in range(8):
        record=files.readline().split(",")
        record[0]=datetime.strptime(record[0],"%d %B %Y")
        record = tuple(record)
        data.append(record)
    
    # inserting values into table
    '''query = "INSERT INTO Patient(Date,name,age,gender,diagnosis,treatment) VALUES (?,?,?,?,?,?)"
    cur.executemany(query,data)
    cur.commit()'''
    
    #preparing name list
    name_list=[]
    query1="select name from Patient"
    result1 = cur.execute(query1)
    for ele in result1:
        name_list.append(ele[0])
        
    #displaying the tuples in database on the screen
    if name in name_list:
        query="select * from Patient where name=?"
        cur.execute(query,name)
        result = cur.fetchall()
        return jsonify({"Date":result[0][0],"Name":result[0][1],"Age":result[0][2],"Gender":result[0][3],
                        "Diagnosis":result[0][4],"Treatment":result[0][5]})
    else:
        return jsonify("Record doesn't exist")
                                                                        