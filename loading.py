def loading():
    from time import sleep
    from random import random
    i=0
    while i<=10:
        sleep(random())
        print("Loading(%s)"% ("."*i).ljust(10))
        i+=1
        
#Exemplo/teste
loading()
