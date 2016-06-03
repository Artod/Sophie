# Classification structures
bots = set()
dataset = {}

# Read from training file
file = open("ClassificationExamples")
for line in file:
    l = line.strip().split(' ')
    dataset[tuple(l[:-2])]=l[-1]
file.close()


# Count frequency of occurences
occurencefreq = {}
botfreq = {}
occurencebotfreq = {}

totalfreq = 0
for prompt in dataset.keys():
    for word in prompt:
        occurencefreq[word]=0
        botfreq[dataset[prompt]]=0
        if dataset[prompt] in occurencebotfreq:
            occurencebotfreq[dataset[prompt]][word]=0
        else:
            occurencebotfreq[dataset[prompt]]={word:0}
        occurencebotfreq[dataset[prompt]]["#TOTAL#"] = 0 

for prompt in dataset.keys():
    for word in prompt:
        occurencefreq[word]+=1
        botfreq[dataset[prompt]]+=1
        occurencebotfreq[dataset[prompt]][word]+=1
        occurencebotfreq[dataset[prompt]]["#TOTAL#"]+=1
        totalfreq+=1
        
print occurencebotfreq
def getNaiveBayesScore(word,bot):
    if word not in occurencefreq.keys():
        if word not in occurencebotfreq[bot]:
            return botfreq[bot]*1.0/(occurencebotfreq[bot]["#TOTAL#"]+1)
        else:
            return ((occurencebotfreq[bot][word]+1)*1.0/(occurencebotfreq[bot]["#TOTAL#"]+1))*botfreq[bot]
    else:
        if word not in occurencebotfreq[bot]:
            return botfreq[bot]*1.0/(occurencebotfreq[bot]["#TOTAL#"]+1)/(occurencefreq[word]+1)
        else:
            return ((occurencebotfreq[bot][word]+1)*1.0/(occurencebotfreq[bot]["#TOTAL#"]+1))*botfreq[bot]/(occurencefreq[word]+1)
        
while(1):
    inputstr = raw_input("\nEnter test sentence : ")
    inputwords = inputstr.split(' ')
    botscore = {}
    for bot in botfreq.keys():
        botscore[bot] = 1
        for word in inputwords:
            botscore[bot] *= getNaiveBayesScore(word,bot)
    
    print botscore
    maxbot = "no matching bot"
    maxvalue = 0
    for bot in botscore.keys():
        if(botscore[bot]>maxvalue):
            maxvalue = botscore[bot]
            maxbot = bot
    
    print "The question is for "+maxbot
