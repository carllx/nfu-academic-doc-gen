# How To: Header Not Enough Lines

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test header not enough lines

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

### Step 1: Assign data = 'skip this\nskip this\na,b,c\n1,2,3\n4,5,6'

```python
data = 'skip this\nskip this\na,b,c\n1,2,3\n4,5,6'
```

**Verification:**
```python
assert header == expected
```

### Step 2: Assign reader = TextReader(...)

```python
reader = TextReader(StringIO(data), delimiter=',', header=2)
```

**Verification:**
```python
assert_array_dicts_equal(recs, expected)
```

### Step 3: Assign header = value

```python
header = reader.header
```

### Step 4: Assign expected = value

```python
expected = [['a', 'b', 'c']]
```

**Verification:**
```python
assert header == expected
```

### Step 5: Assign recs = reader.read(...)

```python
recs = reader.read()
```

### Step 6: Assign expected = value

```python
expected = {0: np.array([1, 4], dtype=np.int64), 1: np.array([2, 5], dtype=np.int64), 2: np.array([3, 6], dtype=np.int64)}
```

### Step 7: Call assert_array_dicts_equal()

```python
assert_array_dicts_equal(recs, expected)
```


## Complete Example

```python
# Workflow
data = 'skip this\nskip this\na,b,c\n1,2,3\n4,5,6'
reader = TextReader(StringIO(data), delimiter=',', header=2)
header = reader.header
expected = [['a', 'b', 'c']]
assert header == expected
recs = reader.read()
expected = {0: np.array([1, 4], dtype=np.int64), 1: np.array([2, 5], dtype=np.int64), 2: np.array([3, 6], dtype=np.int64)}
assert_array_dicts_equal(recs, expected)
```

## Next Steps


---

*Source: test_textreader.py:155 | Complexity: Intermediate | Last updated: 2026-06-02*