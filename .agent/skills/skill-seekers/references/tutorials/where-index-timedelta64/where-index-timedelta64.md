# How To: Where Index Timedelta64

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test where index timedelta64

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
# Fixtures: value
```

## Step-by-Step Guide

### Step 1: Assign tdi = pd.timedelta_range(...)

```python
tdi = pd.timedelta_range('1 Day', periods=4)
```

**Verification:**
```python
assert expected[1] is dtnat
```

### Step 2: Assign cond = np.array(...)

```python
cond = np.array([True, False, False, True])
```

### Step 3: Assign expected = pd.TimedeltaIndex(...)

```python
expected = pd.TimedeltaIndex(['1 Day', value, value, '4 Days'])
```

### Step 4: Assign result = tdi.where(...)

```python
result = tdi.where(cond, value)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 6: Assign dtnat = np.datetime64(...)

```python
dtnat = np.datetime64('NaT', 'ns')
```

### Step 7: Assign expected = pd.Index(...)

```python
expected = pd.Index([tdi[0], dtnat, dtnat, tdi[3]], dtype=object)
```

**Verification:**
```python
assert expected[1] is dtnat
```

### Step 8: Assign result = tdi.where(...)

```python
result = tdi.where(cond, dtnat)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: value

# Workflow
tdi = pd.timedelta_range('1 Day', periods=4)
cond = np.array([True, False, False, True])
expected = pd.TimedeltaIndex(['1 Day', value, value, '4 Days'])
result = tdi.where(cond, value)
tm.assert_index_equal(result, expected)
dtnat = np.datetime64('NaT', 'ns')
expected = pd.Index([tdi[0], dtnat, dtnat, tdi[3]], dtype=object)
assert expected[1] is dtnat
result = tdi.where(cond, dtnat)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_coercion.py:501 | Complexity: Advanced | Last updated: 2026-06-02*