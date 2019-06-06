import pymysql

mydb= pymysql.connect(host='localhost',
        user='root',
        password='password',
        db='food')

mycursor = mydb.cursor()

# most corect. SIMPLE question
sql = " SELECT sim.id, COUNT(studentAnswers)  " \
      " FROM simplequestionstatistic_studentanswers" \
      " JOIN simplequestion AS sim" \
      " WHERE studentAnswers = solution AND Player_id >=1 GROUP BY sim.id "

mycursor.execute (sql)

myresults = mycursor.fetchall()

#for result in myresults :
 #   print(result)
