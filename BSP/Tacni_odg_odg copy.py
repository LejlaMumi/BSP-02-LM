
import tacni_odg_odg_Jedan_foc as sol1, tacni_odg_odg_Dva_simp as sol2, tacni_odg_odg_Tri_build as sol3

result1 = dict(sol1.myresults)
result2 = dict(sol2.myresults)
result3 = dict(sol3.myresults)
#result4 = dict(game4.myresults)
#result5 = dict(game5.myresults)
#result6 = dict(game6.myresults)



def countQuestions(res1, *results):
    for Question in res1:
        for result in results:
            if Question in result:
              res1[Question] += result[Question]
    return res1

if __name__ == "__main__":

    for id in countQuestions(result1,result2,result3) :
        print("Question ID: ", id, "   ", "corect answ.: ", result1[id])
