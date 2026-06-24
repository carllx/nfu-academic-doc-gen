# How To: Series Getitem Multiindex Xs By Label

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series getitem multiindex xs by label

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = MultiIndex.from_tuples(...)

```python
idx = MultiIndex.from_tuples([('a', 'one'), ('a', 'two'), ('b', 'one'), ('b', 'two')])
```

**Verification:**
```python
assert return_value is None
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([1, 2, 3, 4], index=idx)
```

**Verification:**
```python
assert return_value is None
```

### Step 3: Assign return_value = ser.index.set_names(...)

```python
return_value = ser.index.set_names(['L1', 'L2'], inplace=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([1, 3], index=['a', 'b'])
```

### Step 5: Assign return_value = expected.index.set_names(...)

```python
return_value = expected.index.set_names(['L1'], inplace=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 6: Assign result = ser.xs(...)

```python
result = ser.xs('one', level='L2')
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx = MultiIndex.from_tuples([('a', 'one'), ('a', 'two'), ('b', 'one'), ('b', 'two')])
ser = Series([1, 2, 3, 4], index=idx)
return_value = ser.index.set_names(['L1', 'L2'], inplace=True)
assert return_value is None
expected = Series([1, 3], index=['a', 'b'])
return_value = expected.index.set_names(['L1'], inplace=True)
assert return_value is None
result = ser.xs('one', level='L2')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_xs.py:34 | Complexity: Intermediate | Last updated: 2026-06-02*