from colorama import init, Fore
def name(args1, args2,args3): 
  age = args1 + args2+ args3
  if age < 6:
    print(age)
    print(Fore.BLUE + str(age))
  else:
    print(Fore.RED + str(age))
  
  
