def greeting():
    return "Hello"      

print(greeting(),"Schacin")
print(greeting(),"Sohan")
print(greeting(),"Samia")
print(greeting(),"Nafisa")
print(greeting(),"Yanna")
print(greeting(),"Princilla")

#Output
#Hello Schacin
#Hello Sohan    
#Hello Samia    
#Hello Nafisa   
#Hello Yanna    
#Hello Princilla



def greeting(lang):
    if lang == "en":
        return "Hello"
    elif lang == "fr":
        return "Holla"
    elif lang == "jap":
        return "Watashi"        
    else:
        print("Holla Welcome to the club. You are the 13th member of our club.")            

print(greeting("fr"), "NAFISA")
print(greeting("en"), "Yanna")
print(greeting("jap"), "Mahir")



#Output
#Holla NAFISA
#Hello Yanna    
#Watashi Mahir  



def summation(a,b):
    x = a+b
    return x
print(summation(55,55))
print(summation(55,66))
print(summation(54,66))  
#Output
#110
#121
#120





