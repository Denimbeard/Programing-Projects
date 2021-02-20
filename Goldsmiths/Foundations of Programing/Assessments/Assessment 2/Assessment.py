#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author Details
# =============================================================================
__author__ = 'Chet Coenen'
__copyright__ = 'Copyright 2020'
__credits__ = ['Chet Coenen']
__license__ = '/LICENSE'
__version__ = '1.0'
__status__ = 'Building'
# ==============================================================================
# Contact
# ==============================================================================
__maintainer__ = 'Chet Coenen'
__email__ = 'chet.m.coenen@icloud.com'
__socials__ = '@Denimbeard'
__username__ = 'Denimbeard'
# =============================================================================
# Class Data
# =============================================================================
__course__ = 'Foundations of Programing'
__date__ = '8 December 2020'
__teammates__ = ['Chet Coenen']
__laboratory__ = ''
__description__ = 'Assessment 2'
__studentid__ = '33683213'
# =============================================================================
# Instructions
# ==============================================================================
"""
Implement a simple Database Management System in Python (ver 3.7) which 
enables the user to create and maintain a database of students
"""
# ==============================================================================
# Variables
# ==============================================================================

# TODO:
# A
"""
Prompt them to enter a new student’s name and surname
as two separate strings
a new student record (containing name and surname) 
should be added to the current set of students.
"""

# TODO:
# R
"""
Program should ask the user to enter name and surname of an existing student.
If present in the database, the corresponding student record 
should be removed from it.
If the database does not contain the specified student
print a warning message.
"""

# TODO:
# L
"""The program should print the full list of students currently in the database
 with each student’s surname and name printed in order
If the database is empty print a warning.
"""

# TODO:
# X
""" Program should terminate ‘gracefully’. """

# TODO:
# G
""" 
Check if the database is empty
Ask the user to enter a student’s name and surname as two strings.
If the student is currently in the ‘database’, the program should 
then ask the user to enter first a grade (one of ‘A’, ‘B’, ‘C’ or ‘D’) 
as a string, and then the corresponding Credit Hours for that grade, 
as a float > 0.0.
The student’s record should then be updated to contain both the QPs 
and corresponding Credit Hours.
If the database is empty when option G is chosen, or if it does not 
contain a student with the provided name & surname, the code should 
not crash, but print an appropriate warning message and return directly 
to the main ‘menu’.
"""

""" Your interface must closely follow the above requirements. """
# ==============================================================================
# Processes
# ==============================================================================

class Database(object): 
    database = []

    # Counter for student total
    studentid = 000  
    
    # Bool states for functions
    addstate = False
    restate = False
    rosstate = False
    exstate = False
    grastate = False
# ==============================================================================
# Dunder Functitons
# ==============================================================================
    def __init__ (self):
        self.first = str(input('Students Given Name: '))
        self.last = str(input('Students Surname: '))
        self.__class__.database.append(self)
        Database.studentid += 1
        print('{} {} has been added to the database.'.format(self.first, 
            self.last))
    
    def __str__(self):
        return '{} {}'.format(self.first, self.last)

    
# ==============================================================================
# Standard/Custom Functitons
# ==============================================================================   

    # def remove():
    #    pass

    #def roster():
    #    pass

    #def exit():
    #    pass

    #def grade():
    #    pass

    def fullname(self):
        return("{} {}".format(self.first, self.last))

    def main():
        _user = None
        choice = ['A', 'R', 'L', 'G', 'X']
        while _user is None:
            _user = input("Choose 'A', 'R', 'L' or 'G' (‘X’ for exit):")
            try:
                _user in choice 
            except:
                Database.main()      
        if _user in choice:
            if _user == 'A':
                print('Adding Student')
                Database.main()
            if _user == 'R':
                print('Removing Student') 
                Database.main()
            if _user == 'L':
                print('List of Students')
                Database.main()
            if _user == 'G':
                print('Student Grade')
                Database.main()
            if _user == 'X':
                print('Thank You')
                print('Goodbye!')
                exit()   
        else:
            Database.main()
# ==============================================================================
# Output
# ==============================================================================
Database.main()
