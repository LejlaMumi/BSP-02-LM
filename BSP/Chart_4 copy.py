import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
#related third party import
from name_NM_course import mynewresult as nm
from name_SR_course import myresults as sr
from name_MP_course import myresults as mp


creators = ('steffen.rothkugel', 'mike.pereira', 'nicolas.mayer')
y_pos = np.arange(len(creators))
#theSum = [sr.myresults, mp.myresults, mn.myresults]
theSum = [sr, mp, nm]


plt.bar(y_pos, theSum, align='center', alpha=0.3, width = .4, label =(' Programming 1'))
plt.xticks(y_pos, creators)
plt.ylabel('The sum ')
plt.title('Created quizes for course : Programing 1')
plt.legend(loc='upper right')
plt.show()




