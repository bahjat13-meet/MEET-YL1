class Integer(object):
	def __init__(self, n, isPositive):
		if isPositive:
			self.n=n
		else:
			self.n=-1*n
	def display(self):
		print self.n
	def returnN(self):
		return self.n
	def add(self, n2):
		return Integer(self.n+n2.returnN(),True)
	def subtract(self, n2):
		return Integer(self.n-n2.returnN(),True)
	def multiply(self, n2):
		return Integer(self.n*n2.returnN(),True)
	def divide(self, n2):
		return Integer(self.n/n2.returnN(),True)
class NegativeNumber(Integer):
	def __init__(self, n):
		Integer.__init__(self,n,False)
	def display(self):
		Integer.display(self)
		print "This is a NegativeNumber object"
if __name__=="__main__":
	#print "Michele"
	listy=[]
	num=input()
	for i in range(0,num):
		print "N or P ?"
		np=raw_input()
		if(np=="P"):
			tst=Integer(input(),True)
			listy.append(tst)
		elif(np=="N"):
			tst=NegativeNumber(input())
			listy.append(tst)
	for i in listy:
		i.display()
	if(num>=2):
		listy[0].add(listy[1]).display()
	

