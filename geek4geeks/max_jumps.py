"""
class Solution:
	def minJumps(self, arr, n):
	    #code here
	    if(arr[0]==0):
	        return -1
	    max_jumps = 0
	    next_jump = arr[0]
	    stop = False
	    i = 0
	    if(arr[0]==0):
	        return -1
	    while(not stop):
	        
	        if(i >= n-1):
	            max_jumps+=1
	            next_jump = arr[n-1]
	            stop = True
	        else:
	            if(arr[i]==0):
	                return -1
	            else:
	                next_jump = arr[i]
	                if(i>0):
		                max_jumps+=1
	        if(i==n-1):
	            stop = True
	        print(i,next_jump,max_jumps)
	        i+=next_jump
	    return max_jumps
	        
"""
