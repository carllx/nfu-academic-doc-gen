# How To: Series Align Multiindex With Nan

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series align multiindex with nan

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.index`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.boolean`


## Step-by-Step Guide

### Step 1: Assign mi1 = MultiIndex.from_arrays(...)

```python
mi1 = MultiIndex.from_arrays([[81.0, np.nan], [np.nan, np.nan]])
```

### Step 2: Assign mi2 = MultiIndex.from_arrays(...)

```python
mi2 = MultiIndex.from_arrays([[np.nan, 81.0], [np.nan, np.nan]])
```

### Step 3: Assign ser1 = Series(...)

```python
ser1 = Series([1, 2], index=mi1)
```

### Step 4: Assign ser2 = Series(...)

```python
ser2 = Series([1, 2], index=mi2)
```

### Step 5: Assign unknown = ser1.align(...)

```python
result1, result2 = ser1.align(ser2)
```

### Step 6: Assign mi = MultiIndex.from_arrays(...)

```python
mi = MultiIndex.from_arrays([[81.0, np.nan], [np.nan, np.nan]])
```

### Step 7: Assign expected1 = Series(...)

```python
expected1 = Series([1, 2], index=mi)
```

### Step 8: Assign expected2 = Series(...)

```python
expected2 = Series([2, 1], index=mi)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result1, expected1)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result2, expected2)
```


## Complete Example

```python
# Workflow
mi1 = MultiIndex.from_arrays([[81.0, np.nan], [np.nan, np.nan]])
mi2 = MultiIndex.from_arrays([[np.nan, 81.0], [np.nan, np.nan]])
ser1 = Series([1, 2], index=mi1)
ser2 = Series([1, 2], index=mi2)
result1, result2 = ser1.align(ser2)
mi = MultiIndex.from_arrays([[81.0, np.nan], [np.nan, np.nan]])
expected1 = Series([1, 2], index=mi)
expected2 = Series([2, 1], index=mi)
tm.assert_series_equal(result1, expected1)
tm.assert_series_equal(result2, expected2)
```

## Next Steps


---

*Source: test_multiindex.py:170 | Complexity: Advanced | Last updated: 2026-06-02*