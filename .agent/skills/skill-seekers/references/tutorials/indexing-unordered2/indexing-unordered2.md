# How To: Indexing Unordered2

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test indexing unordered2

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range(datetime(2005, 1, 1), periods=20, freq='ME')
```

**Verification:**
```python
assert t.year == 2005
```

### Step 2: Assign ts = Series(...)

```python
ts = Series(np.arange(len(rng)), index=rng)
```

### Step 3: Assign ts = ts.take(...)

```python
ts = ts.take(np.random.default_rng(2).permutation(20))
```

### Step 4: Assign result = value

```python
result = ts['2005']
```

**Verification:**
```python
assert t.year == 2005
```


## Complete Example

```python
# Workflow
rng = date_range(datetime(2005, 1, 1), periods=20, freq='ME')
ts = Series(np.arange(len(rng)), index=rng)
ts = ts.take(np.random.default_rng(2).permutation(20))
result = ts['2005']
for t in result.index:
    assert t.year == 2005
```

## Next Steps


---

*Source: test_datetime.py:412 | Complexity: Intermediate | Last updated: 2026-06-02*