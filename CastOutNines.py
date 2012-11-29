import math
import random

def numsum(n):
	# add the digits in n. E.g. 2947 = 2+9+4+7 = 22 = 2+2 = 4
	s = str(n)
	total = 0
	for i in range(0, len(s)):
		total += int(s[i])
		
	if len(str(total)) > 1:
		return numsum(total)
	else:
		return total

def crossnine(n):
	# strike out all numbers in n which can be added to make 9
	s = str(n)
	l = len(s)
	toRemove = []
	i = 0
	while i < l:
		firstnum = int(s[i])
		total = firstnum
		if total == 9:
			toRemove.append(i)
			break
		provInd = []
		for j in range(i+1, l):
			nextnum = int(s[j])
			provInd.append(j)
			total += nextnum
			if total == 9:
				toRemove.append(i)
				for w in provInd:
					toRemove.append(w)
				i=j+1
				break
			elif total > 9:
				total -= nextnum
				provInd.pop()
		# end for j
		i = i + 1
	#end for i
	
	returnStr = ''
	for i in range(0, len(s)):
		if i not in toRemove:
			returnStr = returnStr + s[i]
	
	if len(returnStr) == 0:
		return 0
	else:
		return int(returnStr)
#end crossnine()

def singleDigitCrossNine(n):
	return crossnine(numsum(crossnine(n)))

def check(x, y, z):
	ckx = singleDigitCrossNine(x)
	cky = singleDigitCrossNine(y)
	ckproduct = singleDigitCrossNine(z)
	return singleDigitCrossNine(ckx * cky) == ckproduct
	
def testCase(x, y, z):
	print 'testing {} * {} = {}'.format(x,y,z)
	prod = x * y
	if prod != z:
		print 'Wrong! {} * {} = {}'.format(x,y,prod)
	print 'cross9 of {} = {}'.format(x, singleDigitCrossNine(x))
	print 'cross9 of {} = {}'.format(y, singleDigitCrossNine(y))
	print 'cross9 of {} * {} = {}'.format(x,y,singleDigitCrossNine(x*y))
	print 'cross9 of {} = {}'.format(z, singleDigitCrossNine(z))
	

def testAccuracy(cnt1, cnt2, rng):
	totalAccuracy = 0.0
	for i in range(0, cnt1):
		falsePositives = 0
		x = random.randrange(0, rng)
		y = random.randrange(0, rng)
		product = x * y
	
		for j in range(0, cnt2):
			rndProduct = random.randrange(0, rng*rng)
			if check(x, y, rndProduct):
				falsePositives += 1
		#end for j
	
		accuracy = 1.0 - (float(falsePositives) / cnt2)
		totalAccuracy += accuracy
		print 'run {}/{} accuracy = {}%'.format(i+1, cnt1, accuracy*100)
	#end for i

	avgAccuracy = totalAccuracy / cnt1
	print '*** average accuracy = {}%'.format(avgAccuracy*100)
# end testAccuracy()


# main
random.seed()
testAccuracy(100, 100, 10000)
#testCase(3030, 20, 11111)

	
	
	
