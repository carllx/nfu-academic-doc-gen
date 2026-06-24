# How To: Timestamp Compare Oob Dt64

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test timestamp compare oob dt64

## Prerequisites

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign us = np.timedelta64(...)

```python
us = np.timedelta64(1, 'us')
```

**Verification:**
```python
assert Timestamp.min > other
```

### Step 2: Assign other = np.datetime64.astype(...)

```python
other = np.datetime64(Timestamp.min).astype('M8[us]')
```

**Verification:**
```python
assert Timestamp.max > other
```

### Step 3: Assign other = np.datetime64.astype(...)

```python
other = np.datetime64(Timestamp.max).astype('M8[us]')
```

**Verification:**
```python
assert other < Timestamp.max
```

### Step 4: Assign other = datetime(...)

```python
other = datetime(9999, 9, 9)
```

**Verification:**
```python
assert Timestamp.max < other + us
```

### Step 5: Assign other = datetime(...)

```python
other = datetime(1, 1, 1)
```

**Verification:**
```python
assert Timestamp.min < other
```


## Complete Example

```python
# Workflow
us = np.timedelta64(1, 'us')
other = np.datetime64(Timestamp.min).astype('M8[us]')
assert Timestamp.min > other
other = np.datetime64(Timestamp.max).astype('M8[us]')
assert Timestamp.max > other
assert other < Timestamp.max
assert Timestamp.max < other + us
other = datetime(9999, 9, 9)
assert Timestamp.min < other
assert other > Timestamp.min
assert Timestamp.max < other
assert other > Timestamp.max
other = datetime(1, 1, 1)
assert Timestamp.max > other
assert other < Timestamp.max
assert Timestamp.min > other
assert other < Timestamp.min
```

## Next Steps


---

*Source: test_comparisons.py:244 | Complexity: Intermediate | Last updated: 2026-06-02*