def caseFold(word):
	# Check if casing of the word matters,
	# this might become apparent later on
	return {word[0],word[1].lower()}
	
# Check if the token is actually a number
def convertToNumber(word):
	try:
		return {"<NUMBER>",float(word)}
	except:
		return word
	
periodwords = []
# Read from periodwords file

# Now for things like IPv4, IPv6; how do we handle the ambiguity?
# Tokens should not be ambiguous. Should be just let these be done at
# the parse level?

# All alternative options and parses must be evaluated
# We need to come up with an algorithm for this

def splitByFullStop(str):
	# First split by word
	sentencewords = str.split(' ')
	sentencewordslen = len(sentencewords)
	sentences = []
	last_index = 0
	
	# Find the actual delimiting full stops by not considering
	# words with periods in them such as Dr., Mr.
	for i in xrange(0,sentencewordslen):
		if(sentencewords[i].endsWith()=='.' and sentenceword not in fullstopwords):
			sentence.append(" ".join(sentencewords[last_index:i])[:-1])
			last_index = i
	words = []
	
	# Combine the words in all sentences together
	for each sentence in sentences:
		wordsofsentence = sentence.split(' ')
		for each word in wordsofsentence:
			words.append(word)
			
# Perform word level operations such as casefolding, removing trail markers
# We return sentence words, since ideally we should process each
# sentence separately. 

# However, it is possible that once sentence does not match any function
# we have to take the next sentence to match.
def tokenizer(str):
	sentences = splitByFullStop(str)
	words = []
	for each word in words:
		wordslen = len(words)
		for i in xrange(0,wordslen):
			words[i] = {"<KEYWORD>",words[i]}
			words[i] = caseFold(words[i])
			words[i] = convertToNumber(words[i])
	return sentencewords

tokenizer(raw_input())
