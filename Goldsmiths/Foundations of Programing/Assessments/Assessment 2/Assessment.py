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
__date__ = '19 Feb 2021'
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
# Processes
# ==============================================================================

def main(): 
# ==============================================================================
# Variables
# ==============================================================================    
    
# User Data
    # Menu State
    user = None
    # Menu Options
    choice = [ 'A', 'G', 'L', 'R', 'T', 'X']
    # Marking Scheme, in float for ease of computation 
    mark = { 'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0}

# Student Data
    # ID Counter
    studentID = 1
    # Full Dictionary
    studentList = {}
    # Student Dictionary
    studentList['Students'] = {}

# Add Student Function
    def add(ID, dct):
        # Collect Student Name
        first = str(input('Students Given Name: '))
        last = str(input('Students Surname: '))

        # Verify Name is not in Database
        if datachk(dct,first,last) is not True:
            print(first + ' ' + last + ' has been added to the database.\n')
            
            # If Name is not in Database, Add it and Generate ID
            dct['Students'][first + last] = {}
            dct['Students'][first + last]['ID'] = ID
            dct['Students'][first + last]['first'] = first
            dct['Students'][first + last]['last'] = last
            dct['Students'][first + last]['Hours'] = 0
            dct['Students'][first + last]['QP'] = 0
            return dct

# Removal Function
    def remove(dct):
        # Collect Student Name
        first = str(input('Students Given Name: '))
        last = str(input('Students Surname: '))
        
        # Verify Name is in Database
        if datachk(dct,first,last) is True:
            
            # Remove Item
            del dct['Students'][first+last]
            print('{} {} has been removed from the database.'.format(first, last))
            return dct

# List Function        
    def catalog(dct):
        print('| ')
        catalogFormat(dct, 4)

# Pretty Print
    def catalogFormat(dct):
        for key, value in dct.items():
            # Checks for multiple instances of dict in the main dict
            if isinstance(value, dict):
                # Brings out the next dictionary if there is one
                catalogFormat(value)
            
            else:
                GPA = 0
                
                try:
                    GPA = dct.get('QP')/dct.get('Hours')

                except ZeroDivisionError:
                    GPA = 'No'
                
                print('| {}, {} : {} GPA'.format(dct.get('last'), dct.get('first'),GPA))
                break



# Grade Entry Functions
    def grade(dct, user, mark): 
        
        # Grade Menu States
        guser = None
        choice = ['A', 'B', 'C', 'D', 'E', 'F']
        first = None
        last = None
        grade = None
        hours = None        
            
        # First Name Verifier
        while guser is None:
            first = str(input('Students Given Name: '))
            guser = 'A'

            # Begin Grade Menu
            while guser in choice:
                
                # Check if First Name is alphanumerical
                if guser == 'A':
                    
                    # If yes, Move on
                    if namechk(first) is True:
                        guser = 'B' 
                    
                    # If no, Try Again
                    else: 
                        print('Please do not use special symbols.')
                        guser = None
            
            # Last Name Verifier
                # Check if Last Name is alphanumerical
                if guser == 'B':
                    last = str(input('Students Surname: '))
                    
                    # If yes, Move on
                    if namechk(last):
                        guser = 'C' 
                            
                    # If no, Try Again    
                    else:
                        print('Please do not use special symbols.') 
                        guser = 'B'
                         
            # Data Verifier    
                if guser == 'C':
                    
                    # Check Database for Full Name Combination
                    # If Student is in Database, Move on
                    if datachk(dct, first, last) is True:
                        guser = 'D'
                         
                    # If not, Try Again    
                    else:
                        print('No student by that name in the database. Please try again.')
                        user = None
                        break
            
            # Grade Input
                if guser == 'D':
                    grade = input('Grade: ')

                    # Verify that the mark provided is valid, per the user settings above
                    try: 
                        type(grade) == str
                        
                        # If so, Move on
                        if grade in mark:
                            guser = 'E'
                    
                    # If not, Try Again
                    except: 
                        print('Please enter a proper grade letter. (A, B, C, or D)')
                        
            # Credit Hours Input
                if guser == 'E':
                    
                    #Verify that the hours provided are a float
                    try: 
                        hours = float(input('Hours: '))

                    #If not, Try Again    
                    except:
                        print('Sorry, please enter a decimal number.')
                        guser = 'E'    

                    #If so, Move on    
                    guser = 'F'
                        
            # Database Updater
                if guser == 'F':
                    
                    # Update Student Grade
                    dct['Students'][first + last]['Grade'] = grade
                    
                    # Update Student Credit Hours
                    dct['Students'][first + last]['Hours'] = hours
                    
                    # Update Student QP
                    #Student QP is Credit Hours times Mark Value
                    dct['Students'][first + last]['QP'] = hours * mark[grade]
                    
                    # Return to Main Menu
                    user = None
                    break
            
            # Menu Loop for bad input
            else:
                guser = None

# Exit Function
    def exstate():
        print('Thank you.')
        print('Goodbye!')
        exit()

# Test Student Generator for System Validation
    def testing():

        # Generate Student File
        studentList['Students']['TestStudent'] = {}
        
        # Test Student Will Always Be ID 0
        studentList['Students']['TestStudent']['ID'] = 0
        
        # Test Student is named 'Test Student'
        studentList['Students']['TestStudent']['first'] = 'Test'
        studentList['Students']['TestStudent']['last'] = 'Student'
        
        # Given Mark to Verify Calculations
        studentList['Students']['TestStudent']['Grade'] = 'A'
        studentList['Students']['TestStudent']['Hours'] = 100.0
        studentList['Students']['TestStudent']['QP'] = studentList['Students']['TestStudent']['Hours'] * mark[studentList['Students']['TestStudent']['Grade']]
        
        # Confirms Creation
        print('Test Student added.')

# Student Name Verification, to ensure name data is alphanumerical
    def namechk(name):
        return name.isalnum()

# Database Checker  
    def datachk(dct, fname, lname):
        if fname+lname in dct['Students']:
            
            # Confirms Student Location
            print('{} {} is in the database.'.format(fname, lname))
            return True

        else: 
            # Confirms Student Location
            print('{} {} is not in the database.'.format(fname, lname))
            return False

# Choice Function, Main Menu Controller
    while user is None:
        user = input("Choose 'A', 'G', 'L' or 'R' (‘X’ for exit): ")

        while user in choice:
            
            # Add a new Student Record
            if user == 'A':
                add(studentID,studentList)
                studentID =+ 1
                user = None    
                break
            
            # Remove an Existing Student Record
            if user == 'R':
                remove(studentList)
                user = None    
                break

            # Print Full Database    
            if user == 'L':
                catalogFormat(studentList)
                user = None    
                break
            
            # Add Grade to Existing Student Record
            if user == 'G':
                grade(studentList, user, mark)
                user = None
                break
            
            # Build Test Student
            # Disabled for Graded Build
            if user == 'T':
                testing()
                user = None    
                break   

            # Exit Program        
            if user == 'X':
                exstate() 
        
        # Continue Menu Loop
        else:
            user = None

# ==============================================================================
# Output
# ==============================================================================

# Print a Break, Welcome the User, Start the Program
print('\n')
print('Welcome Administrator!\n')
main()