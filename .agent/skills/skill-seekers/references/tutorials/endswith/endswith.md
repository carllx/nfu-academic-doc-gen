# How To: Endswith

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test endswith

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas.tests.strings`

**Setup Required:**
```python
# Fixtures: pat, dtype, null_value, na, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign values = Series(...)

```python
values = Series(['om', null_value, 'foo_nom', 'nom', 'bar_foo', null_value, 'foo'], dtype=dtype)
```

### Step 2: Assign result = values.str.endswith(...)

```python
result = values.str.endswith(pat)
```

### Step 3: Assign exp = Series(...)

```python
exp = Series([False, np.nan, False, False, True, np.nan, True])
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, exp)
```

### Step 5: Assign result = values.str.endswith(...)

```python
result = values.str.endswith(pat, na=na)
```

### Step 6: Assign exp = Series(...)

```python
exp = Series([False, na, False, False, True, na, True])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, exp)
```

### Step 8: Assign mixed = np.array(...)

```python
mixed = np.array(['a', np.nan, 'b', True, datetime.today(), 'foo', None, 1, 2.0], dtype=object)
```

### Step 9: Assign rs = Series.str.endswith(...)

```python
rs = Series(mixed).str.endswith('f')
```

### Step 10: Assign xp = Series(...)

```python
xp = Series([False, np.nan, False, np.nan, np.nan, False, None, np.nan, np.nan])
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(rs, xp)
```

### Step 12: Assign exp = exp.fillna(...)

```python
exp = exp.fillna(null_value)
```

### Step 13: Assign unknown = None

```python
exp[exp.isna()] = None
```

### Step 14: Assign exp = exp.fillna.astype(...)

```python
exp = exp.fillna(False).astype(bool)
```


## Complete Example

```python
# Setup
# Fixtures: pat, dtype, null_value, na, using_infer_string

# Workflow
values = Series(['om', null_value, 'foo_nom', 'nom', 'bar_foo', null_value, 'foo'], dtype=dtype)
result = values.str.endswith(pat)
exp = Series([False, np.nan, False, False, True, np.nan, True])
if dtype == 'object' and null_value is pd.NA:
    exp = exp.fillna(null_value)
elif dtype == 'object' and null_value is None:
    exp[exp.isna()] = None
elif using_infer_string and dtype == 'category':
    exp = exp.fillna(False).astype(bool)
tm.assert_series_equal(result, exp)
result = values.str.endswith(pat, na=na)
exp = Series([False, na, False, False, True, na, True])
tm.assert_series_equal(result, exp)
mixed = np.array(['a', np.nan, 'b', True, datetime.today(), 'foo', None, 1, 2.0], dtype=object)
rs = Series(mixed).str.endswith('f')
xp = Series([False, np.nan, False, np.nan, np.nan, False, None, np.nan, np.nan])
tm.assert_series_equal(rs, xp)
```

## Next Steps


---

*Source: test_find_replace.py:456 | Complexity: Advanced | Last updated: 2026-06-02*