class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret_arr = []

        counter = 1
        for i in range(n):
            builder = ""
            if(counter % 3) == 0:
                builder += "Fizz"
            if(counter % 5) == 0:
                builder += "Buzz"
            
            if(builder == ""):
                ret_arr.append(str(counter))
            else:
                ret_arr.append(builder)
            counter += 1

        return ret_arr