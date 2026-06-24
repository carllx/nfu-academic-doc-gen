# How To: Filter Series

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test filter series

## Prerequisites

**Required Modules:**
- `string`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series([1, 3, 20, 5, 22, 24, 7])
```

### Step 2: Assign expected_odd = Series(...)

```python
expected_odd = Series([1, 3, 5, 7], index=[0, 1, 3, 6])
```

### Step 3: Assign expected_even = Series(...)

```python
expected_even = Series([20, 22, 24], index=[2, 4, 5])
```

### Step 4: Assign grouper = s.apply(...)

```python
grouper = s.apply(lambda x: x % 2)
```

### Step 5: Assign grouped = s.groupby(...)

```python
grouped = s.groupby(grouper)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(grouped.filter(lambda x: x.mean() < 10), expected_odd)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(grouped.filter(lambda x: x.mean() > 10), expected_even)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(grouped.filter(lambda x: x.mean() < 10, dropna=False), expected_odd.reindex(s.index))
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(grouped.filter(lambda x: x.mean() > 10, dropna=False), expected_even.reindex(s.index))
```


## Complete Example

```python
# Workflow
s = Series([1, 3, 20, 5, 22, 24, 7])
expected_odd = Series([1, 3, 5, 7], index=[0, 1, 3, 6])
expected_even = Series([20, 22, 24], index=[2, 4, 5])
grouper = s.apply(lambda x: x % 2)
grouped = s.groupby(grouper)
tm.assert_series_equal(grouped.filter(lambda x: x.mean() < 10), expected_odd)
tm.assert_series_equal(grouped.filter(lambda x: x.mean() > 10), expected_even)
tm.assert_series_equal(grouped.filter(lambda x: x.mean() < 10, dropna=False), expected_odd.reindex(s.index))
tm.assert_series_equal(grouped.filter(lambda x: x.mean() > 10, dropna=False), expected_even.reindex(s.index))
```

## Next Steps


---

*Source: test_filters.py:15 | Complexity: Advanced | Last updated: 2026-06-02*