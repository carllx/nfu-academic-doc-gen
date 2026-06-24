# How To: Rolling Min Min Periods

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rolling min min periods

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
a = Series([1, 2, 3, 4, 5])
```

### Step 2: Assign result = a.rolling.min(...)

```python
result = a.rolling(window=100, min_periods=1, step=step).min()
```

### Step 3: Assign expected = value

```python
expected = Series(np.ones(len(a)))[::step]
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign msg = 'min_periods 5 must be <= window 3'

```python
msg = 'min_periods 5 must be <= window 3'
```

### Step 6: Call Series.rolling.min()

```python
Series([1, 2, 3]).rolling(window=3, min_periods=5, step=step).min()
```


## Complete Example

```python
# Setup
# Fixtures: step

# Workflow
a = Series([1, 2, 3, 4, 5])
result = a.rolling(window=100, min_periods=1, step=step).min()
expected = Series(np.ones(len(a)))[::step]
tm.assert_series_equal(result, expected)
msg = 'min_periods 5 must be <= window 3'
with pytest.raises(ValueError, match=msg):
    Series([1, 2, 3]).rolling(window=3, min_periods=5, step=step).min()
```

## Next Steps


---

*Source: test_api.py:381 | Complexity: Intermediate | Last updated: 2026-06-02*