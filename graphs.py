################################
#Chapger 9
#Plotting and Visualization
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy.random import randn
data = np.arange(10)
plt.plot(data)
#plt.show()

fig=plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 4) #to create facets (2x2) and selecting the 4th one
plt.plot([1.5, 3.5, -2, 1.6])

fig1=plt.figure()
ax22 = fig1.add_subplot(2, 2, 2)
ax11=fig1.add_subplot(2,2,1)
ax33=fig1.add_subplot(2,2,3)
plt.plot(np.random.randn(50).cumsum(), 'k--') #k-- dashed line
ax11.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
ax22.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
#plt.show()


fig, axes = plt.subplots(2, 2, sharex=True, sharey=True) #Another way of creating figure with subplots
axes[0,0].hist(np.random.randn(100), bins=20, color='k', alpha=0.3) #creating histogram on the subplot first column first row
axes[1,1].scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
#plt.show()

figQ, axes1 =plt.subplots(2, 2, sharex=True, sharey=True)
axes1[0,0].plot(range(1,21), [-1,2,5,10,-3,-9,8,6,10,1,2,2,3,0,0,-9,-2,5,7,1], color='m', linestyle='--')
axes1[0,1].scatter(np.arange(20), np.arange(20) + 3 * np.random.randn(20))
plt.subplots_adjust(wspace=0.1, hspace=0.1)
plt.ylim([-10,10])
#plt.show()

data = np.random.randn(30).cumsum()
plt.plot(data, 'k--', label='Default')
plt.plot(data, 'k-', drawstyle='steps-post', label='steps-post')
plt.legend(loc='best')
#plt.show()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(np.random.randn(1000).cumsum())
ticks = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'],rotation=30, fontsize='small')
ax.set_title('My first matplotlib plot')
ax.set_xlabel("Stage")
ax.set_ylabel("Output change")
#plt.show()

#Adding legend
#Use 'legend' argument
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(randn(1000).cumsum(), 'k',label="one")
ax.plot(randn(1000).cumsum(), 'm--',label="two")
ax.plot(randn(1000).cumsum(), 'r.', label="three")
ax.legend(loc="best")
plt.savefig('figpath.png', dpi=400, bbox_inches='tight')
#plt.show()


ax.legend



fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
a=pd.DataFrame({"Name":[6,12,0,1,7,11,-1,-2,-5,6]},index=range(1,11))
a.plot(ax=ax, style='k-')
ax.annotate("loc min", xy=(9,-5), xytext=(4,-5),arrowprops=dict(facecolor='black', headwidth=4, width=2,headlength=4),horizontalalignment='left', verticalalignment='top')
#plt.show()


#Seaborn library
import seaborn as sns
s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
s.plot()


df = pd.DataFrame(np.random.rand(6, 4),index=['one', 'two', 'three', 'four', 'five', 'six'],columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
df.plot.bar(stacked=True, alpha=0.5)
#plt.show()




exdata=pd.read_excel("exampledata.xlsx")
exdata.loc[exdata["Name"]=="Elena","Age"]=38
exdata.loc[exdata["Name"]=="Jerry", "Age"]=33
exdata["Sex"]=["F","M","F","M","M","F"]
print(exdata)
exdata1=exdata
figp=plt.figure()
ax01=figp.add_subplot(1,1,1)
ax01.bar(exdata["Name"], exdata["Age"])
plt.show()
col=["orange" if x=="F" else "blue" for x in exdata["Sex"]]
sns.barplot(x="Salary", y="Name", data=exdata, orient="h")
plt.show()
exdata["Salary"].plot.hist()

plt.show()

figp1=plt.figure()
ax011=figp1.add_subplot(1,1,1)
sns.regplot(x="Age",y="Salary",data=exdata1)
plt.show()

figp1=plt.figure()
ax011=figp1.add_subplot(1,1,1)
sns.pairplot(exdata, diag_kind='kde', plot_kws={'alpha': 0.2})
plt.show()

figp1=plt.figure()
ax011=figp1.add_subplot(1,1,1)
sns.catplot(x='Name', y='Salary', col='Sex',kind='bar', data=exdata)
plt.show()