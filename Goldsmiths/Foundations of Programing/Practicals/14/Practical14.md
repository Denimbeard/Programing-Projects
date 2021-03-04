# Foundations of Programming – Lab Session 14

- [Foundations of Programming – Lab Session 14](#foundations-of-programming--lab-session-14)
  - [Sieve of Eratosthenes](#sieve-of-eratosthenes)
    - [Example](#example)
  - [Write a Python implementation of the “Sieve of Eratosthenes” algorithm using lists](#write-a-python-implementation-of-the-sieve-of-eratosthenes-algorithm-using-lists)
    - [Example – Here’s what an interactive session with your program should look like](#example--heres-what-an-interactive-session-with-your-program-should-look-like)
  - [OPTIONAL – attempt this only after completing Question 1)](#optional--attempt-this-only-after-completing-question-1)
    - [Modify / extend the program you have written for Question 1) so that, instead of producing the list of all primes £ m, it outputs the first m prime numbers.](#modify--extend-the-program-you-have-written-for-question-1-so-that-instead-of-producing-the-list-of-all-primes--m-it-outputs-the-first-m-prime-numbers)
  - [Sieve](#sieve)

## Sieve of Eratosthenes

An integer number $n > 1$ is prime if and only if n has no positive divisors other than 1 and itself.

The following example illustrates an algorithm – known as the “Sieve of Eratosthenes” – for finding all prime numbers less than or equal to a given upper bound $n$ (with $n > 1$):

### Example

Let $n$ be $30$; to find all the prime numbers $<= 30$, first generate a `list` of integers from $2$ to $30$:

`list` = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

The first number in the list is $2$. We note that $2x2<= 30$, so we proceed and cross out every 2nd number in the list after 2 (these will be all the multiples of $2$ larger than $2$) itself:

`list` = [2, 3, ~~4~~, 5, ~~6~~ , 7, ~~8~~, 9, ~~10~~, 11, ~~12~~, 13, ~~14~~, 15, ~~16~~, 17, ~~18~~, 19, ~~20~~, 21, ~~22~~, 23, ~~24~~, 25, ~~26~~, 27, ~~28~~, 29, ~~30~~]

The next number in the (resulting) list after 2 is 3. We note that $3 x 3 <= 30$, so we proceed and cross out all multiples of $3$ (larger than $3$) in the list:

`list` = [2, 3, ~~4~~, 5, ~~6~~ , 7, ~~8~~, ~~9~~, ~~10~~, 11, ~~12~~, 13, ~~14~~, ~~15~~, ~~16~~, 17, ~~18~~, 19, ~~20~~, ~~21~~, ~~22~~, 23, ~~24~~, 25, ~~26~~, ~~27~~, ~~28~~, 29, ~~30~~]

The next number not yet crossed out in the (remaining) list is $5$. We note that $5 x 5 <= 30$, so we proceed and cross out all multiples of $5$ (larger than $5$) in the list:

`list` = [2, 3, ~~4~~, 5, ~~6~~ , 7, ~~8~~, ~~9~~, ~~10~~, 11, ~~12~~, 13, ~~14~~, ~~15~~, ~~16~~, 17, ~~18~~, 19, ~~20~~, ~~21~~, ~~22~~, 23, ~~24~~, 25, ~~26~~, ~~27~~, ~~28~~, 29, ~~30~~]

The next number not yet crossed out in the list after 5 is 7. The next step would be to cross out all multiples of 7 in the list (larger than 7). However, we note that 7 x 7 > 30, so we stop.

The numbers not crossed out at this point in the list are all the prime numbers £ 30:

## Write a Python implementation of the “Sieve of Eratosthenes” algorithm using lists

Your code should ask the user to enter an integer m as input (assume, or ensure, that m is
integer and larger than 1) and then print in output the list of all primes £ m.

### Example – Here’s what an interactive session with your program should look like

|Step Input|Output|
|--|--|
|<The program asks for the upper bound >|Please enter an upper limit (>1)|
|<The user enters “30”>| 30|
|<Program prints the list of all primes £ 30 > |[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]|

HINT: Start by just thinking about the problem. Once the solution is clear in your mind, then,
and only then, use flowcharts or pseudocode to write a first draft of your program.

## OPTIONAL – attempt this only after completing Question 1)

One way to determine if a number n is prime is to use the Sieve of Erathostenes and produce
the list all primes £ n: if, after the Sieve has terminated, n still belongs to that list (i.e., it has not been crossed out), then it is prime. 

### Modify / extend the program you have written for Question 1) so that, instead of producing the list of all primes £ m, it outputs the first m prime numbers.

## Sieve

Sieve of Eratosthenes is a simple and ancient algorithm used to find the prime numbers up to any given limit. It is one of the most efficient ways to find small prime numbers.

For a given upper limit n the algorithm works by iteratively marking the multiples of primes as composite, starting from 2. Once all multiples of 2 have been marked composite, the multiples of next prime, i.e. 3 are marked composite. This process continues until p*p ≤ n where p is the current prime number.

Following is the algorithm of Sieve of Eratosthenes to find prime numbers.

1. To find out all primes under n, generate a list of all integers from 2 to n.

(Note: 1 is not a prime number)

2. Start with a smallest prime number, i.e. p = 2
3. Mark all the multiples of p which are less than n as composite. To do this, we will mark the number as 0. (Do not mark p itself as composite.)
4. Assign the value of p to the next non-zero number in the list which is greater than p.
5. Repeat the process until p*p ≤ n