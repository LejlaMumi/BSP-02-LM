import numpy as np
import matplotlib.pyplot as plt
import Diff_foc as foc
import Diff_simp as sim
import Diff_buil as buil
#I wanted to use each table separate, show them separately on the chart
#

#using the results from folder Diff_foc - data to plot
# extract respectively x and y values from the list of tuples in myresults
x = [i[0] for i in foc.myresults]
y = [i[1] for i in foc.myresults]


#using the results from folder Diff_vek_simp - data to plot
x2 = [i[0] for i in sim.myresults]
y2 = [i[1] for i in sim.myresults]

#using the results from folder Diff_buil - data to plot
x3 = [i[0] for i in buil.myresults]
y3 = [i[1] for i in buil.myresults]

#assigning name and color to the bars
ax = plt.subplot(111)
ax.bar([i-.25 for i in x],y, label= 'Simple focus activity ', width=0.2, color='b')
ax.bar(x2,y2, label= 'Simple question activity  ', width=0.2, color='g')
ax.bar([i+.25 for i in x3],y3, label= 'Build pairs activity ', width=0.2, color='r')
#i-25 is offesting the x coordinate of the bar , that way they are not overlapping
# but next to each other.

#assigning name to the x,y axis
plt.xlabel('Difficulty level')
plt.ylabel('Sum of activities')

#naming the chart and assigning legend
plt.title('Sum of correctly answered activities with difficulty ≥0 (Yactul usage data)')
plt.legend(loc='upper right')

#plt.yticks(np.arange(0, 8001, 500))


plt.show()
#imports:  Players and questions and  how many of them were difficulty ≥ 0. SIMPLE question

