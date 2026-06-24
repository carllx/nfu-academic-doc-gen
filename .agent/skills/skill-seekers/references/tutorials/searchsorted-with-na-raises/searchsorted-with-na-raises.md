# How To: Searchsorted With Na Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test searchsorted with na raises

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `string`
- `typing`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.core.dtypes.base`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.arrays`
- `pandas.core.arrays.string_`
- `pandas.tests.arrays.string_.test_string`
- `pandas.tests.extension`

**Setup Required:**
```python
# Fixtures: data_for_sorting, as_series
```

## Step-by-Step Guide

### Step 1: Assign unknown = data_for_sorting

```python
b, c, a = data_for_sorting
```

### Step 2: Assign arr = data_for_sorting.take(...)

```python
arr = data_for_sorting.take([2, 0, 1])
```

### Step 3: Assign unknown = value

```python
arr[-1] = pd.NA
```

### Step 4: Assign msg = 'searchsorted requires array to be sorted, which is impossible with NAs present.'

```python
msg = 'searchsorted requires array to be sorted, which is impossible with NAs present.'
```

### Step 5: Assign arr = pd.Series(...)

```python
arr = pd.Series(arr)
```

### Step 6: Call arr.searchsorted()

```python
arr.searchsorted(b)
```


## Complete Example

```python
# Setup
# Fixtures: data_for_sorting, as_series

# Workflow
b, c, a = data_for_sorting
arr = data_for_sorting.take([2, 0, 1])
arr[-1] = pd.NA
if as_series:
    arr = pd.Series(arr)
msg = 'searchsorted requires array to be sorted, which is impossible with NAs present.'
with pytest.raises(ValueError, match=msg):
    arr.searchsorted(b)
```

## Next Steps


---

*Source: test_string.py:263 | Complexity: Intermediate | Last updated: 2026-06-02*