def feet_to_steps(user_feet):
   result = int(user_feet / 2.5)
   return result

if __name__ == '__main__':
    feet_walked = float(input())
      
    print(feet_to_steps(feet_walked))