# How To: Drop Dst Boundary

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test drop dst boundary

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign tz = 'Europe/Brussels'

```python
tz = 'Europe/Brussels'
```

### Step 2: Assign freq = '15min'

```python
freq = '15min'
```

### Step 3: Assign start = Timestamp(...)

```python
start = Timestamp('201710290100', tz=tz)
```

### Step 4: Assign end = Timestamp(...)

```python
end = Timestamp('201710290300', tz=tz)
```

### Step 5: Assign index = date_range(...)

```python
index = date_range(start=start, end=end, freq=freq)
```

### Step 6: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex(['201710290115', '201710290130', '201710290145', '201710290200', '201710290215', '201710290230', '201710290245', '201710290200', '201710290215', '201710290230', '201710290245', '201710290300'], dtype='M8[ns, Europe/Brussels]', freq=freq, ambiguous=[True, True, True, True, True, True, True, False, False, False, False, False])
```

### Step 7: Assign result = index.drop(...)

```python
result = index.drop(index[0])
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
tz = 'Europe/Brussels'
freq = '15min'
start = Timestamp('201710290100', tz=tz)
end = Timestamp('201710290300', tz=tz)
index = date_range(start=start, end=end, freq=freq)
expected = DatetimeIndex(['201710290115', '201710290130', '201710290145', '201710290200', '201710290215', '201710290230', '201710290245', '201710290200', '201710290215', '201710290230', '201710290245', '201710290300'], dtype='M8[ns, Europe/Brussels]', freq=freq, ambiguous=[True, True, True, True, True, True, True, False, False, False, False, False])
result = index.drop(index[0])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_timezones.py:71 | Complexity: Advanced | Last updated: 2026-06-02*