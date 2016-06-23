import os

class DropDownSelectWidget():
	def __init__(self):
		self.items = []
		self.width = 10
		self.selectedIndex = 0
		self.no_of_items = 0
		self.isDropDownActive = False
		self.isFocused = False
	def _scrollDown(self):
		if(self.selectedIndex<self.no_of_items-1):
			self.selectedIndex += 1
	def _scrollUp(self):
		if(self.selectedIndex>0):
			self.selectedIndex -= 1
	def addItem(self,item):
		self.items.append(item)
		self.no_of_items += 1
	def setHorizontalWidth(self,width):
		self.width = width
	def _activateDropDown(self):
		self.isDropDownActive = True
	def _collapseDropDown(self):
		self.isDropDownActive = False
	def selectedItem(self):
		return self.items[selectedIndex]
	def _listenEvent(self):
		ch = raw_input()
		if(ch==''):
			if not self.isFocused:
				self.isFocused = True
			elif not self.isDropDownActive:
				self._activateDropDown()
			else:
				self._collapseDropDown()
		if(ch=='`'):
			if self.isDropDownActive:
				self._collapseDropDown()
			elif self.isFocused:
				self.isFocused = False
		if(ch=='^'):
			self._scrollUp()
		if(ch=='v'):
			self._scrollDown()
		
	def _render(self):
		os.system("clear")	
		toprint = ""
		if(self.no_of_items):
			toprint = self.items[self.selectedIndex]
		if(self.isFocused):
			toprint = toprint.upper()
		print toprint + (self.width-len(toprint))*" ",
		print u'\u25bc'
		if(self.isDropDownActive):
			for i in xrange(0,self.no_of_items):
				if(i==self.selectedIndex):
					print self.items[i].upper()
				else:
					print self.items[i].lower()
						
ddw = DropDownSelectWidget()	
items = ["Honey Oat","Parmesan Oregano","White Italian","Roasted Garlic"]
for item in items:
	ddw.addItem(item)
while(1):
	ddw._render()
	ddw._listenEvent()
	
