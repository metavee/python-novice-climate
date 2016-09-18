---
title: Making Choices
teaching: 30
exercises: 0
questions:
- "How can my programs do different things based on data values?"
objectives:
- "Write conditional statements including `if`, `elif`, and `else` branches."
- "Correctly evaluate expressions containing `and` and `or`."
keypoints:
- "Use `if condition` to start a conditional statement, `elif condition` to provide additional tests, and `else` to provide a default."
- "The bodies of the branches of conditional statements must be indented."
- "Use `==` to test for equality."
- "`X and Y` is only true if both X and Y are true."
- "`X or Y` is true if either X or Y, or both, are true."
- "Zero, the empty string, and the empty list are considered false; all other numbers, strings, and lists are considered true."
- "Nest loops to operate on multi-dimensional data."
- "Put code whose parameters change frequently in a function, then call it with different parameter values to customize its behavior."
---

For more complicated programs, it would be nice to have a mechanism for code to
act differently in response to some condition.

## Conditionals

We can ask Python to take different actions, depending on a condition, with an `if` statement:

~~~
num = 37
if num > 100:
    print('greater')
else:
    print('not greater')
print('done')
~~~
{: .python}

~~~
not greater
done
~~~
{: .output}

The second line of this code uses the keyword `if` to tell Python that we want to make a choice.
If the test that follows the `if` statement is true,
the body of the `if`
(i.e., the lines indented underneath it) are executed.
If the test is false,
the body of the `else` is executed instead.
Only one or the other is ever executed:

![Executing a Conditional](../fig/python-flowchart-conditional.png)

Conditional statements don't have to include an `else`.
If there isn't one,
Python simply does nothing if the test is false:

~~~
num = 53
print('before conditional...')
if num > 100:
    print('53 is greater than 100')
print('...after conditional')
~~~
{: .python}

~~~
before conditional...
...after conditional
~~~
{: .output}

We can also chain several tests together using `elif`,
which is short for "else if".
The following Python code uses `elif` to print the sign of a number.

~~~
num = -3

if num > 0:
    print(num, "is positive")
elif num == 0:
    print(num, "is zero")
else:
    print(num, "is negative")
~~~
{: .python}

~~~
"-3 is negative"
~~~
{: .output}

One important thing to notice in the code above is that we use a double equals sign `==` to test for equality
rather than a single equals sign
because the latter is used to mean assignment.

We can also combine tests using `and` and `or`.
`and` is only true if both parts are true:

~~~
if (1 > 0) and (-1 > 0):
    print('both parts are true')
else:
    print('at least one part is false')
~~~
{: .python}

~~~
at least one part is false
~~~
{: .output}

while `or` is true if at least one part is true:

~~~
if (1 < 0) or (-1 < 0):
    print('at least one test is true')
~~~
{: .python}

~~~
at least one test is true
~~~
{: .output}

## Checking our Data

Now that we've seen how conditionals work,
we can use them to analyze our data.

Let's say we wanted to compare two countries and find out which one is warmer.
We could use the average temperature across all years, but this might be easily
skewed if there a few outliers. Instead, let's tally up the number of years where
one country is warmer than the other.

~~~
temp_CAN = numpy.loadtxt('CAN.csv', delimiter=',', skiprows=1)[:,1]
temp_USA = numpy.loadtxt('USA.csv', delimiter=',', skiprows=1)[:,1]
    
# tally of which country is warmer on a given year
count1 = 0
count2 = 0

for t1, t2 in zip(temp_CAN, temp_USA):
    if t1 > t2:
        count1 = count1 + 1
    elif t2 > t1:
        count2 = count2 + 1

print(count1)
print(count2)

if count1 > count2:
    print('CAN is typically warmer than USA.')
elif count2 > count1:
    print('USA is typically warmer than CAN.')
else:
    print('Neither USA nor CAN are clearly warmer than the other.')

~~~
{: .python}

In this way,
we have asked Python to do something different depending on the condition of our data.

> ## How Many Paths?
>
> Which of the following would be printed if you were to run this code?
> Why did you pick this answer?
>
> 1.  A
> 2.  B
> 3.  C
> 4.  B and C
>
> ~~~
> if 4 > 5:
>     print('A')
> elif 4 == 5:
>     print('B')
> elif 4 < 5:
>     print('C')
> ~~~
> {: .python}
>
> > ## Solution
> > C gets printed because the first two conditions, `4 > 5` and `4 == 5`, are not true,
> > but `4 < 5` is true.
> {: .solution}
{: .challenge}

