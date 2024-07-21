class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_rep = {}

        for s in strs:
            sorted_str = "".join(sorted(s))
            print(sorted_str)
            if sorted_str in dict_rep:
                dict_rep[sorted_str].append(s)
            else:
                dict_rep[sorted_str] = [s]
        
        res = [val for val in dict_rep.values()]
        return res
            

            

"""
Relatively simple string manipulation problem, essentially just 
set up a dictionary where the keys are the anagram agnostic version of
the string aka the string in sorted order, and then the value for that 
spot in the dictionary should be a list containing the original strings

Just return this list at the end. 

"""