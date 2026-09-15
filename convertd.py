inputOption = None
inputOptionCount = None
priceAdm = None
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

	def __init__ (self, inputDM, inputM):
		self.diamond = inputDM
		self.millions = inputM

	def convertData (self):
		if self.millions is None:
			resultDM = self.diamond * priceAdm
			viewDM = f"{resultDM:,.0f}".replace(',','.')
			return (viewDM)
		elif self.diamond is None:
			resultM = self.millions / priceAdm
			viewM = f"{resultM:,.0f}".replace(',','.')
			return (viewM)
		else:
			print("You must input all require data")
			
class premData():
	durMin = 11
	pOneM = None
	workTime = None

	def __init__ (self, priceAmonth, price6month, balAmonth, bal6month, perHit):
		self.pAmonth = priceAmonth
		self.p6month = price6month
		self.bAmonth = balAmonth
		self.b6month = bal6month
		self.Ahit = perHit

	def monthPrem (self):
		if self.p6month is None and self.b6month is None:
			dayGross = ((premData.workTime * 60) / premData.durMin) * self.Ahit
			dcBalance = dayGross - (self.bAmonth / 30)
			dcPrice = (dcBalance / 1000000) * premData.pOneM
			dcpMonthly = dcPrice * 30
			dcbMonthly = (dayGross * 30) - self.bAmonth
			viewProfit = f"""Daily price profit : Rp {dcPrice:,.0f}\nbalance profit : $ {dcBalance:,.0f}\nMonthly price profit : Rp {dcpMonthly:,.0f}\nMonthly balance profit : $ {dcbMonthly:,.0f}""".replace(',','.')
			return (viewProfit)
			
	def sixMonthPrem (self):
		if self.pAmonth is None and self.bAmonth is None:
			dayGross = (( premData.workTime*60 )/premData.durMin) * self.Ahit
			dcBalance = dayGross - (self.b6month/(30*6))
			dcPrice = (dcBalance / 1000000) * premData.pOneM
			dcpSixMonthly = dcPrice * (30*6)
			dcbSixMonthly = (dayGross * (30*6)) - self.b6month
			viewProfit = f"""Daily price profit : Rp {dcPrice:,.0f}\nbalance profit : $ {dcBalance:,.0f}\nSix monthly price profit : Rp {dcpSixMonthly:,.0f}\nSix monthly balance profit : $ {dcbSixMonthly:,.0f}""".replace(',','.')
			return (viewProfit)

print(intro)
priceAdm = int(input("Input number of balance avg for 1dm in markets: "))

print(mainMenu)
inputOption = int(input("Type your selection: "))

if inputOption == 1:
	DM = int(input("Input your number of diamonds: "))
	M = None
	covData = infoData(DM, M)
	resultData = covData.convertData()
	print("$", resultData)

elif inputOption == 2:
	M = int(input("Input you number of balance: "))
	DM = None
	covData = infoData(DM, M)
	resultData = covData.convertData()
	print(resultData, "DM")

elif inputOption == 3:
	premData.pOneM = int(input("how much does one M cost in the market today: "))
	premData.workTime = int(input("How long do you work until the resources run out [ hours ]: "))
	print(countIntro)
	inputOptionCount = int(input("Type your selection: "))

	if inputOptionCount == 1:
		poneMonth = int(input("Input market price for premium: "))
		boneMonth = int(input("Input market balance for premium: "))
		oneHit = int(input("Input balance you get for one hit: "))
		psixMonth = None
		bsixMonth = None

		monthlyPrem = premData(poneMonth, psixMonth, boneMonth, bsixMonth, oneHit)
		profmPrem = monthlyPrem.monthPrem()
		print(f"""\n[ RESULT ]\n{profmPrem}""")

	elif inputOptionCount == 2:
		psixMonth = int(input("Input market price for premium: "))
		bsixMonth = int(input("Input market balance for premium: "))
		oneHit = int(input("Input balance you get for one hit: "))
		poneMonth = None
		boneMonth = None

		sixMonthlyPrem = premData(poneMonth, psixMonth, boneMonth, bsixMonth, oneHit)
		profmPrem = sixMonthlyPrem.sixMonthPrem()
		print(f"""\n[ RESULT ]\n{profmPrem}""")
	else:
		print("Choose correctly!")

elif inputOption == 4:
	print("See You!")
else :
	print("Choose answer (1/2/3)")