> ## What Is Truth?
>
> `True` and `False` are special words in Python called `booleans`
> which represent true and false statements.
> However, they aren't the only values in Python that are true and false.
> In fact, *any* value can be used in an `if` or `elif`.
> After reading and running the code below,
> explain what the rule is for which values are considered true and which are considered false.
>
> ~~~
> if '':
>     print('empty string is true')
> if 'word':
>     print('word is true')
> if []:
>     print('empty list is true')
> if [1, 2, 3]:
>     print('non-empty list is true')
> if 0:
>     print('zero is true')
> if 1:
>     print('one is true')
> ~~~
> {: .python}
{: .challenge}

> ## That's Not Not What I Meant
>
> Sometimes it is useful to check whether some condition is not true.
> The Boolean operator `not` can do this explicitly.
> After reading and running the code below,
> write some `if` statements that use `not` to test the rule
> that you formulated in the previous challenge.
>
> ~~~
> if not '':
>     print('empty string is not true')
> if not 'word':
>     print('word is not true')
> if not not True:
>     print('not not True is true')
> ~~~
> {: .python}
{: .challenge}

> ## Close Enough
>
> Write some conditions that print `True` if the variable `a` is within 10% of the variable `b`
> and `False` otherwise.
> Compare your implementation with your partner's:
> do you get the same answer for all possible pairs of numbers?
>
> > ## Solution 1
> > ~~~
> > a = 5
> > b = 5.1
> >
> > if abs(a - b) < 0.1 * abs(b):
> >     print('True')
> > else:
> >     print('False')
> > ~~~
> > {: .python}
> {: .solution}
>
> > ## Solution 2
> > ~~~
> > print(abs(a - b) < 0.1 * abs(b))
> > ~~~
> > {: .python}
> >
> > This works because the Booleans `True` and `False`
> > have string representations which can be printed.
> {: .solution}
{: .challenge}

> ## In-Place Operators
>
> Python (and most other languages in the C family) provides [in-place operators]({{ site.github.url }}/reference/#in-place-operators)
> that work like this:
>
> ~~~
> x = 1  # original value
> x += 1 # add one to x, assigning result back to x
> x *= 3 # multiply x by 3
> print(x)
> ~~~
> {: .python}
>
> ~~~
> 6
> ~~~
> {: .output}
>
> Write some code that sums the positive and negative numbers in a list separately,
> using in-place operators.
> Do you think the result is more or less readable than writing the same without in-place operators?
>
> > ## Solution
> > ~~~
> > positive_sum = 0
> > negative_sum = 0
> > test_list = [3, 4, 6, 1, -1, -5, 0, 7, -8]
> > for num in test_list:
> >     if num > 0:
> >         positive_sum += num
> >     elif num == 0:
> >         pass
> >     else:
> >         negative_sum += num
> > print(positive_sum, negative_sum)
> > ~~~
> > {: .python}
> >
> > Here `pass` means "don't do anything".
> In this particular case, it's not actually needed, since if `num == 0` neither
> > sum needs to change, but it illustrates the use of `elif`.
> {: .solution}
{: .challenge}

> ## Tuples and Exchanges
>
> Explain what the overall effect of this code is:
>
> ~~~
> left = 'L'
> right = 'R'
>
> temp = left
> left = right
> right = temp
> ~~~
> {: .python}
>
> > ## Solution
> > The code swaps the contents of the variables right and left.
> {: .solution}
>
> Compare it to:
>
> ~~~
> left, right = right, left
> ~~~
> {: .python}
>
> Do they always do the same thing?
> Which do you find easier to read?
>
> > ## Solution
> > Yes, although it's possible the internal implementation is different.
> {: .solution}
{: .challenge}

> ## Counting Vowels
>
> 1.  Write a loop that counts the number of vowels in a character string.
>
> 2. Test it on a few individual words and full sentences.
>
> 3. Once you are done, compare your solution to your neighbor's.
>    Did you make the same decisions about how to handle the letter 'y'
>    (which some people think is a vowel, and some do not)?
> > ## Solution
> > ~~~
> > vowels = 'aeiouAEIOU'
> > sentence = 'Mary had a little lamb."
> > count = 0
> > for char in sentence:
> >     if char in vowels:
> >         count += 1
> >         
> > print("The number of vowels in this string is " + str(count))
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}
