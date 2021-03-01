#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author Details
# =============================================================================
__author__ = 'Chet Coenen, Aleksander Szczepanski'
__copyright__ = 'Copyright 2020'
__credits__ = ['Chet Coenen', 'Aleksander Szczepanski']
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
__date__ = 'Friday, 19 February 2021'
__teammates__ = ['Chet Coenen', 'Aleksander Szczepanski']
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
# ==============================================================================
# Processes
# ==============================================================================
class Student(object):
    count = 0
    
    def __init__(self, first, last):
        self.number = Student.count
        self.first = first
        self.last = last
        Student.count += 1
    
    def main():
        __user = None
        __choice = ['A', 'R', 'L', 'X', 'Test']
        

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
                Student.add()
                Student.main()
           
            """ Will Remove a class instance """
            if __user == 'R':
                Student.remove()
                print('Removing Student') 
                Student.main()
            
            """ Will list all available instances """
            if __user == 'L':
                print('List of Students: \n')
                print('Given Name' + ' | ' + 'Family Name' + ' | ' + 'GPA' + ' | ' + 'Credit Hours\n')
                for obj in studentList: 
                    print( obj.first, obj.last, sep =' | ' )
                Student.main()
            
            """ Will add grades to class instance (See class init for maths) """
            if __user == 'G':
                print('Student Grade')
                obj.gpa = input('Enter Grade: ')
                obj.credit = input('Enter Credit Hours: ')
                Student.main()
            
            """ If X is chosen, close system and do not offer main menu. """
            if __user == 'X':
                   Student.exstate()

            if __user == 'Test':
                Student.test()
                Student.main()
        else:
            Student.main()

    def add():
        sl = studentList
        print('Adding Student')
        first = str(input('Students Given Name: '))
        last = str(input('Students Surname: '))
        
        cnt = studentList.count(str(first))
        
        if cnt >1:
            print('Student already in database.')
        else:
            studentList.append(Student(first, last))
            print(first + ' ' + last + ' has been added to the database.\n')
            
    def remove():
        first = str(input('Students Given Name: '))
        last = str(input('Students Surname: '))


    def exstate():
        print('Thank you.')
        print('Goodbye!')
        exit()
    
    def test():
        first = 'Test'
        last = 'Student'
        Student(first, last)
        studentList.append(Student(first, last))
# ==============================================================================
# Output
# ==============================================================================

studentList = []

print('\n')
print('Welcome Administrator!\n')
Student.main()