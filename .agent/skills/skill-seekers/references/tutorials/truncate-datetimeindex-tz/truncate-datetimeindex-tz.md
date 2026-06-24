# How To: Truncate Datetimeindex Tz

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test truncate datetimeindex tz

## Prerequisites

**Required Modules:**
- `datetime`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = date_range(...)

```python
idx = date_range('4/1/2005', '4/30/2005', freq='D', tz='US/Pacific')
```

### Step 2: Assign s = Series(...)

```python
s = Series(range(len(idx)), index=idx)
```

### Step 3: Assign lb = value

```python
lb = idx[1]
```

### Step 4: Assign ub = value

```python
ub = idx[3]
```

### Step 5: Assign result = s.truncate(...)

```python
result = s.truncate(lb.to_pydatetime(), ub.to_pydatetime())
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([1, 2, 3], index=idx[1:4])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Call s.truncate()

```python
s.truncate(datetime(2005, 4, 2), datetime(2005, 4, 4))
```


## Complete Example

```python
# Workflow
idx = date_range('4/1/2005', '4/30/2005', freq='D', tz='US/Pacific')
s = Series(range(len(idx)), index=idx)
with pytest.raises(TypeError, match='Cannot compare tz-naive'):
    s.truncate(datetime(2005, 4, 2), datetime(2005, 4, 4))
lb = idx[1]
ub = idx[3]
result = s.truncate(lb.to_pydatetime(), ub.to_pydatetime())
expected = Series([1, 2, 3], index=idx[1:4])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_truncate.py:14 | Complexity: Advanced | Last updated: 2026-06-02*