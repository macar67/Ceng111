
def is_firmus(l1,l2):
	if l1[1]<=l1[3]:
		if l2[1]<=l2[3]:
			if l1[1]<=l2[1]:
				smallest=l1[1]
				lowerrectangle=l1
				upperrectangle=l2	
			else:
				smallest=l2[1]
				lowerrectangle=l2
				upperrectangle=l1
		else:
			if l1[1]<=l2[3]:
				smallest=l1[1]
				lowerrectangle=l1
				upperrectangle=l2
	
			else:
				smallest=l2[3]
				lowerrectangle=l2
				upperrectangle=l1
	if l1[3]<=l1[1]:
		if l2[1]<=l2[3]:
			if l1[3]<=l2[1]:
				smallest=l1[3]
				lowerrectangle=l1
				upperrectangle=l2
					
			else:
				smallest=l2[1]
				lowerrectangle=l2
				upperrectangle=l1
		else:
			if l1[1]<=l2[3]:
				smallest=l1[1]
				lowerrectangle=l1
				upperrectangle=l2
			else:
				smallest=l2[3]
				lowerrectangle=l2
				upperrectangle=l1
				
	

	mx,my=(upperrectangle[0]+upperrectangle[2])/2,abs(upperrectangle[1]+upperrectangle[3])/2
	#print mx,my

	if lowerrectangle[1]==0 or lowerrectangle[3]==0: 
		firstCondition=1
	else:
		firstCondition=0			

	
	if lowerrectangle[2]<=mx<=lowerrectangle[0] or lowerrectangle[2]>=mx>=lowerrectangle[0]:
		thirdCondition=1
	
			
	else:
		thirdCondition=0
	
		
	#2.condition 
	
	if upperrectangle[1]<=upperrectangle[3]:
		small_y=upperrectangle[1]
	else:
		small_y=upperrectangle[3]
		 
	if lowerrectangle[1]>=lowerrectangle[3]:
		big_y=lowerrectangle[1]
	else:
		big_y=lowerrectangle[3]
	#print small_y,big_y
	
	if small_y==big_y:
		secondCondition=1
	else: 
		secondCondition=0
		
	x=abs(upperrectangle[0]-upperrectangle[2])
	y=abs(upperrectangle[1]-upperrectangle[3])
	z=abs(lowerrectangle[0]-lowerrectangle[2])
	w=abs(lowerrectangle[1]-lowerrectangle[3])
	
	area=float(x*y+z*w)
	
	if (firstCondition==1 and secondCondition==1 and thirdCondition==1):
		return ["FIRMUS", area]
	

	elif (firstCondition==1 and secondCondition==1 and thirdCondition==0) :
		
		##################xxxxxxxxxxxxxxxx###########
		
		if(lowerrectangle[0]<lowerrectangle[2]):
			left_lx=lowerrectangle[0]
			right_lx=lowerrectangle[2]
		else:
			left_lx=lowerrectangle[2]
			right_lx=lowerrectangle[0]
			
		if(upperrectangle[0]>upperrectangle[2]):
			right_ux=upperrectangle[0]
			left_ux=upperrectangle[2]
		else:
			right_ux=upperrectangle[2]
			left_ux=upperrectangle[0]
			
	        ############yyyyyyyyyyyyyyyy#############
		
		
			
		if(upperrectangle[1]>upperrectangle[3]):
			big_uy=upperrectangle[1]
			small_uy=upperrectangle[3]
		else:
			big_uy=upperrectangle[3]
			small_uy=upperrectangle[1]
		
		
		########################################	
			
		if(mx<left_lx):
			a=2*(left_lx-mx)+right_ux
			return ["ADDENDUM", [right_ux,small_uy,a,big_uy]]  #[right_ux,small_uy,a,big_uy]
		
		elif(mx>right_lx):
			
			a=left_ux-2*(mx-right_lx)
			return ["ADDENDUM",[left_ux,small_uy,a,big_uy]]
				
		
		
		
		
		
		
	
	else:
		
			if(max(upperrectangle[0],upperrectangle[2])<max(lowerrectangle[0],lowerrectangle[2]) and	min(upperrectangle[0],upperrectangle[2])>min(lowerrectangle[0],lowerrectangle[2]) and min(upperrectangle[1],upperrectangle[3])>min(lowerrectangle[1],lowerrectangle[3]) and max(upperrectangle[1],upperrectangle[3])<max(lowerrectangle[1],lowerrectangle[3]) ):
				
				
				newarea=abs(lowerrectangle[0]-lowerrectangle[2])*abs(lowerrectangle[1]-lowerrectangle[3])
				return ["DAMNARE", newarea]

			elif(max(upperrectangle[0],upperrectangle[2])<max(lowerrectangle[0],lowerrectangle[2]) and	min(upperrectangle[0],upperrectangle[2])>min(lowerrectangle[0],lowerrectangle[2])and min(upperrectangle[1],upperrectangle[3])<max(lowerrectangle[1],lowerrectangle[3])):
				h=max(lowerrectangle[1],lowerrectangle[3])-min(upperrectangle[1],upperrectangle[3])		
				t=abs(upperrectangle[0]-upperrectangle[2])
				newarea=area-(h*t)
				
			
				return ["DAMNARE", newarea]	
			elif(max(upperrectangle[0],upperrectangle[2])>max(lowerrectangle[0],lowerrectangle[2]) and	min(upperrectangle[0],upperrectangle[2])<min(lowerrectangle[0],lowerrectangle[2]) and min(upperrectangle[1],upperrectangle[3])<max(lowerrectangle[1],lowerrectangle[3]) and min(upperrectangle[1],upperrectangle[3])<max(lowerrectangle[1],lowerrectangle[3])  ):
				
				t=abs(lowerrectangle[0]-lowerrectangle[2])
				h=abs(upperrectangle[1]-upperrectangle[3])
				newarea=area-(h*t)
			
			 
				return ["DAMNARE", newarea]	#correct
			
			
		
					
			
			
			elif(max(upperrectangle[0],upperrectangle[2])>max(lowerrectangle[0],lowerrectangle[2]) and	min(upperrectangle[0],upperrectangle[2])<min(lowerrectangle[0],lowerrectangle[2]) and min(upperrectangle[1],upperrectangle[3])<max(lowerrectangle[1],lowerrectangle[3])):
				
				t=abs(lowerrectangle[0]-lowerrectangle[2])
				h=max(lowerrectangle[1],lowerrectangle[3])-min(upperrectangle[1],upperrectangle[3])
				newarea=area-(h*t)
			
			 
				return ["DAMNARE", newarea]
	
			elif(max(upperrectangle[0],upperrectangle[2])>max(lowerrectangle[0],lowerrectangle[2]) and	min(upperrectangle[0],upperrectangle[2])>min(lowerrectangle[0],lowerrectangle[2]) and min(upperrectangle[1],upperrectangle[3])<max(lowerrectangle[1],lowerrectangle[3])):
				t=abs(max(lowerrectangle[0],lowerrectangle[2])-min(upperrectangle[0],upperrectangle[2]))
				h=max(lowerrectangle[1],lowerrectangle[3])-min(upperrectangle[1],upperrectangle[3])
				newarea=area-(h*t)
				return ["DAMNARE", newarea]#correct
				
					
			elif(max(upperrectangle[0],upperrectangle[2])<max(lowerrectangle[0],lowerrectangle[2]) and	min(upperrectangle[0],upperrectangle[2])<min(lowerrectangle[0],lowerrectangle[2]) and min(upperrectangle[1],upperrectangle[3])<max(lowerrectangle[1],lowerrectangle[3])):
				t=abs(max(upperrectangle[0],upperrectangle[2])-min(lowerrectangle[0],lowerrectangle[2]))
				h=max(lowerrectangle[1],lowerrectangle[3])-min(upperrectangle[1],upperrectangle[3])
				
				newarea=area-(h*t)
				return ["DAMNARE", newarea]#correct

			
		 	
	return ["DAMNARE", area]




