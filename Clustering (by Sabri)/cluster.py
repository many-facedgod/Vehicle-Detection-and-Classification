import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


from sklearn.cluster import KMeans
from sklearn import datasets

np.random.seed(5)

centers = [[1, 1], [-1, -1]]

labels=[]
labels.append(0)

X=np.array([0.0,0.0])
mxX=-1.0
mxY=-1.0
mnX=1000000.0
mnY=1000000.0

with open('points.txt') as f:
	for line in f:
		x,y,label = line.strip().split()
		x=float(x)
		y=float(y)
		labels.append(label)
		mxX=max(x,mxX)
		mxY=max(y,mxY)
		mnX=min(x,mnX)
		mnY=min(y,mnY)
		X=np.vstack((X,np.array([float(x),float(y)])))



for i in range(0,len(X)):
	X[i][0]-=mnX
	X[i][0]/=(mxX-mnX)
	X[i][1]-=mnY
	X[i][1]/=(mxY-mnY)
	X[i][1]*=0.100
	X[i][0]*=0.0


est=KMeans(n_clusters=2)
est.fit(X)



colors = ['#4EACC5', '#FF9C34']
plt.figure()
plt.hold(True)

x1=[]
x2=[]
y1=[]
y2=[]

# ff=open('opp45.txt','w')

for i in range(1,len(X)):
	clstr=est.predict(X[i])[0]
	# ff.write(str(labels[i])+' : '+str(clstr)+'\n')
	if clstr==0:
		x1.append(X[i][0])
		y1.append(X[i][1])
	else:
		x2.append(X[i][0])
		y2.append(X[i][1])
	
# ff.flush()
plt.scatter(x1,y1,color=colors[0])
plt.scatter(x2,y2,color=colors[1])

plt.grid(True)
plt.show()
