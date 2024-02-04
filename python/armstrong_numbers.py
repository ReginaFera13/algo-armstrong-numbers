# How can you make this more scalable and reusable later?
import math

def find_armstrong_numbers(numbers):
   answer = [] 
   for num in numbers:
       num_compare = num
       str_num = str(num)
       digits = []
       final_num = 0
       print('num_compare:', num_compare)
       print('str_num:', str_num)
       
       for digit in str_num:
           digits.append(int(digit))
           print('digits:', digits)
           
       for digit in digits:
           final_num += math.pow(digit, len(digits))
           print('final_num:', final_num)
           
       if final_num == num_compare:
           answer.append(int(final_num))

   return answer
     

find_armstrong_numbers()


