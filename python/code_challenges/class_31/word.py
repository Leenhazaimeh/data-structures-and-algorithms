from collections import Counter
 
'''''
Write a function called repeated word that finds the first word to occur more than once in a string
'''''
def  repeatedWord( word ):
 
   
    hash = list( word .split(" "))
   
    repeat  = Counter(hash)
     
   
    for i in hash:
       
         
        if(repeat[i] > 1):
           
            return i
 
 

word  = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
print(repeatedWord( word ))
