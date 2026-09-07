inputOption = None
inputOptionAuto = None
intro = """
[ DICOVERTION TOOLS ]
Information tools:
- Created date = 07/09/26
- Created by = Fikriydk
- Tools version = 1.0

[ CHOOSE YOUR OPTION ]
1. Convert DM to M
2. Convert M to DM
3. Count profitable premium
"""
countIntro = """
[ SELECT ROUTE AUTO ]
1. Money to Premium
2. M to Premium
"""

def convertData (inputIDM, inputIM, inputDM = None, inputM = None):
	if inputM is None:
		resultDM = (inputIM / inputIDM) * inputDM
		viewDM = f"{resultDM:,.0f}".replace(',','.')
		return (viewDM)
	elif inputDM is None:
		resultM = (inputIDM / inputIM) * inputM
		viewM = f"{resultM:,.0f}".replace(',','.')
		return (viewM)
	else:
		print("You must input all require data")

print(intro)

inputOption = int(input("Type your selection: "))

if inputOption == 1:
	IDM = float(input("Masukkan nilai pasar DM: "))
	IM = float(input("Masukkan nilai pasar M: "))
	DM = float(input("Masukkan nilai DM: "))
	M = None
	covData = convertData(IDM, IM, DM, M)
	print(covData,"M")

elif inputOption == 2:
	IDM = float(input("Masukkan nilai pasar DM: "))
	IM = float(input("Masukkan nilai pasar M: "))
	M = float(input("Masukkan nilai M: "))
	DM = None
	covData = convertData(IDM, IM, DM, M)
	print(covData, "DM")

elif inputOption == 3:
        print(countIntro)
else :
	print("Choose answer (1/2/3)")
