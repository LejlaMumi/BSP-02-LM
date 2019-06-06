import pymysql

mydb= pymysql.connect(host='localhost',
        user='root',
        password='password',
        db='food')

mycursor = mydb.cursor()

sql = "SELECT Player_id, " \
      "COUNT(simplequestionstatistic_id) " \
      "FROM simplequestionstatistic_studentanswers " \
      "WHERE Player_id >1 GROUP BY Player_id"


mycursor.execute(sql)

myresults = mycursor.fetchall()

#for result in myresults :
 #   print("Student ID: ", result[0], "     ", "Number of Q: ", result[1])


#for result in myresults :
 #   print(result)