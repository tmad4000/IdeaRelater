import math,operator

ideas={}


def autoRelate(idea1, idea2):
	#todo
	# extract concepts
	# pairwise numerical comparison of concepts
	# return sum of top 5 relations as score


	#Dumb mockup comparison

	i1Cs=idea1.rsplit()
	i2Cs=idea2.rsplit()

	score=0
	for i1 in i1Cs:
		for i2 in i2Cs:
			if i1==i2:
				score+=1
	score/=(len(i1Cs)*len(i2Cs)*1.0)


	rel=Edge(None,idea2,score)
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

class Edge:
	# val
	# target

	def __init__(self,val,target,weight=0):
		self.val=val
		self.target=target
		self.weight = weight

	def __str__(self):
		return "<"+str((self.weight,self.val))+">"+str(self.target)

# featureList=["good","awesome","bad","horrible","ok"]
#people=["jean", "joe", "jack", "nando", "nina", "nancy"]
featureList = ["jean", "joe", "nando", "nina"]

def sigmoid(x):
  return ((1/ (1 + math.exp(-x)))-.5)*2

def dotP(x,y):
	#Todo: check dimension
	# print x
	# print y
	if len(y) != len(x):
		raise Exception("vectors of different length!")
	return sum(map(operator.mul,x,y))

class Neuron:
	w = [0 for i in range(len(featureList))]
	a = 0.2	#learning rate

	def evalI(self,x):

		return sigmoid(dotP(self.w,x))

	def trainOne(self,x,d):
		delta = d-self.evalI(x)
		for i,wi in enumerate(self.w):
			self.w[i] += self.a*delta*x[i]

	def train(self,ds):
		for d in ds:
			self.trainOne(*d)

def wordsToFeatures(ws):

	fv=[0 for i in range(len(featureList))]

	for i,f in enumerate(featureList):
		if f in ws:
			fv[i]=1

	return fv

def dpToFv(datapoints):

	return map(lambda t: (wordsToFeatures(t[0]),t[1]),datapoints)


def testws(n,ws):
	print ws, n.evalI(wordsToFeatures(ws))

if __name__ == "__main__":

	datapoints = [
		(["good","awesome"],1),
		(["bad","horrible"],-1),
		(["bad","ok"],-1),
		(["good","ok"],1)
	]

	# fvDataPoints = map(lambda t: (wordsToFeatures(t[0]),t[1]),datapoints)

	# n = Neuron()
	# testws(n,["good"])
	# print n.w
	# n.train(fvDataPoints)
	# testws(n,["good"])
	# print n.w

	#siblings: jean joe  # nando nina 
	datapoints1 = [
		(["jean","joe"],1),
		(["jean","nando"],0),
		(["jean","nina"],0),
		(["nando","nina"],1),
	]

	people = featureList
	# \
	# -h0   
	# \	 \
	# -h1-o-

	d={}
	o = Neuron()

	h1 = Neuron([o])
	h0 = Neuron([o])

	inputLayer = [h0,h1]


	inp=dp
	q=[]
	while not empty q:
		n=q.pop()
		n.evalI(x)
		q.append(n.children)

	inp=dp
	for n in currLayer:
		if n.allInpSubmitted()
			n.takeAction()

	for n in neurons:
		n.next()

	if n.allInpSubmitted():
		if wdoti>0:
			self.fire()
		

		q.append(n.children)


	#fvN = [ Neuron([h0,h1]) for p in people ]
	fvDataPoints1 = dpToFv(datapoints1)
	
	h0,h1.trainOne()	

	# # build semantic network
	# ideas['cat']=Node("cat")
	# ideas['dog']=Node("dog")
	# ideas['animal']=Node("animal")
	# ideas['cat'].addConnection(Edge('isA',ideas['animal']))
	# ideas['dog'].addConnection(Edge('isA',ideas['animal']))
	# ideas['facebook'] = Node('facebook')


	# # test
	# idea1 = "facebook for cats"
	# idea2 = "facebook for dogs"
	# print "autoRelate('" + idea1 + "','"+idea2+"') = ",autoRelate(idea1,idea2)


	# ideaQuery = "facebook for parrots"
	# print "getRelatedIdeas('"+ideaQuery+"') = "
	# for i in getRelatedIdeas(ideaQuery):
	# 	print i
