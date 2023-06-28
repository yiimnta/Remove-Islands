# Remove-Islands
Medium Google Coding - Remove Islands

# Description

Given a matrix n*n:

1 -> black color

0 -> white color

Removing all black pixels that are not connected with the black-pixel in the border

# Input
Input is a 

E.g.
```
  matrix = [
     [1, 0, 0, 0, 0, 0],
     [0, 1, 0, 1, 1, 1],
     [0, 0, 1, 0, 1, 0],
     [1, 1, 0, 0, 1, 0],
     [1, 0, 1, 1, 0, 0],
     [1, 0, 0, 0, 0, 1],
 ]
```

# Output

```
  matrix = [
     [1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 1, 1],
     [0, 0, 0, 0, 1, 0],
     [1, 1, 0, 0, 1, 0],
     [1, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 1],
 ]
```
