import pickle

dbfilename = 'assginment3-20171624.dat'

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
				print("Unable to add")
		elif parse[0] == 'del':
			for p in scdb:
				if p['Name'] == parse[1]:
						scdb.remove(p)
		elif parse[0] == 'show':
			sortKey ='Name' if len(parse) == 1 else parse[1]
			showScoreDB(scdb, sortKey)
		elif parse[0] == 'find':
			findedDB = []
			for i in scdb:
				if i['Name'] == parse[1]:
					findedDB += [i]
					sortKey = 'Name' if len(parse) == 2 else parse[2]
			showScoreDB(findedDB,sortKey)
		elif parse[0] == 'inc':
			try:
				added = parse[2]
				for i in scdb:
					if i['Name'] == parse[1]:
						editedDB = i
						scdb.remove(i)
						num = editedDB["Score"]
						num = int(num)
						num += int(added)
						num = str(num)
						editedDB["Score"] = num
						scdb.append(editedDB)
					break
			except:
				print("Unable to find name")
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

