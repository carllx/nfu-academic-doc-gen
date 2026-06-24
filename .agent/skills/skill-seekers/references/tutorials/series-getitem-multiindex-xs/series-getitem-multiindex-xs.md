# How To: Series Getitem Multiindex Xs

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series getitem multiindex xs

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dt = list(...)

```python
dt = list(date_range('20130903', periods=3))
```

### Step 2: Assign idx = MultiIndex.from_product(...)

```python
idx = MultiIndex.from_product([list('AB'), dt])
```

### Step 3: Assign ser = Series(...)

```python
ser = Series([1, 3, 4, 1, 3, 4], index=idx)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([1, 1], index=list('AB'))
```

### Step 5: Assign result = ser.xs(...)

```python
result = ser.xs('20130903', level=1)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
dt = list(date_range('20130903', periods=3))
idx = MultiIndex.from_product([list('AB'), dt])
ser = Series([1, 3, 4, 1, 3, 4], index=idx)
expected = Series([1, 1], index=list('AB'))
result = ser.xs('20130903', level=1)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_xs.py:49 | Complexity: Intermediate | Last updated: 2026-06-02*