# How To: To String With Col Space

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to string with col space

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
df = DataFrame(np.random.default_rng(2).random(size=(1, 3)))
```

**Verification:**
```python
assert c10 < c20 < c30
```

### Step 2: Assign c10 = len(...)

```python
c10 = len(df.to_string(col_space=10).split('\n')[1])
```

**Verification:**
```python
assert len(with_header_row1) == len(no_header)
```

### Step 3: Assign c20 = len(...)

```python
c20 = len(df.to_string(col_space=20).split('\n')[1])
```

### Step 4: Assign c30 = len(...)

```python
c30 = len(df.to_string(col_space=30).split('\n')[1])
```

**Verification:**
```python
assert c10 < c20 < c30
```

### Step 5: Assign with_header = df.to_string(...)

```python
with_header = df.to_string(col_space=20)
```

### Step 6: Assign with_header_row1 = value

```python
with_header_row1 = with_header.splitlines()[1]
```

### Step 7: Assign no_header = df.to_string(...)

```python
no_header = df.to_string(col_space=20, header=False)
```

**Verification:**
```python
assert len(with_header_row1) == len(no_header)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).random(size=(1, 3)))
c10 = len(df.to_string(col_space=10).split('\n')[1])
c20 = len(df.to_string(col_space=20).split('\n')[1])
c30 = len(df.to_string(col_space=30).split('\n')[1])
assert c10 < c20 < c30
with_header = df.to_string(col_space=20)
with_header_row1 = with_header.splitlines()[1]
no_header = df.to_string(col_space=20, header=False)
assert len(with_header_row1) == len(no_header)
```

## Next Steps


---

*Source: test_to_string.py:184 | Complexity: Intermediate | Last updated: 2026-06-02*