
#define variables globally so that it can be accessed from any other function
n=0
arr=[]
bui=[]
lazyT=[]
lazyA=[]
M=10**9+7
def AssUpdate(root,start,end,range_start,range_end,inc):
	if start > end: #base case return from recursion
		return
	if lazyT[root]!=0:#before going further down the tree update the tree
		bui[root]+=lazyT[root]*(end-start+1)#update the actual node
		bui[root]%(M)
		if(start!=end):#only you are not the end of the node push a littl further down
			lazyT[root*2]+=lazyT[root]
			lazyT[root*2+1]+=lazyT[root]
			lazyT[root]=0 #this node is not lazy anymore
	if lazyA[root]!=0:#before going further down the tree update the tree
		bui[root]=lazyA[root]*(end-start+1)#update the actual node
		bui[root]%(M)
		if(start!=end):#only you are not the end of the node push a littl further down
			lazyA[root*2]=lazyA[root]
			lazyA[root*2+1]=lazyA[root]
			lazyA[root]=0 #this node is not lazy anymore
	if (start > range_end or end < range_start):
		 return #no overlap return from this brance of the 
	if start >= range_start and end <= range_end:
		bui[root]=inc*(end-start+1)
		bui[root]=bui[root]%M
		if (start!=end):
			lazyT[root*2]=inc;
			lazyT[root*2+1]=inc;
		return
		
	AssUpdate(root*2,start,(start+end)//2,range_start,range_end,inc)
	AssUpdate(root*2+1,(start+end)//2+1,end,range_start,range_end,inc)
	bui[root]=bui[root*2] + bui[root*2+1]
	bui[root]%(M)
			
def SumUpdate(root,start,end,range_start,range_end,inc):
	if start > end: #base case return from recursion
		return
	if lazyT[root]!=0:#before going further down the tree update the tree
		bui[root]+=lazyT[root]*(end-start+1)#update the actual node
		bui[root]%(M)
		if(start!=end):#only you are not the end of the node push a littl further down
			lazyT[root*2]+=lazyT[root]
			lazyT[root*2+1]+=lazyT[root]
			lazyT[root]=0 #this node is not lazy anymore
	if lazyA[root]!=0:#before going further down the tree update the tree
		bui[root]=lazyA[root]*(end-start+1)#update the actual node
		bui[root]%(M)
		if(start!=end):#only you are not the end of the node push a littl further down
			lazyA[root*2]+=lazyA[root]
			lazyA[root*2+1]+=lazyA[root]
			lazyA[root]=0 #this node is not lazy anymore
	if (start > range_end or end < range_start):
		 return #no overlap return from this brance of the 
	if start >= range_start and end <= range_end:
		bui[root]+=inc*(end-start+1)
		bui[root]=bui[root]%M
		if (start!=end):
			lazyT[root*2]+=inc;
			lazyT[root*2+1]+=inc;
		return
		
	SumUpdate(root*2,start,(start+end)//2,range_start,range_end,inc)
	SumUpdate(root*2+1,(start+end)//2+1,end,range_start,range_end,inc)
	bui[root]=bui[root*2] + bui[root*2+1]
	bui[root]%(M)
			
def SumQuery(root,start,end,range_start,range_end):
	
	if start > end: # no overlap or base condition
		return 0
	
	if (lazyT[root]!= 0):
		bui[root]+=lazyT[root]*(end-start+1)
		bui[root]%(M)
		if start != end:
			lazyT[root*2]+=lazyT[root]
			lazyT[root*2+1]+=lazyT[root]
		lazyT[root]=0
	if lazyA[root]!=0:#before going further down the tree update the tree
		bui[root]=lazyA[root]*(end-start+1)#update the actual node
		bui[root]%(M)
		if(start!=end):#only you are not the end of the node push a littl further down
			lazyA[root*2]+=lazyA[root]
			lazyA[root*2+1]+=lazyA[root]
		lazyA[root]=0 #this node is not lazy anymore
	if end < range_start or start > range_end:
		return 0
	if start >= range_start and end <= range_end:
		return bui[root]
	q1=SumQuery(root*2,start, (start+end)//2,range_start,range_end)
	q1=q1%(M)
	q2=SumQuery(root*2+1,((start+end)//2) +1,end,range_start,range_end)
	q2=q2%(M)
	return int(q1+q2)%(M)
				

def build(root,start,end): #recursive build tree function

	if(start!=end):
		bui[root]=build(root*2,start,(start+end)//2)+build(root*2+1,(start+end)//2+1,end)
		#make a recursive call to sum the values of the two child node
		bui[root]=bui[root]%(M)
		return int(bui[root]%(M))#return the value at the node root
	if(start==end):#base case if the node is the leaf just assign the value of the array
		bui[root]=arr[start]
		return int(bui[root]%(M))
  

 #n=int(input("enter the number of elements in the array"))
try:
	N,Q = map(int, raw_input().split())

	#print(N,Q)
	arr=[0]*N
	arr[1:] = list(map(int, raw_input().split()))
	#print(arr)
	q=Q
	n=N
 #arr=[0]*n #create an array to hold n number of elements in the array
 #for i in range(n): #run the loop to 
  #arr[i]=int(input())#take input and assign it to the array


	bui=[0]*int(2*n)#if n is number of leaf then total number of nodes is  2*n-1 
	lazyT=[0]*int(2*n)
	lazyA=[0]*int(2*n)
	root=1 #tree node root
	start=1
	en=n#last member of array location
	sucess=build(root,start,en)#call the function

#SumUpdate(root,start,en,0,1,1)
#print("sumquery",SumQuery(root,start,en,0,1))
#print(bui)
	#print(bui)

	for i in range(q):
		#print(bui)
		qu = list(map(int, raw_input().split()))

		if(qu[0]==4):
			print(int(SumQuery(root,start,en,(qu[1]),(qu[2]))%(M)))
		elif(qu[0]==3):
			AssUpdate(root,start,en,(qu[1]),(qu[2]),qu[3])
		elif(qu[0]==1):
			SumUpdate(root,start,en,(qu[1]),(qu[2]),qu[3])
		else:
			zebra=1
except:
	pass
		
	



  
  

  
	
	
 
   
