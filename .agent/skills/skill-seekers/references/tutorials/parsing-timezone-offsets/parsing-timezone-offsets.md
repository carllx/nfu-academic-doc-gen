# How To: Parsing Timezone Offsets

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test parsing timezone offsets

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `dateutil.tz.tz`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.tslibs.dtypes`
- `pandas._libs.tslibs.np_datetime`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: dt_string, expected_tz
```

## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array(['01-01-2013 00:00:00'], dtype=object)
```

**Verification:**
```python
assert result_tz == timezone(timedelta(minutes=expected_tz))
```

### Step 2: Assign unknown = tslib.array_to_datetime(...)

```python
expected, _ = tslib.array_to_datetime(arr)
```

### Step 3: Assign arr = np.array(...)

```python
arr = np.array([dt_string], dtype=object)
```

### Step 4: Assign unknown = tslib.array_to_datetime(...)

```python
result, result_tz = tslib.array_to_datetime(arr)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

**Verification:**
```python
assert result_tz == timezone(timedelta(minutes=expected_tz))
```


## Complete Example

```python
# Setup
# Fixtures: dt_string, expected_tz

# Workflow
arr = np.array(['01-01-2013 00:00:00'], dtype=object)
expected, _ = tslib.array_to_datetime(arr)
arr = np.array([dt_string], dtype=object)
result, result_tz = tslib.array_to_datetime(arr)
tm.assert_numpy_array_equal(result, expected)
assert result_tz == timezone(timedelta(minutes=expected_tz))
```

## Next Steps


---

*Source: test_array_to_datetime.py:172 | Complexity: Intermediate | Last updated: 2026-06-02*