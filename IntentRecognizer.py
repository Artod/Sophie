# Populating intent dictionary
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
	
# Helper function for pretty printing (part of UI module)
def boldprint(str):
	print '\033[1m'+" ".join(str)+'\033[0m',

# Check if the wordlist at the current index, matches the pattern
# Note that the pattern can consist of RE type specifications for eg: pipe(|) to specify either word
# This matches a single pattern, we need to optimize all pattern matches to happen simultaneously
# through the creation of a FSM/ created using a CLR parser.

# The issue however is dynamic updating. Is it possible to build a CLR parser incrementally by rule?
# It seems possible at surface - start with start state, add this rule, undergo a transition 
# then	- if transition exists add this rule to the next state.
#       - else create a new state bringing forward all required rules from the previous state    
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

# Tokenize classes of words as a common grouping, these usually do not change the meaning
# of a sentence as much.
# So far, we decide to tokenize date and time formats, number.
# Everything else is understood as a keyword or intent (phrasal keyword with significant meaning)
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
			
# Recognize intent phrases in the given list of words
# This does a greedy matching (longest prefix matching)
def intentRecognize(words):
	wordslen = len(words)
	temp = ""
	i = 0
	while(i<wordslen):
		flag = True
		bestlen = -1
		for key in intentdict.keys():
			shiftlen = match(words,i,key)
			if(bestlen<shiftlen):
				bestlen = shiftlen
				bestkey = key
				
		if(bestlen):
			boldprint(words[i:i+bestlen])
			print intentdict[bestkey]
			i+=(bestlen-1)
			flag = False
				
		if(flag):
			print words[i]
		i+=1

# Driver function		
loadIntents()
while(1):
	str = raw_input()
	if(str!="quit"):
		intentRecognize(tokenizer(str))
	else:
		break
