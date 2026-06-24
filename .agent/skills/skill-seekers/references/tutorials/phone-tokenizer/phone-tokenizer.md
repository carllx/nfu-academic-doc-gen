# How To: Phone Tokenizer

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test a string that resembles a phone number but contains a newline

## Prerequisites

**Required Modules:**
- `typing`
- `pytest`
- `nltk.tokenize`
- `nltk.tokenize.simple`
- `nltk.corpus`


## Step-by-Step Guide

### Step 1: '\n        Test a string that resembles a phone number but contains a newline\n        '

```python
'\n        Test a string that resembles a phone number but contains a newline\n        '
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign tokenizer = TweetTokenizer(...)

```python
tokenizer = TweetTokenizer()
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign test1 = '(393)  928 -3010'

```python
test1 = '(393)  928 -3010'
```

### Step 4: Assign expected = value

```python
expected = ['(393)  928 -3010']
```

### Step 5: Assign result = tokenizer.tokenize(...)

```python
result = tokenizer.tokenize(test1)
```

**Verification:**
```python
assert result == expected
```

### Step 6: Assign test2 = '(393)\n928 -3010'

```python
test2 = '(393)\n928 -3010'
```

### Step 7: Assign expected = value

```python
expected = ['(', '393', ')', '928 -3010']
```

### Step 8: Assign result = tokenizer.tokenize(...)

```python
result = tokenizer.tokenize(test2)
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
'\n        Test a string that resembles a phone number but contains a newline\n        '
tokenizer = TweetTokenizer()
test1 = '(393)  928 -3010'
expected = ['(393)  928 -3010']
result = tokenizer.tokenize(test1)
assert result == expected
test2 = '(393)\n928 -3010'
expected = ['(', '393', ')', '928 -3010']
result = tokenizer.tokenize(test2)
assert result == expected
```

## Next Steps


---

*Source: test_tokenize.py:337 | Complexity: Advanced | Last updated: 2026-06-02*