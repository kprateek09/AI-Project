from pylab import *
import pandas as pd
# import csv

def main():
	with open('input.txt',encoding="utf8") as f:
		a=[]
		# count=1
		for i in f:
			data = i.split()
			a.append(data)
	# print (a)		

	T2 = [list(map(int, x)) for x in a]
	# print(T2)
	algo(T2)

def algo(d):
	trainingData = pd.DataFrame(data=d,columns =['x0', 'x1', 'x2', 'x3','x4', 'y'])
	X = trainingData[['x0', 'x1', 'x2', 'x3','x4']]
	y = trainingData[['y']]
	xTx = X.T.dot(X)
	XtX = pinv(xTx)
	XtX_xT = XtX.dot(X.T)
	theta = XtX_xT.dot(y)
	print(theta)
	# print (theta[0][0])
	m = int(input('Conditions:'))
	n = int(input('Humidity'))
	o = int(input('Temperature'))
	p = int(input('Visibilty'))
	h = (1*theta[0][0])+(m*theta[1][0])+(n*theta[2][0])+(o*theta[3][0])+(p*theta[4][0])
	# print (h)
	print('The chances of playing is :',h*100)
	if(h<0.5):
		h=0
	else:
		h=1
	print('Probability of playing is :',h)

	with open('input.txt','a') as i:
		i.write(str(1)+'\t'+str(m)+'\t'+str(n)+'\t'+str(o)+'\t'+str(p)+'\t'+str(h)+'\n')


main()
