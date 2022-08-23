# Templated Cartesian Text Product

Create all message combinations from a text with embedded 


## Usage

### Example 1

```python
text = "The {quick|fast|slow} {brown|red} fox {jumps|leaps|stumbles} over the {lazy|sleepy} dog."
templated_cartesian_product(text)
```

```bash
$ python handler.py
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the sleepy dog.
The quick brown fox leaps over the lazy dog.
The quick brown fox leaps over the sleepy dog.
The quick brown fox stumbles over the lazy dog.
The quick brown fox stumbles over the sleepy dog.
The quick red fox jumps over the lazy dog.
The quick red fox jumps over the sleepy dog.
The quick red fox leaps over the lazy dog.
...
```

### Example 2

```python
text = "My name is {Huh?|What?|Chika-chika}"
templated_cartesian_product(text)
```

```bash
$ python text_template.py
My name is Huh?
My name is What?
My name is Chika-chika
```