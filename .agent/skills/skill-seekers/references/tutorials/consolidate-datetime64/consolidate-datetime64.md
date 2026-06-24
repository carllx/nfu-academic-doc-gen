# How To: Consolidate Datetime64

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test consolidate datetime64

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.internals.blocks`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'starting': pd.to_datetime(['2012-06-21 00:00', '2012-06-23 07:00', '2012-06-23 16:30', '2012-06-25 08:00', '2012-06-26 12:00']), 'ending': pd.to_datetime(['2012-06-23 07:00', '2012-06-23 16:30', '2012-06-25 08:00', '2012-06-26 12:00', '2012-06-27 08:00']), 'measure': [77, 65, 77, 0, 77]})
```

### Step 2: Assign ser_starting = value

```python
ser_starting = df.starting
```

### Step 3: Assign ser_starting.index = value

```python
ser_starting.index = ser_starting.values
```

### Step 4: Assign ser_starting = ser_starting.tz_localize(...)

```python
ser_starting = ser_starting.tz_localize('US/Eastern')
```

### Step 5: Assign ser_starting = ser_starting.tz_convert(...)

```python
ser_starting = ser_starting.tz_convert('UTC')
```

### Step 6: Assign ser_starting.index.name = 'starting'

```python
ser_starting.index.name = 'starting'
```

### Step 7: Assign ser_ending = value

```python
ser_ending = df.ending
```

### Step 8: Assign ser_ending.index = value

```python
ser_ending.index = ser_ending.values
```

### Step 9: Assign ser_ending = ser_ending.tz_localize(...)

```python
ser_ending = ser_ending.tz_localize('US/Eastern')
```

### Step 10: Assign ser_ending = ser_ending.tz_convert(...)

```python
ser_ending = ser_ending.tz_convert('UTC')
```

### Step 11: Assign ser_ending.index.name = 'ending'

```python
ser_ending.index.name = 'ending'
```

### Step 12: Assign df.starting = value

```python
df.starting = ser_starting.index
```

### Step 13: Assign df.ending = value

```python
df.ending = ser_ending.index
```

### Step 14: Call tm.assert_index_equal()

```python
tm.assert_index_equal(pd.DatetimeIndex(df.starting), ser_starting.index)
```

### Step 15: Call tm.assert_index_equal()

```python
tm.assert_index_equal(pd.DatetimeIndex(df.ending), ser_ending.index)
```


## Complete Example

```python
# Workflow
df = DataFrame({'starting': pd.to_datetime(['2012-06-21 00:00', '2012-06-23 07:00', '2012-06-23 16:30', '2012-06-25 08:00', '2012-06-26 12:00']), 'ending': pd.to_datetime(['2012-06-23 07:00', '2012-06-23 16:30', '2012-06-25 08:00', '2012-06-26 12:00', '2012-06-27 08:00']), 'measure': [77, 65, 77, 0, 77]})
ser_starting = df.starting
ser_starting.index = ser_starting.values
ser_starting = ser_starting.tz_localize('US/Eastern')
ser_starting = ser_starting.tz_convert('UTC')
ser_starting.index.name = 'starting'
ser_ending = df.ending
ser_ending.index = ser_ending.values
ser_ending = ser_ending.tz_localize('US/Eastern')
ser_ending = ser_ending.tz_convert('UTC')
ser_ending.index.name = 'ending'
df.starting = ser_starting.index
df.ending = ser_ending.index
tm.assert_index_equal(pd.DatetimeIndex(df.starting), ser_starting.index)
tm.assert_index_equal(pd.DatetimeIndex(df.ending), ser_ending.index)
```

## Next Steps


---

*Source: test_block_internals.py:281 | Complexity: Advanced | Last updated: 2026-06-02*