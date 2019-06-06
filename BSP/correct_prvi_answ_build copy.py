import pymysql

mydb= pymysql.connect(host='localhost',
        user='root',
        password='password',
        db='food')

mycursor = mydb.cursor()

# Players who answered corect and the solutions. BUILD PAIRS
sql = " SELECT Player_id, COUNT(studentAnswers) " \
      " FROM buildpairs_studentanswer " \
      " JOIN buildpairs" \
      " WHERE studentAnswers = answers AND Player_id >= 1 GROUP BY Player_id "

mycursor.execute (sql)

myresults = mycursor.fetchall()

#for result in myresults :
 #   print(result)

