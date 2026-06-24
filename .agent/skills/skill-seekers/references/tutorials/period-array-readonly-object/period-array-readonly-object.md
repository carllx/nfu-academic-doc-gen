# How To: Period Array Readonly Object

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test period array readonly object

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.period`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign pa = period_array(...)

```python
pa = period_array([pd.Period('2019-01-01')])
```

### Step 2: Assign arr = np.asarray(...)

```python
arr = np.asarray(pa, dtype='object')
```

### Step 3: Call arr.setflags()

```python
arr.setflags(write=False)
```

### Step 4: Assign result = period_array(...)

```python
result = period_array(arr)
```

### Step 5: Call tm.assert_period_array_equal()

```python
tm.assert_period_array_equal(result, pa)
```

### Step 6: Assign result = pd.Series(...)

```python
result = pd.Series(arr)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, pd.Series(pa))
```

### Step 8: Assign result = pd.DataFrame(...)

```python
result = pd.DataFrame({'A': arr})
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, pd.DataFrame({'A': pa}))
```


## Complete Example

```python
# Workflow
pa = period_array([pd.Period('2019-01-01')])
arr = np.asarray(pa, dtype='object')
arr.setflags(write=False)
result = period_array(arr)
tm.assert_period_array_equal(result, pa)
result = pd.Series(arr)
tm.assert_series_equal(result, pd.Series(pa))
result = pd.DataFrame({'A': arr})
tm.assert_frame_equal(result, pd.DataFrame({'A': pa}))
```

## Next Steps


---

*Source: test_constructors.py:36 | Complexity: Advanced | Last updated: 2026-06-02*