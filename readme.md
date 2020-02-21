# Google Hash Code


## Problem

We've got librays contianing books, 
1. Sign up a library, 1 at a time
2. Once a library is signed up, send books to be scanned, unlimited books can be scanned at the facility at a time
    But each library can only send n books a day


**Scheduling Problem**

## Goal
Work out best order of libraries to maximise score

## Approach
Import file and convert data

Order books into order of score
Libraries need a score function that takes in parameter time
Work out best order of libraries to maximise score

Output into scoring format

## Data format 
6 2 7 // 6 books, 2 libraries, 7 days
1 2 3 6 5 4 // book scores

5 2 2 // library 0, 5 books, 2 days signup, ship 2 a day
0 1 2 3 4 // book scores

4 3 1// library 1, 4 books, 3 days sign up, 1 book per day
0 2 3 5 // the books and scores

## Threading
Each library is running independently, therefore each can be run on a unique thread in parralel

## Issues
Issue, might have multiple books repeat scanned
To solve we need to know all books in all libraries with reference to which libraries can scan which books