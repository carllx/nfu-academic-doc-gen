# How To: To Timestamp Pi Combined

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to timestamp pi combined

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = period_range(...)

```python
idx = period_range(start='2011', periods=2, freq='1D1h', name='idx')
```

### Step 2: Assign result = idx.to_timestamp(...)

```python
result = idx.to_timestamp()
```

### Step 3: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex(['2011-01-01 00:00', '2011-01-02 01:00'], dtype='M8[ns]', name='idx')
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign result = idx.to_timestamp(...)

```python
result = idx.to_timestamp(how='E')
```

### Step 6: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex(['2011-01-02 00:59:59', '2011-01-03 01:59:59'], name='idx', dtype='M8[ns]')
```

### Step 7: Assign expected = value

```python
expected = expected + Timedelta(1, 's') - Timedelta(1, 'ns')
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 9: Assign result = idx.to_timestamp(...)

```python
result = idx.to_timestamp(how='E', freq='h')
```

### Step 10: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex(['2011-01-02 00:00', '2011-01-03 01:00'], dtype='M8[ns]', name='idx')
```

### Step 11: Assign expected = value

```python
expected = expected + Timedelta(1, 'h') - Timedelta(1, 'ns')
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx = period_range(start='2011', periods=2, freq='1D1h', name='idx')
result = idx.to_timestamp()
expected = DatetimeIndex(['2011-01-01 00:00', '2011-01-02 01:00'], dtype='M8[ns]', name='idx')
tm.assert_index_equal(result, expected)
result = idx.to_timestamp(how='E')
expected = DatetimeIndex(['2011-01-02 00:59:59', '2011-01-03 01:59:59'], name='idx', dtype='M8[ns]')
expected = expected + Timedelta(1, 's') - Timedelta(1, 'ns')
tm.assert_index_equal(result, expected)
result = idx.to_timestamp(how='E', freq='h')
expected = DatetimeIndex(['2011-01-02 00:00', '2011-01-03 01:00'], dtype='M8[ns]', name='idx')
expected = expected + Timedelta(1, 'h') - Timedelta(1, 'ns')
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_to_timestamp.py:115 | Complexity: Advanced | Last updated: 2026-06-02*