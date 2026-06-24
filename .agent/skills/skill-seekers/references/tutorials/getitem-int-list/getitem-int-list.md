# How To: Getitem Int List

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem int list

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.compat.numpy`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tseries.frequencies`


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range(start='1/1/2005', end='12/1/2005', freq='ME')
```

**Verification:**
```python
assert v1 == Timestamp('2/28/2005')
```

### Step 2: Assign dti2 = value

```python
dti2 = dti[[1, 3, 5]]
```

**Verification:**
```python
assert v2 == Timestamp('4/30/2005')
```

### Step 3: Assign v1 = value

```python
v1 = dti2[0]
```

**Verification:**
```python
assert v3 == Timestamp('6/30/2005')
```

### Step 4: Assign v2 = value

```python
v2 = dti2[1]
```

**Verification:**
```python
assert dti2.freq is None
```

### Step 5: Assign v3 = value

```python
v3 = dti2[2]
```

**Verification:**
```python
assert v1 == Timestamp('2/28/2005')
```


## Complete Example

```python
# Workflow
dti = date_range(start='1/1/2005', end='12/1/2005', freq='ME')
dti2 = dti[[1, 3, 5]]
v1 = dti2[0]
v2 = dti2[1]
v3 = dti2[2]
assert v1 == Timestamp('2/28/2005')
assert v2 == Timestamp('4/30/2005')
assert v3 == Timestamp('6/30/2005')
assert dti2.freq is None
```

## Next Steps


---

*Source: test_indexing.py:103 | Complexity: Intermediate | Last updated: 2026-06-02*