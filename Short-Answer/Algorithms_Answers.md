#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This program runs as long as "a," which starts as zero, is less than our input "n" cubed. As long as "a" meets those conditions we do some addition/multiplication. So, if we increase "n" by an amount "f," we do (n + f)^3 more operations, or, written out more explicitly, `n^3 + 3*n^2*f + 3*n*f^2 + f^3` where as with an input of n, we had to do `n^3` number of inputs. So in the `(n+f)` case we are doing `3*n^2*f + 3*n*f^2 + f^3` more computations than before. So, as f approaches infinity, the largest term in their runtime differences is `f^3.` So, as we increase `f` we expect the run time to cube. This algorithm is `O(n^3)`


b) As we increase n we run this for a number times that increase in linear fashion. For the while loop, because we increase j by a factor of 2 each time, the while loop ends in a log(n) amount of time. As we do both together, I believe this function to be O(n * log(n))


c) If we run this recursion with an input of n, the recursion function is called n times (+ or - 1 depending on edge cases which we don't care about at the moment). If we increase our input by f, we run the recursion n+f many times. Thus, as we increase n, the runtime increases linearly, so code has time complexity O(n).

## Exercise II
I would start in the middle of the building, if it's odd just start at the lower of the two middles. In code this would be at location n // 2. I would then throw an egg off and see if it breaks. If it did, I know f is below me, so I would go to the halfway point of whatever amount of buidling is underneath me and throw another egg off. If the first egg I threw didn't break, I would know that f is above me, so I would go to the halfway point of whatever amount of building was above me and throw another egg of there. I repeat this process of going to the halfway point in the half of the building that contains f until I find it.

This algorithm halves the number of floors I need to check every step of the way. So, as n increases, it has to increase a lot before I need to check a ton more floors. Specifically, if x is the number of comparisons we need to do to find the answer, we do (2^x = n) and then solve for x. This gives x = log_2(n).

So, as we increase n by f, this gives that x = log_2(n + f). Thus, as f goes to infinity, we do about log_2(f) number of comparisions. So the time complexity of this algorithm is log(n).  
