#coding: utf-8

import os

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

class card(object):

	def __init__(self,filename):
		tmp = self.loadCard(filename)
		self.answer = tmp[0]
		self.hints = tmp[1]
		self.usedHints = []
		for i in range(len(self.hints)):
			self.usedHints.append(False)


	def get_answer(self):
		return self.answer


	def get_hint(self, hintIndex):
		return self.hints[hintIndex]


	def get_hint_player(self, hintIndex):
		if hintIndex >= 0 and hintIndex < len(self.hints):
			if not self.get_usedHint(hintIndex):
				self.set_usedHint(hintIndex, True)
				return self.hints[hintIndex]
			else:
				os.system(cls)
				print "Hinweis " + str(hintIndex) + " wurde bereits benutzt."
				hintIndex = raw_input("Bitte geben Sie eine neue Nummer ein: ")
				self.get_hint(hintIndex)
		else:
			os.system(cls)
			print "Die eingegebene Zahl war entweder negativ oder zu gross."
			hintIndex = raw_input("Bitte geben Sie eine neue Nummer ein: ")
			self.get_hint(hintIndex)


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
		f1 = open(filename)
		content = f1.read()
		f1.close()

		hints = []

		content = content.split("\n")
		for element in content:
			if "# " in element:
				answer = element.replace("# ","")
			else:
				hints.append(element)

		return (answer,hints)


	def get_hintNumber(self):
		return len(self.hints)


	def listAllHints(self):
		for i in xrange(self.get_hintNumber()):
			print self.get_hint(i)

	def listAllUsedHints(self):
		for i in range(self.get_hintNumber()):
			if self.get_usedHint(i):
				print self.get_hint(i)

card1 = card(defaultCardFilename)



raw_input()