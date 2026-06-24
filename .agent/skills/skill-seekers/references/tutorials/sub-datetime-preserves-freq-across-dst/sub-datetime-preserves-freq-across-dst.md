# How To: Sub Datetime Preserves Freq Across Dst

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test sub datetime preserves freq across dst

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ts = Timestamp(...)

```python
ts = Timestamp('2016-03-11', tz='US/Pacific')
```

**Verification:**
```python
assert res.freq == expected.freq
```

### Step 2: Assign dti = date_range(...)

```python
dti = date_range(ts, periods=4)
```

### Step 3: Assign res = value

```python
res = dti - dti[0]
```

### Step 4: Assign expected = TimedeltaIndex(...)

```python
expected = TimedeltaIndex([Timedelta(days=0), Timedelta(days=1), Timedelta(days=2), Timedelta(days=2, hours=23)])
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, expected)
```

**Verification:**
```python
assert res.freq == expected.freq
```


## Complete Example

```python
# Workflow
ts = Timestamp('2016-03-11', tz='US/Pacific')
dti = date_range(ts, periods=4)
res = dti - dti[0]
expected = TimedeltaIndex([Timedelta(days=0), Timedelta(days=1), Timedelta(days=2), Timedelta(days=2, hours=23)])
tm.assert_index_equal(res, expected)
assert res.freq == expected.freq
```

## Next Steps


---

*Source: test_arithmetic.py:41 | Complexity: Intermediate | Last updated: 2026-06-02*