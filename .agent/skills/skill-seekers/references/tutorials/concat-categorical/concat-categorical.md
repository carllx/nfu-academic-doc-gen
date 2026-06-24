# How To: Concat Categorical

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat categorical

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s1 = Series(...)

```python
s1 = Series([1, 2, np.nan], dtype='category')
```

### Step 2: Assign s2 = Series(...)

```python
s2 = Series([2, 1, 2], dtype='category')
```

### Step 3: Assign exp = Series(...)

```python
exp = Series([1, 2, np.nan, 2, 1, 2], dtype='category')
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(pd.concat([s1, s2], ignore_index=True), exp)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s1._append(s2, ignore_index=True), exp)
```

### Step 6: Assign s1 = Series(...)

```python
s1 = Series([3, 2], dtype='category')
```

### Step 7: Assign s2 = Series(...)

```python
s2 = Series([2, 1], dtype='category')
```

### Step 8: Assign exp = Series(...)

```python
exp = Series([3, 2, 2, 1])
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(pd.concat([s1, s2], ignore_index=True), exp)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s1._append(s2, ignore_index=True), exp)
```

### Step 11: Assign s1 = Series(...)

```python
s1 = Series([10, 11, np.nan], dtype='category')
```

### Step 12: Assign s2 = Series(...)

```python
s2 = Series([np.nan, 1, 3, 2], dtype='category')
```

### Step 13: Assign exp = Series(...)

```python
exp = Series([10, 11, np.nan, np.nan, 1, 3, 2], dtype=np.float64)
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(pd.concat([s1, s2], ignore_index=True), exp)
```

### Step 15: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s1._append(s2, ignore_index=True), exp)
```


## Complete Example

```python
# Workflow
s1 = Series([1, 2, np.nan], dtype='category')
s2 = Series([2, 1, 2], dtype='category')
exp = Series([1, 2, np.nan, 2, 1, 2], dtype='category')
tm.assert_series_equal(pd.concat([s1, s2], ignore_index=True), exp)
tm.assert_series_equal(s1._append(s2, ignore_index=True), exp)
s1 = Series([3, 2], dtype='category')
s2 = Series([2, 1], dtype='category')
exp = Series([3, 2, 2, 1])
tm.assert_series_equal(pd.concat([s1, s2], ignore_index=True), exp)
tm.assert_series_equal(s1._append(s2, ignore_index=True), exp)
s1 = Series([10, 11, np.nan], dtype='category')
s2 = Series([np.nan, 1, 3, 2], dtype='category')
exp = Series([10, 11, np.nan, np.nan, 1, 3, 2], dtype=np.float64)
tm.assert_series_equal(pd.concat([s1, s2], ignore_index=True), exp)
tm.assert_series_equal(s1._append(s2, ignore_index=True), exp)
```

## Next Steps


---

*Source: test_append_common.py:471 | Complexity: Advanced | Last updated: 2026-06-02*