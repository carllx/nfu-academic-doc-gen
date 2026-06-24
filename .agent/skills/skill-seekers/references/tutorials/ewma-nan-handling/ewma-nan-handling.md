# How To: Ewma Nan Handling

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ewma nan handling

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series([1.0] + [np.nan] * 5 + [1.0])
```

### Step 2: Assign result = s.ewm.mean(...)

```python
result = s.ewm(com=5).mean()
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, Series([1.0] * len(s)))
```

### Step 4: Assign s = Series(...)

```python
s = Series([np.nan] * 2 + [1.0] + [np.nan] * 2 + [1.0])
```

### Step 5: Assign result = s.ewm.mean(...)

```python
result = s.ewm(com=5).mean()
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, Series([np.nan] * 2 + [1.0] * 4))
```


## Complete Example

```python
# Workflow
s = Series([1.0] + [np.nan] * 5 + [1.0])
result = s.ewm(com=5).mean()
tm.assert_series_equal(result, Series([1.0] * len(s)))
s = Series([np.nan] * 2 + [1.0] + [np.nan] * 2 + [1.0])
result = s.ewm(com=5).mean()
tm.assert_series_equal(result, Series([np.nan] * 2 + [1.0] * 4))
```

## Next Steps


---

*Source: test_ewm.py:260 | Complexity: Intermediate | Last updated: 2026-06-02*