
**From now on, the function diagonal is done.**

**Ellyptium adds its first function: diagonal.**

This function allows you to return the diagonal trace from a N x N square. It also has some built-in formatted returns, as the addition of all, the subtraction of all and the product of all. You can also return it reversed.

The syntax is:
`diagonal(list, startSide, mode, reversed)`.

**PARAMETERS**

**list**

list must be an NxN list of lists, as can be:
`[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`.

**startSide**

startSide must be `'r'` or `'l'` depending if you want the trace from right to left or left to right, respectively.
By default, the value is `'l'`.

**mode**

There are 4 different modes:

- `'ret'`: Is the default mode. It returns a list with the diagonal trace. Using the list example variable, the return result is `[1, 5, 9]`.

- `'sum'`: This mode returns the sum of the values of the diagonal trace. Using the last example, return result is `15`.

- `'sub'`: This mode returns the substraction of the values of the diagonal trace. Using the last example, return result is `-13`.

- `'mult'`: This last mode returns the product of all values of the diagonal trace. Using the last example, return result is `45`.

**reversed**

This parameter allows you to do the trace from down to up instead of up to down.
If you want to do this, you must turn `True` the `reversed` value. It's `False` from default.
