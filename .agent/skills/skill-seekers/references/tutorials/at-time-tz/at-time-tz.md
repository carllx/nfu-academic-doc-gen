# How To: At Time Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test at time tz

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2018', periods=3, freq='h', tz='US/Pacific')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(list(range(len(dti))), index=dti)
```

### Step 3: Assign result = df.at_time(...)

```python
result = df.at_time(time(4, tzinfo=pytz.timezone('US/Eastern')))
```

### Step 4: Assign expected = value

```python
expected = df.iloc[1:2]
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
dti = date_range('2018', periods=3, freq='h', tz='US/Pacific')
df = DataFrame(list(range(len(dti))), index=dti)
result = df.at_time(time(4, tzinfo=pytz.timezone('US/Eastern')))
expected = df.iloc[1:2]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_at_time.py:82 | Complexity: Intermediate | Last updated: 2026-06-02*