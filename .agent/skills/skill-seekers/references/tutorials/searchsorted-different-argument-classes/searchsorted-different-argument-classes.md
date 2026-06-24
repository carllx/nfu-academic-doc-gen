# How To: Searchsorted Different Argument Classes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test searchsorted different argument classes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: listlike_box
```

## Step-by-Step Guide

### Step 1: Assign pidx = PeriodIndex(...)

```python
pidx = PeriodIndex(['2014-01-01', '2014-01-02', '2014-01-03', '2014-01-04', '2014-01-05'], freq='D')
```

### Step 2: Assign result = pidx.searchsorted(...)

```python
result = pidx.searchsorted(listlike_box(pidx))
```

### Step 3: Assign expected = np.arange(...)

```python
expected = np.arange(len(pidx), dtype=result.dtype)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 5: Assign result = pidx._data.searchsorted(...)

```python
result = pidx._data.searchsorted(listlike_box(pidx))
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: listlike_box

# Workflow
pidx = PeriodIndex(['2014-01-01', '2014-01-02', '2014-01-03', '2014-01-04', '2014-01-05'], freq='D')
result = pidx.searchsorted(listlike_box(pidx))
expected = np.arange(len(pidx), dtype=result.dtype)
tm.assert_numpy_array_equal(result, expected)
result = pidx._data.searchsorted(listlike_box(pidx))
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_searchsorted.py:38 | Complexity: Intermediate | Last updated: 2026-06-02*