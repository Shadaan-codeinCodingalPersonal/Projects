print("here comes mr. fibbonaci.")
print("Hi! I am Mr. Fibbonaci")
def run():
   sequence = [1,1]
   fibbonacinum = int(input("Can you give me a fibbonacci number to add to my set? "))
   number = 0
   var = 0
   while (number < fibbonacinum):
     number = int(sequence[var]) + int(sequence[var + 1])
     sequence.append(number)
     var = var + 1
   if (number > fibbonacinum):
      print("Sorry! That does not add up to the laws of fibbonacci.")
      run()
   elif (number == fibbonacinum):
      print("Yes! It does match my rules.")
      print("Thank you! You are a great mathematician.")
      print("Bye!")
      print("Vroom! Vroom!")
   else:
      run()
run()