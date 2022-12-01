Advent of Code

## Philosophy

Advent of code, for me, is about learning clever techniques, data structures, algorithms, and how to simplify problems. To facilitate this better, I've turned this whole repo into a python module with it's own library of utilities which are used throughout the submodules.

## Running a day

From the root directory of this repo, all you need to do to run a given day is:
```
python3 -m YEAR.DAY.go
```

A more specific example:
```
python3 -m y2022.day1.go
```

## Running unit tests

From the root directory of this repo, all you need to do to run a year's tests is:
```
python3 -m unittest tests.YEAR
```

A more specific example:
```
python3 -m unittest tests.2022
```

To run *all* unit tests at once:
```
python3 -m unittest
```