# How To: Comparison Object Array

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test comparison object array

## Prerequisites

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ts = Timestamp(...)

```python
ts = Timestamp('2011-01-03 00:00:00-0500', tz='US/Eastern')
```

**Verification:**
```python
assert (res == expected).all()
```

### Step 2: Assign other = Timestamp(...)

```python
other = Timestamp('2011-01-01 00:00:00-0500', tz='US/Eastern')
```

**Verification:**
```python
assert res.shape == expected.shape
```

### Step 3: Assign naive = Timestamp(...)

```python
naive = Timestamp('2011-01-01 00:00:00')
```

**Verification:**
```python
assert (res == expected).all()
```

### Step 4: Assign arr = np.array(...)

```python
arr = np.array([other, ts], dtype=object)
```

### Step 5: Assign res = value

```python
res = arr == ts
```

### Step 6: Assign expected = np.array(...)

```python
expected = np.array([False, True], dtype=bool)
```

**Verification:**
```python
assert (res == expected).all()
```

### Step 7: Assign arr = np.array(...)

```python
arr = np.array([[other, ts], [ts, other]], dtype=object)
```

### Step 8: Assign res = value

```python
res = arr != ts
```

### Step 9: Assign expected = np.array(...)

```python
expected = np.array([[True, False], [False, True]], dtype=bool)
```

**Verification:**
```python
assert res.shape == expected.shape
```

### Step 10: Assign arr = np.array(...)

```python
arr = np.array([naive], dtype=object)
```

### Step 11: Assign msg = 'Cannot compare tz-naive and tz-aware timestamps'

```python
msg = 'Cannot compare tz-naive and tz-aware timestamps'
```

### Step 12: arr < ts

```python
arr < ts
```


## Complete Example

```python
# Workflow
ts = Timestamp('2011-01-03 00:00:00-0500', tz='US/Eastern')
other = Timestamp('2011-01-01 00:00:00-0500', tz='US/Eastern')
naive = Timestamp('2011-01-01 00:00:00')
arr = np.array([other, ts], dtype=object)
res = arr == ts
expected = np.array([False, True], dtype=bool)
assert (res == expected).all()
arr = np.array([[other, ts], [ts, other]], dtype=object)
res = arr != ts
expected = np.array([[True, False], [False, True]], dtype=bool)
assert res.shape == expected.shape
assert (res == expected).all()
arr = np.array([naive], dtype=object)
msg = 'Cannot compare tz-naive and tz-aware timestamps'
with pytest.raises(TypeError, match=msg):
    arr < ts
```

## Next Steps


---

*Source: test_comparisons.py:80 | Complexity: Advanced | Last updated: 2026-06-02*