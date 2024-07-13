# Dynamic String Implementation Using Linked List in Python

This project demonstrates the implementation of a dynamic string using a linked list in Python. The string is stored in fixed-size blocks, and each block can hold up to 4 characters. New blocks are dynamically allocated as needed when the string grows.

## Classes and Methods

### Node Class
The `Node` class represents a block in the linked list.

- `__init__(self)`: Initializes a block with an array of 4 null characters and sets the next pointer to `None`.

### DynamicString Class
The `DynamicString` class manages the dynamic string using a linked list of `Node` blocks.

- `__init__(self, initial_str="")`: Initializes the dynamic string. If an initial string is provided, it is appended to the dynamic string.
- `append(self, string)`: Appends a string to the end of the dynamic string. Allocates new blocks if needed.
- `print_string(self)`: Prints the complete dynamic string.
- `clear(self)`: Clears the dynamic string and resets its length.
- `get_length(self)`: Returns the total length of the dynamic string.
