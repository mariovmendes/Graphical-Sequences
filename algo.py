import graphviz

# Função Auxiliar que permite ler todos os números da sequência e
# ordená-los por ordem decrescente 
def readSequence():
	sequence = list(map(int, input().split(" ")))
	sequence.sort(reverse=True)
	print()
	print("Sorted sequence: "+ str(sequence))
	print()
	return sequence

# Função Auxiliar que verifica se todos os valores da sequência
# estão dentro dos valores permitidos para serem uma sequência gráfica
def acceptableRange(sequence):
	if not(len(sequence)-1 >= sequence[0] and sequence[len(sequence)-1] >= 0):
		print("Error - outside range!")
	return len(sequence)-1 >= sequence[0] and sequence[len(sequence)-1] >= 0

def degreeSumIsEven(sequence):
	if not(sum(sequence) % 2 == 0):
		print("Error - Sum of degress is not even!")
	return sum(sequence) % 2 == 0

def hasRepeatedDegress(sequence):
	repeated = False
	for x in sequence:
		if(sequence.count(x) > 1):
			repeated = True
			break
	if(not(repeated)):
		print("Error - no degrees repeated!")
	return repeated

def thereIsNoNegatives(sequence):
	return sequence.count(-1) == 0

def highestIsOne(sequence):
	return max(sequence) == 1

def allAreZero(sequence):
	return sequence.count(0) == len(sequence)

def allAreZeroNodes(sequence):
	for x in sequence:
		if x["degree"] > 0:
			return False

	return True

def numOfOnesIsEven(sequence):
	return sequence.count(1) % 2 == 0

def checkIfSequenceIsPossible(sequence):
	for x in range(len(sequence)-1):
		count = x
		for j in range(x+1,len(sequence)-1):
			if(sequence[j] > 0):
				count += 1
		if count < sequence[x]:
			return False
	return True

def scaleDown(sequence):
	if allAreZero(sequence):
		return sequence
	copiedSequenced = sequence.copy()
	firstValue = copiedSequenced[0]
	copiedSequenced.remove(firstValue)
	for x in range(firstValue):
		copiedSequenced[x] = copiedSequenced[x] - 1
	copiedSequenced.sort(reverse=True)
	if thereIsNoNegatives(copiedSequenced):
		return copiedSequenced
	return sequence

def checkIfRelationExists(relations,index1,index2):
	for x in relations:
		if index1 in x and index2 in x:
			return True
	return False

def generateSimpleGraph(sequence):
	g = graphviz.Graph()
	#g.attr(layout='neato')
	count = 0
	for x in range(len(sequence)):
		g.node(str(x),label=chr(ord('A')+count))
		count = count + 1

	for x in range(len(sequence)-1,-1,-1):
		for y in range(len(sequence)-1,x,-1):
			if sequence[y] > 0:
				sequence[y] = sequence[y] - 1
				sequence[x] = sequence[x] - 1
				g.edge(str(x),str(y))
	g.view()


#def generateComplexGraph(sequenceTimeline):
#	g = graphviz.Graph()
#	count = 0
#	for x in range(len(sequenceTimeline[0])):
#	g.node(str(x),label=chr(ord('A')+count))
#		count = count + 1
#	firstSequence = sequenceTimeline[len(sequenceTimeline)-1]
#	sequenceTimeline.remove(firstSequence)
#	for nextIndex in range(len(sequenceTimeline)-1,-1,-1):
#		firstSequence.insert(0,sequenceTimeline[nextIndex][0])
#		for x in range(firstSequence[0]):
#			firstSequence[len(firstSequence)-1-x] = firstSequence[len(firstSequence)-1-x] + 1
#			g.edge(str(len(sequenceTimeline[0])-len(firstSequence)),str(len(sequenceTimeline[0])-1-x))
		#for x in range(firstSequence[0]):
		#	firstSequence[x+1] = firstSequence[x+1] + 1
		#	g.edge(str(len(sequenceTimeline[0])-len(firstSequence)),str(len(sequenceTimeline[0])-len(firstSequence)+x+1))
#		firstSequence.sort(reverse=True)
#	g.view()

def generateComplexGraph(sequence):
	g = graphviz.Graph()
	count = 0
	nodesSequence = []
	for x in range(len(sequence)):
		g.node(chr(ord('A')+count))
		nodesSequence.append({
			"des": chr(ord('A')+count),
			"degree": sequence[x]
			})
		count = count + 1

	while not(allAreZeroNodes(nodesSequence)):
		nextNode = nodesSequence[0]
		nodesSequence.remove(nextNode)
		for x in range(nextNode["degree"]):
			nodesSequence[x]["degree"] = nodesSequence[x]["degree"] - 1
			g.edge(nextNode["des"],nodesSequence[x]["des"])
		nodesSequence = sorted(nodesSequence, key= lambda d: d["degree"],reverse=True)
	g.view()

#	Lema dos apertos de mãos
#def lam(sequence):
#	numNotEven = 0
#	for x in sequence:
#		if x % 2 != 0:
#			numNotEven += 1
#	return numNotEven % 2 == 0

def main():
	originalSequence = readSequence()

	#S - simplificado
	#A - sequencia introduzida
	sequenceTimeline = [originalSequence]
	sequence = originalSequence.copy()
	isValid = acceptableRange(sequence) and degreeSumIsEven(sequence) and hasRepeatedDegress(sequence)
	if (isValid):
		print("Prerequesites passed!")
		while sequence != scaleDown(sequence):
			sequence = scaleDown(sequence)
			print(sequence)
			sequenceTimeline.append(sequence)

		print()

		if (highestIsOne(sequence) and numOfOnesIsEven(sequence)) or allAreZero(sequence) or checkIfSequenceIsPossible(sequence):
			print("The given sequence is a graphical sequence!")
		
		else:
			isValid = False
			print("The given sequence is not a graphical sequence!")

		if isValid:
			mode = input("S-Mais simplificado possivel | A-sequencia introduzida: ")
			print()
			print("-----------------------")
			print("Generating .pdf diagram")
			print("-----------------------")
			print()
			if(mode=='S'):
				generateSimpleGraph(sequenceTimeline[len(sequenceTimeline)-2])
			else:
				generateComplexGraph(sequenceTimeline[0])
	else:
		print("Invalid sequence")

if __name__ == "__main__":
	main()	