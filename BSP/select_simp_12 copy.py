import pymysql

mydb= pymysql.connect(host='localhost',
        user='root',
        password='password',
        db='food')

mycursor = mydb.cursor()

sql = "SELECT Player_id FROM simplefocusstatistic_studentanswers  WHERE simplefocusstatistic_id = 3" \

mycursor.execute (sql)

myresults = mycursor.fetchall()

for result in myresults :
    print(result)
