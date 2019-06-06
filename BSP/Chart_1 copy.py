import numpy as np
import matplotlib.pyplot as plt
import vek
import corr

#using the results from folder vek

#This creates a list using list comprehension,
# it appends every id vek.countGames() returns to the list x
x = [id for id in vek.countGames(vek.result1, vek.result2, vek.result3)]
#This creates a list using list comprehension containing vek.result1[id]
# with id returned from vek.countGames()
y = [vek.result1[id] for id in vek.countGames(vek.result1, vek.result2, vek.result3)]

#creates a list out of IDs colected from the vek.result1,2,3


#using the results from folder corr
x2 = [id for id in corr.countAnswers(corr.result1, corr.result2, corr.result3)]
y2 = [corr.result1[id] for id in corr.countAnswers(corr.result1, corr.result2, corr.result3)]

#assigning name and color to the bars
plt.bar(x2,y2, label= 'Correct answered activities ', color ='b')
plt.bar(x,y, label= 'Answered activities ', color='c', alpha=0.85)


#assigning name to the x,y axis
plt.xlabel('Player ID')
plt.ylabel('Sum of played activities')

#naming the chart and assigning legend
plt.title('Correctly answered activities per player (Yactul usage data)')
plt.legend(loc='upper right')



plt.show()
#PRVI, DRUGI, TRECI| correct answ: shows the number of correct answered activity and Player_id} Corr
#BIL, FOC, ANSW | count : shows the number of player activity and Player_id } vek