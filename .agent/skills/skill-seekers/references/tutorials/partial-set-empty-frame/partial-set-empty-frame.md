# How To: Partial Set Empty Frame

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test partial set empty frame

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame()
```

### Step 2: Assign msg = 'cannot set a frame with no defined columns'

```python
msg = 'cannot set a frame with no defined columns'
```

### Step 3: Assign msg = 'cannot set a frame with no defined index and a scalar'

```python
msg = 'cannot set a frame with no defined index and a scalar'
```

### Step 4: Assign unknown = 1

```python
df.loc[1] = 1
```

### Step 5: Assign unknown = Series(...)

```python
df.loc[1] = Series([1], index=['foo'])
```

### Step 6: Assign unknown = 1

```python
df.loc[:, 1] = 1
```


## Complete Example

```python
# Workflow
df = DataFrame()
msg = 'cannot set a frame with no defined columns'
with pytest.raises(ValueError, match=msg):
    df.loc[1] = 1
with pytest.raises(ValueError, match=msg):
    df.loc[1] = Series([1], index=['foo'])
msg = 'cannot set a frame with no defined index and a scalar'
with pytest.raises(ValueError, match=msg):
    df.loc[:, 1] = 1
```

## Next Steps


---

*Source: test_partial.py:78 | Complexity: Intermediate | Last updated: 2026-06-02*