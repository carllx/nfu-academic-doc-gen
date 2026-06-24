# How To: At With Duplicate Axes Requires Scalar Lookup

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test at with duplicate axes requires scalar lookup

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arr = np.random.default_rng.standard_normal.reshape(...)

```python
arr = np.random.default_rng(2).standard_normal(6).reshape(3, 2)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(arr, columns=['A', 'A'])
```

### Step 3: Assign msg = 'Invalid call for scalar access'

```python
msg = 'Invalid call for scalar access'
```

### Step 4: df.at[[1, 2]]

```python
df.at[[1, 2]]
```

### Step 5: df.at[1, ['A']]

```python
df.at[1, ['A']]
```

### Step 6: df.at[:, 'A']

```python
df.at[:, 'A']
```

### Step 7: Assign unknown = 1

```python
df.at[[1, 2]] = 1
```

### Step 8: Assign unknown = 1

```python
df.at[1, ['A']] = 1
```

### Step 9: Assign unknown = 1

```python
df.at[:, 'A'] = 1
```


## Complete Example

```python
# Workflow
arr = np.random.default_rng(2).standard_normal(6).reshape(3, 2)
df = DataFrame(arr, columns=['A', 'A'])
msg = 'Invalid call for scalar access'
with pytest.raises(ValueError, match=msg):
    df.at[[1, 2]]
with pytest.raises(ValueError, match=msg):
    df.at[1, ['A']]
with pytest.raises(ValueError, match=msg):
    df.at[:, 'A']
with pytest.raises(ValueError, match=msg):
    df.at[[1, 2]] = 1
with pytest.raises(ValueError, match=msg):
    df.at[1, ['A']] = 1
with pytest.raises(ValueError, match=msg):
    df.at[:, 'A'] = 1
```

## Next Steps


---

*Source: test_at.py:142 | Complexity: Advanced | Last updated: 2026-06-02*