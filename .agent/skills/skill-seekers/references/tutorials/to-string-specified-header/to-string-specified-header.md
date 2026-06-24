# How To: To String Specified Header

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to string specified header

## Prerequisites

**Required Modules:**
- `datetime`
- `io`
- `re`
- `sys`
- `textwrap`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
```

**Verification:**
```python
assert df_s == expected
```

### Step 2: Assign df_s = df.to_string(...)

```python
df_s = df.to_string(header=['X', 'Y'])
```

### Step 3: Assign expected = '   X  Y\n0  1  4\n1  2  5\n2  3  6'

```python
expected = '   X  Y\n0  1  4\n1  2  5\n2  3  6'
```

**Verification:**
```python
assert df_s == expected
```

### Step 4: Assign msg = 'Writing 2 cols but got 1 aliases'

```python
msg = 'Writing 2 cols but got 1 aliases'
```

### Step 5: Call df.to_string()

```python
df.to_string(header=['X'])
```


## Complete Example

```python
# Workflow
df = DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
df_s = df.to_string(header=['X', 'Y'])
expected = '   X  Y\n0  1  4\n1  2  5\n2  3  6'
assert df_s == expected
msg = 'Writing 2 cols but got 1 aliases'
with pytest.raises(ValueError, match=msg):
    df.to_string(header=['X'])
```

## Next Steps


---

*Source: test_to_string.py:236 | Complexity: Intermediate | Last updated: 2026-06-02*