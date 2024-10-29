def swap_values(user_val1, user_val2, user_val3, user_val4):
   #Store values in new order
   value_order = [user_val2, user_val1, user_val4, user_val3]

   user_val1 = value_order[0]
   user_val2 = value_order[1]
   user_val3 = value_order[2]
   user_val4 = value_order[3]
   return user_val1, user_val2, user_val3, user_val4

if __name__ == '__main__':   
   user_input1 = int(input())
   user_input2 = int(input())
   user_input3 = int(input())
   user_input4 = int(input())
   
   #Get output
   user_output = swap_values(user_input1, user_input2, user_input3, user_input4)
   print(f'{user_output[0]} {user_output[1]} {user_output[2]} {user_output[3]}')

 