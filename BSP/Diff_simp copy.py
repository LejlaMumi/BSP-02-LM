import pymysql

mydb= pymysql.connect(host='localhost',
        user='root',
        password='password',
        db='food')

mycursor = mydb.cursor()

# Players and questions and  how many of them were difficulty ≥ 0. SIMPLE question



sql=" SELECT difficulty, COUNT(studentAnswers) " \
     "FROM simplequestionstatistic_studentanswers " \
     "JOIN activity AS ac " \
     "JOIN simplequestion AS si " \
     "WHERE studentAnswers = solution " \
     "AND ac.dtype IN ('SimpleQuestion') " \
     "AND ac.difficulty >=0 " \
     "AND Player_id BETWEEN 1 AND 5 " \
     "GROUP BY difficulty" \
    " HAVING COUNT(studentAnswers) < 1000" \
    " ORDER BY difficulty DESC " \
    " LIMIT 2500; "



mycursor.execute (sql)

myresults = mycursor.fetchall()


#for result in myresults :
 #   print("Difficulty: ", result[0], "   ", "Q Sum: ", result[1])

#for result in myresults :
 #   print(result)