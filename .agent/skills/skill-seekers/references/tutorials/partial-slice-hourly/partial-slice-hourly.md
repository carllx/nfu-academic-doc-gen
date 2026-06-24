# How To: Partial Slice Hourly

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test partial slice hourly

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range(freq='min', start=datetime(2005, 1, 1, 20, 0, 0), periods=500)
```

**Verification:**
```python
assert s['2005-1-1 20:00'] == s.iloc[0]
```

### Step 2: Assign s = Series(...)

```python
s = Series(np.arange(len(rng)), index=rng)
```

### Step 3: Assign result = value

```python
result = s['2005-1-1']
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, s.iloc[:60 * 4])
```

### Step 5: Assign result = value

```python
result = s['2005-1-1 20']
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, s.iloc[:60])
```

**Verification:**
```python
assert s['2005-1-1 20:00'] == s.iloc[0]
```

### Step 7: s['2004-12-31 00:15']

```python
s['2004-12-31 00:15']
```


## Complete Example

```python
# Workflow
rng = date_range(freq='min', start=datetime(2005, 1, 1, 20, 0, 0), periods=500)
s = Series(np.arange(len(rng)), index=rng)
result = s['2005-1-1']
tm.assert_series_equal(result, s.iloc[:60 * 4])
result = s['2005-1-1 20']
tm.assert_series_equal(result, s.iloc[:60])
assert s['2005-1-1 20:00'] == s.iloc[0]
with pytest.raises(KeyError, match="^'2004-12-31 00:15'$"):
    s['2004-12-31 00:15']
```

## Next Steps


---

*Source: test_partial_slicing.py:207 | Complexity: Intermediate | Last updated: 2026-06-02*