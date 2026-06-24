# How To: Combine First Timezone Series With Empty Series

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test combine first timezone series with empty series

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign time_index = date_range(...)

```python
time_index = date_range(datetime(2021, 1, 1, 1), datetime(2021, 1, 1, 10), freq='h', tz='Europe/Rome')
```

### Step 2: Assign s1 = Series(...)

```python
s1 = Series(range(10), index=time_index)
```

### Step 3: Assign s2 = Series(...)

```python
s2 = Series(index=time_index)
```

### Step 4: Assign msg = 'The behavior of array concatenation with empty entries is deprecated'

```python
msg = 'The behavior of array concatenation with empty entries is deprecated'
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, s1)
```

### Step 6: Assign result = s1.combine_first(...)

```python
result = s1.combine_first(s2)
```


## Complete Example

```python
# Workflow
time_index = date_range(datetime(2021, 1, 1, 1), datetime(2021, 1, 1, 10), freq='h', tz='Europe/Rome')
s1 = Series(range(10), index=time_index)
s2 = Series(index=time_index)
msg = 'The behavior of array concatenation with empty entries is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = s1.combine_first(s2)
tm.assert_series_equal(result, s1)
```

## Next Steps


---

*Source: test_combine_first.py:106 | Complexity: Intermediate | Last updated: 2026-06-02*