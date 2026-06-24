# How To: Rename Series With Multiindex Keeps Ea Dtypes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rename series with multiindex keeps ea dtypes

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arrays = value

```python
arrays = [Index([1, 2, 3], dtype='Int64').astype('category'), Index([1, 2, 3], dtype='Int64')]
```

### Step 2: Assign mi = MultiIndex.from_arrays(...)

```python
mi = MultiIndex.from_arrays(arrays, names=['A', 'B'])
```

### Step 3: Assign ser = Series(...)

```python
ser = Series(1, index=mi)
```

### Step 4: Assign result = ser.rename(...)

```python
result = ser.rename({1: 4}, level=1)
```

### Step 5: Assign arrays_expected = value

```python
arrays_expected = [Index([1, 2, 3], dtype='Int64').astype('category'), Index([4, 2, 3], dtype='Int64')]
```

### Step 6: Assign mi_expected = MultiIndex.from_arrays(...)

```python
mi_expected = MultiIndex.from_arrays(arrays_expected, names=['A', 'B'])
```

### Step 7: Assign expected = Series(...)

```python
expected = Series(1, index=mi_expected)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
arrays = [Index([1, 2, 3], dtype='Int64').astype('category'), Index([1, 2, 3], dtype='Int64')]
mi = MultiIndex.from_arrays(arrays, names=['A', 'B'])
ser = Series(1, index=mi)
result = ser.rename({1: 4}, level=1)
arrays_expected = [Index([1, 2, 3], dtype='Int64').astype('category'), Index([4, 2, 3], dtype='Int64')]
mi_expected = MultiIndex.from_arrays(arrays_expected, names=['A', 'B'])
expected = Series(1, index=mi_expected)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_rename.py:146 | Complexity: Advanced | Last updated: 2026-06-02*