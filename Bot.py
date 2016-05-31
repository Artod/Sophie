# Defines a template Bot class to be
# used by every bot in Sophie's pipeline

# Defines Entity class
# It takes a SophieEML string to match candidates against,
# maps it to an entity label
class Entity:
	entitystring = ""
	entitylabel = ""
	
# Defines Intent class
# It takes a SophieIML string to match candidates against,
# maps it to an intent label
class Intent:
	intentstring = ""
	intentlabel = ""
	
# Defines Action class
# It consists of a list of intents to be considered
# and which action to fire if the list is satisfied
class Action:
	intentlist = []
	mappedactions = []
	
class Bot:
	entities = Entity()
	intents = Intent()
	actions = Action()
