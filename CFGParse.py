import sys

# Data structures to store rules in internal format
rules = {}
nonterms = {}
terms = set()
ntcount = 0

# To complete the parsing based on constructed SLR parser
def parse(inputstring):
    print inputstring

# Load rules in internal format    
def loadRules(rulestring):
    global ntcount
    #print rulestring
    
    rulebreak = rulestring.split(':')
    print rulebreak[0],"->",rulebreak[1]
    
    if rulebreak[0] not in nonterms.keys():
        nonterms[rulebreak[0]] = ntcount
        ntcount += 1
    #print ntcount
    
    options = rulebreak[1].split('|')
    if(nonterms[rulebreak[0]] not in rules.keys()):
        rules[nonterms[rulebreak[0]]] = []
    
    #print rules
    #print options
    
    for option in options:
        tokens = option.split(' ')
        print tokens
        symbolictokens = []
        for token in tokens:
            # Non-terminal
            if token.startswith('<') and token.endswith('>'):
                if token not in nonterms.keys():
                    nonterms[token] = ntcount
                    ntcount+=1
                symbolictokens.append(nonterms[token])
            # Terminal
            else:
                terms.add(token)
                symbolictokens.append(token)
        rules[nonterms[rulebreak[0]]].append(symbolictokens)
        #print symbolictokens
        #print rules
    #print ""
          
fp = open(sys.argv[1])
for rulestring in fp:
    loadRules(rulestring.strip())
while(1):
    inputstr = raw_input()
    if(inputstr=="quit"):
        break
    parse(inputstr)
print rules
fp.close()
