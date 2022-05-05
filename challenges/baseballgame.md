**#Baseball Game**

#This is a practice test for turing.
#Keeping the description short
#Disclaimer: Not sure if the soulution clear all test cases, use at your own risk

##Problem:
You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future round scores.
'ops' is a list of strings, where ops[i] is the ith operation.
 if ops[i] is 
  - an integer, value of x, Record a new score of x
  - "+" - Record a new score that is sum of previous two scores. Make sure there are two previous scores.
  - "D" - Record a new score double of previous last score. Make sure there is one score in the record
  - "C" - Invalidate the previous score, make sure you have one score in the record
Return the sum of all scores on the record.

##Input:
 ops = ["5","2","C","D","+"]
##Output:
 30
##Explanation:
 Iterate the scores as they did, 
 5 - Add 5 to the record; record=[5]
 2 - Add 2 to the record; record=[5,2]
 C - Invalid, remove last entry in the record; record=[5]
 D - Double the last score, that is 5X2=10 and add that to record; record=[5,10]
 + - Add last two, 5+10=15; record=[5,10,15]
 
 As the iteration finshes, now return the sum of the record. ie: 5+10+15 = 30.
 
 ##Sample Input2:
  5 -2 4 C D 9 + +
  Output2:
  5 + -2 + -4 + 9 + 5 + 14 = 27


