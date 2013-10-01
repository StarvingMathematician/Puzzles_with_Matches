'''
Created on Sep 30, 2013

@author: Jonathan A Simon
'''

#Returns all values relevant to transformations from one digit into another 
def get_digit_data():
    import numpy as np    
    #number of matches in each digit
    digit_sizes = [6,2,5,5,4,5,6,3,7,6]
    #digits reachable by 1 or 2 moves 
    digit_neighborhoods = [[0,2,3,5,6,8,9],
                           [1,4,7],
                           [0,2,3,5,6,8,9],
                           [0,2,3,4,5,6,7,8,9],
                           [1,3,4,5,7,9],
                           [0,2,3,4,5,6,8,9],
                           [0,2,3,5,6,8,9],
                           [1,3,4,7],
                           [0,2,3,5,6,8,9],
                           [0,2,3,4,5,6,8,9]]
    #number of moves required (list form) 
    move_dist_list = [[0,2,2,2,1,1,1],
                      [0,2,1],
                      [2,0,1,2,2,2,2],
                      [2,1,0,2,1,2,2,2,1],
                      [2,2,0,2,2,2],
                      [2,2,1,2,0,1,2,1],
                      [1,2,2,1,0,1,1],
                      [1,2,2,0],
                      [1,2,2,2,1,0,1],
                      [1,2,1,2,1,1,1,0]]
    #number of moves required (matrix form); all nonsensical entries contain -1
    move_dist_mat = -1*np.ones([10,10])
    for i1,row in enumerate(digit_neighborhoods):
        for i2,elm in enumerate(row):
            move_dist_mat[i1,elm] = move_dist_list[i1][i2] 
    
    within_match_dist = -1*np.ones([10,10]) #number of matches moved internally
    add_match_dist = -1*np.ones([10,10]) #number of matches added
    sub_match_dist = -1*np.ones([10,10]) #number of matches removed
    for idx,val in np.ndenumerate(move_dist_mat):
        if(val != -1):
            size_difference = digit_sizes[idx[1]] - digit_sizes[idx[0]]
            within_match_dist[idx] = val - np.abs(size_difference) 
            if size_difference >= 0:
                add_match_dist[idx] = size_difference
                sub_match_dist[idx] = 0
            elif size_difference <= 0:
                sub_match_dist[idx] = -size_difference
                add_match_dist[idx] = 0

    return digit_neighborhoods, within_match_dist, add_match_dist, sub_match_dist

#Gets problem-relevant info from user, and reformats/returns it 
def get_input():
    
    input_eq = raw_input("What is the initial equation? Do NOT put spaces between the characters: ")
    #Check validity of input equation
    if len(input_eq) == 5: #if the equation contains the correct number of characters
        #if the equation is not structured correctly 
        if not(str.isdigit(input_eq[0]+input_eq[2]+input_eq[4]) and ((input_eq[1] == '-') or (input_eq[1] == '+')) and (input_eq[3] == '=')):
            raise Exception("This is not a valid equation!")
    else:
        raise Exception("This is not a valid equation!")
        
    char_shift = ord('0')
    d1 = ord(input_eq[0]) - char_shift
    d2 = ord(input_eq[2]) - char_shift
    d3 = ord(input_eq[4]) - char_shift
    if input_eq[1] == "+":
        is_addition = 1
    else:
        is_addition = 0
        
    total_moves = raw_input("Is the number of moves 1 or 2? ")
    #Check validity of number of moves
    if total_moves == '1' or total_moves == '2':
        total_moves = ord(total_moves) - char_shift
    else:
        raise Exception("This is not a valid number of moves!")
    
    return [d1,d2,d3], is_addition, total_moves

#Generates all possible correct equations
def get_correct_equations():
    
    equation_list = [] #list in which to store equations
    
    for operation in range(2): #choose the operation (0 - subtraction, 1 - addition)
        for digit1 in range(10): #choose the 1st digit
            if operation == 0:
                digit2_range = range(digit1+1)
            else:
                digit2_range = range(10-digit1)
            
            for digit2 in digit2_range: #choose the 2nd digit (depends on the operation)
                if operation == 0: #choose the 3rd digit (depends on the first 2 digits, and the operation)
                    digit3 = digit1 - digit2
                else:
                    digit3 = digit1 + digit2
                
                equation_list.append([operation, [digit1, digit2, digit3]]) #append new equation to the list
    
    return equation_list

#Takes the correct solution as input, and reforms/returns it 
def output_solution(new_digit_list, new_op, solution_found):
    if not solution_found:
        print "Something's gone horribly wrong!"
    else:
        char_shift = ord('0')
        final_d1 = chr(new_digit_list[0]+char_shift)
        final_d2 = chr(new_digit_list[1]+char_shift)
        final_d3 = chr(new_digit_list[2]+char_shift)
        final_op = '+' if new_op==1 else '-'
        print "The correct configuration is: " + final_d1 + final_op + final_d2 + '=' + final_d3
        