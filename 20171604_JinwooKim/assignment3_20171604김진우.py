'''
국민대학교 소프트웨어학부
20171604 김진우
Software Project-2
assignment3
edit filename
add, show : Try_except

+find kim : notfound
+del : notfound
'''


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
        scdb = pickle.load(fH)
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
    while (True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if len(parse) > 2:
            split_addscore = parse[2].strip('\'')
            try:
                add_score = int(split_addscore)
            except ValueError:
                print("ValueError")
                continue
        if parse[0] == 'add':
            try :
                record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
                scdb += [record]
            except:
                print("Invalid command: " + parse[0] + " " + parse[1])
        elif parse[0] == 'del':
            Co_scdb = scdb[:]
            for l in range(len(scdb)):
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
            if len(scdb) == len(Co_scdb):
                print("Not Found", parse[1])
                continue
        elif parse[0] == 'inc':
            try:
                for j in scdb:
                    if j['Name'] == parse[1]:
                        j['Score'] = str(int(j['Score']) + add_score)
            except:
                print("inc Error")
        elif parse[0] == 'show':
            try:
                sortKey = 'Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)
            except:
                print("Invalid command: " + parse[0] + " " + parse[1])
        elif parse[0] == 'find':
            empty_list = []
            for i in scdb:
                if i['Name'] == parse[1]:
                    empty_list.append(i)
            if len(empty_list) == 0:
                print("Not Found")
            showScoreDB(empty_list, 'Age')
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])

#scdb type == list in dictionary
#scdb속 Keyname 의 값 순서대로 sort후 출력
def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()

scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)