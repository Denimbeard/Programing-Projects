# Foundations of Programming 2020-21

![Due](https://img.shields.io/date/1616673600?label=Due%20in)

## Term-2 Assignment 100 points (25% of the module)

**Implement a simple Database Management System in Python (ver 3.7) which enables the user to create and maintain a database of students** in Python’s RAM (not on the hard drive).

## PART A (45 marks):  Requirements specification and Interface

Your program will contain a function `main()` which will print a 1-line message containing four possible options (see below) and prompt the user to choose one of these. Depending on what the user’s choice is, the program should perform a different action, as follows:

### PROGRAM’S BEHAVIOUR

- **A** (**A**dd student):
  - **(i)** if the user enters “A”, your code should prompt them to enter a new student’s name and surname (in this order) as two separate strings (see below for “Input Validation / Error checking”). Then, a new student record (containing name and surname) should be added to the current set of students (the ‘database’).
  - **(ii)** If the database *already contains a student with that name and surname*, the program should ***not crash***, but print a warning message (e.g., “Student …. already exists”) and *leave the database unchanged*.
  - **[(i) 5 marks; (ii) 5 marks]**
- **R** (**R**emove student):
  - **(i)** when this option is chosen, the program should ask the user to enter name and surname of an existing student; if present in the database, the corresponding student record should be ***removed*** from it.
  - **(ii)** If the database does not contain the specified student, or it is **empty**, the program **should not** crash but print a warning message (e.g., “Student not found” or “Database empty”) and leave the database unchanged.
  - **[(i) 5 marks; (ii) 5 marks]**
- **L** (**L**ist database):
  - the program should print the full list of students currently in the database, with each student’s surname and name printed (in this order) on a ***separate line***. If the database is empty, the program should ***not crash*** but print a warning (e.g., “Database empty”).
  - **[5 marks]**

After any of ‘A’, ‘R’ or ‘L’ have completed, the code should repeat from the start (i.e., print the 4-option ‘menu’ and wait for a choice). This should be repeated ***until the user enters “X”*** :

- **X** (**E**XIT): the program should terminate ‘gracefully’, ie, without crashing or producing an error.
- **[5 marks]**

**NOTE**: *your interface must closely follow the above requirements. Any differences (e.g., using lowercase ‘a’, ‘r’, ‘l’, ‘x’ instead of ‘A’, ‘R’, ‘L’, ‘X’) will incur in up to **50 PENALTY MARKS**.

## INPUT VALIDATION / ERROR CHECKING

- **(i) If the user enters *anything* other than the allowed options A, R, L, X** (including, e.g, an *empty string*, a number, etc.) **your software should NOT crash.** Instead, it should ignore the invalid input and prompt the user for a new choice.
- (ii) If the name or surname string entered by the user in cases A or R above contains any *non-alphanumeric characters*, or it is empty, the code should **discard the input** (and *not crash*), print an appropriate warning, and ask the user to enter the string again. *This behaviour should be repeated until a valid string is entered.*
- **[(i) 7 marks; (ii) 8 marks]**

### IMPORTANT: THE USE OF PYTHON MODULES IS FORBIDDEN

The presence of an `import` statement in your code will carry a penalty of up to 80 MARKS

## PART B (35 marks):  Requirements specification & Interface

At “Hypothetical University” (who commissioned your software) marks are on a 4-point scale (**A** = 4.0 points, **B** = 3.0, **C**=2.0 and **D**=1.0). Each course is worth a number of “credit hours”. Each student’s final grade is computed using “*Quality Points*” (**QP**s): e.g.,

- if a course is worth 30 credit hours and the student gets an A on it (A= 4.0), then they earn 30 * 4.0 = 120 QPs.

***Extend the code written for Part A so that the menu includes the following additional choice:***

**G** (Add **G**rade):

- When this option is chosen, the program should first:
  - (1) check if the database is empty; if it isn’t
  - (2) ask the user to enter a student’s name and surname (in this order) as two strings.
    - If the student is currently in the ‘database’, the program should then ask the user to enter **first** a grade (one of ‘A’, ‘B’, ‘C’ or ‘D’) as a string, **and then** the corresponding Credit Hours for that grade, as **a float** > 0.0.
    - The student’s record should then be updated to contain ***both*** the QPs *and* corresponding Credit Hours.
    - If the database is *empty* when option G is chosen, or if it does not contain a student with the provided name & surname, the code should ***not crash***, but print an appropriate warning message and *return directly to the main ‘menu’*
      - i.e., without asking the user to enter any further details, e.g., name / grade / credit hours etc.
- **[20 marks]**

*To avoid PENALTY marks, ensure the interface adheres closely to the above specifications.*

## INPUT VALIDATION / ERROR CHECKING (Cont.)

Other than allowing the new option (‘G’), input validation should be *analogous to Part A*.

In addition, when G is chosen:

- (i) **If** the name or surname entered by the user is an empty string or contains a *non-alphanumeric* character; or
- (ii): **If** anything other than a float > 0.0 is entered for credit hours; or
- (iii): If anything other than one of ‘A’, ... ,‘D’ is entered as a grade
  - e.g., an empty string, a number, etc.;
- **then**, the program should ***not crash*** but print an appropriate warning
  - e.g., “Invalid name”, or “Invalid credit hours”, etc.
- and **ask the user to enter the required string (or value) again.**
  - ***This behaviour should be repeated until a correct input is provided***; then, and only then, will the program be allowed to move to the next step.
- **[(i) 5 marks; (ii) 5 marks; (iii) 5 marks]**

## PART C (20 marks): NB: marks for Part C will be awarded *only if* Part B works

### ***Modify the code written for Part B so that option “L” produces the following behaviour***

**L** (**L**ist):

- print all students in the current database. For each, print surname, name, and Grade Point Average, GPA (see below), ***in this exact order***; each student should be printed on a new line. If a student’s record contains no grades, their GPA should be displayed as “**None**”.
  - **[10 marks]**
- The list of students should be printed in *descending* GPA’s order
  - i.e., best students first
  - **[10 marks]**

A student’s GPA is their **total QPs** divided by the **total credit hours** completed. For example, if a student has accumulated 155 QPs by taking different courses *together* worth 55.0 credit hours, his GPA should be 155 / 55.0 = 2.81818181... (or, rounded up to 2 decimals: 2.82).

IMPORTANT: THE USE OF PYTHON MODULES IS FORBIDDEN

## The presence of an `import` statement in your code will carry a penalty of up to 80 MARKS

## TESTING YOUR CODE

Parts B relies on having correctly completed Part A, and Part C relies on Part B. Before moving on to Part B (or C), you should test the correctness of your Part A’s (or B’s) solution. Below are examples of interactive sessions which your system should be able to replicate as shown:

### EXAMPLE TESTING for PART A

|Explanation| Program’s on-screen Output / User Input |
|--|--|
|The user is prompted to make a choice|`Choose A, R, or L (‘X’ for exit):`|
|The user enters ‘A’ and hits “Enter” |`A`|
|The user is prompted to enter a name|`New student’s name:`|
|The user enters “John” and hits “Enter”|`John`|
|The user is prompted to enter a surname|`New student’s surname:`|
|The user enters “White” + Enter|`White`|
|The system outputs a confirmation message|`Student John White has been added`
||`Choose A, R, or L (‘X’ for exit):`|
|The user chooses ‘A’|`A`|
|The user is prompted to enter a name|`New student’s name:`|
|The user enters “Mary” + Enter|`Mary`|
|The user is prompted to enter a surname|`New student’s surname:`|
|The user enters “Smith” + Enter|`Smith`|
|The system outputs a confirmation message|`Student Mary Smith has been added`
||`Choose A, R, or L (‘X’ for exit):`|
|The user chooses ‘L’|`L`|
|The program prints the current database|`White, John`|
||`Smith, Mary` |
||`Choose A, R, or L (‘X’ for exit):`|
|The user chooses ‘R’|`R`|
|The user is prompted to enter a name|`Name of the student to be removed:`|
|The user enters “John”|`John`|
|The user is prompted to enter a surname|`Surname of student to be removed:`|
|The user erroneously enters “Smith”|`Smith`|
|The system issues a warning message...|`No John Smith in database!`|
|... and returns directly to the main menu|`Choose A, R, or L (‘X’ for exit):`|
|The user chooses ‘R’ again|`R`|
|The user is prompted to enter a name|`Name of the student to be removed:`|
|The user enters “John”|`John`|
|The user is prompted to enter a surname|`Surname of student to be removed:`|
|The user enters “White”|`White`|
|The system outputs a confirmation message|`Student John White has been removed`|
||`Choose A, R, or L (‘X’ for exit):`|
|The user chooses ‘L’|`L`|
|The program prints the current database|`Smith, Mary`|
||`Choose A, R, or L (‘X’ for exit):`|
|The user chooses ‘X’|`X`|
|The program gracefully terminates|`Thank you – Goodbye.`|

### EXAMPLE TESTING for PART B & C

#### *Assume the database contains students John White and Mary Smith, as from above Part-A testing>*

|Explanation| Program’s on-screen Output / User Input |
|--|--|
|The user is prompted to make a choice|``Choose A, R, L or G (‘X’ for exit):`|
|The user chooses ‘G’|`G`|
|The user is prompted to enter a name|`Student’s name:`|
|The user enters “John” + Enter|`John`|
|The user is prompted to enter a surname|`Student’s surname:`|
|The user enters “White”|`White`|
|The user is prompted to enter a new grade|`Please enter a grade (A/B/C/D):`|
|The user erroneously enters ‘4.0’|`4.0`|
|The system issues a warning message...|`Invalid grade!`|
|... and asks the user again to enter a grade|`Please enter a grade (A/B/C/D):`|
|The user enters “A”|`A`|
|User is prompted to enter the credit hours|`Please enter credit hours (>0):`|
|The user enters “25.0”|`25.0`|
|The system outputs a confirmation message|`100.0 QPs added to White, John`|
||`Choose A, R, L or G (‘X’ for exit):`|
|The user chooses ‘G’|`G`|
|The user is prompted to enter a name|`Student’s name:`|
||`John`|
|The user is prompted to enter a surname|`Student’s surname:`|
||`White`|
|The user is prompted to enter a new grade|`Please enter a grade (A/B/C/D):`|
|The user enters “C”|`C`|
|User is prompted to enter the credit hours|`Please enter credit hours (>0):`|
|The user enters “35.0”|`35.0`|
|The system outputs a confirmation message|`70.0 QPs added to White, John`|
||`Choose A, R, L or G (‘X’ for exit):`|
|The user enters ‘L’|`L`|
|The program prints the database, with GPAs|`White, John – GPA: 2.83`|
||`Smith, Mary – GPA: None`|
||`Choose A, R, L or G (‘X’ for exit):`|
||`X Thank you – Goodbye.`|

## NOTE: *A different set of tests will be used to assess your code. If your program produces the expected outputs in the above examples, it does not necessarily mean that it is correct, or that it will score full marks.*
