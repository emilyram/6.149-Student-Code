# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 15:23:38 2016

@author: Emily
"""

def weighted_total(total_weight, grades, points_possible):
    grade_total = 0
    for grade in grades:
        grade_total += grade
    raw_grade = grade_total / points_possible
    weighted_total = total_weight * raw_grade
    return weighted_total #This replaces the long function with the output
    #in case I want to use that output for something else. Example: a function
    #for 5 + 5 would give an output of 10, and return function allows me to
    #store function as variable with value 10

psets = weighted_total(30.0, [23.0, 100.00, 95.00, 85.00, 85.00, 90.00], 523)
labs = weighted_total(30.0, [10.0, 10.0, 10.0, 7.5], 40)
exams = weighted_total(40.0, [25.5, 35, 31], 120)

print psets
print labs
print exams
grade = psets + labs + exams
print grade