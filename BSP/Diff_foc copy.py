import pymysql

mydb= pymysql.connect(host='localhost',
        user='root',
        password='password',
        db='food')

mycursor = mydb.cursor()

# Players and questions and  how many of them were difficulty ≥ 0. SIMPLE FOCUS

#IT'S FUCKING WORKING

sql= " SELECT difficulty, COUNT(studentAnswers) " \
     "FROM simplefocusstatistic_studentanswers " \
     "JOIN activity AS ac " \
     "JOIN simplefocus AS si " \
     "WHERE studentAnswers = solution " \
     "AND ac.dtype IN ('SimpleFocus') " \
     "AND ac.difficulty >=0 " \
     "AND Player_id BETWEEN 1 AND 20 " \
     "GROUP BY difficulty "

mycursor.execute (sql)

myresults = mycursor.fetchall()
#print(myresults)

#for result in myresults :
 #   print("Difficulty: ", result[0], "   ", "Q Sum: ", result[1])

#for result in myresults :
 #   print(result)


