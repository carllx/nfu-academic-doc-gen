# How To: To String Header False

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to string header false

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
df = DataFrame([1, 2])
```

**Verification:**
```python
assert s == expected
```

### Step 2: Assign df.index.name = 'a'

```python
df.index.name = 'a'
```

**Verification:**
```python
assert s == expected
```

### Step 3: Assign s = df.to_string(...)

```python
s = df.to_string(header=False)
```

### Step 4: Assign expected = 'a   \n0  1\n1  2'

```python
expected = 'a   \n0  1\n1  2'
```

**Verification:**
```python
assert s == expected
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 2], [3, 4]])
```

### Step 6: Assign df.index.name = 'a'

```python
df.index.name = 'a'
```

### Step 7: Assign s = df.to_string(...)

```python
s = df.to_string(header=False)
```

### Step 8: Assign expected = 'a      \n0  1  2\n1  3  4'

```python
expected = 'a      \n0  1  2\n1  3  4'
```

**Verification:**
```python
assert s == expected
```


## Complete Example

```python
# Workflow
df = DataFrame([1, 2])
df.index.name = 'a'
s = df.to_string(header=False)
expected = 'a   \n0  1\n1  2'
assert s == expected
df = DataFrame([[1, 2], [3, 4]])
df.index.name = 'a'
s = df.to_string(header=False)
expected = 'a      \n0  1  2\n1  3  4'
assert s == expected
```

## Next Steps


---

*Source: test_to_string.py:207 | Complexity: Advanced | Last updated: 2026-06-02*