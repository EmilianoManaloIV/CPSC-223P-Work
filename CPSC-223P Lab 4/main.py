#---IMPORT USEFUL BUILT-IN FUNCTIONS---
import random

#---PACKAGE IMPORT CHECK---
#Check base package
from mathematics import *
print(whoami.getName())

#Now sub packages
from mathematics.numbers import *
print(whoami.getName())
from mathematics.geometry import *
print(whoami.getName())

#Import unlisted packages
from mathematics.numbers import simple

#---CHECK IF ALL FUNCTIONS WORK---
#--mathematics package--
#--numbers sub-package--
#Create a random list to test against
randomList = [random.randint(-10,10) for _ in range(random.randint(1,20))]
randomLeft = random.randint(-10,10)
randomRight = random.randint(-10,10)
#-series.sum-
if sum(randomList) == series.sum(list = randomList):
    print("SUM PASS")
else:
    print("SUM FAIL")
#-series.average
if (sum(randomList)/len(randomList)) == series.average(list = randomList):
    print("AVERAGE PASS")
else:
    print("AVERAGE FAIL")
#-simple.addition-
if (randomLeft + randomRight) == simple.addition(left=randomLeft,right=randomRight):
    print("ADD PASS")
else:
    print("ADD FAIL")
#-simple.subtraction-
if (randomLeft - randomRight) == simple.subtraction(left=randomLeft,right=randomRight):
    print("SUB PASS")
else:
    print("SUB FAIL")
#-simple.multiplication
if (randomLeft*randomRight) == simple.multiplication(left=randomLeft,right=randomRight):
    print("MULTI PASS")
else:
    print("MULTI FAIL")
#-simple.division
if (randomLeft/randomRight) == simple.division(left=randomLeft,right=randomRight):
    print("DIV PASS")
else:
    print("DIV FAIL")

#--