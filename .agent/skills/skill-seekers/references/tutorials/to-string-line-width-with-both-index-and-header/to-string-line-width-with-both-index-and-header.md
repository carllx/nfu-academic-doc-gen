# How To: To String Line Width With Both Index And Header

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to string line width with both index and header

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
df_s = df.to_string(line_width=1)
```

**Verification:**
```python
assert df_s == expected
```

### Step 3: Assign expected = '   x  \\\n0  1   \n1  2   \n2  3   \n\n   y  \n0  4  \n1  5  \n2  6  '

```python
expected = '   x  \\\n0  1   \n1  2   \n2  3   \n\n   y  \n0  4  \n1  5  \n2  6  '
```

**Verification:**
```python
assert df_s == expected
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame({'x': [11, 22, 33], 'y': [4, 5, 6]})
```

### Step 5: Assign df_s = df.to_string(...)

```python
df_s = df.to_string(line_width=1)
```

### Step 6: Assign expected = '    x  \\\n0  11   \n1  22   \n2  33   \n\n   y  \n0  4  \n1  5  \n2  6  '

```python
expected = '    x  \\\n0  11   \n1  22   \n2  33   \n\n   y  \n0  4  \n1  5  \n2  6  '
```

**Verification:**
```python
assert df_s == expected
```

### Step 7: Assign df = DataFrame(...)

```python
df = DataFrame({'x': [11, 22, -33], 'y': [4, 5, -6]})
```

### Step 8: Assign df_s = df.to_string(...)

```python
df_s = df.to_string(line_width=1)
```

### Step 9: Assign expected = '    x  \\\n0  11   \n1  22   \n2 -33   \n\n   y  \n0  4  \n1  5  \n2 -6  '

```python
expected = '    x  \\\n0  11   \n1  22   \n2 -33   \n\n   y  \n0  4  \n1  5  \n2 -6  '
```

**Verification:**
```python
assert df_s == expected
```


## Complete Example

```python
# Workflow
df = DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
df_s = df.to_string(line_width=1)
expected = '   x  \\\n0  1   \n1  2   \n2  3   \n\n   y  \n0  4  \n1  5  \n2  6  '
assert df_s == expected
df = DataFrame({'x': [11, 22, 33], 'y': [4, 5, 6]})
df_s = df.to_string(line_width=1)
expected = '    x  \\\n0  11   \n1  22   \n2  33   \n\n   y  \n0  4  \n1  5  \n2  6  '
assert df_s == expected
df = DataFrame({'x': [11, 22, -33], 'y': [4, 5, -6]})
df_s = df.to_string(line_width=1)
expected = '    x  \\\n0  11   \n1  22   \n2 -33   \n\n   y  \n0  4  \n1  5  \n2 -6  '
assert df_s == expected
```

## Next Steps


---

*Source: test_to_string.py:301 | Complexity: Advanced | Last updated: 2026-06-02*