---
layout: lesson
---

The best way to learn how to program is to do something useful,
so this introduction to Python is built around a common scientific task:
data analysis.

Our real goal isn't to teach you Python,
but to teach you the basic concepts that all programming depends on.
We use Python in our lessons because:

1.  we have to use *something* for examples;
2.  it's free, well-documented, and runs almost everywhere;
3.  it has a large (and growing) user base among scientists; and
4.  experience shows that it's easier for novices to pick up than most other languages.

But the two most important things are
to use whatever language your colleagues are using,
so that you can share your work with them easily,
and to use that language *well*.

We are studying historical climate data for some countries in North America.
The data sets are stored in [comma-separated values]({{ site.github.url }}/reference/#comma-separated-values) (CSV) format:
each row holds information for a single year,
and the columns represent the year, the average
temperature (in Celsius), and average precipitation (in millimetres).
The first few rows of our first file look like this:

~~~
1901,-7.672419071,37.44835281
1902,-7.86271143,38.25142288
1903,-7.910782814,37.5530014
1904,-8.155729294,37.35193253
1905,-7.547311306,37.51586914
1906,-7.684103489,37.51700592
~~~
{: .source}

We want to:

*   load that data into memory,
*   do some basic analysis and calculations, and
*   plot the result.

To do all that, we'll have to learn a little bit about programming.

> ## Prerequisites
>
> Learners need to understand the concepts of files and directories
> (including the working directory) and how to start a Python
> interpreter before tackling this lesson. This lesson references the Jupyter (IPython)
> Notebook although it can be taught through any Python interpreter.
> The commands in this lesson pertain to **Python 3**.
{: .prereq}

### Getting Started
To get started, follow the directions in the "[Setup](setup/)" tab to download data to your computer and follow any installation instructions. 
