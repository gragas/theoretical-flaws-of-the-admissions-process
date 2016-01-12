# Theoretical Flaws of the Admissions Process
This is the code I used to investigate the theoretical flaws of the admissions process. You can read my writeup [here](https://medium.com/@gragas/theoretical-flaws-of-the-admissions-process-e9c20519cd0b).

## How to run my code
All of my code is contained in one file, `machines.py`. It is Python 3 code. It requires these packages:

   * [NumPy](http://www.numpy.org/)
   * [matplotlib](http://matplotlib.org/)

Once you have Python 3 and those packages, you can run my code with `python3 machines.py`.

## How to change the variables in my code
There are three key variables in my code that are meant to be modified:

   1. The acceptance rate
   2. The population size
   3. The number of trials per {number of machines}

Luckily, all three variables are right at the top of `machines.py`. The acceptance rate should be a real number between zero and one. The population size should be a positive integer. The number of trials per {number of machines} should be a positive integer (the higher, the better).
