# How To: Masked Kleene Logic

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test masked kleene logic

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `builtins`
- `datetime`
- `string`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.missing`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`
- `pandas.util`
- `scipy.stats`

**Setup Required:**
```python
# Fixtures: bool_agg_func, skipna, data
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(data, dtype='boolean')
```

### Step 2: Assign expected_data = getattr(...)

```python
expected_data = getattr(ser, bool_agg_func)(skipna=skipna)
```

### Step 3: Assign expected = Series(...)

```python
expected = Series(expected_data, index=np.array([0]), dtype='boolean')
```

### Step 4: Assign result = ser.groupby.agg(...)

```python
result = ser.groupby([0, 0, 0]).agg(bool_agg_func, skipna=skipna)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: bool_agg_func, skipna, data

# Workflow
ser = Series(data, dtype='boolean')
expected_data = getattr(ser, bool_agg_func)(skipna=skipna)
expected = Series(expected_data, index=np.array([0]), dtype='boolean')
result = ser.groupby([0, 0, 0]).agg(bool_agg_func, skipna=skipna)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_reductions.py:99 | Complexity: Intermediate | Last updated: 2026-06-02*