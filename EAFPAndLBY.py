# EAFP approach
def divide_numbers(a, b):
  try:
      result = a / b
  except ZeroDivisionError:
      result = None
      return result

# LBYL (Look Before You Leap) approach
def divide_numbers(a, b):
   if b != 0:
     result = a / b
   else:
     result = None
     return result