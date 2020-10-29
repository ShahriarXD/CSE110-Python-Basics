#lang() function Is an alias for whatever the first parameter is going to be.
a = input("Please input Your name sir: \n")
def greeting(lang):
    if lang == "Hello":
        print(f"Hello {a}")
    elif lang == "Hi":
        print(f"Hi {a}")
    elif lang == "Holla":
        print(f"Holla {a}")        
    elif lang == "en":
        print(f"ko {a}")
    elif lang == "jap":
        print(f"Watashi {a}")        
    else:
        print("Holla {a} Welcome to the club. You are the 13th member of our club.")            

greeting("Hello")
greeting("Hi")
greeting("en")
greeting("jap")
greeting(input())





#OUTPUTS
#Shahriar
#Hello Shahriar
#Hi Shahriar
#ko Shahriar
#Watashi Shahriar
#Hello
#Hello Shahriar
