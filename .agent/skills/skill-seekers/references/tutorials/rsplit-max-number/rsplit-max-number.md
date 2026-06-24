# How To: Rsplit Max Number

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rsplit max number

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas.tests.strings`

**Setup Required:**
```python
# Fixtures: any_string_dtype
```

## Step-by-Step Guide

### Step 1: Assign values = Series(...)

```python
values = Series(['a_b_c', 'c_d_e', np.nan, 'f_g_h'], dtype=any_string_dtype)
```

### Step 2: Assign result = values.str.rsplit(...)

```python
result = values.str.rsplit('_', n=1)
```

### Step 3: Assign exp = Series(...)

```python
exp = Series([['a_b', 'c'], ['c_d', 'e'], np.nan, ['f_g', 'h']])
```

### Step 4: Assign exp = _convert_na_value(...)

```python
exp = _convert_na_value(values, exp)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, exp)
```


## Complete Example

```python
# Setup
# Fixtures: any_string_dtype

# Workflow
values = Series(['a_b_c', 'c_d_e', np.nan, 'f_g_h'], dtype=any_string_dtype)
result = values.str.rsplit('_', n=1)
exp = Series([['a_b', 'c'], ['c_d', 'e'], np.nan, ['f_g', 'h']])
exp = _convert_na_value(values, exp)
tm.assert_series_equal(result, exp)
```

## Next Steps


---

*Source: test_split_partition.py:133 | Complexity: Intermediate | Last updated: 2026-06-02*