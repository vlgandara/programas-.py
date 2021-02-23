def incomodam(n):
   if (type(n) == int):
      if n > 0:
         return "incomodam " + incomodam(n-1)
   return ""

def elefantes(n):
   if n <1:
       return str()
   elif n== 1:
       return str("Um elefante incomoda muita gente ")
   elif n== 2:
       return str("Um elefante incomoda muita gente " + "2 elefantes incomodam incomodam muito mais")
   else:
       fraseA= str(n-1) + " elefantes " + str(incomodam(n-1)) + "muita gente"
       fraseB= str(n) + " elefantes " + str(incomodam(n)) + "muito mais"       
       return elefantes(n-1) + str(fraseA) + str(fraseB) 
