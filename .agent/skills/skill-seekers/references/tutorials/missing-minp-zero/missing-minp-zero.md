# How To: Missing Minp Zero

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test missing minp zero

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign x = Series(...)

```python
x = Series([np.nan])
```

### Step 2: Assign result = x.expanding.sum(...)

```python
result = x.expanding(min_periods=0).sum()
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([0.0])
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = x.expanding.sum(...)

```python
result = x.expanding(min_periods=1).sum()
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([np.nan])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
x = Series([np.nan])
result = x.expanding(min_periods=0).sum()
expected = Series([0.0])
tm.assert_series_equal(result, expected)
result = x.expanding(min_periods=1).sum()
expected = Series([np.nan])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_expanding.py:68 | Complexity: Intermediate | Last updated: 2026-06-02*