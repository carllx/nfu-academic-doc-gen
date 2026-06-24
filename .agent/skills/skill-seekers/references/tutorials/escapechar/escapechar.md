# How To: Escapechar

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test escapechar

## Prerequisites

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas._libs.parsers`
- `pandas._libs.parsers`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.io.parsers`
- `pandas.io.parsers.c_parser_wrapper`


## Step-by-Step Guide

### Step 1: Assign data = '\\"hello world"\n\\"hello world"\n\\"hello world"'

```python
data = '\\"hello world"\n\\"hello world"\n\\"hello world"'
```

**Verification:**
```python
assert_array_dicts_equal(result, expected)
```

### Step 2: Assign reader = TextReader(...)

```python
reader = TextReader(StringIO(data), delimiter=',', header=None, escapechar='\\')
```

### Step 3: Assign result = reader.read(...)

```python
result = reader.read()
```

### Step 4: Assign expected = value

```python
expected = {0: np.array(['"hello world"'] * 3, dtype=object)}
```

### Step 5: Call assert_array_dicts_equal()

```python
assert_array_dicts_equal(result, expected)
```


## Complete Example

```python
# Workflow
data = '\\"hello world"\n\\"hello world"\n\\"hello world"'
reader = TextReader(StringIO(data), delimiter=',', header=None, escapechar='\\')
result = reader.read()
expected = {0: np.array(['"hello world"'] * 3, dtype=object)}
assert_array_dicts_equal(result, expected)
```

## Next Steps


---

*Source: test_textreader.py:171 | Complexity: Intermediate | Last updated: 2026-06-02*