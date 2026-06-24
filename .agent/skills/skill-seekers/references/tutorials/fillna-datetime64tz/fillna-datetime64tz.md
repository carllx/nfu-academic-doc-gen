# How To: Fillna Datetime64Tz

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test fillna datetime64tz

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
# Fixtures: index_or_series, fill_val, fill_dtype
```

## Step-by-Step Guide

### Step 1: Assign klass = index_or_series

```python
klass = index_or_series
```

**Verification:**
```python
assert obj.dtype == 'datetime64[ns, US/Eastern]'
```

### Step 2: Assign tz = 'US/Eastern'

```python
tz = 'US/Eastern'
```

### Step 3: Assign obj = klass(...)

```python
obj = klass([pd.Timestamp('2011-01-01', tz=tz), pd.NaT, pd.Timestamp('2011-01-03', tz=tz), pd.Timestamp('2011-01-04', tz=tz)])
```

**Verification:**
```python
assert obj.dtype == 'datetime64[ns, US/Eastern]'
```

### Step 4: Assign exp = klass(...)

```python
exp = klass([pd.Timestamp('2011-01-01', tz=tz), fv, pd.Timestamp('2011-01-03', tz=tz), pd.Timestamp('2011-01-04', tz=tz)])
```

### Step 5: Call self._assert_fillna_conversion()

```python
self._assert_fillna_conversion(obj, fill_val, exp, fill_dtype)
```

### Step 6: Assign fv = fill_val

```python
fv = fill_val
```

### Step 7: Assign fv = fill_val.tz_convert(...)

```python
fv = fill_val.tz_convert(tz)
```


## Complete Example

```python
# Setup
# Fixtures: index_or_series, fill_val, fill_dtype

# Workflow
klass = index_or_series
tz = 'US/Eastern'
obj = klass([pd.Timestamp('2011-01-01', tz=tz), pd.NaT, pd.Timestamp('2011-01-03', tz=tz), pd.Timestamp('2011-01-04', tz=tz)])
assert obj.dtype == 'datetime64[ns, US/Eastern]'
if getattr(fill_val, 'tz', None) is None:
    fv = fill_val
else:
    fv = fill_val.tz_convert(tz)
exp = klass([pd.Timestamp('2011-01-01', tz=tz), fv, pd.Timestamp('2011-01-03', tz=tz), pd.Timestamp('2011-01-04', tz=tz)])
self._assert_fillna_conversion(obj, fill_val, exp, fill_dtype)
```

## Next Steps


---

*Source: test_coercion.py:647 | Complexity: Intermediate | Last updated: 2026-06-02*