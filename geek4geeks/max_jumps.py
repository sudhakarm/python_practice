#https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1
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

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends	

#Sample input
#10
#2 3 1 1 2 4 2 0 1 1
#Expected output 4
"""
