# How To: Shift Corner Cases

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test shift corner cases

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = PeriodIndex(...)

```python
idx = PeriodIndex([], name='xxx', freq='h')
```

### Step 2: Assign msg = '`freq` argument is not supported for PeriodIndex.shift'

```python
msg = '`freq` argument is not supported for PeriodIndex.shift'
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.shift(0), idx)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.shift(3), idx)
```

### Step 5: Assign idx = PeriodIndex(...)

```python
idx = PeriodIndex(['2011-01-01 10:00', '2011-01-01 11:00', '2011-01-01 12:00'], name='xxx', freq='h')
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.shift(0), idx)
```

### Step 7: Assign exp = PeriodIndex(...)

```python
exp = PeriodIndex(['2011-01-01 13:00', '2011-01-01 14:00', '2011-01-01 15:00'], name='xxx', freq='h')
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.shift(3), exp)
```

### Step 9: Assign exp = PeriodIndex(...)

```python
exp = PeriodIndex(['2011-01-01 07:00', '2011-01-01 08:00', '2011-01-01 09:00'], name='xxx', freq='h')
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.shift(-3), exp)
```

### Step 11: Call idx.shift()

```python
idx.shift(1, freq='h')
```


## Complete Example

```python
# Workflow
idx = PeriodIndex([], name='xxx', freq='h')
msg = '`freq` argument is not supported for PeriodIndex.shift'
with pytest.raises(TypeError, match=msg):
    idx.shift(1, freq='h')
tm.assert_index_equal(idx.shift(0), idx)
tm.assert_index_equal(idx.shift(3), idx)
idx = PeriodIndex(['2011-01-01 10:00', '2011-01-01 11:00', '2011-01-01 12:00'], name='xxx', freq='h')
tm.assert_index_equal(idx.shift(0), idx)
exp = PeriodIndex(['2011-01-01 13:00', '2011-01-01 14:00', '2011-01-01 15:00'], name='xxx', freq='h')
tm.assert_index_equal(idx.shift(3), exp)
exp = PeriodIndex(['2011-01-01 07:00', '2011-01-01 08:00', '2011-01-01 09:00'], name='xxx', freq='h')
tm.assert_index_equal(idx.shift(-3), exp)
```

## Next Steps


---

*Source: test_shift.py:65 | Complexity: Advanced | Last updated: 2026-06-02*