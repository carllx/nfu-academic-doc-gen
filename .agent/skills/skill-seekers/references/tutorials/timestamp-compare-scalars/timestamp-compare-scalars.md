# How To: Timestamp Compare Scalars

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test timestamp compare scalars

## Prerequisites

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign lhs = np.datetime64(...)

```python
lhs = np.datetime64(datetime(2013, 12, 6))
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign rhs = Timestamp(...)

```python
rhs = Timestamp('now')
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign nat = Timestamp(...)

```python
nat = Timestamp('nat')
```

### Step 4: Assign ops = value

```python
ops = {'gt': 'lt', 'lt': 'gt', 'ge': 'le', 'le': 'ge', 'eq': 'eq', 'ne': 'ne'}
```

### Step 5: Assign left_f = getattr(...)

```python
left_f = getattr(operator, left)
```

### Step 6: Assign right_f = getattr(...)

```python
right_f = getattr(operator, right)
```

### Step 7: Assign expected = left_f(...)

```python
expected = left_f(lhs, rhs)
```

### Step 8: Assign result = right_f(...)

```python
result = right_f(rhs, lhs)
```

**Verification:**
```python
assert result == expected
```

### Step 9: Assign expected = left_f(...)

```python
expected = left_f(rhs, nat)
```

### Step 10: Assign result = right_f(...)

```python
result = right_f(nat, rhs)
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
lhs = np.datetime64(datetime(2013, 12, 6))
rhs = Timestamp('now')
nat = Timestamp('nat')
ops = {'gt': 'lt', 'lt': 'gt', 'ge': 'le', 'le': 'ge', 'eq': 'eq', 'ne': 'ne'}
for left, right in ops.items():
    left_f = getattr(operator, left)
    right_f = getattr(operator, right)
    expected = left_f(lhs, rhs)
    result = right_f(rhs, lhs)
    assert result == expected
    expected = left_f(rhs, nat)
    result = right_f(nat, rhs)
    assert result == expected
```

## Next Steps


---

*Source: test_comparisons.py:206 | Complexity: Advanced | Last updated: 2026-06-02*