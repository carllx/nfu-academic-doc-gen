# How To: Treebank Span Tokenizer

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test TreebankWordTokenizer.span_tokenize function

## Prerequisites

**Required Modules:**
- `typing`
- `pytest`
- `nltk.tokenize`
- `nltk.tokenize.simple`
- `nltk.corpus`


## Step-by-Step Guide

### Step 1: '\n        Test TreebankWordTokenizer.span_tokenize function\n        '

```python
'\n        Test TreebankWordTokenizer.span_tokenize function\n        '
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign tokenizer = TreebankWordTokenizer(...)

```python
tokenizer = TreebankWordTokenizer()
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign test1 = 'Good muffins cost $3.88\nin New (York).  Please (buy) me\ntwo of them.\n(Thanks).'

```python
test1 = 'Good muffins cost $3.88\nin New (York).  Please (buy) me\ntwo of them.\n(Thanks).'
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign expected = value

```python
expected = [(0, 4), (5, 12), (13, 17), (18, 19), (19, 23), (24, 26), (27, 30), (31, 32), (32, 36), (36, 37), (37, 38), (40, 46), (47, 48), (48, 51), (51, 52), (53, 55), (56, 59), (60, 62), (63, 68), (69, 70), (70, 76), (76, 77), (77, 78)]
```

### Step 5: Assign result = list(...)

```python
result = list(tokenizer.span_tokenize(test1))
```

**Verification:**
```python
assert result == expected
```

### Step 6: Assign test2 = 'The DUP is similar to the "religious right" in the United States and takes a hardline stance on social issues'

```python
test2 = 'The DUP is similar to the "religious right" in the United States and takes a hardline stance on social issues'
```

### Step 7: Assign expected = value

```python
expected = [(0, 3), (4, 7), (8, 10), (11, 18), (19, 21), (22, 25), (26, 27), (27, 36), (37, 42), (42, 43), (44, 46), (47, 50), (51, 57), (58, 64), (65, 68), (69, 74), (75, 76), (77, 85), (86, 92), (93, 95), (96, 102), (103, 109)]
```

### Step 8: Assign result = list(...)

```python
result = list(tokenizer.span_tokenize(test2))
```

**Verification:**
```python
assert result == expected
```

### Step 9: Assign test3 = 'The DUP is similar to the "religious right" in the United States and takes a ``hardline\'\' stance on social issues'

```python
test3 = 'The DUP is similar to the "religious right" in the United States and takes a ``hardline\'\' stance on social issues'
```

### Step 10: Assign expected = value

```python
expected = [(0, 3), (4, 7), (8, 10), (11, 18), (19, 21), (22, 25), (26, 27), (27, 36), (37, 42), (42, 43), (44, 46), (47, 50), (51, 57), (58, 64), (65, 68), (69, 74), (75, 76), (77, 79), (79, 87), (87, 89), (90, 96), (97, 99), (100, 106), (107, 113)]
```

### Step 11: Assign result = list(...)

```python
result = list(tokenizer.span_tokenize(test3))
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
'\n        Test TreebankWordTokenizer.span_tokenize function\n        '
tokenizer = TreebankWordTokenizer()
test1 = 'Good muffins cost $3.88\nin New (York).  Please (buy) me\ntwo of them.\n(Thanks).'
expected = [(0, 4), (5, 12), (13, 17), (18, 19), (19, 23), (24, 26), (27, 30), (31, 32), (32, 36), (36, 37), (37, 38), (40, 46), (47, 48), (48, 51), (51, 52), (53, 55), (56, 59), (60, 62), (63, 68), (69, 70), (70, 76), (76, 77), (77, 78)]
result = list(tokenizer.span_tokenize(test1))
assert result == expected
test2 = 'The DUP is similar to the "religious right" in the United States and takes a hardline stance on social issues'
expected = [(0, 3), (4, 7), (8, 10), (11, 18), (19, 21), (22, 25), (26, 27), (27, 36), (37, 42), (42, 43), (44, 46), (47, 50), (51, 57), (58, 64), (65, 68), (69, 74), (75, 76), (77, 85), (86, 92), (93, 95), (96, 102), (103, 109)]
result = list(tokenizer.span_tokenize(test2))
assert result == expected
test3 = 'The DUP is similar to the "religious right" in the United States and takes a ``hardline\'\' stance on social issues'
expected = [(0, 3), (4, 7), (8, 10), (11, 18), (19, 21), (22, 25), (26, 27), (27, 36), (37, 42), (42, 43), (44, 46), (47, 50), (51, 57), (58, 64), (65, 68), (69, 74), (75, 76), (77, 79), (79, 87), (87, 89), (90, 96), (97, 99), (100, 106), (107, 113)]
result = list(tokenizer.span_tokenize(test3))
assert result == expected
```

## Next Steps


---

*Source: test_tokenize.py:621 | Complexity: Advanced | Last updated: 2026-06-02*