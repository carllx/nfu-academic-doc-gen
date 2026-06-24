# How To: At Iat Coercion

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test at iat coercion

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dates = date_range(...)

```python
dates = date_range('1/1/2000', periods=8)
```

**Verification:**
```python
assert result == xp
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((8, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
```

### Step 3: Assign s = value

```python
s = df['A']
```

### Step 4: Assign result = value

```python
result = s.at[dates[5]]
```

### Step 5: Assign xp = value

```python
xp = s.values[5]
```

**Verification:**
```python
assert result == xp
```


## Complete Example

```python
# Workflow
dates = date_range('1/1/2000', periods=8)
df = DataFrame(np.random.default_rng(2).standard_normal((8, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
s = df['A']
result = s.at[dates[5]]
xp = s.values[5]
assert result == xp
```

## Next Steps


---

*Source: test_scalar.py:75 | Complexity: Intermediate | Last updated: 2026-06-02*