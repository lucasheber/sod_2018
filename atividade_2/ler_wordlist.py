# coding utf-8

import hashlib


def geraHash (sd):
	hash = hashlib.md5()
	hash.update(sd)

	return hash.hexdigest()

palavra = geraHash("passwor4354d")

print("Hash palavra: {}".format(palavra))

wordlista = open('wordlista', 'r')

encontrou = False
word = ""

for x in wordlista:

	if geraHash(x.strip()) == palavra:
		word = x
		encontrou = True
		break


if encontrou == True:
    print("Palavra encontrada: {} => {}".format(x, palavra))
else:
    print("Palavra nao encontrada!")

wordlista.close()