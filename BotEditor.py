import os
import shutil

numbots = 0
botnames = []

# Count number of bots currently installed
def botCount():
    global numbots,botnames
    botnames = [e for e in os.listdir('.') if not os.path.isfile(e)]
    numbots = len(botnames)

# List all bots currently installed
def botList():
    botindex = 1
    for botname in botnames:
        try:
            desc = open(os.path.join(botname,"metadata.txt")).readlines()
        except:
            desc = ""
        print " "*(3-len(str(botindex))),botindex,":",botname," "*(15-len(botname)),"".join(desc)
        botindex+=1

# Edit a given bot
def botEdit():
    pass

def createFile(filename,initialdata=""):
    file = open(filename,"w")
    file.write(initialdata)
    file.close()
    
# Add a new bot
def botAdd():
    while(1):
        print "Give a name for the new bot : ",
        newbotname = raw_input()
        if(newbotname!=""):
            break
        
    if(newbotname.lower().endswith("bot")):
        newdirname = newbotname[0].upper()+newbotname[1:-3].lower()+"Bot"
    else:
        newdirname = newbotname[0].upper()+newbotname[1:].lower()+"Bot"

    print "Give a description for the bot : ",
    desc = raw_input()

    os.mkdir(newdirname)
    os.chdir(newdirname)
    createFile("metadata.txt",desc)
    createFile(newdirname[:-3].lower()+"_intents")
    createFile(newdirname[:-3].lower()+"_entities")
    os.chdir('..')
    print "Bot successfully added."
    botCount()
    
# Delete a selected bot
def botDelete():
    while(1):
        botList()
        print "Enter the index of bot to delete : "
        try:
            deleteindex = int(raw_input())
            if(deleteindex>=0 and deleteindex<=numbots):
                break
            else:
                continue
        except:
            pass
    while(1):
        print "Are you sure you want to delete",botnames[deleteindex-1]+"? (Yes/No)"
        option = raw_input()
        if(option.lower()=="yes"):
            shutil.rmtree(botnames[deleteindex-1])
            print "Bot successfully deleted."
            botCount()
            break
        elif(option.lower()=="no"):
            break
        else:
            print "Enter a valid option."
            continue

e = Exception()
def mainInterface():
    print "1 : List bots"
    print "2 : Edit bot"
    print "3 : Add new bot"
    print "4 : Delete bot"
    print "5 : Quit"
    print ">>",
    try:
        op = int(raw_input())
        if(not(op>=0 and op<=5)):
            raise Exception()
        if(op==1):
            botList()
        elif(op==2):
            botEdit()
        elif(op==3):
            botAdd()
        elif(op==4):
            botDelete()
        elif(op==5):
            return False
    except e:
        print "Kindly enter a valid option.",e
    return True

botCount()
print "Bot Editor interface loaded."
while(mainInterface()):
    pass
print "Bot Editor session closed."
