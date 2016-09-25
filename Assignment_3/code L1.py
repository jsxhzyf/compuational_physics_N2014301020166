print('My name is Fei')
x=int(input('input a number:'))
for i in range(x):
    print(i*' '+'#########             # ') 
    print(i*' '+'#                       ') 
    print(i*' '+'#            # #      # ') 
    print(i*' '+'######### #      #    # ') 
    print(i*' '+'#        #        #   # ') 
    print(i*' '+'#        ##########   # ') 
    print(i*' '+'#        #            # ') 
    print(i*' '+'#         #       #   # ') 
    print(i*' '+'#          # # # #    # ') 
    if i==x-1:
        break
    import time
    time.sleep(0.2)
    import os
    i=os.system('cls')
