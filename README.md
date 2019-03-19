# mypackage

Mypackage is a Python library to demonstrate a basic understanding of recursive funtions as well as
three different sorting algorithms. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install mypackage.

```bash
pip install git+https://github.com/faulty-it/mypackage.git
```

## Usage

```python
from mypackage import recursion
from mypackage import sorting

mypackage.recursion.sum_array([1,2,3,4,5]) # returns sum of all elements = 15
mypackage.recursion.fibonacci(3) # returns the third number in the fibonacci sequance.
mypackage.recursion.factorial(3) # returns the factorial of the user's input = 6
mypackage.recursion.reverse("Apple") # returns string in reverse order = "elppA"

mypackage.sorting.bubble_sort([5,4,3,2,1]) #returns array sorted [1,2,3,4,5]
mypackage.sorting.merge_sort([5,4,3,2,1]) #returns array sorted [1,2,3,4,5]
mypackage.sorting.quick_sort([5,4,3,2,1]) #returns array sorted [1,2,3,4,5]

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
