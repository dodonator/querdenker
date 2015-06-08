# Kartenersteller
import os

answer = raw_input("Bitte geben Sie die Loesung ein: \n")
typ = raw_input("Bitte geben Sie die Art der Loesung ein: \n")
filename = answer + ".txt"
curDir = os.getcwd()
filename = curDir + "\\cards\\" + filename


hints = []
running = True
while running:
	print ""
	print "Bitte geben Sie einen Hinweis als Satz ein."
	print "Oder geben sie nichts ein, um zu beenden."
	tmp = raw_input()
	if len(tmp) == 0:
		break
	else:
		hints.append(tmp)

content = "# " + answer + "\n" + "* " + typ + "\n"
for i in range(len(hints)-2):
	content += hints[i] + "\n"
content += hints[len(hints)-1]

f1 = open(filename, "w")
f1.write(content)
f1.close()
