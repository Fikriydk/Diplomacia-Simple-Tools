inputOption = None
inputOptionCount = None
intro = """
Before we start, please input this data first...
"""
mainMenu = """
[ DICOVERTION TOOLS ]
Information tools:
- Created date = 07/09/26
- Created by = Fikriydk
- Tools version = 1.0

[ CHOOSE YOUR OPTION ]
1. Convert diamonds to balance
2. Convert balance to diamonds
3. Count profitable premium
4. Exit
"""
countIntro = """
[ SELECT ROUTE AUTO ]
1. A Month Premium
2. 6 Month Premium
"""
class infoData():
	priceAdm = None

	def __init__ (self, inputDM, inputM):
		self.diamond = inputDM
		self.millions = inputM

	def convertData (self):
		if self.millions is None:
			resultDM = self.diamond * infoData.priceAdm
			viewDM = f"{resultDM:,.0f}".replace(',','.')
			return (viewDM)
		elif self.diamond is None:
			resultM = self.millions / infoData.priceAdm
			viewM = f"{resultM:,.0f}".replace(',','.')
			return (viewM)
		else:
			print("You must input all require data")
class premData():
	durMin = 11

	def __init__ (self, priceAmonth, price6month, balAmonth, bal6month, perHit):
		self.pAmonth = priceAmonth
		self.p6month = price6month
		self.bAmonth = balAmonth
		self.b6month = bal6month
		self.Ahit = perHit

	def monthPrem (self):
		if self.p6month and self.b6month is None:
			dayGross = (1440/premData.durMin) * self.Ahit
			dcPrice = dayGross - self.pAmonth
			dcBalance = dayGross - self.bAmonth
			dcpMonthly = dcPrice * 30
			dcbMonthly = dcBalance * 30
			viewProfit = f"""Daily price profit : {dcPrice:,.0f}, balance profit : {dcBalance:,.0f}
Monthly price profit : {dcpMonthly:,.0f}, balance profit : {dcbMonthly:,.0f}""".replace(',','.')
			return (viewProfit)

print(intro)
infoData.priceAdm = float(input("Input number of balance avg for 1dm in markets: "))

print(mainMenu)
inputOption = int(input("Type your selection: "))

if inputOption == 1:
	DM = float(input("Input your number of diamonds: "))
	M = None
	covData = infoData(DM, M)
	resultData = covData.convertData()
	print("$", resultData)

elif inputOption == 2:
	M = float(input("Input you number of balance: "))
	DM = None
	covData = infoData(DM, M)
	resultData = covData.convertData()
	print(resultData, "DM")

elif inputOption == 3:
	print(countIntro)
	inputOptionCount = int(input("Type your selection"))

	if inputOptionCount == 1:
		poneMonth = float(input("Input market price for premium: "))
		boneMonth = float(input("Input market balance for premium: "))
		oneHit = float(input("Input balance you get for one hit: "))
		psixMonth = None
		bsixMonth = None

		monthlyPrem = premData(poneMonth, psixMonth, boneMonth, bsixMonth, oneHit)
		profmPrem = monthlyPrem.monthPrem()
		print(profmPrem)

	elif inputOptionCount == 2:
		print("2-")
	else:
		print("Choose correctly!")

elif inputOption == 4:
	print("See You!")
else :
	print("Choose answer (1/2/3)")
