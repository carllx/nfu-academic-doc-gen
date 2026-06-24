# How To: Add Bday Offset Nanos

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test add bday offset nanos

## Prerequisites

**Required Modules:**
- `__future__`
- `datetime`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas`
- `pandas.tests.tseries.offsets.common`


## Step-by-Step Guide

### Step 1: Assign idx = date_range(...)

```python
idx = date_range('2010/02/01', '2010/02/10', freq='12h', unit='ns')
```

### Step 2: Assign off = BDay(...)

```python
off = BDay(offset=Timedelta(3, unit='ns'))
```

### Step 3: Assign result = value

```python
result = idx + off
```

### Step 4: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex([x + off for x in idx])
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx = date_range('2010/02/01', '2010/02/10', freq='12h', unit='ns')
off = BDay(offset=Timedelta(3, unit='ns'))
result = idx + off
expected = DatetimeIndex([x + off for x in idx])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_business_hour.py:990 | Complexity: Intermediate | Last updated: 2026-06-02*