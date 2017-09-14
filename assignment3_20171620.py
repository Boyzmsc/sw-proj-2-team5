import pickle

dbfilename = 'assignment3.dat'

def readScoreDB():
	try:
		fH = open(dbfilename, 'rb')
	except FileNotFoundError as e:
		print("New DB: ", dbfilename)
		return []

	scdb = []
	try:
		scdb =  pickle.load(fH)
	except:
		print("Empty DB: ", dbfilename)
	else:
		print("Open DB: ", dbfilename)
	fH.close()
	return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

def doScoreDB(scdb):
	while(True):
		inputstr = (input("Score DB > "))
		if inputstr == "": continue
		parse = inputstr.split(" ")
		if parse[0] == 'add':
			try:
				record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
				scdb += [record]
			except:
				print("TypeError")
				continue
		elif parse[0] == 'del':
			#예외처리 코드 추가 필요
			for l in range(len(scdb)):
				for p in scdb:
					if p['Name'] == parse[1]:
						scdb.remove(p)
		elif parse[0] == 'show':
			if len(parse) == 1:
				sortKey = 'Name'
			elif len(parse) == 2:
				if parse[1] == 'Name':
					sortKey = 'Name'
				elif parse[1] == 'Age':
					sortKey = 'Age'
				elif parse[1] == 'Score':
					sortKey = 'Score'
				else:
					print("TypeError")
					continue
			else:
				print("TypeError")
				continue
			showScoreDB(scdb, sortKey)
		elif parse[0] == 'find':
			for k in scdb:
				if k['Name'] == parse[1]:
					print("Age=%s Name=%s Score=%s" %(k['Age'],k['Name'],k['Score']))
		elif parse[0] == 'inc':
			try:
				for j in scdb:
					if j['Name'] == parse[1]:
						j['Score'] = str(int(j['Score'])+int(parse[2]))
			except:
				print("Error")
		elif parse[0] == 'quit':
			break
		else:
			print("Invalid command: " + parse[0])

def showScoreDB(scdb, keyname):
	for p in sorted(scdb, key=lambda person: person[keyname]):
		for attr in sorted(p):
			print(attr + "=" + p[attr], end=' ')
		print()
	


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
