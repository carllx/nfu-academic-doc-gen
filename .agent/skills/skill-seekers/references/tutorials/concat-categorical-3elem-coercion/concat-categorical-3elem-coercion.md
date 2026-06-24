# How To: Concat Categorical 3Elem Coercion

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat categorical 3elem coercion

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

### Step 3: Assign s3 = Series(...)

```python
s3 = Series([1, 2, 1, 2, np.nan])
```

### Step 4: Assign exp = Series(...)

```python
exp = Series([1, 2, np.nan, 2, 1, 2, 1, 2, 1, 2, np.nan], dtype='float')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(pd.concat([s1, s2, s3], ignore_index=True), exp)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s1._append([s2, s3], ignore_index=True), exp)
```

### Step 7: Assign exp = Series(...)

```python
exp = Series([1, 2, 1, 2, np.nan, 1, 2, np.nan, 2, 1, 2], dtype='float')
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(pd.concat([s3, s1, s2], ignore_index=True), exp)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s3._append([s1, s2], ignore_index=True), exp)
```

### Step 10: Assign s1 = Series(...)

```python
s1 = Series([4, 5, 6], dtype='category')
```

### Step 11: Assign s2 = Series(...)

```python
s2 = Series([1, 2, 3], dtype='category')
```

### Step 12: Assign s3 = Series(...)

```python
s3 = Series([1, 3, 4])
```

### Step 13: Assign exp = Series(...)

```python
exp = Series([4, 5, 6, 1, 2, 3, 1, 3, 4])
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(pd.concat([s1, s2, s3], ignore_index=True), exp)
```

### Step 15: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s1._append([s2, s3], ignore_index=True), exp)
```

### Step 16: Assign exp = Series(...)

```python
exp = Series([1, 3, 4, 4, 5, 6, 1, 2, 3])
```

### Step 17: Call tm.assert_series_equal()

```python
tm.assert_series_equal(pd.concat([s3, s1, s2], ignore_index=True), exp)
```

### Step 18: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s3._append([s1, s2], ignore_index=True), exp)
```

### Step 19: Assign s1 = Series(...)

```python
s1 = Series([4, 5, 6], dtype='category')
```

### Step 20: Assign s2 = Series(...)

```python
s2 = Series([1, 2, 3], dtype='category')
```

### Step 21: Assign s3 = Series(...)

```python
s3 = Series([10, 11, 12])
```

### Step 22: Assign exp = Series(...)

```python
exp = Series([4, 5, 6, 1, 2, 3, 10, 11, 12])
```

### Step 23: Call tm.assert_series_equal()

```python
tm.assert_series_equal(pd.concat([s1, s2, s3], ignore_index=True), exp)
```

### Step 24: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s1._append([s2, s3], ignore_index=True), exp)
```

### Step 25: Assign exp = Series(...)

```python
exp = Series([10, 11, 12, 4, 5, 6, 1, 2, 3])
```

### Step 26: Call tm.assert_series_equal()

```python
tm.assert_series_equal(pd.concat([s3, s1, s2], ignore_index=True), exp)
```

### Step 27: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s3._append([s1, s2], ignore_index=True), exp)
```


## Complete Example

```python
# Workflow
s1 = Series([1, 2, np.nan], dtype='category')
s2 = Series([2, 1, 2], dtype='category')
s3 = Series([1, 2, 1, 2, np.nan])
exp = Series([1, 2, np.nan, 2, 1, 2, 1, 2, 1, 2, np.nan], dtype='float')
tm.assert_series_equal(pd.concat([s1, s2, s3], ignore_index=True), exp)
tm.assert_series_equal(s1._append([s2, s3], ignore_index=True), exp)
exp = Series([1, 2, 1, 2, np.nan, 1, 2, np.nan, 2, 1, 2], dtype='float')
tm.assert_series_equal(pd.concat([s3, s1, s2], ignore_index=True), exp)
tm.assert_series_equal(s3._append([s1, s2], ignore_index=True), exp)
s1 = Series([4, 5, 6], dtype='category')
s2 = Series([1, 2, 3], dtype='category')
s3 = Series([1, 3, 4])
exp = Series([4, 5, 6, 1, 2, 3, 1, 3, 4])
tm.assert_series_equal(pd.concat([s1, s2, s3], ignore_index=True), exp)
tm.assert_series_equal(s1._append([s2, s3], ignore_index=True), exp)
exp = Series([1, 3, 4, 4, 5, 6, 1, 2, 3])
tm.assert_series_equal(pd.concat([s3, s1, s2], ignore_index=True), exp)
tm.assert_series_equal(s3._append([s1, s2], ignore_index=True), exp)
s1 = Series([4, 5, 6], dtype='category')
s2 = Series([1, 2, 3], dtype='category')
s3 = Series([10, 11, 12])
exp = Series([4, 5, 6, 1, 2, 3, 10, 11, 12])
tm.assert_series_equal(pd.concat([s1, s2, s3], ignore_index=True), exp)
tm.assert_series_equal(s1._append([s2, s3], ignore_index=True), exp)
exp = Series([10, 11, 12, 4, 5, 6, 1, 2, 3])
tm.assert_series_equal(pd.concat([s3, s1, s2], ignore_index=True), exp)
tm.assert_series_equal(s3._append([s1, s2], ignore_index=True), exp)
```

## Next Steps


---

*Source: test_append_common.py:572 | Complexity: Advanced | Last updated: 2026-06-02*