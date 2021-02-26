''' we start with the center , continue to expand along it to make a larger palindromic string as multiple palindromes have the same centers
for any odd length palindromic string, a single character will be the center 
whereas for an even length palindromic string each pair of consecutive characters will be the centers'''



class Solution(object):
    def count_sub(self,s,low,high):
        count=0
        while(low>=0 and high<len(s)):
            if(s[low]!=s[high]):
                break
            
            low-=1  # expand around center
            high+=1  #expand around center
            
            count+=1
        
        return count
    
    def countSubstrings(self, s):
        result=0
        n=len(s)
        
        for i in range(n):
            #odd length palindromic string
            result+=self.count_sub(s,i,i)
            
            #even length palindromic string
            result+=self.count_sub(s,i,i+1)
        
        return result #final answer 
