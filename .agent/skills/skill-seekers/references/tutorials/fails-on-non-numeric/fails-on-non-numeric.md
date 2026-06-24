# How To: Fails On Non Numeric

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test fails on non numeric

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `re`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`

**Setup Required:**
```python
# Fixtures: kernel
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': object})
```

### Step 2: Assign args = value

```python
args = (df,) if kernel == 'corrwith' else ()
```

### Step 3: Assign msg = unknown.join(...)

```python
msg = '|'.join(['not allowed for this dtype', 'argument must be a string or a number', 'not supported between instances of', 'unsupported operand type', 'argument must be a string or a real number'])
```

### Step 4: Assign msg1 = "Cannot convert \\[\\[<class 'object'> <class 'object'> <class 'object'>\\]\\] to numeric"

```python
msg1 = "Cannot convert \\[\\[<class 'object'> <class 'object'> <class 'object'>\\]\\] to numeric"
```

### Step 5: Assign msg2 = "Cannot convert \\[<class 'object'> <class 'object'> <class 'object'>\\] to numeric"

```python
msg2 = "Cannot convert \\[<class 'object'> <class 'object'> <class 'object'>\\] to numeric"
```

### Step 6: Assign msg = unknown.join(...)

```python
msg = '|'.join([msg1, msg2])
```

### Step 7: Call getattr()

```python
getattr(df, kernel)(*args)
```


## Complete Example

```python
# Setup
# Fixtures: kernel

# Workflow
df = DataFrame({'a': [1, 2, 3], 'b': object})
args = (df,) if kernel == 'corrwith' else ()
msg = '|'.join(['not allowed for this dtype', 'argument must be a string or a number', 'not supported between instances of', 'unsupported operand type', 'argument must be a string or a real number'])
if kernel == 'median':
    msg1 = "Cannot convert \\[\\[<class 'object'> <class 'object'> <class 'object'>\\]\\] to numeric"
    msg2 = "Cannot convert \\[<class 'object'> <class 'object'> <class 'object'>\\] to numeric"
    msg = '|'.join([msg1, msg2])
with pytest.raises(TypeError, match=msg):
    getattr(df, kernel)(*args)
```

## Next Steps


---

*Source: test_reductions.py:2031 | Complexity: Intermediate | Last updated: 2026-06-02*