import numpy as np
import math
PI = np.pi
#trans_mat = np.eye(4)
#end effect -51
def tmatrix (a,alpha,theta,d):
	temp = np.array([[np.cos(theta), -np.sin(theta)*np.cos(alpha), np.sin(theta)*np.sin(alpha), a*np.cos(theta)],
	[np.sin(theta), np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha), a*np.sin(theta)],
	[0, np.sin(alpha), np.cos(alpha), d],
	[0, 0, 0, 1]])
	return temp
def goalpos(theta1,theta2,theta3,theta4):
	trans_mat = np.eye(4)
	t1 = tmatrix(0,-PI * 0.5,theta1,65)
	t2 = tmatrix(129,0,-PI*(70/180.0)+theta2,0)
	t3 = tmatrix(65,0,(37/180.0)*PI+theta3,0)
	t4 = tmatrix(83,0,(54/180.0)*PI+theta4,0)
	trans_mat = np.dot(trans_mat,t1)
	trans_mat = np.dot(trans_mat,t2)
	trans_mat = np.dot(trans_mat,t3)
	trans_mat = np.dot(trans_mat,t4)
	return trans_mat
#print(np.dot(goalpos(0,0,0,0),[[189],[34],[-81],[1]]))