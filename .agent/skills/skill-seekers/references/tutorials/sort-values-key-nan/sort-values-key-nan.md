# How To: Sort Values Key Nan

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort values key nan

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign series = Series(...)

```python
series = Series(np.array([0, 5, np.nan, 3, 2, np.nan]))
```

### Step 2: Assign result = series.sort_values(...)

```python
result = series.sort_values(axis=0)
```

### Step 3: Assign expected = value

```python
expected = series.iloc[[0, 4, 3, 1, 2, 5]]
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = series.sort_values(...)

```python
result = series.sort_values(axis=0, key=lambda x: x + 5)
```

### Step 6: Assign expected = value

```python
expected = series.iloc[[0, 4, 3, 1, 2, 5]]
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign result = series.sort_values(...)

```python
result = series.sort_values(axis=0, key=lambda x: -x, ascending=False)
```

### Step 9: Assign expected = value

```python
expected = series.iloc[[0, 4, 3, 1, 2, 5]]
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
series = Series(np.array([0, 5, np.nan, 3, 2, np.nan]))
result = series.sort_values(axis=0)
expected = series.iloc[[0, 4, 3, 1, 2, 5]]
tm.assert_series_equal(result, expected)
result = series.sort_values(axis=0, key=lambda x: x + 5)
expected = series.iloc[[0, 4, 3, 1, 2, 5]]
tm.assert_series_equal(result, expected)
result = series.sort_values(axis=0, key=lambda x: -x, ascending=False)
expected = series.iloc[[0, 4, 3, 1, 2, 5]]
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_sort_values.py:233 | Complexity: Advanced | Last updated: 2026-06-02*