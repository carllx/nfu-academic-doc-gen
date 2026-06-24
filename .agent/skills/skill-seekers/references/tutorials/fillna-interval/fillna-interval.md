# How To: Fillna Interval

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test fillna interval

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: index_or_series, fill_val
```

## Step-by-Step Guide

### Step 1: Assign ii = pd.interval_range.insert(...)

```python
ii = pd.interval_range(1.0, 5.0, closed='right').insert(1, np.nan)
```

**Verification:**
```python
assert isinstance(ii.dtype, pd.IntervalDtype)
```

### Step 2: Assign obj = index_or_series(...)

```python
obj = index_or_series(ii)
```

### Step 3: Assign exp = index_or_series(...)

```python
exp = index_or_series([ii[0], fill_val, ii[2], ii[3], ii[4]], dtype=object)
```

### Step 4: Assign fill_dtype = object

```python
fill_dtype = object
```

### Step 5: Call self._assert_fillna_conversion()

```python
self._assert_fillna_conversion(obj, fill_val, exp, fill_dtype)
```


## Complete Example

```python
# Setup
# Fixtures: index_or_series, fill_val

# Workflow
ii = pd.interval_range(1.0, 5.0, closed='right').insert(1, np.nan)
assert isinstance(ii.dtype, pd.IntervalDtype)
obj = index_or_series(ii)
exp = index_or_series([ii[0], fill_val, ii[2], ii[3], ii[4]], dtype=object)
fill_dtype = object
self._assert_fillna_conversion(obj, fill_val, exp, fill_dtype)
```

## Next Steps


---

*Source: test_coercion.py:689 | Complexity: Intermediate | Last updated: 2026-06-02*