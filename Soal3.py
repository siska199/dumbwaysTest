def polaUnik(panjang):
  for i in range(1,panjang+1):
    if i%2 != 0:
      print("*"*(panjang))
    else:
      print("*",end="")
      print("="*(panjang-2),end="")
      print("*")

polaUnik(5)