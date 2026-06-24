# How To: Astype Ms To S

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype ms to s

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: index_or_series
```

## Step-by-Step Guide

### Step 1: Assign scalar = Timedelta(...)

```python
scalar = Timedelta(days=31)
```

**Verification:**
```python
assert expected.dtype == 'm8[s]'
```

### Step 2: Assign td = index_or_series(...)

```python
td = index_or_series([scalar, scalar, scalar + timedelta(minutes=5, seconds=3), NaT], dtype='m8[ns]')
```

### Step 3: Assign exp_values = np.asarray.astype(...)

```python
exp_values = np.asarray(td).astype('m8[s]')
```

### Step 4: Assign exp_tda = TimedeltaArray._simple_new(...)

```python
exp_tda = TimedeltaArray._simple_new(exp_values, dtype=exp_values.dtype)
```

### Step 5: Assign expected = index_or_series(...)

```python
expected = index_or_series(exp_tda)
```

**Verification:**
```python
assert expected.dtype == 'm8[s]'
```

### Step 6: Assign result = td.astype(...)

```python
result = td.astype('timedelta64[s]')
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: index_or_series

# Workflow
scalar = Timedelta(days=31)
td = index_or_series([scalar, scalar, scalar + timedelta(minutes=5, seconds=3), NaT], dtype='m8[ns]')
exp_values = np.asarray(td).astype('m8[s]')
exp_tda = TimedeltaArray._simple_new(exp_values, dtype=exp_values.dtype)
expected = index_or_series(exp_tda)
assert expected.dtype == 'm8[s]'
result = td.astype('timedelta64[s]')
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_astype.py:118 | Complexity: Intermediate | Last updated: 2026-06-02*