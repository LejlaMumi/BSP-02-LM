import pymysql
# imports random module
from random import randint

#database connection
mydb= pymysql.connect(host='localhost',
        user='root',
        password='password',
        db='food')
mycursor = mydb.cursor()


def getQuestion(id):
    sql = f'SELECT simplequestionstatistic_id FROM simplequestionstatistic_studentanswers  WHERE ID = {id}'
    mycursor.execute(sql)
    myresults = mycursor.fetchall()
    return myresults[0][0]


def tableLength():
    sql = 'SELECT simplequestionstatistic_id FROM simplequestionstatistic_studentanswers'
    mycursor.execute(sql)
    myresults = mycursor.fetchall()
    return len(myresults)



def fillRandID(lastID, rangeID=60):
    questions = {}

    for answer in range(1, tableLength()+1):

        # manage the dictionary
        questionNumber = getQuestion(answer)
        if questionNumber not in questions:
            questions[questionNumber] = []

        # generate ID numbers that do not repeat
        random_playerID = randint(1,rangeID)
        while random_playerID in questions[questionNumber]:
            random_playerID = randint(1,rangeID)

        # keep track of IDs and place it in table
        questions[questionNumber].append(random_playerID)
        sql = "UPDATE simplequestionstatistic_studentanswers SET Player_id = {} WHERE ID = {}".format(random_playerID, answer)
        mycursor.execute(sql)
        mydb.commit()


if __name__ == '__main__':
    fillRandID(148)
    # print(tableLength())
