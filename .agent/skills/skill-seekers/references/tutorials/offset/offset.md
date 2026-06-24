# How To: Offset

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test offset

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil.relativedelta`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tests.tseries.offsets.common`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign offset = makeFY5253NearestEndMonthQuarter(...)

```python
offset = makeFY5253NearestEndMonthQuarter(1, startingMonth=8, weekday=WeekDay.THU, qtr_with_extra_week=4)
```

**Verification:**
```python
assert_offset_equal(offset, date, expected)
```

### Step 2: Assign MU = value

```python
MU = [datetime(2012, 5, 31), datetime(2012, 8, 30), datetime(2012, 11, 29), datetime(2013, 2, 28), datetime(2013, 5, 30)]
```

**Verification:**
```python
assert_offset_equal(offset, datetime(2012, 5, 31), datetime(2012, 8, 30))
```

### Step 3: Assign date = value

```python
date = MU[0] + relativedelta(days=-1)
```

**Verification:**
```python
assert_offset_equal(offset, datetime(2012, 5, 30), datetime(2012, 5, 31))
```

### Step 4: Call assert_offset_equal()

```python
assert_offset_equal(offset, datetime(2012, 5, 31), datetime(2012, 8, 30))
```

**Verification:**
```python
assert_offset_equal(offset2, datetime(2013, 1, 15), datetime(2013, 3, 30))
```

### Step 5: Call assert_offset_equal()

```python
assert_offset_equal(offset, datetime(2012, 5, 30), datetime(2012, 5, 31))
```

### Step 6: Assign offset2 = FY5253Quarter(...)

```python
offset2 = FY5253Quarter(weekday=5, startingMonth=12, variation='last', qtr_with_extra_week=4)
```

### Step 7: Call assert_offset_equal()

```python
assert_offset_equal(offset2, datetime(2013, 1, 15), datetime(2013, 3, 30))
```

### Step 8: Call assert_offset_equal()

```python
assert_offset_equal(offset, date, expected)
```

### Step 9: Assign date = value

```python
date = date + offset
```


## Complete Example

```python
# Workflow
offset = makeFY5253NearestEndMonthQuarter(1, startingMonth=8, weekday=WeekDay.THU, qtr_with_extra_week=4)
MU = [datetime(2012, 5, 31), datetime(2012, 8, 30), datetime(2012, 11, 29), datetime(2013, 2, 28), datetime(2013, 5, 30)]
date = MU[0] + relativedelta(days=-1)
for expected in MU:
    assert_offset_equal(offset, date, expected)
    date = date + offset
assert_offset_equal(offset, datetime(2012, 5, 31), datetime(2012, 8, 30))
assert_offset_equal(offset, datetime(2012, 5, 30), datetime(2012, 5, 31))
offset2 = FY5253Quarter(weekday=5, startingMonth=12, variation='last', qtr_with_extra_week=4)
assert_offset_equal(offset2, datetime(2013, 1, 15), datetime(2013, 3, 30))
```

## Next Steps


---

*Source: test_fiscal.py:571 | Complexity: Advanced | Last updated: 2026-06-02*