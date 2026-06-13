# we need to find the longest substring of a string that has no repeating characters

def longestSubstring(self , s : string) -> int :
    # the set to store unique characters 
    charSet = set()
    # define the window : 
    l = 0 

    res = 0

    for r in range(len(s)):
        # two conditions either => already in the window, so remove 
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1

        # not there in the window => add to the window.
        charSet.add(s[r])

        # updated window size after calc.
        res = max(res, r-1 + l)

    return res        

    



