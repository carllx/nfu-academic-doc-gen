# How To: Constructor

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test constructor

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.timedeltas`


## Step-by-Step Guide

### Step 1: Assign expected = TimedeltaIndex(...)

```python
expected = TimedeltaIndex(['1 days', '1 days 00:00:05', '2 days', '2 days 00:00:02', '0 days 00:00:03'])
```

### Step 2: Assign result = TimedeltaIndex(...)

```python
result = TimedeltaIndex(['1 days', '1 days, 00:00:05', np.timedelta64(2, 'D'), timedelta(days=2, seconds=2), pd.offsets.Second(3)])
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 4: Assign expected = TimedeltaIndex(...)

```python
expected = TimedeltaIndex(['0 days 00:00:00', '0 days 00:00:01', '0 days 00:00:02'])
```

### Step 5: Assign result = TimedeltaIndex(...)

```python
result = TimedeltaIndex(range(3), unit='s')
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 7: Assign expected = TimedeltaIndex(...)

```python
expected = TimedeltaIndex(['0 days 00:00:00', '0 days 00:00:05', '0 days 00:00:09'])
```

### Step 8: Assign result = TimedeltaIndex(...)

```python
result = TimedeltaIndex([0, 5, 9], unit='s')
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 10: Assign expected = TimedeltaIndex(...)

```python
expected = TimedeltaIndex(['0 days 00:00:00.400', '0 days 00:00:00.450', '0 days 00:00:01.200'])
```

### Step 11: Assign result = TimedeltaIndex(...)

```python
result = TimedeltaIndex([400, 450, 1200], unit='ms')
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
expected = TimedeltaIndex(['1 days', '1 days 00:00:05', '2 days', '2 days 00:00:02', '0 days 00:00:03'])
result = TimedeltaIndex(['1 days', '1 days, 00:00:05', np.timedelta64(2, 'D'), timedelta(days=2, seconds=2), pd.offsets.Second(3)])
tm.assert_index_equal(result, expected)
expected = TimedeltaIndex(['0 days 00:00:00', '0 days 00:00:01', '0 days 00:00:02'])
result = TimedeltaIndex(range(3), unit='s')
tm.assert_index_equal(result, expected)
expected = TimedeltaIndex(['0 days 00:00:00', '0 days 00:00:05', '0 days 00:00:09'])
result = TimedeltaIndex([0, 5, 9], unit='s')
tm.assert_index_equal(result, expected)
expected = TimedeltaIndex(['0 days 00:00:00.400', '0 days 00:00:00.450', '0 days 00:00:01.200'])
result = TimedeltaIndex([400, 450, 1200], unit='ms')
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_constructors.py:144 | Complexity: Advanced | Last updated: 2026-06-02*