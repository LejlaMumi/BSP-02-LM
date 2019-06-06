
import Count_Simplefocus as game2, Count_Buildpairs as game1, Count_Simplequestion as game3

result1 = dict(game1.myresults)
result2 = dict(game2.myresults)
result3 = dict(game3.myresults)
#result4 = dict(game4.myresults)
#result5 = dict(game5.myresults)
#result6 = dict(game6.myresults)



def countGames(res1, *results):
    # go through all the results that are passed in
    for player in res1:
        # go through the results and grab the number of player wins
        # and add them to the first list
        for result in results:
            if player in result:
              res1[player] += result[player]
    # return total number of wins
    return res1

if __name__ == "__main__":

    for id in countGames(result1,result2,result3) :
        print("Student ID: ", id, "   ", "Number of activity: ", result1[id])

#it counts how many questions have been answered