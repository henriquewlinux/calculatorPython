# CalculatorPy

It's a simple calculator created in python to pratice units tests.<br>
This calculator was created as a challenge requested by mentor [Nathan Araujo](https://github.com/araujosnathan).


## Installation Dependencies

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```python
pip install -r requirements.txt
```

## Usage

Run the code below to start.

```python
python main.py
```

you will see the available options.

```
Options:
Type '1' to add two numbers
Type '2' to subtract two numbers
Type '3' to multiply two numbers
Type '4' to divide two numbers
Type 'exit' to exit the progrm
```

Now just choose the option you want. If you choose exit, the calculator will close. If you choose the options 1 to 4 you'll be asked to enter the first number e after second number. After adding two numbers, the result will be shown.

```python
Type the first number: 
Type the second number: 
```
<br>

# Units Tests

The unit tests were done in pytest. The file is in the __test__/test_calculator.py .

## Run units tests

```python
pytest __test__/test_calculator.py
```


