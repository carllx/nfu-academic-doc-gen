# How To: Multiindex Align To Series With Common Index Level Missing In Left

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiindex align to series with common index level missing in left

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign foo_index = Index(...)

```python
foo_index = Index([1, 2, 3], name='foo')
```

### Step 2: Assign bar_index = Index(...)

```python
bar_index = Index([1, 2], name='bar')
```

### Step 3: Assign series = Series(...)

```python
series = Series([1, 2, 3, 4], index=Index([1, 2, 3, 4], name='bar'), name='foo_series')
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame({'col': np.arange(6)}, index=pd.MultiIndex.from_product([foo_index, bar_index]))
```

### Step 5: Assign expected_r = Series(...)

```python
expected_r = Series([1, 2] * 3, index=df.index, name='foo_series')
```

### Step 6: Assign unknown = df.align(...)

```python
result_l, result_r = df.align(series, axis=0)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result_l, df)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result_r, expected_r)
```


## Complete Example

```python
# Workflow
foo_index = Index([1, 2, 3], name='foo')
bar_index = Index([1, 2], name='bar')
series = Series([1, 2, 3, 4], index=Index([1, 2, 3, 4], name='bar'), name='foo_series')
df = DataFrame({'col': np.arange(6)}, index=pd.MultiIndex.from_product([foo_index, bar_index]))
expected_r = Series([1, 2] * 3, index=df.index, name='foo_series')
result_l, result_r = df.align(series, axis=0)
tm.assert_frame_equal(result_l, df)
tm.assert_series_equal(result_r, expected_r)
```

## Next Steps


---

*Source: test_align.py:313 | Complexity: Advanced | Last updated: 2026-06-02*