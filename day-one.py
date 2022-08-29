def dayOne():

  f = open('dayOne.txt','r')
  puzzle_input = f.read()
  
  data = puzzle_input.split("\n")
  data = [int(i) for i in data]  


  print(data)
  
  for num in data:
    for num_two in data:
      if 2020 - num - num_two in data:
        print(num * (2020 -num - num_two) * num_two)
        return "" 
