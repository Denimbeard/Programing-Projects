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
class Student(object):

    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    def __name__(self, first, last):
        self.first + self.last


    def main():
        __user = None
        __choice = ['A', 'R', 'L', 'X']
        

        """ While user input is null, offer to accept input. """
        while __user is None:
            __user = input("Choose 'A', 'R', 'L' or 'G' (‘X’ for exit): ")
            
            """ Check that the user has entered an appropriate option, otherwise offer main menu. """
            try:
                __user in __choice 
            except:
                Student.main()      
        
        """ Once a choice is made, perform the following action and then offer main menu again. """
        if __user in __choice:
            
            """ Initiates class as new instance to build a student """
            if __user == 'A':
            #    print('Adding Student')
                first = str(input('Students Given Name: '))
                last = str(input('Students Surname: '))

                print(first + ' ' + last + ' has been added to the database.\n')
                studentList.append(Student(first, last))
                Student.main()
           
            """ Will Remove a class instance """
            if __user == 'R':
                Student.remove()
                print('Removing Student') 
                Student.main()
            
            """ Will list all available instances """
            if __user == 'L':
                print('List of Students: \n')
                for obj in studentList: 
                    print('Given Name' + ' | ' + 'Family Name' + ' | ' + 'GPA' + ' | ' + 'Credit Hours\n')
                    print( obj.first, obj.last, sep =' | ' )
                    print(type(studentList))
                    return studentList
                Student.main()
            
            """ Will add grades to class instance (See class init for maths) """
            if __user == 'G':
                print('Student Grade')
                Student.main()
            
            """ If X is chosen, close system and do not offer main menu. """
            if __user == 'X':
                   Student.exstate()
        else:
            Student.main()

    def remove():
        first = str(input('Students Given Name: '))
        last = str(input('Students Surname: '))


    def exstate():
        print('Thank you.')
        print('Goodbye!')
        exit()

# ==============================================================================
# Output
# ==============================================================================

studentList = []

print('\n')
print('Welcome Administrator!\n')
Student.main()