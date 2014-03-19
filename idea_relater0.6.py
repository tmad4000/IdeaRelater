ideas={}


def autoRelate(idea1, idea2):
	#todo
	# extract concepts
	# pairwise numerical comparison of concepts
	# return sum of top 5 relations as score


	#Dumb mockup comparison

	i1Cs=idea1.rsplit()
	i2Cs=idea2.rsplit()

	ptsOfTan=[]

	score=0
	for i1 in i1Cs:
		for i2 in i2Cs:
			if i1==i2:
				score+=1
				ptsOfTan.append(i1)
	score/=(len(i1Cs)*len(i2Cs)*1.0)


	rel=Edge(ptsOfTan,idea2,score)
	return rel


#args: @idea string, @ideas array of ideas to search, @max int max number of results
#returns: type (score,annotation); sorted array of related ideas and relations 
def getRelatedIdeas(idea, max=None):
	#todo 
	rels=map(lambda i2: autoRelate(idea,i2),ideas)
	rels=sorted(rels,key=lambda edge: edge.weight,reverse=True)
	return rels


class Node:
	# val
	# connections = []
	def addConnection(self,c):
		self.connections.append(c)

	def __init__(self,val=None):
		self.val=val
		self.connections = []

	def __str__(self):
		return self.val

class Node:
	# val
	# connections = []
	def addConnection(self,c):
		self.connections.append(c)

	def takeAction(self):
		if(self.o)
			connections.filter("respBy").open();

	def __init__(self,val=None):
		self.val=val
		self.connections = []

	def __str__(self):
		return self.val

	def activate(self):
		self.o=True

class TurnSubG(Node):

	def __init__(self,val=None,turnLG=None,turnRG=None):
		super(TurnSubG, self).__init__()
		self.turnLG=turnLG
		self.turnRG=turnRG

	def takeAction(self):
		if(self.o)
			if(math.random()>.5)
				self.turnLG.open()
			else
				self.turnRG.open()

class TurnSubG(Node):


class Edge:
	# val
	# target

	def __init__(self,val,target,weight=0):
		self.val=val
		self.target=target
		self.weight = weight

	def __str__(self):
		return "<"+str((self.weight,self.val))+">"+str(self.target)

if __name__ == "__main__":
	# build semantic network
	ideas['cat']=Node("cat")
	ideas['dog']=Node("dog")
	ideas['animal']=Node("animal")
	ideas['cat'].addConnection(Edge('isA',ideas['animal']))
	ideas['dog'].addConnection(Edge('isA',ideas['animal']))
	ideas['facebook'] = Node('facebook')


	# build semantic network
	ideas['touchG']=Node("touchG")
	ideas['turnLG']=Node("turnLG")
	ideas['turnRG']=Node("turnRG")
	ideas['turnSubG']=Node("turnSubG")

	ideas['turnSubG'].addConnection(Edge('respBy',ideas['turnRG']))
	ideas['cat'].addConnection(Edge('isA',ideas['animal']))
	ideas['cat'].addConnection(Edge('isA',ideas['animal']))
	ideas['dog'].addConnection(Edge('isA',ideas['animal']))
	ideas['facebook'] = Node('facebook')



	# test
	idea1 = "facebook for cats"
	idea2 = "facebook for dogs"
	print("autoRelate('" + idea1 + "','"+idea2+"') = ",autoRelate(idea1,idea2))


	ideaQuery = "facebook for parrots"
	print("getRelatedIdeas('"+ideaQuery+"') = ")
	for i in getRelatedIdeas(ideaQuery):
		print(i)
