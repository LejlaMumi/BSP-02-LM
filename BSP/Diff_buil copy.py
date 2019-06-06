import pymysql

mydb= pymysql.connect(host='localhost',
        user='root',
        password='password',
        db='food')

mycursor = mydb.cursor()

# Players and questions and  how many of them were difficulty ≥ 0. SIMPLE question

#IT'S FUCKING WORKING

sql= " SELECT difficulty, COUNT(studentAnswers) " \
     "FROM buildpairs_studentanswer " \
     "JOIN activity AS ac " \
     "JOIN buildpairs AS bi " \
     "WHERE studentAnswers = answers " \
     "AND ac.dtype IN ('BuildPairs') " \
     "AND ac.difficulty >=0 " \
     "AND Player_id BETWEEN 1 AND 20 " \
     "GROUP BY difficulty "

mycursor.execute (sql)

myresults = mycursor.fetchall()



#for result in myresults :
 #   print("Difficulty: ", result[0], "   ", "Q Sum: ", result[1])

#for result in myresults :
 #   print(result)



