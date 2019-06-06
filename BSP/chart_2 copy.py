import numpy as np
import matplotlib.pyplot as plt
import Tacni_odg_odg as naj

#using the results from folder Tacni odg odg
x = [id for id in naj.countQuestions(naj.result1, naj.result2, naj.result3)]
y = [naj.result1[id] for id in naj.countQuestions(naj.result1, naj.result2, naj.result3)]

#assigning name and color to the bars
plt.bar(x,y, label= 'Times played', color ='c')

#naming chart and naming x,y axis
plt.title('Qestions that have been answered correctly(Yactul usage data)')
plt.xlabel('Question Id')
plt.ylabel('Number of correct answers')
#assigning legend
plt.legend(loc='upper right')


plt.bar(x,y)
plt.show()

#import Jedan__foc,  Dva__simp , Tri_build | tacni_odg_odg_ :
# shows the activity id and how many times it was answered corect.
