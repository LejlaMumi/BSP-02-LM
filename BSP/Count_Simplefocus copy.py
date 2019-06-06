import pymysql

mydb= pymysql.connect(host='localhost',
        user='root',
        password='password',
        db='food')

mycursor = mydb.cursor()

sql = "SELECT DISTINCT Player_id, " \
      "COUNT(simplefocusstatistic_id) " \
      "FROM simplefocusstatistic_studentanswers " \
      "WHERE Player_id < 30 GROUP BY Player_id"


mycursor.execute(sql)

myresults = mycursor.fetchall()

#for result in myresults :
 #   print("Student ID: ", result[0], "     ", "Number of Q: ", result[1])
