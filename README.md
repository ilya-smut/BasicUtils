# Helper Utils

Welcome to the Helper Utils repository! This repository is a collection of different utilities developed to automate and simplify routine processes in your everyday coding life.

## Getting Started

To get started, simply clone this repository and import the necessary functions from the modules. Functions are organized by their use-case, making it easy to find the utility you need.

## Utilities

Currently, the repository includes utilities for encoding and decoding text, converting strings to bits and vice versa, performing bitwise XOR operation, finding modular inverse, and sanitizing input. Here are some examples:

### Encoding and Decoding Utilities

The `encoder.py` module provides functions for base64 and URL encoding and decoding:

- `b64_e(text)`: This function takes a string as an argument and returns the base64 encoded version of the string.
- `b64_d(text)`: This function takes a base64 encoded string as an argument and returns the original string.
- `url_e(text)`: This function takes a string as an argument and returns the URL encoded version of the string.
- `url_d(text)`: This function takes a URL encoded string as an argument and returns the original string.

### Bitwise Operations and Conversion Utilities

The `bit_strings.py` and `bit_xor.py` modules provide functions for converting strings to bits and vice versa, and performing bitwise XOR operation:

- `string_to_bits(string)`: This function converts a string into a sequence of bits.
- `bits_to_string(bits)`: This function converts a sequence of bits into the corresponding string.
- `xor_bits(bits1, bits2)`: This function performs bitwise XOR operation on two bit strings of the same length.

### Extended Euclidean Algorithm Utility

The `extended_euclidean_find_inverse.py` module provides a function for finding modular inverse using Extended Euclidean Algorithm:

- `findModInverse(a, m)`: This function finds the modular inverse of a number 'a' mod 'm'.

### Input Sanitization Utility

The `input_sanitization.py` module provides a function for sanitizing input:

- `sanitize_input(input_string)`: This function removes everything from the input string but capital English letters, numbers, and some special characters(!,?,.).

## Future Improvements

While the repository currently contains utilities for encoding and decoding, bit operations, finding modular inverse, and input sanitization, we plan to add more utilities for different purposes soon.

Stay tuned for updates and feel free to contribute!