# Foundations of Programming 2020-2021

## Term1 Assignment – contains 100 marks (**25% of module**)

### Introduction – Finite State Acceptors

Similar to flowcharts, **Finite State Acceptors (FSA)** – also known as *Finite State Automata* or **‘recognizers’** – describe systems (algorithms) which, given a string of characters of any length, produce a binary output (`True`/`False`) indicating whether the string is *‘accepted’* or not.

Each state of an FSA is either *“accepting”* or *“non accepting”*. The FSA scans (*from left to right*) all characters of the input string, one by one. After the last character has been scanned, if the current state of the FSA is an ‘*accepting state*’, the string is accepted; otherwise, it is rejected.

The example below shows an FSA that accepts (exclusively) the string “nice”. In this recognizer, the only accepting state is state **S5**:

S1 n S2 i S3 c S4 e S5
(Start) (n found) (i found) (c found) (Accept)
not n not i not c not e any character
S6
(Error)
any character

Note that FSAs are case sensitive (e.g., the character “n” is not the same as “N”, etc.). Also, in the above recognizer the string “nice ” (containing a space, ‘ ’, at the end) would not be accepted, as this additional character would cause the FSA to terminate in state **S6** (which is not an accepting state). Similarly, the string “nic” (containing just the first 3 correct characters of “nice”), for example, would not be accepted, either.

Recognizers can also be described using an equivalent “state transition table”. For illustrative purposes, the state transition table for the FSA shown above is provided below:

|INPUT\Current State|S1 (Start)|S2|S3|S4|S5 (Accept)|S6 (Error)|
|--|--|--|--|--|--|--|
|n|**S2**|S6|S6|S6|S6|S6|
|i|S6|**S3**|S6|S6|S6|S6|
|c|S6|S6|**S4**|S6|S6|S6|
|e|S6|S6|S6|**S5**|S6|S6|
|any other character|S6|S6|S6|S6|S6|S6|

### IMPLEMENTING AN FSA in PYTHON

This assignment requires you to implement the FSA shown below, using Python (ver. 3.7):
CAC BBACCB
S1 A S2 S3 B S4 B S5 A S6 S7

any character
not (A or B or C)
not A
not (A or B)
any character
S8
**Fig. 1**

In this recognizer, the starting state is S1, and S7 is the only accepting state (empty strings are not accepted). Your program should ask the user to enter a string and print “`True`” if the above FSA accepts it, “`False`” otherwise. After printing the result (and a ‘`Goodbye`’ message), the program should immediately stop.

### USER INTERFACE SPECIFICATIONS

|Here is an example of what a single run of your program should look like:||
|--|--|
|(on-screen output):|`Please enter the string to be recognized:`|
|(the user enters a string, e.g., “`ABHello!#`”)||
|(on-screen output):|`False.`|
||`Goodbye.`|

**Note:** after printing the outcome, the program should not ask the user to enter another string, but simply terminate.

### Any significant departures from the above requirements will lead to a loss of up to 20 marks.

**NOTE:** the string entered by the user can be of ***any length***. In case the user enters an ***empty*** string (‘’), the program should *not crash*, but print the correct result (`False`) and stop.

### ASSESSMENT

Your program will be assessed purely on its ability to correctly recognise “acceptable” strings and to correctly reject “non-acceptable” ones, as specified by the FSA given in Fig. 1 above.

The mark will be calculated by running the code you submit on a set of 50 tests, including a variable number of acceptable and non-acceptable strings (generated at random). For each acceptable string correctly recognised, and for each non-acceptable string correctly rejected (i.e., such that your code prints “True” or “False” as required), 2 points will be awarded. If your program prints the incorrect result, crashes, or fails to terminate, it will score 0 points on that test. The final mark will be the sum of the points scored by your code on the 50 tests.
