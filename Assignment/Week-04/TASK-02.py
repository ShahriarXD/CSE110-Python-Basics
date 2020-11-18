# 1st one by using Function just because i want to practise bot way . :D
# def shahriar(lol):
#     if lol.endswith ("er"):
#         print (f"{lol[:-2]}est")
#     elif lol.endswith ("est"):
#         print (lol)    
#     elif len(lol) > 3:
#         print (f"{lol}er")    
#     elif len(lol) < 4:
#         print (lol)
			

# shahriar(input(""))



user_input = input("")
if user_input.endswith ("er"):
    print (f"{user_input[:-2]}est")
elif user_input.endswith ("est"):
    print (user_input)    
elif len(user_input) > 3:
    print (f"{user_input}er")    
elif len(user_input) < 4:
    print (user_input)
