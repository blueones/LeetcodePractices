
class Solution:
    import math
    def myAtoi(self, str: str) -> int:
        processed = ""
        for cha in str:
            if cha == " ":
                
                if processed!="" and processed[-1].isdecimal():
                    
                    if -2**31<=float(processed)<=2**31-1:
                        return math.floor(float(processed))
                    elif float(processed)< -2**31:
                        return -2**31
                    else:
                        return 2**31-1
                elif processed =="":
                    continue
                else:
                    return 0
            elif cha =="-" or cha == "+":
                if processed =="":
                    processed += cha
                else:
                    if processed !="" and processed[-1].isdecimal():
                        if -2**31<=float(processed)<=2**31-1:
                            return math.floor(float(processed))
                        elif float(processed)< -2**31:
                            return -2**31
                        else:
                            return 2**31-1
                    else:
                        return 0
            elif cha ==".":
                processed += cha
            elif cha.isdecimal():
                processed +=cha
                print(processed)
            elif cha.isdecimal() is False:
                if processed !="" and processed[-1].isdecimal():
                    if -2**31<=float(processed)<=2**31-1:
                        return math.floor(float(processed))
                    elif float(processed)< -2**31:
                        return -2**31
                    else:
                        return 2**31-1
                else:
                    return 0
        if processed and processed[-1].isdecimal():
            # print(processed)
            if -2**31<=float(processed)<=2**31-1:
                return math.floor(float(processed))
            elif float(processed)< -2**31:
                return -2**31
            else:
                return 2**31-1
        else:
            return 0