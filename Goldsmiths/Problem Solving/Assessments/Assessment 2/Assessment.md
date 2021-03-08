# Foundations of Problem Solving IS50003C

- [Foundations of Problem Solving IS50003C](#foundations-of-problem-solving-is50003c)
  - [Coursework 2](#coursework-2)
  - [Question 1 (Allocation Problem)](#question-1-allocation-problem)
    - [Original](#original)
    - [Convert "No" to 0](#convert-no-to-0)
    - [Remove Smallest Row Value from Each Row](#remove-smallest-row-value-from-each-row)
    - [Remove Smallest Column Values](#remove-smallest-column-values)
    - [Complete the data in the table by choosing suitable numbers to put at the sites marked ‘No’ so that they become ‘unattractive’](#complete-the-data-in-the-table-by-choosing-suitable-numbers-to-put-at-the-sites-marked-no-so-that-they-become-unattractive)
      - [Chosen numbers: 366, 290, 501](#chosen-numbers-366-290-501)
    - [Remove Smallest Row Value from Each Row](#remove-smallest-row-value-from-each-row-1)
    - [Remove Smallest Column Values](#remove-smallest-column-values-1)
    - [New Reduced Cost Matrix](#new-reduced-cost-matrix)
  - [Using the Hungarian algorithm, determine an allocation that provides](#using-the-hungarian-algorithm-determine-an-allocation-that-provides)
    - [Maximum Daily Profit](#maximum-daily-profit)
    - [Minimum Daily Profit](#minimum-daily-profit)
      - [Adding 55 to Each Covered Row and Column](#adding-55-to-each-covered-row-and-column)
      - [Removing 55 From Each Item](#removing-55-from-each-item)

## Coursework 2

- Due 26th March 2021, 17:00
- Chet Coenen
- ccoen001

## Question 1 (Allocation Problem)

### Original

||Cafe|Dessert Shop|Restaurant|Snack Shop|
|:--|:-:|:-:|:-:|:-:|
|A|835|366|No|649|
|B|875|376|581|594|
|C|744|290|No|666|
|D|900|501|795|No|

### Convert "No" to 0

||Cafe|Dessert Shop|Restaurant|Snack Shop|Smallest Values|
|:--|:-:|:-:|:-:|:-:|-:|
|A|835|366|0|649|0|
|B|875|376|581|594|376|
|C|744|290|0|666|0|
|D|900|501|795|0|0|
|Smallest Values|744|290|0|501|
|Totals|3354|1533|1376|2410|

### Remove Smallest Row Value from Each Row

||Cafe|Dessert Shop|Restaurant|Snack Shop|Smallest Values|
|:--|:-:|:-:|:-:|:-:|-:|
|A|835|366|0|649|0|
|B|499|0|205|218|0|
|C|744|290|0|666|0|
|D|900|501|795|0|0|
|Smallest Values|499|0|0|0|
|Totals|2978|1157|1000|1533|

### Remove Smallest Column Values

||Cafe|Dessert Shop|Restaurant|Snack Shop|Smallest Values|
|:--|:-:|:-:|:-:|:-:|-:|
|A|336|366|0|649|0|
|B|0|0|205|218|0|
|C|245|290|0|666|0|
|D|401|501|795|0|0|
|Smallest Values|0|0|0|0|
|Totals|982|1157|1000|1533|

### Complete the data in the table by choosing suitable numbers to put at the sites marked ‘No’ so that they become ‘unattractive’

#### Chosen numbers: 366, 290, 501

||Cafe|Dessert Shop|Restaurant|Snack Shop|Smallest Values|
|:--|:-:|:-:|:-:|:-:|--:|
|A|835|366|*366*|649|0|
|B|875|376|581|594|376|
|C|744|290|*290*|666|0|
|D|900|501|795|*501*|0|
|Smallest Values|744|290|290|501|
|Totals|3354|1533|2032|2410|

### Remove Smallest Row Value from Each Row

||Cafe|Dessert Shop|Restaurant|Snack Shop|Smallest Values|
|:--|:-:|:-:|:-:|:-:|--:|
|A|469|0|0|283|0|
|B|499|0|205|218|0|
|C|454|0|0|376|0|
|D|399|0|294|0|0|
|Smallest Values|399|0|0|0|
|Totals|1821|0|499|877|

### Remove Smallest Column Values

||Cafe|Dessert Shop|Restaurant|Snack Shop|Smallest Values|
|:--|:-:|:-:|:-:|:-:|--:|
|A|70|0|0|283|0|
|B|100|0|205|218|0|
|C|55|0|0|376|0|
|D|0|0|294|0|0|
|Smallest Values|0|0|0|0|
|Totals|225|0|499|877|

### New Reduced Cost Matrix

||Cafe|Dessert Shop|Restaurant|Snack Shop|Smallest Values|
|:--|:-:|:-:|:-:|:-:|--:|
|A|70|0|0|283|0|
|B|100|0|205|218|0|
|C|55|0|0|376|0|
|D|0|0|294|0|0|
|Smallest Values|0|0|0|0|
|Totals|225|0|499|877|

## Using the Hungarian algorithm, determine an allocation that provides


### Maximum Daily Profit


Start:

- Lines required: 4
- Total lines: 3/4

||Cafe|~~Dessert Shop~~|~~Restaurant~~|Snack Shop||Row Line|
|:-|:-:|:-:|:-:|:-:|:-:|-:|
|A|70|~~0~~|~~0~~|283||N|
|B|100|~~0~~|~~205~~|218||N|
|C|55|~~0~~|~~0~~|376||N|
|~~D~~|~~0~~|~~0~~|~~294~~|~~0~~||**Y**|
|Totals|225|0|499|877|
|||||||
|Column Line|N|**Y**|**Y**|N|


Smallest uncovered number: 55

### Minimum Daily Profit

Start:

- Lines required: 4
- Total lines: 3/4

||Cafe|~~Dessert Shop~~|~~Restaurant~~|Snack Shop||Row Line|
|:-|:-:|:-:|:-:|:-:|:-:|-:|
|A|70|~~0~~|~~0~~|283||N|
|B|100|~~0~~|~~205~~|218||N|
|C|55|~~0~~|~~0~~|376||N|
|~~D~~|~~0~~|~~0~~|~~294~~|~~0~~||**Y**|
|Totals|225|0|499|877|
|||||||
|Column Line|N|**Y**|**Y**|N||$3/4$|

Smallest uncovered number: 55

#### Adding 55 to Each Covered Row and Column

||Cafe|Dessert Shop|Restaurant|Snack Shop||Row Line|
|:-|:-:|:-:|:-:|:-:|:-:|-:|
|A|70|55|55|283|||
|B|100|55|260|218|||
|C|55|55|55|376|||
|D|55|110|404|55|||
|Totals|225|0|499|877||
|||||||
|Column Line|||||

#### Removing 55 From Each Item

||Cafe|Dessert Shop|Restaurant|Snack Shop||Row Line|
|:-|:-:|:-:|:-:|:-:|:-:|-:|
|A|15|~~0~~|~~0~~|228||n|
|B|45|~~0~~|~~205~~|163||n|
|C|~~0~~|~~0~~|~~0~~|~~321~~||**Y**|
|D|~~0~~|~~0~~|~~349~~|~~0~~||**Y**|
|Totals|225|0|499|877|
|||||||
|Column Line|N|**Y**|**Y**|N||$4/4$|

End:

- Lines required: 4
- Total lines: 4/4

|-|Cafe|Dessert Shop|Restaurant|Snack Shop|-|-|Daily Min Profit|
|:-|:-:|:-:|:-:|:-:|:-:|:-:|-:|
|A|Y|n|n|Y|2|$15+228=$|$248$|
|B|Y|n|Y|Y|3|$45+205+163=$|$413$|
|C|n|n|n|Y|1|$321$|||
|D|n|Y|Y|n|2|$55+349=404$|||
|||||||||
|Totals|2|1|2|3|**8**||$1381$|