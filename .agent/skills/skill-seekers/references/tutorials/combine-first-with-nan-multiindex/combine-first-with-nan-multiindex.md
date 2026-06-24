# How To: Combine First With Nan Multiindex

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test combine first with nan multiindex

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.core.dtypes.cast`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign mi1 = MultiIndex.from_arrays(...)

```python
mi1 = MultiIndex.from_arrays([['b', 'b', 'c', 'a', 'b', np.nan], [1, 2, 3, 4, 5, 6]], names=['a', 'b'])
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'c': [1, 1, 1, 1, 1, 1]}, index=mi1)
```

### Step 3: Assign mi2 = MultiIndex.from_arrays(...)

```python
mi2 = MultiIndex.from_arrays([['a', 'b', 'c', 'a', 'b', 'd'], [1, 1, 1, 1, 1, 1]], names=['a', 'b'])
```

### Step 4: Assign s = Series(...)

```python
s = Series([1, 2, 3, 4, 5, 6], index=mi2)
```

### Step 5: Assign res = df.combine_first(...)

```python
res = df.combine_first(DataFrame({'d': s}))
```

### Step 6: Assign mi_expected = MultiIndex.from_arrays(...)

```python
mi_expected = MultiIndex.from_arrays([['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'd', np.nan], [1, 1, 4, 1, 1, 2, 5, 1, 3, 1, 6]], names=['a', 'b'])
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({'c': [np.nan, np.nan, 1, 1, 1, 1, 1, np.nan, 1, np.nan, 1], 'd': [1.0, 4.0, np.nan, 2.0, 5.0, np.nan, np.nan, 3.0, np.nan, 6.0, np.nan]}, index=mi_expected)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expected)
```


## Complete Example

```python
# Workflow
mi1 = MultiIndex.from_arrays([['b', 'b', 'c', 'a', 'b', np.nan], [1, 2, 3, 4, 5, 6]], names=['a', 'b'])
df = DataFrame({'c': [1, 1, 1, 1, 1, 1]}, index=mi1)
mi2 = MultiIndex.from_arrays([['a', 'b', 'c', 'a', 'b', 'd'], [1, 1, 1, 1, 1, 1]], names=['a', 'b'])
s = Series([1, 2, 3, 4, 5, 6], index=mi2)
res = df.combine_first(DataFrame({'d': s}))
mi_expected = MultiIndex.from_arrays([['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'd', np.nan], [1, 1, 4, 1, 1, 2, 5, 1, 3, 1, 6]], names=['a', 'b'])
expected = DataFrame({'c': [np.nan, np.nan, 1, 1, 1, 1, 1, np.nan, 1, np.nan, 1], 'd': [1.0, 4.0, np.nan, 2.0, 5.0, np.nan, np.nan, 3.0, np.nan, 6.0, np.nan]}, index=mi_expected)
tm.assert_frame_equal(res, expected)
```

## Next Steps


---

*Source: test_combine_first.py:452 | Complexity: Advanced | Last updated: 2026-06-02*