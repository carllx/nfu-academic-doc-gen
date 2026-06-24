# How To: To String Line Width No Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to string line width no index

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
df_s = df.to_string(line_width=1, index=False)
```

**Verification:**
```python
assert df_s == expected
```

### Step 3: Assign expected = ' x  \\\n 1   \n 2   \n 3   \n\n y  \n 4  \n 5  \n 6  '

```python
expected = ' x  \\\n 1   \n 2   \n 3   \n\n y  \n 4  \n 5  \n 6  '
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
df_s = df.to_string(line_width=1, index=False)
```

### Step 6: Assign expected = ' x  \\\n11   \n22   \n33   \n\n y  \n 4  \n 5  \n 6  '

```python
expected = ' x  \\\n11   \n22   \n33   \n\n y  \n 4  \n 5  \n 6  '
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
df_s = df.to_string(line_width=1, index=False)
```

### Step 9: Assign expected = '  x  \\\n 11   \n 22   \n-33   \n\n y  \n 4  \n 5  \n-6  '

```python
expected = '  x  \\\n 11   \n 22   \n-33   \n\n y  \n 4  \n 5  \n-6  '
```

**Verification:**
```python
assert df_s == expected
```


## Complete Example

```python
# Workflow
df = DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
df_s = df.to_string(line_width=1, index=False)
expected = ' x  \\\n 1   \n 2   \n 3   \n\n y  \n 4  \n 5  \n 6  '
assert df_s == expected
df = DataFrame({'x': [11, 22, 33], 'y': [4, 5, 6]})
df_s = df.to_string(line_width=1, index=False)
expected = ' x  \\\n11   \n22   \n33   \n\n y  \n 4  \n 5  \n 6  '
assert df_s == expected
df = DataFrame({'x': [11, 22, -33], 'y': [4, 5, -6]})
df_s = df.to_string(line_width=1, index=False)
expected = '  x  \\\n 11   \n 22   \n-33   \n\n y  \n 4  \n 5  \n-6  '
assert df_s == expected
```

## Next Steps


---

*Source: test_to_string.py:255 | Complexity: Advanced | Last updated: 2026-06-02*