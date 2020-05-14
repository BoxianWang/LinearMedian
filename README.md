# Linear Time Selecting algorithm

### Written by Boxian Wang, May 6, 2020

## Introduction

This is a python implementation of an amazing algrithm that finds the k-th greatest number in 
an unordered list

## Algorithm

For reference, see CLRS p. 220.

For a basic idea, the algorithm divides the input into groups of five and find their medians.

Then, it finds the median of these medians via recursion.

Finally, it partitions the input according to the median of medians found, computing its rank *n*.
Then it recursively searches the k-th or *k-n*th greatest in the lesser or greater half of the partition.

*Note that this implementation is only for demostrating this elegant algorithm; it has not been optimized 
for constant hence may not be the most efficient in real life*