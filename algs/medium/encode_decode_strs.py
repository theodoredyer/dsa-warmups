class Solution:

    def encode(self, strs: List[str]) -> str:
        builder = ''

        for s in strs:
            slen = len(s)
            builder += str(slen) + "." + s
        
        return builder

    def decode(self, s: str) -> List[str]:

        res = []
        cur = 0
        while cur < len(s):
            int_rep = ''
            while s[cur] != '.':
                int_rep += s[cur]
                cur += 1
            int_rep = int(int_rep)
            res.append(s[cur+1:(cur + int_rep + 1)])
            cur += 1 + int_rep            

        return res
    

"""
The secret to this is specifying within our encoding how many places of the string correspond
to the next word in the string, followed by a terminating character. 

So for example we would preface "neet" by 4. in order to indicate the next word is going to be 
the next 4 indices, we use the period because suppose this word was longer than 9 characters, we wouldn't
want to just read "1" and then process one character, we want to keep building up the integer representation
of the length of the next word until encountering the terminating character. 

"""