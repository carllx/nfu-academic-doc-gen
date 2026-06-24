# How To: Filter Single Column Df

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test filter single column df

## Prerequisites

**Required Modules:**
- `string`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([1, 3, 20, 5, 22, 24, 7])
```

### Step 2: Assign expected_odd = DataFrame(...)

```python
expected_odd = DataFrame([1, 3, 5, 7], index=[0, 1, 3, 6])
```

### Step 3: Assign expected_even = DataFrame(...)

```python
expected_even = DataFrame([20, 22, 24], index=[2, 4, 5])
```

### Step 4: Assign grouper = unknown.apply(...)

```python
grouper = df[0].apply(lambda x: x % 2)
```

### Step 5: Assign grouped = df.groupby(...)

```python
grouped = df.groupby(grouper)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(grouped.filter(lambda x: x.mean() < 10), expected_odd)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(grouped.filter(lambda x: x.mean() > 10), expected_even)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(grouped.filter(lambda x: x.mean() < 10, dropna=False), expected_odd.reindex(df.index))
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(grouped.filter(lambda x: x.mean() > 10, dropna=False), expected_even.reindex(df.index))
```


## Complete Example

```python
# Workflow
df = DataFrame([1, 3, 20, 5, 22, 24, 7])
expected_odd = DataFrame([1, 3, 5, 7], index=[0, 1, 3, 6])
expected_even = DataFrame([20, 22, 24], index=[2, 4, 5])
grouper = df[0].apply(lambda x: x % 2)
grouped = df.groupby(grouper)
tm.assert_frame_equal(grouped.filter(lambda x: x.mean() < 10), expected_odd)
tm.assert_frame_equal(grouped.filter(lambda x: x.mean() > 10), expected_even)
tm.assert_frame_equal(grouped.filter(lambda x: x.mean() < 10, dropna=False), expected_odd.reindex(df.index))
tm.assert_frame_equal(grouped.filter(lambda x: x.mean() > 10, dropna=False), expected_even.reindex(df.index))
```

## Next Steps


---

*Source: test_filters.py:34 | Complexity: Advanced | Last updated: 2026-06-02*