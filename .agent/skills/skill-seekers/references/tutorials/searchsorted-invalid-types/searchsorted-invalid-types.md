# How To: Searchsorted Invalid Types

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test searchsorted invalid types

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: other, index
```

## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = np.arange(10, dtype='i8') * 24 * 3600 * 10 ** 9
```

### Step 2: Assign arr = value

```python
arr = pd.TimedeltaIndex(data, freq='D')._data
```

### Step 3: Assign msg = unknown.join(...)

```python
msg = '|'.join(['searchsorted requires compatible dtype or scalar', "value should be a 'Timedelta', 'NaT', or array of those. Got"])
```

### Step 4: Assign arr = pd.Index(...)

```python
arr = pd.Index(arr)
```

### Step 5: Call arr.searchsorted()

```python
arr.searchsorted(other)
```


## Complete Example

```python
# Setup
# Fixtures: other, index

# Workflow
data = np.arange(10, dtype='i8') * 24 * 3600 * 10 ** 9
arr = pd.TimedeltaIndex(data, freq='D')._data
if index:
    arr = pd.Index(arr)
msg = '|'.join(['searchsorted requires compatible dtype or scalar', "value should be a 'Timedelta', 'NaT', or array of those. Got"])
with pytest.raises(TypeError, match=msg):
    arr.searchsorted(other)
```

## Next Steps


---

*Source: test_timedeltas.py:248 | Complexity: Intermediate | Last updated: 2026-06-02*