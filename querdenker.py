#coding: utf-8

import os
import random

# Querdenker
# Spielprinzip:
# Ein Spieler zieht eine Karte
# Die Karte beinhaltet ein "Wer", ein "Was" oder ein "Wo"
# Die anderen Spieler dürfen nun nacheinander durchnummerierte
# Hinweise erfragen.
# Wird die Frage beantwortet bekommt der Spieler, der die Frage
# gestellt hat soviele Punkte, wie viele Fragen gestellt wurden.
# Der Anworter kriegt den Rest.

defaultCardFilename = "Homer Simpson.txt"

cls = ""

class player(object):
	def __init__(self,name, ID=0):
		self.name = name
		self.cards = cardStack()
		self.score = 0
		self.ID = ID

	def get_cards(self):
		return self.cards

	def get_score(self):
		return self.score

	def add_card(self, tmpCard):
		self.cards.add_card(tmpCard)

	def add_score(self, score):
		self.score = self.score + score

	def get_name(self):
		return self.name

	def get_ID(self):
		return self.ID

	def set_ID(self, tmpID):
		self.ID = tmpID

	def listAllCards(self):
		print "Karten von " + self.get_name() + ":"
		for c in self.cards.get_stack():
			print c.get_answer()


class card(object):

	def __init__(self,filename):
		tmp = self.loadCard(filename)
		self.answer = tmp[0]
		self.typ = tmp[1]
		self.hints = tmp[2]
		self.usedHints = []
		for i in range(len(self.hints)):
			self.usedHints.append(False)


	def get_answer(self):
		return self.answer


	def get_typ(self):
		return self.typ


	def get_hint(self, hintIndex):
		return self.hints[hintIndex]


	def get_hint_player(self):
		
		running = True
		while running:
			print "Bitte geben Sie die Nummer des Hinweises ein,"
			print "den Sie erhalten wollen"
			hintIndex = int(raw_input(":"))
			if hintIndex >= self.get_hint_number():
				running = True
			elif hintIndex < 0:
				running = True
			else:
				hint = self.get_hint(hintIndex)
				return hint


	def set_usedHint(self, hintIndex, value):
		if hintIndex >= 0 and hintIndex < len(self.usedHints):
			self.usedHints[hintIndex] = value


	def get_usedHint(self, hintIndex):
		if hintIndex >= 0 and hintIndex < len(self.usedHints):
			return self.usedHints[hintIndex]
		else:
			os.system(cls)
			print "Die eingegebene Zahl war entweder negativ oder zu gross."
			hintIndex = raw_input("Bitte geben Sie eine neue Nummer ein: ")
			self.get_usedHint(hintIndex)


	def loadCard(self, filename):
		curDir = os.getcwd()
		filename = curDir + "\\cards\\" + filename
		f1 = open(filename)
		content = f1.read()
		f1.close()

		answer = ""
		typ = ""

		hints = []

		content = content.split("\n")
		for element in content:
			if "# " in element:
				answer = element.replace("# ","")
			elif "* " in element:
				typ = element.replace("* ","")
			else:
				hints.append(element)

		return (answer,typ,hints)


	def get_hint_number(self):
		return len(self.hints)


	def listAllHints(self):
		for i in xrange(self.get_hint_number()):
			print self.get_hint(i)

	def listAllUsedHints(self):
		for i in range(self.get_hint_number()):
			if self.get_usedHint(i):
				print self.get_hint(i)

class cardStack(object):
	def __init__(self):
		self.stack = []

	def add_card(self, tmpCard):
		self.stack.append(tmpCard)

	def remove_card(self, tmpIndex):
		result = self.stack.pop(tmpIndex)
		self.stack = result

	def get_last_card(self):
		return self.stack(self.get_stack_length()-1)

	def get_stack_length(self):
		return len(self.stack)

	def get_card(self, i):
		return self.stack[i]

	def get_random_card(self):
		r = random.randint(0,self.get_stack_length()-1)
		return self.get_card(r)

	def get_stack(self):
		return self.stack


# class gameRound(object): # ???


class game(object):

	def __init__(self):
		self.Player = []
		self.nextID = 0
		self.currentPlayer = None
		self.stack = cardStack()
		self.currentID = 0

	def get_current_player(self):
		return self.Player[self.currentID]

	def set_current_player(self):
		tmp = (self.currentID + 1) % len(self.Player)
		self.currentID = tmp

	def load_all_cards(self):
		curDir = os.getcwd() + "\\cards\\"
		curDir = os.listdir(curDir)
		for element in curDir:
			if ".txt" in element:
				self.stack.add_card(card(element))

	def add_player(self, name):
		self.Player.append(player(name, self.nextID))
		self.nextID += 1

	def get_player(self, tmpID):
		return self.Player[tmpID]

	def list_all_player(self):
		for p in self.Player:
			print p.get_name() + " " + str(p.get_score())

	def load_player(self):
		x = int(raw_input("Wie viele Spieler? "))
		for i in range(x):
			print "Spieler " + str(i) + " bitte geben Sie ihren Namen ein: "
			tmp = raw_input(":")
			self.add_player(tmp)
		print "okay"
		self.list_all_player()

	def gameRound(self):
		
		cp = self.get_current_player()
		print cp.get_name() + " Sie duerfen die Fragen stellen."
		cc = self.stack.get_random_card()
		print "Typ: " + cc.get_typ()
		counter = 0
		for p in self.Player:
			if p == cp:
				pass
			else:
				counter += 1
				print cc.get_hint_player()
				print "Nun duerfen sie die Antwort raten:"
				ca = raw_input(":")
				if ca == cc.get_answer():
					cp.add_score(counter)
					p.add_score(cc.get_hint_number()-counter)
					break
		self.stack.remove_card(self.stack.get_stack().index(cc))

	def main(self):
		self.load_all_cards()
		self.load_player()
		for i in range(self.stack.get_stack_length()):
			self.gameRound()



		

g = game()
g.main()


raw_input()
