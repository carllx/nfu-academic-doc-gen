# How To: Parsing Different Timezone Offsets

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test parsing different timezone offsets

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

### Step 1: Assign data = value

```python
data = ['2015-11-18 15:30:00+05:30', '2015-11-18 15:30:00+06:30']
```

**Verification:**
```python
assert result_tz is None
```

### Step 2: Assign data = np.array(...)

```python
data = np.array(data, dtype=object)
```

### Step 3: Assign msg = 'parsing datetimes with mixed time zones will raise an error'

```python
msg = 'parsing datetimes with mixed time zones will raise an error'
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([datetime(2015, 11, 18, 15, 30, tzinfo=tzoffset(None, 19800)), datetime(2015, 11, 18, 15, 30, tzinfo=tzoffset(None, 23400))], dtype=object)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

**Verification:**
```python
assert result_tz is None
```

### Step 6: Assign unknown = tslib.array_to_datetime(...)

```python
result, result_tz = tslib.array_to_datetime(data)
```


## Complete Example

```python
# Workflow
data = ['2015-11-18 15:30:00+05:30', '2015-11-18 15:30:00+06:30']
data = np.array(data, dtype=object)
msg = 'parsing datetimes with mixed time zones will raise an error'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result, result_tz = tslib.array_to_datetime(data)
expected = np.array([datetime(2015, 11, 18, 15, 30, tzinfo=tzoffset(None, 19800)), datetime(2015, 11, 18, 15, 30, tzinfo=tzoffset(None, 23400))], dtype=object)
tm.assert_numpy_array_equal(result, expected)
assert result_tz is None
```

## Next Steps


---

*Source: test_array_to_datetime.py:198 | Complexity: Intermediate | Last updated: 2026-06-02*