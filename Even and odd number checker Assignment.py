def even_number_filter(a):
  if a % 2 == 0:
    print("This is an even number.")
  else:
    print("This is an odd number.")

a = int(input("Please enter a number: "))
result = even_number_filter(a)

result