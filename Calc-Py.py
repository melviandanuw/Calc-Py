try:
  A = int(input('Input A Number..\n'))
  X = input('Input Operator.. (+, -, /, *)\n')
  B = int(input('Input B Number..\n'))
 
  
  if X == '+':
    print(A + B)

  if X == '-':
    print(A - B)
  elif X == '/':
    print(A / B)
  elif X == '*':
    print(A * B)
  else:
    print("Please input the correct operator.")
      
except:
  print("Please input the correct value.")