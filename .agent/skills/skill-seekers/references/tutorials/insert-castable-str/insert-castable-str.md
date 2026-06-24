# How To: Insert Castable Str

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test insert castable str

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz_aware_fixture
```

## Step-by-Step Guide

### Step 1: Assign tz = tz_aware_fixture

```python
tz = tz_aware_fixture
```

### Step 2: Assign dti = date_range(...)

```python
dti = date_range('2019-11-04', periods=3, freq='-1D', name=9, tz=tz)
```

### Step 3: Assign value = '2019-11-05'

```python
value = '2019-11-05'
```

### Step 4: Assign result = dti.insert(...)

```python
result = dti.insert(0, value)
```

### Step 5: Assign ts = Timestamp.tz_localize(...)

```python
ts = Timestamp(value).tz_localize(tz)
```

### Step 6: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex([ts] + list(dti), dtype=dti.dtype, name=9)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tz_aware_fixture

# Workflow
tz = tz_aware_fixture
dti = date_range('2019-11-04', periods=3, freq='-1D', name=9, tz=tz)
value = '2019-11-05'
result = dti.insert(0, value)
ts = Timestamp(value).tz_localize(tz)
expected = DatetimeIndex([ts] + list(dti), dtype=dti.dtype, name=9)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_insert.py:244 | Complexity: Intermediate | Last updated: 2026-06-02*