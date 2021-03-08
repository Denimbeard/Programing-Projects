# Foundations of Problem Solving IS50003C

- [Foundations of Problem Solving IS50003C](#foundations-of-problem-solving-is50003c)
  - [Coursework 2](#coursework-2)
    - [Due: 26th March, 2021, 17:00](#due-26th-march-2021-1700)
  - [Question 1. (Allocation Problem)](#question-1-allocation-problem)
    - [Using Hungarian algorithm, determine an allocation that provides](#using-hungarian-algorithm-determine-an-allocation-that-provides)
      - [The maximum daily profit](#the-maximum-daily-profit)
      - [The minimum daily profit](#the-minimum-daily-profit)
  - [Question 2. (Transportation Problem)](#question-2-transportation-problem)
    - [Explain why it is necessary to add a dummy demand point](#explain-why-it-is-necessary-to-add-a-dummy-demand-point)
    - [Complete the table below](#complete-the-table-below)
    - [Use the north west corner method to obtain a transportation pattern and calculate the total cost](#use-the-north-west-corner-method-to-obtain-a-transportation-pattern-and-calculate-the-total-cost)
    - [Show that this pattern is not optimal by calculating improvement indices](#show-that-this-pattern-is-not-optimal-by-calculating-improvement-indices)
      - [You must clearly show your shadow costs](#you-must-clearly-show-your-shadow-costs)
    - [Taking the most negative improvement index to indicate the entering square, use the stepping-stone method to obtain an optimal solution](#taking-the-most-negative-improvement-index-to-indicate-the-entering-square-use-the-stepping-stone-method-to-obtain-an-optimal-solution)
      - [You must make your shadow costs and improvement indices clear and demonstrate that your solution is optimal](#you-must-make-your-shadow-costs-and-improvement-indices-clear-and-demonstrate-that-your-solution-is-optimal)
        - [State entering cell, exiting cell and O max at each stage](#state-entering-cell-exiting-cell-and-o-max-at-each-stage)
        - [State the cost of your optimal solution](#state-the-cost-of-your-optimal-solution)
  - [Question 3. (Simplex Algorithm)](#question-3-simplex-algorithm)
    - [Write the information about these components as constraints](#write-the-information-about-these-components-as-constraints)
    - [Write down the objective function](#write-down-the-objective-function)
    - [Determine how many of each should be produced to maximize the profit by doing the following](#determine-how-many-of-each-should-be-produced-to-maximize-the-profit-by-doing-the-following)
      - [Introduce slack variable to convert inequalities to equations and display all the information given above in a simplex tableau. You must write your equations before displaying them in a simplex tableau](#introduce-slack-variable-to-convert-inequalities-to-equations-and-display-all-the-information-given-above-in-a-simplex-tableau-you-must-write-your-equations-before-displaying-them-in-a-simplex-tableau)
      - [By first identifying the pivot column at each stage, solve this linear programming problem. You must clearly show any workings in your table that allows you to choose your pivot row. You must also indicate the pivot row, pivot value and state the row operations you use](#by-first-identifying-the-pivot-column-at-each-stage-solve-this-linear-programming-problem-you-must-clearly-show-any-workings-in-your-table-that-allows-you-to-choose-your-pivot-row-you-must-also-indicate-the-pivot-row-pivot-value-and-state-the-row-operations-you-use)
      - [State the final value of each variable (including slack variables) and of the objective function](#state-the-final-value-of-each-variable-including-slack-variables-and-of-the-objective-function)
  - [Question 4. (Travelling Salesman Problem)](#question-4-travelling-salesman-problem)
    - [By inspection, complete the table of least distances below](#by-inspection-complete-the-table-of-least-distances-below)
    - [Obtain a minimum spanning tree for the network using Prim’s algorithm starting at H, stating the order in which you select the arcs. State it’s length](#obtain-a-minimum-spanning-tree-for-the-network-using-prims-algorithm-starting-at-h-stating-the-order-in-which-you-select-the-arcs-state-its-length)
    - [Use your answer to part (b) to determine an initial upper bound for the length of the route](#use-your-answer-to-part-b-to-determine-an-initial-upper-bound-for-the-length-of-the-route)
    - [Starting from your initial upper bound use short cuts to find an upper bound, which is below 620km. Make your working clear and state the corresponding route](#starting-from-your-initial-upper-bound-use-short-cuts-to-find-an-upper-bound-which-is-below-620km-make-your-working-clear-and-state-the-corresponding-route)
    - [Use the nearest neighbour algorithm starting at E to find a second upper bound for the length of the route](#use-the-nearest-neighbour-algorithm-starting-at-e-to-find-a-second-upper-bound-for-the-length-of-the-route)
    - [By deleting F, and all of its arcs, find a lower bound for the length of the route](#by-deleting-f-and-all-of-its-arcs-find-a-lower-bound-for-the-length-of-the-route)
    - [Use your results to write down the smallest interval which you are confident contains the optimal length of the route](#use-your-results-to-write-down-the-smallest-interval-which-you-are-confident-contains-the-optimal-length-of-the-route)
  - [Question 5. (Network Flow)](#question-5-network-flow)
    - [Write down the source vertices and the sink vertex](#write-down-the-source-vertices-and-the-sink-vertex)
    - [State the value of the feasible flow shown in the network. You must make your method clear](#state-the-value-of-the-feasible-flow-shown-in-the-network-you-must-make-your-method-clear)
    - [Use the labelling procedure to find a maximum flow pattern through this network. You must list each flow-augmenting route you use together with its flow](#use-the-labelling-procedure-to-find-a-maximum-flow-pattern-through-this-network-you-must-list-each-flow-augmenting-route-you-use-together-with-its-flow)
    - [Show the maximum flow obtained in (c) on a new copy of the network and state its value](#show-the-maximum-flow-obtained-in-c-on-a-new-copy-of-the-network-and-state-its-value)
    - [By finding a suitable cut, prove that your flow is maximal](#by-finding-a-suitable-cut-prove-that-your-flow-is-maximal)
  - [Question 6. (Dynamic Programming)](#question-6-dynamic-programming)
    - [Use dynamic programming to find the building schedule that maximises the total expected profit](#use-dynamic-programming-to-find-the-building-schedule-that-maximises-the-total-expected-profit)

## Coursework 2

### Due: 26th March, 2021, 17:00

Each question carries 20 marks. You should answer 5 questions out
of 6. You may answer ALL 6 but marks will only be awarded to the
best 5 questions. Good luck!

## Question 1. (Allocation Problem)

||Cafe|Dessert Shop|Restaurant|Snack Shop|
|--|--|--|--|--|
|A|835|366|No|649|
|B|875|376|581|594|
|C|744|290|No|666|
|D|900|501|795|No|

The owner of a theme park wishes to provide a snack shop, a restaurant, a café and a dessert shop at four sites A, B, C and D. He employs a market researcher who estimates the daily profit of each type of catering at each site.

The market researcher also suggests some of the catering are not suitable at some of the
sites and these are indicated by a No.

Complete the data in the table by choosing suitable numbers to put at the sites marked ‘No’ so that they become ‘unattractive’

### Using Hungarian algorithm, determine an allocation that provides

#### The maximum daily profit

#### The minimum daily profit

In either case, you must make your method clear and show the table after each
stage. You must present the possible allocations showing optimal solution from your
results in a bipartite graph and also state all possible allocations (if more than one)
and give the total (maximum or minimum) daily profit.

## Question 2. (Transportation Problem)

The table below shows the cost, in pounds, of transporting a car from each factory
A, B and C, to each showroom X and Y. It also shows the number of cars available at each
factory and the number required at each showroom. The total cost of transporting the cars
is to be minimized.

||X|Y|Supply|
|--|--|--|--|
|A|4|7|60|
|B|6|9|50|
|C|3|7|25|
|Demand|45|75| _ |

### Explain why it is necessary to add a dummy demand point

### Complete the table below

||X|Y|Z|Supply|
|--|--|--|--|--|
|A|4|7|_|60|
|B|6|9|_|50|
|C|3|7|_|25|
|Demand|45|75|_|_|

### Use the north west corner method to obtain a transportation pattern and calculate the total cost

### Show that this pattern is not optimal by calculating improvement indices

#### You must clearly show your shadow costs

### Taking the most negative improvement index to indicate the entering square, use the stepping-stone method to obtain an optimal solution
  
#### You must make your shadow costs and improvement indices clear and demonstrate that your solution is optimal

##### State entering cell, exiting cell and O max at each stage

##### State the cost of your optimal solution

## Question 3. (Simplex Algorithm)

Suppose a company manufactures different electronic components A, B and C for computers. Component A requires 3 hours of fabrication and 2 hours of assembly; component B requires 4 hours of fabrication and 2 hours of assembly; component C requires 3 hours of fabrication and 3 hours of assembly. The company has up to 1200 labour-hours for fabrication and 1000 hours for assembly time each week.

- Let $x$ = the number of components of type $A$
- Let $y$ = the number of components of type $B$
- Let $z$ = the number of components of type $C$, and $x ≥ 0$, $y ≥ 0$, $z ≥ 0$

### Write the information about these components as constraints

If the profit on each component A, B and C is £8, £9 and £11 respectively,

### Write down the objective function

### Determine how many of each should be produced to maximize the profit by doing the following

#### Introduce slack variable to convert inequalities to equations and display all the information given above in a simplex tableau. You must write your equations before displaying them in a simplex tableau

#### By first identifying the pivot column at each stage, solve this linear programming problem. You must clearly show any workings in your table that allows you to choose your pivot row. You must also indicate the pivot row, pivot value and state the row operations you use

#### State the final value of each variable (including slack variables) and of the objective function

## Question 4. (Travelling Salesman Problem)

! [TravellingSalesmanProblem](/Goldsmiths/Problem Solving/Assessments/Assessment 2/img/Salesman.png)

The network in the diagram above shows the distances, in km, between eight weather data collection points. Starting and finishing at A, Alice needs to visit each collection point at least once, in a minimum distance.

### By inspection, complete the table of least distances below

||A|B|C|D|E|F|G|H|
|--|--|--|--|--|--|--|--|--|
|A|-|102|57|_|98|132|_|_|
|B|102|-|68|108|127|_|_|219|
|C|57|68|-|64|59|75|_|_|
|D|_|108|64|-|_|89|_|111|
|E|98|127|59|_|-|61|87|_|
|F|132|_|75|89|61|-|56|75|
|G|_|_|_|_|87|56|-|38|
|H|_|219|_|111|_|75|38|-|

### Obtain a minimum spanning tree for the network using Prim’s algorithm starting at H, stating the order in which you select the arcs. State it’s length

### Use your answer to part (b) to determine an initial upper bound for the length of the route

### Starting from your initial upper bound use short cuts to find an upper bound, which is below 620km. Make your working clear and state the corresponding route

### Use the nearest neighbour algorithm starting at E to find a second upper bound for the length of the route

### By deleting F, and all of its arcs, find a lower bound for the length of the route

### Use your results to write down the smallest interval which you are confident contains the optimal length of the route

## Question 5. (Network Flow)

The above network models a drainage system. The capacity of each arc is shown on the arc, in litres per second, and the numbers in circles indicate a feasible flow through the network.

### Write down the source vertices and the sink vertex

### State the value of the feasible flow shown in the network. You must make your method clear

Taking the flow shown as your initial flow pattern,

### Use the labelling procedure to find a maximum flow pattern through this network. You must list each flow-augmenting route you use together with its flow

### Show the maximum flow obtained in (c) on a new copy of the network and state its value

### By finding a suitable cut, prove that your flow is maximal

## Question 6. (Dynamic Programming)

Annie is planning to build four properties 𝐴, 𝐵, 𝐶 and 𝐷 at the rate of 1 per year. The order in which the properties are built depend on choice, but the costs will vary as some left-over materials from building one property can be used for the next one. The expected profits, in pounds, are given in the table below.

|Already Built|Expected Profit|||||
|--|--|--|--|--|--|
|||A|B|C|D||
|None||55|70|75|85|

|Already Built|Expected Profit|A|B|C|D|
|--|--|--|--|--|--|
|A||-|77|88|85|
|B||65|-|85|88|
|C||62|73|-|90|
|D||67|75|86|-|
|A and B||-|-|89|93|
|A and C||-|76|-|87|
|A and D||-|79|88|-|
|B and C||70|-|-|91|
|B and D||74|-|90|-|
|C and D||71|78|-|-|
|A, B and C||-|-|-|95|
|A, B and D||-|-|92|-|
|A, C and D||-|81|-|-|
|B, C and D||75|-|-|-|

### Use dynamic programming to find the building schedule that maximises the total expected profit
