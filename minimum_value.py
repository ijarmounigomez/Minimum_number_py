def minimum_value(list):
  smallest_until_now = list[0] # We set the smallest number found until now to be the first value of the list.
  for number in list: # Now we iterate through each value in the list.
    if number < smallest_until_now: # With this "if" statement, if a smaller value than the one set at the beginning is found, that value will be the new smallest_until_now. 
      smallest_until_now = number
  return smallest_until_now
    
