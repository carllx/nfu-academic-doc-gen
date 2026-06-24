# How To: Value Counts Categorical Ordered

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test value counts categorical ordered

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign values = Categorical(...)

```python
values = Categorical([1, 2, 3, 1, 1, 3], ordered=True)
```

### Step 2: Assign exp_idx = CategoricalIndex(...)

```python
exp_idx = CategoricalIndex([1, 3, 2], categories=[1, 2, 3], ordered=True, name='xxx')
```

### Step 3: Assign exp = Series(...)

```python
exp = Series([3, 2, 1], index=exp_idx, name='count')
```

### Step 4: Assign ser = Series(...)

```python
ser = Series(values, name='xxx')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser.value_counts(), exp)
```

### Step 6: Assign idx = CategoricalIndex(...)

```python
idx = CategoricalIndex(values, name='xxx')
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(idx.value_counts(), exp)
```

### Step 8: Assign exp = Series(...)

```python
exp = Series(np.array([3.0, 2.0, 1]) / 6.0, index=exp_idx, name='proportion')
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser.value_counts(normalize=True), exp)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(idx.value_counts(normalize=True), exp)
```


## Complete Example

```python
# Workflow
values = Categorical([1, 2, 3, 1, 1, 3], ordered=True)
exp_idx = CategoricalIndex([1, 3, 2], categories=[1, 2, 3], ordered=True, name='xxx')
exp = Series([3, 2, 1], index=exp_idx, name='count')
ser = Series(values, name='xxx')
tm.assert_series_equal(ser.value_counts(), exp)
idx = CategoricalIndex(values, name='xxx')
tm.assert_series_equal(idx.value_counts(), exp)
exp = Series(np.array([3.0, 2.0, 1]) / 6.0, index=exp_idx, name='proportion')
tm.assert_series_equal(ser.value_counts(normalize=True), exp)
tm.assert_series_equal(idx.value_counts(normalize=True), exp)
```

## Next Steps


---

*Source: test_value_counts.py:95 | Complexity: Advanced | Last updated: 2026-06-02*