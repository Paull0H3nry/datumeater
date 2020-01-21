def typing(str):
  from time import sleep
  i=0
  while i<len(str):
    sleep(0.2)
    print(str[i],end="")
    i+=1
  print("\n")
