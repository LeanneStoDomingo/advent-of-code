# Advent of Code

[https://adventofcode.com/](https://adventofcode.com/)

## Setup

1. ```bash
   python3 -m venv .venv
   ```

2. ```bash
   source .venv/bin/activate
   ```

3. ```bash
   pip install --upgrade pip
   ```

4. ```bash
   pip install -r requirements.txt
   ```

5. ```bash
   pip install -e ./utils
   ```

## Future Plans

- [ ] cache input
  - check if file exists
  - if it does, read from file
  - if it doesn't, get input and write to file
- [ ] add test data flag
  - check if test file exists
  - if it does and flag is True, read from file
  - if it doesn't and flag is True, print that test file wasn't found and use real data instead
- [ ] add test answer argument(s):
  - ways to do it
    - dict with keys 'a'/'part_one' and 'b'/'part_two'
    - list with two elements
    - two arguments
  - have function ouput be tuple with puzzle_input and test data answers
- [ ] maybe make utils in a class
  - arguments
    - year
    - day
    - test data answers
  - functions
    - [ ] get_input
    - [ ] get_test_input
    - [ ] test_a/test_part_one
    - [ ] test_b/test_part_two
