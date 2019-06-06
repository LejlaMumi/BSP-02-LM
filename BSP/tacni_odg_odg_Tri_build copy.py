import pymysql

mydb= pymysql.connect(host='localhost',
        user='root',
        password='password',
        db='food')

mycursor = mydb.cursor()

# most corect. SIMPLE question
sql = " SELECT buil.id, COUNT(studentAnswers)  " \
      " FROM buildpairs_studentanswer" \
      " JOIN buildpairs AS buil" \
      " WHERE studentAnswers = answers AND Player_id >=1 GROUP BY buil.id "

mycursor.execute (sql)

myresults = mycursor.fetchall()

#for result in myresults :
 #   print(result)
