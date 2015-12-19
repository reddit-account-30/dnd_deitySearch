import string
from sets import Set

def printAll():
	print row["deity"]
	print "Alignment: " + row["alignment"]
	print "Domain(s): " + row["domain"]
	print "Symbol(s): " + row["symbol"]

print "Enter name of file to sort through: ",
INPUTFILE = raw_input()
input = open(INPUTFILE, 'r')

deityArray = []
domainSet = Set()

rawText = input.readlines()
for row in rawText:
	deityRow = dict(zip(["deity","alignment","domain","symbol"],row.split(": ")))
	deityArray.append(deityRow)

print "Enter category to search (Deity, Alignment, Domain, Symbol, or Advanced): "
category = raw_input().lower()

if category == "debug":
	print "Enter term (all, or domainall): "
	term = raw_input().lower()
elif category == "deity":
	print "Enter part or all of Deity name: "
	term = raw_input().lower()
elif category == "alignment":
	print "Enter alignment(LG,NG,CG,NG,N,NE,LE,NE,CE): "
	term = raw_input().lower()
elif category == "domain":
	print "Enter domain: "
	term = raw_input().lower()
elif category == "symbol":
	print "Enter symbol: "
	term = raw_input().lower()
elif category == "advanced":
	print "Enter part or all of Deity name: "
	termName = raw_input().lower()
	print "Enter alignment(LG,NG,CG,NG,N,NE,LE,NE,CE): "
	termAlign = raw_input().lower()
	print "Enter domain: "
	termDomain = raw_input().lower()
	print "Enter symbol: "
	termSymbol = raw_input().lower()

for row in deityArray:
	if category == "debug":
		if term == "all":
			print row["deity"] + " | " + row["alignment"] + " | " + row["domain"]
		elif term == "domainall":
			domainString = row["domain"]
			for string in domainString.split(", "):
				domainSet.add(string)
	elif category == "deity":
		if term in row["deity"].lower():
			printAll()
	elif category == "alignment":
		if term in row[category].lower():
			printAll()
	elif category == "domain":
		if term in row[category].lower():
			printAll()
	elif category == "symbol":
		if term in row[category].lower():
			printAll()
	elif category == "advanced":
		if ( (termName in row["deity"].lower()) and (termAlign in row["alignment"].lower()) and (termDomain in row["domain"].lower()) and (termSymbol in row["symbol"].lower()) ):
			printAll()

if(category == "debug" and term == "domainall"):
	print domainSet
