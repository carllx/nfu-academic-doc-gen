# How To: Repr Should Return Str

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test repr should return str

## Prerequisites

**Required Modules:**
- `datetime`
- `io`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = [8, 5, 3, 5]
```

**Verification:**
```python
assert type(df.__repr__()) is str
```

### Step 2: Assign index1 = value

```python
index1 = ['σ', 'τ', 'υ', 'φ']
```

**Verification:**
```python
assert type(ser.__repr__()) is str
```

### Step 3: Assign cols = value

```python
cols = ['ψ']
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(data, columns=cols, index=index1)
```

**Verification:**
```python
assert type(df.__repr__()) is str
```

### Step 5: Assign ser = value

```python
ser = df[cols[0]]
```

**Verification:**
```python
assert type(ser.__repr__()) is str
```


## Complete Example

```python
# Workflow
data = [8, 5, 3, 5]
index1 = ['σ', 'τ', 'υ', 'φ']
cols = ['ψ']
df = DataFrame(data, columns=cols, index=index1)
assert type(df.__repr__()) is str
ser = df[cols[0]]
assert type(ser.__repr__()) is str
```

## Next Steps


---

*Source: test_repr.py:29 | Complexity: Intermediate | Last updated: 2026-06-02*