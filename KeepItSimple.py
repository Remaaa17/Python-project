# Complex version violating the KIS principle
def calculate_average(numbers):
   total = 0
   count = 0
   for num in numbers:
       total += num
       count += 1
       average = total / count
       return average


# Simple version following the KIS principle
def calculate_average(numbers):
   if not numbers:
      return None
      average = sum(numbers) / len(numbers)
      return average