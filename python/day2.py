# numpy , pandas, seaborn, data time , Math

# ...........Numpy Starts here.............#
# 1.Numpy : it is used during workig on arrays
import numpy as np
list1=[1,2,3,4,5]
a=np.array(list1)
b=np.array([1,2,3],[4,5,6])
# c=np.array([[1,2,3],[4,,5,6],[5,4,3]])

# identity matrix 5*5 with all zeros
np.zeros((5,5)) 
np.ones((10,10))

np.full((2,3),10)

# prints from 0-9
np.arrange(0,10)
np.arrange(1,10,2)

np.random.randint(100,200,10)

n2=np.array([10,20,30,40,50])
n2+2
n2-2
n2*2
n2/2

# ............numpy ends hrer......#

# ...........pandas Starts here.........#
import pandas as pd
# 1-d is called as series and 2-d, 3-d are called as data frame
series1=pd.Series([1,2,3,4,5],index=["a","b","c","d","e"])
type(series1)

series1[3]
series1[-2]
series1[0:3]

series1+5

series2=pd.Series([1,2,3,4,5])
series3=pd.Series([5,6,7,8,9])
series2+series3

pd.DataFrame({"name":["bob", "sam", "essi"],"marks":[72,89,56]})
# .....pandas end here......#

df=pd.read_excel("295Employee Data.xlsx")

df.describe()

df.iloc[0:3,0:2]
df.loc[0:3,"Age","Job"]

df.drop("Exit Data" ,axis=1)

df["Job title"].value_counts

# ...matplotlib starts here........#

import matplotlib as m

# 
student={"bob":87,"sam":90, "raj":78}
names=list(student.keys())
marks=list(student.values)

plt.bar(names,marks)
plt.show()

# scattering graph
x=[10,20,30,40,50]
y=[20,30,40,50,60]
plt.scatter(x,y)
plt.show()

# pie chart
fruits=["apples","banana", "mango","watermelon"]
quantity=[90,30,50,80]
plt.pie(quantity,Labels=fruits)
plt.show()

#.......matplot lib ends here......#
import seaborn as sns

df2=sns.load_dataset("fmri")

df2.head()

sns.lineplot(x="timepoint", y="signal", data=df2)
plt.show()

sns.barplot(x="region", y="signal", data=df2)
plt.show()

# ............Math starts here.......#
import math

math.sqrt(2)

math.log(2)