import random, os, secrets
def randomkey(output=False):
      key = int(secrets.token_hex().upper(), base=16)
      if output != False:
         print("KEY IS %s" %key)
      return key
def generator(key, string):
       algorithm = str()
       for i in string:
            algorithm += str(random.randint(1,9))
            algorithm += str(random.randint(0,1))
       return algorithm
def encode(string="hello world", key=randomkey(), output=0):
             def calc(num1, num2, decider):
                  if decider == 0:
                    result = num1+num2
                  else:
                    result = num1-num2
                  return result
             last = random.randint(1,9)
             x=0
             pointer = 0
             random.seed(key)
             result = str()
             algorithm = generator(key, string)
             while pointer < len(algorithm)-1:
                      result += str(chr(calc(ord(string[round(pointer/2)]), int(algorithm[pointer]), int(algorithm[pointer+1]))))
                      pointer += 2
             while x < last:
                     algorithm += str(random.randint(1,9))
                     x +=1
             algorithm += str(last-1)
             if output == 0:
               return result
             else:
               return algorithm
def decode(string, key):
           	 random.seed(key)
             def calc(num1, num2, decider):
                  if decider == 1:
                    result = num1+num2
                  else:
                    result = num1-num2
                  return result
             pointer = 0
             result = str()
             algorithm = generator(key, string)
#             algorithm = algorithm[:-int(algorithm[-1])]
             while pointer < len(algorithm)-1:
                      result += str(chr(calc(ord(string[round(pointer/2)]), int(algorithm[pointer]), int(algorithm[pointer+1]))))
                      pointer += 2
             return result
