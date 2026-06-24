# How To: Parsing Non Iso Timezone Offset

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test parsing non iso timezone offset

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign dt_string = '01-01-2013T00:00:00.000000000+0000'

```python
dt_string = '01-01-2013T00:00:00.000000000+0000'
```

**Verification:**
```python
assert result_tz is timezone.utc
```

### Step 2: Assign arr = np.array(...)

```python
arr = np.array([dt_string], dtype=object)
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array([np.datetime64('2013-01-01 00:00:00.000000000')])
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

**Verification:**
```python
assert result_tz is timezone.utc
```

### Step 5: Assign unknown = tslib.array_to_datetime(...)

```python
result, result_tz = tslib.array_to_datetime(arr)
```


## Complete Example

```python
# Workflow
dt_string = '01-01-2013T00:00:00.000000000+0000'
arr = np.array([dt_string], dtype=object)
with tm.assert_produces_warning(None):
    result, result_tz = tslib.array_to_datetime(arr)
expected = np.array([np.datetime64('2013-01-01 00:00:00.000000000')])
tm.assert_numpy_array_equal(result, expected)
assert result_tz is timezone.utc
```

## Next Steps


---

*Source: test_array_to_datetime.py:185 | Complexity: Intermediate | Last updated: 2026-06-02*