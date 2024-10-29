def feet_to_steps(user_feet):
   result = user_feet / 2.5
   return result

if __name__ == '__main__':
    feet_walked = float(input())
      
    print(f'{feet_to_steps(feet_walked):.0f}')