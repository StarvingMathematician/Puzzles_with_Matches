'''
Created on Sep 30, 2013

@author: Jonathan A Simon

Solves any level from the "Number" portion of the Android game "Puzzles with Matches".
Auxiliary methods are stored in the file "helper_functions".
'''

if __name__ == '__main__':
    from helper_functions import *
    
    neighbors, within_dists, add_dists, sub_dists = get_digit_data() #get transformation data
    digit_list,is_addition,total_moves = get_input() #get problem-specific data from user
    correct_eq_list = get_correct_equations() #get list of all possible correct equations
    
    # Loop through all possible correct equations, and stop when
    # we find one which is reachable from the initial equation.
    solution_found = False
    for new_eq in correct_eq_list:
        
        transform_failed = False
        
        internal_matches = 0
        added_matches = 0
        taken_matches = 0
        
        new_op = new_eq[0]
        new_digit_list = new_eq[1]
        
        if is_addition != new_op:
            if new_op == 0:
                taken_matches += 1
            else:
                added_matches += 1
        
        for idx,old_digit in enumerate(digit_list):
            new_digit = new_digit_list[idx]
            if new_digit in neighbors[old_digit]:
                internal_matches += within_dists[old_digit,new_digit]
                added_matches += add_dists[old_digit,new_digit]
                taken_matches += sub_dists[old_digit,new_digit]
            else:
                transform_failed = True
                break
            
        #This equation is the solution if:
        #1) Each digit was able to be properly transformed
        #2) All added/removed matches are properly accounted for
        #3) The total number of matches moved was exactly the number required
        if (not transform_failed) and (added_matches == taken_matches) and (internal_matches + added_matches == total_moves):
            solution_found = True
            break
    
    output_solution(new_digit_list, new_op, solution_found) #output the solution
    