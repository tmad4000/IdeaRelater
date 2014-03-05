ideas={}


def autoRelate(idea1, idea2):
	#todo
	# extract concepts
	# pairwise numerical comparison of concepts
	# return sum of top 5 relations as score


	#Dumb mockup comparison
	rel=None

	i1Cs=idea1.rsplit()
	i2Cs=idea2.rsplit()

	score=0
	for i1 in i1Cs:
		for i2 in i2Cs:
			if i1==i2:
				score+=1
	score/=(len(i1Cs)*len(i2Cs)*1.0)
	return (score,rel);


#args: @idea string, @ideas array of ideas to search, @max int max number of results
#returns: type (score,annotation); sorted array of related ideas and relations 
def getRelatedIdeas(idea, ideas,max=None):
	#todo 
	rels=map(lambda i2: autoRelate(idea,i2),ideas)
	rels=sorted(rels)
	return rels


class Node:
	val
	connections = []
	def addConnection(c):
		connections.append(c)

	__init__(self,val=None):
		self.val=val

	def __string__(self):
		return self.val

class Edge:
	val
	target

	__init__(self,val,target):
		self.val=val
		self.target=target

	def __string__(self):
		return self.val

if __name__ == "__main__":
	# build semantic network
	ideas['cat']=Node("cat")
	ideas['dog']=Node("dog")
	ideas['animal']=Node("animal")
	ideas['cat'].addConnection(Edge('isA',ideas['animal']))
	ideas['dog'].addConnection(Edge('isA',ideas['animal']))
	ideas['facebook'] = Node('facebook')


	# test
	idea1 = "facebook for cats"
	idea2 = "facebook for dogs"
	print autoRelate(idea1,idea2)


	ideaQuery = "facebook for parrots"
	print getRelatedIdeas(ideaQuery)
