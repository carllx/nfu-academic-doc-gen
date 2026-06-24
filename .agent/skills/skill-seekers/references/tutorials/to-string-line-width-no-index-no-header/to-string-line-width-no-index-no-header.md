# How To: To String Line Width No Index No Header

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to string line width no index no header

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
df_s = df.to_string(line_width=1, index=False, header=False)
```

**Verification:**
```python
assert df_s == expected
```

### Step 3: Assign expected = '1  \\\n2   \n3   \n\n4  \n5  \n6  '

```python
expected = '1  \\\n2   \n3   \n\n4  \n5  \n6  '
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
df_s = df.to_string(line_width=1, index=False, header=False)
```

### Step 6: Assign expected = '11  \\\n22   \n33   \n\n4  \n5  \n6  '

```python
expected = '11  \\\n22   \n33   \n\n4  \n5  \n6  '
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
df_s = df.to_string(line_width=1, index=False, header=False)
```

### Step 9: Assign expected = ' 11  \\\n 22   \n-33   \n\n 4  \n 5  \n-6  '

```python
expected = ' 11  \\\n 22   \n-33   \n\n 4  \n 5  \n-6  '
```

**Verification:**
```python
assert df_s == expected
```


## Complete Example

```python
# Workflow
df = DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
df_s = df.to_string(line_width=1, index=False, header=False)
expected = '1  \\\n2   \n3   \n\n4  \n5  \n6  '
assert df_s == expected
df = DataFrame({'x': [11, 22, 33], 'y': [4, 5, 6]})
df_s = df.to_string(line_width=1, index=False, header=False)
expected = '11  \\\n22   \n33   \n\n4  \n5  \n6  '
assert df_s == expected
df = DataFrame({'x': [11, 22, -33], 'y': [4, 5, -6]})
df_s = df.to_string(line_width=1, index=False, header=False)
expected = ' 11  \\\n 22   \n-33   \n\n 4  \n 5  \n-6  '
assert df_s == expected
```

## Next Steps


---

*Source: test_to_string.py:330 | Complexity: Advanced | Last updated: 2026-06-02*