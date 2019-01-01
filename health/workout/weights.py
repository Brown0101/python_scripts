import math
from os import system

plates = [45,35,25,10,5,2.5]

def main():
	num = input("Total weight: ")
	getPlatesPerSide(num)

def getPlatesPerSide(weight):
	numPlates = ""

	remainingWeight = int(weight) - 45 # remove bar
	remainingWeight = remainingWeight / 2

	for x in range(len(plates)):
		numOfThisPlate = math.floor(remainingWeight / plates[x])

		if numOfThisPlate > 0:
			numPlates = str(numPlates) + str(numOfThisPlate) + " " + str(plates[x]) + "'s, "			
			remainingWeight = remainingWeight % plates[x]

	numPlates = str(numPlates) + " with " + str(remainingWeight) + " left over."
	print(numPlates + "\n\n")
	system("pause")


if __name__ == "__main__":
	main()
