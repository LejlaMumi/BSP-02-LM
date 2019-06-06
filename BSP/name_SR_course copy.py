import pymysql

mydb= pymysql.connect(host='localhost',
        user='root',
        password='password',
        db='food')

mycursor = mydb.cursor()

#sql = "SELECT DISTINCT creator, COUNT(name) FROM quiz WHERE creator = 'steffen.rothkugel'  GROUP BY creator  " \

#sql = " SELECT DISTINCT name FROM quiz WHERE CREATOR = 'steffen.rothkugel' "


#you can see how many quizes have been made by SR in the course:programming1
sql= "SELECT COUNT(qui.name) " \
     "FROM quiz AS qui " \
     "JOIN quizgroup AS gr " \
     "ON quizgroup_id = gr.id " \
     "WHERE gr.name =  'course:programming1' " \
     "AND gr.creator = 'steffen.rothkugel'"

mycursor.execute (sql)

myresults = mycursor.fetchall()



#for result in myresults :
 #   print(result)
