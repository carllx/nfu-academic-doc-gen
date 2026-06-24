# How To: Rolling Max Min Periods

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rolling max min periods

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: step
```

## Step-by-Step Guide

### Step 1: Assign a = Series(...)

```python
a = Series([1, 2, 3, 4, 5], dtype=np.float64)
```

### Step 2: Assign result = a.rolling.max(...)

```python
result = a.rolling(window=100, min_periods=1, step=step).max()
```

### Step 3: Assign expected = value

```python
expected = a[::step]
```

### Step 4: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```

### Step 5: Assign msg = 'min_periods 5 must be <= window 3'

```python
msg = 'min_periods 5 must be <= window 3'
```

### Step 6: Call Series.rolling.max()

```python
Series([1, 2, 3]).rolling(window=3, min_periods=5, step=step).max()
```


## Complete Example

```python
# Setup
# Fixtures: step

# Workflow
a = Series([1, 2, 3, 4, 5], dtype=np.float64)
result = a.rolling(window=100, min_periods=1, step=step).max()
expected = a[::step]
tm.assert_almost_equal(result, expected)
msg = 'min_periods 5 must be <= window 3'
with pytest.raises(ValueError, match=msg):
    Series([1, 2, 3]).rolling(window=3, min_periods=5, step=step).max()
```

## Next Steps


---

*Source: test_api.py:391 | Complexity: Intermediate | Last updated: 2026-06-02*