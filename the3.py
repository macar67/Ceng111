#
# WRITE YOUR CODE HERE AND SEND ONLY THIS FILE TO US.
#
# DO NOT DEFINE get_data() OR ANYTHING IN draw.py HERE AGAIN

from evaluator import *
from draw import *
import math
mydata=[]
mydata=get_data()

def new_move():
	"""Function that calculates the position updates.
       * Returns [[Delta_x1, Delta_y2], ..., [Delta_xm, Delta_ym]]"""

	# You will need to call "get_data()" in this function once at the beginning.
	
	#@TODO: FILL IN THIS FUNCTION
	
	#initiliaze
	
	#get_data()
	global mydata
	
	nokta=[]
	
	
	G=mydata[0]  # we take G value in the list
	Delta_T=mydata[1]  # we take unit time value in the list
	for i in range(2,len(mydata)):   # we are finding each element
		nokta.append(mydata[i])
			
		#print G,Delta_T,nokta[0]

	
		
	# F_1= Rrt+delta_t=rt+delta_t*v
	# F_2= Vt +delta_t=Vt+delta_t*F/m
	# F_3= ?

	# After these forces affect your points new positions are returned!!

	#some initialize lists

	mass=[]
	#old_rx
	old_rx=[]
	#old_ry
	old_ry=[]
	#vx
	vx=[]
	#vy
	vy=[]


	for j in range(len(nokta)):         # there are 5 list  mass,old_rx,old_ry,vx,vy 
						# each list hold all values for all data
		mass.append(nokta[j][0])
		old_rx.append(nokta[j][1])
		old_ry.append(nokta[j][2])
		vx.append(nokta[j][3])
		vy.append(nokta[j][4])
	

		
	 
	toplamx=0
	toplamy=0
	new_toplamx=[]
	new_toplamy=[]
	#F_sumx
	F_sumx=[]
	#F_sumy
	F_sumy=[]

	
	rx=[]
	ry=[]
	for k in range(len(nokta)):
		rx.append(old_rx[k]+vx[k]*Delta_T)
		ry.append(old_ry[k]+vy[k]*Delta_T)
		



	for i in range(len(nokta)):
		for j in range(len(nokta)):
			
			if i==j: 
				continue
			else:
				
				dx=(old_rx[j]-old_rx[i])**2
				dy=(old_ry[j]-old_ry[i])**2 
				
				
				if old_rx[i]>old_rx[j]:
					toplamx=toplamx-(mass[j]/((dx+dy)**0.5)**3)*abs(old_rx[j]-old_rx[i])
					
					
				else:				
					toplamx=toplamx+(mass[j]/((dx+dy)**0.5)**3)*abs(old_rx[j]-old_rx[i])
					
					
				if old_ry[i]>old_ry[j]:
					
					toplamy=toplamy-(mass[j]/((dx+dy)**0.5)**3)*abs(old_ry[j]-old_ry[i])
					
				else:				
					
					toplamy=toplamy+(mass[j]/((dx+dy)**0.5)**3)*abs(old_ry[j]-old_ry[i])
				
				
		new_toplamx.append(toplamx)
		new_toplamy.append(toplamy)
		F_sumx.append(G*mass[i]*new_toplamx[i])
		F_sumy.append(G*mass[i]*new_toplamy[i])
		toplamx=0
		toplamy=0
	#print new_toplamx
	
	#print F_sumx,F_sumy
	#print new_toplamx,new_toplamy

	


	#second formula
	for m in range(len(nokta)):
		vx[m]=vx[m]+(F_sumx[m]/mass[m])*Delta_T
		vy[m]=vy[m]+(F_sumy[m]/mass[m])*Delta_T

	#print vx


	
	
	
	
	for j in range(2,len(mydata)):

			mydata[j][1]=rx[j-2]
			mydata[j][2]=ry[j-2]
			mydata[j][3]=vx[j-2]
			mydata[j][4]=vy[j-2]

	
	
	
	
	
	
	#print mydata
	lastlist=[]
	for i in range(len(rx)):
		lastlist.append([rx[i]-old_rx[i],ry[i]-old_ry[i]])

	
	#print lastlist
	return lastlist              
 	
	
