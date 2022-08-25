def arithmetic_arranger(problems, solution=False):
    
    while True:
      # Check to see if problems exceed maximum amount
      if (len(problems) > 5):
        return "Error: Too many problems."
        break
        
      uppernum = ''
      lowernum = ''
      dividerline = ''
      answernum = ''
  
      # Split the list so that each index can be called and assigned
      for prob in problems:
        probs = prob.split()     
    
    
        if probs[1] not in ['+', '-',]:
          return "Error: Operator must be '+' or '-'."
          break
          
        if not probs[0].isdigit() or not probs[2].isdigit(): 
          return 'Error: Numbers must only contain digits.'
          break
          
        for item in probs:
          if len(item) > 4:
            return 'Error: Numbers cannot be more than four digits.'
            break
            
        if probs[1] == '+':
          result = int(probs[0]) + int(probs[2])
        else:
          result = int(probs[0]) - int(probs[2])
        
        
        max_length = max(len(probs[0]), len(probs[2])) + 2
        upperline = str(probs[0]).rjust(max_length) + '    '
        lowerline = str(probs[1]) + str(probs[2].rjust(max_length - 1)) + "    "
        divider = '-' * max_length + "    "
        answer = str(result).rjust(max_length) + "    "
  
        uppernum += upperline
        lowernum += lowerline
        dividerline += divider
        answernum += answer
  
          
      if solution == True:
        return (f'{uppernum.rstrip()}\n{lowernum.rstrip()}\n{dividerline.rstrip()}\n{answernum.rstrip()}')
      elif solution == False:
        return (f'{uppernum.rstrip()}\n{lowernum.rstrip()}\n{dividerline.rstrip()}')