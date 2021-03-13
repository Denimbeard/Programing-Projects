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
Implement a simple Student Management System in Python (ver 3.7) which 
enables the user to create and maintain a database of students
"""
# ==============================================================================
# Variables
# ==============================================================================

# TODO:
# A
"""
Prompt them to enter a new student’s first and surname
as two separate strings
a new Student record (containing first and surname) 
should be added to the current set of students.
"""

# TODO:
# R
"""
Program should ask the user to enter first and surname of an existing Student.
If present in the database, the corresponding Student record 
should be removed from it.
If the database does not contain the specified Student
print a warning message.
"""

# TODO:
# L
"""The program should print the full list of students currently in the database
 with each student’s surname and first printed in order
If the database is empty print a warning.
"""

# TODO:
# X
""" Program should terminate ‘gracefully’. """

# TODO:
# G
""" 
Check if the database is empty
Ask the user to enter a student’s first and surname as two strings.
If the Student is currently in the ‘database’, the program should 
then ask the user to enter first a grade (one of ‘A’, ‘B’, ‘C’ or ‘D’) 
as a string, and then the corresponding Credit Hours for that grade, 
as a float > 0.0.
The student’s record should then be updated to contain both the QPs 
and corresponding Credit Hours.
If the database is empty when option G is chosen, or if it does not 
contain a Student with the provided first & surname, the code should 
not crash, but print an appropriate warning message and return directly 
to the main ‘menu’.
"""

""" Your interface must closely follow the above requirements. """
# ==============================================================================
# Processes
# ==============================================================================
def main():
    user = None
    choice = ['A', 'R', 'L', 'X', 'T']
    
    mark = { 'A':4, 'B':3, 'C':2, 'D':1}
    
    studentList = {}
    studentList['Students'] = {}
    studentID = 1

    def add(ID, dct):
        #    print('Adding Student')
        first = str(input('Students Given Name: '))
        last = str(input('Students Surname: '))

        if first in dct['Students']:
            print('test')
            if last in dct['Students']:
                print('[{} {}] in database already.'.format(first, last))
        
        else:
            print(first + ' ' + last + ' has been added to the database.\n')
            dct['Students'][first + last] = {}
            dct['Students'][first + last]['ID'] = ID
            dct['Students'][first + last]['first'] = first
            dct['Students'][first + last]['last'] = last
            return dct

    def remove():
        first = str(input('Students Given Name: '))
        last = str(input('Students Surname: '))
        print(first + ' ' + last + ' has been removed from the database.\n')

    def catalog(dct):
        print('List of Students: \n')
        print('Given Name' + ' | ' + 'Family Name' + ' | ' + 'Mark' + ' | ' + 'Credit Hours\n')
        print(dct)
        
    def grade():
        pass




    def exstate():
        print('Thank you.')
        print('Goodbye!')
        exit()

    def testing():
        studentList['Students']['TestStudent'] = {}
        studentList['Students']['TestStudent']['ID'] = 0
        studentList['Students']['TestStudent']['first'] = 'Test'
        studentList['Students']['TestStudent']['last'] = 'Student'
        studentList['Students']['TestStudent']['mark'] = 'A'
        studentList['Students']['TestStudent']['hours'] = 100.0

    while user is None:
        user = input("Choose 'A', 'R', 'L' or 'G' (‘X’ for exit): ")

        while user in choice:
            
            if user == 'A':
                add(studentID,studentList)
                studentID =+ 1
                user = None    
                break
            
            if user == 'R':
                print('Removing Student') 
                remove()
                user = None    
                break
                
            if user == 'L':
                catalog(studentList)
                user = None    
                break

            if user == 'G':
                print('Student Grade')
                user = None
                break
        
            if user == 'T':
                testing()
                user = None    
                break   

            if user == 'X':
                exstate() 
        
        else:
            user = None



# ==============================================================================
# Output
# ==============================================================================

print('\n')
print('Welcome Administrator!\n')
main()