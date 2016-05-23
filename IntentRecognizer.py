intentdict = {}
intentdictlen = 0
def loadIntents():
	file = open("IntentList","r")
	for line in file:
		if(line[0]=='#'):
			continue
		intenttriple = line.strip().split(',')
		intentdict[intenttriple[0]]=intenttriple[1]
	intentdictlen = len(intentdict.keys())
	
def boldprint(str):
	print '\033[1m'+" ".join(str)+'\033[0m',

def match(wordlist, index, pattern):
	patternwords = pattern.split(' ')
	patternwordlength = len(patternwords)
	wordslength = len(wordlist)
	if(index+patternwordlength>wordslength):
		return 0
	for i in xrange(0,patternwordlength):
		if('|' in patternwords[i]):
			patternwordlis = patternwords[i].split('|')
			if(wordlist[index+i] not in patternwordlis):
				return 0
		elif(wordlist[index+i]!=patternwords[i]):
			return 0
	return patternwordlength

def tokenizer(str):
	words = str.split(' ')
	wordslen = len(words)
	for i in xrange(0,wordslen):
		try:
			float(words[i])
			words[i] = "<NUMBER>"
		except:
			continue
	return words
			
def intentRecognize(words):
	wordslen = len(words)
	temp = ""
	i = 0
	while(i<wordslen):
		flag = True
		for key in intentdict.keys():
			shiftlen = match(words,i,key)
			if(shiftlen):
				boldprint(words[i:i+shiftlen])
				print intentdict[key]
				i+=(shiftlen-1)
				flag = False
				break
		if(flag):
			print words[i]
		i+=1
		
loadIntents()
while(1):
	str = raw_input()
	if(str!="quit"):
		intentRecognize(tokenizer(str))
	else:
		break
