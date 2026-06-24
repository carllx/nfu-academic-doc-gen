# How To: Insert

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test insert

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = TimedeltaIndex(...)

```python
idx = TimedeltaIndex(['4day', '1day', '2day'], name='idx')
```

**Verification:**
```python
assert not isinstance(result, TimedeltaIndex)
```

### Step 2: Assign result = idx.insert(...)

```python
result = idx.insert(2, timedelta(days=5))
```

**Verification:**
```python
assert result.name == expected.name
```

### Step 3: Assign exp = TimedeltaIndex(...)

```python
exp = TimedeltaIndex(['4day', '1day', '5day', '2day'], name='idx')
```

**Verification:**
```python
assert result.name == expected.name
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp)
```

**Verification:**
```python
assert result.freq == expected.freq
```

### Step 5: Assign result = idx.insert(...)

```python
result = idx.insert(1, 'inserted')
```

### Step 6: Assign expected = Index(...)

```python
expected = Index([Timedelta('4day'), 'inserted', Timedelta('1day'), Timedelta('2day')], name='idx')
```

**Verification:**
```python
assert not isinstance(result, TimedeltaIndex)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

**Verification:**
```python
assert result.name == expected.name
```

### Step 8: Assign idx = timedelta_range(...)

```python
idx = timedelta_range('1day 00:00:01', periods=3, freq='s', name='idx')
```

### Step 9: Assign expected_0 = TimedeltaIndex(...)

```python
expected_0 = TimedeltaIndex(['1day', '1day 00:00:01', '1day 00:00:02', '1day 00:00:03'], name='idx', freq='s')
```

### Step 10: Assign expected_3 = TimedeltaIndex(...)

```python
expected_3 = TimedeltaIndex(['1day 00:00:01', '1day 00:00:02', '1day 00:00:03', '1day 00:00:04'], name='idx', freq='s')
```

### Step 11: Assign expected_1_nofreq = TimedeltaIndex(...)

```python
expected_1_nofreq = TimedeltaIndex(['1day 00:00:01', '1day 00:00:01', '1day 00:00:02', '1day 00:00:03'], name='idx', freq=None)
```

### Step 12: Assign expected_3_nofreq = TimedeltaIndex(...)

```python
expected_3_nofreq = TimedeltaIndex(['1day 00:00:01', '1day 00:00:02', '1day 00:00:03', '1day 00:00:05'], name='idx', freq=None)
```

### Step 13: Assign cases = value

```python
cases = [(0, Timedelta('1day'), expected_0), (-3, Timedelta('1day'), expected_0), (3, Timedelta('1day 00:00:04'), expected_3), (1, Timedelta('1day 00:00:01'), expected_1_nofreq), (3, Timedelta('1day 00:00:05'), expected_3_nofreq)]
```

### Step 14: Assign result = idx.insert(...)

```python
result = idx.insert(n, d)
```

### Step 15: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

**Verification:**
```python
assert result.name == expected.name
```


## Complete Example

```python
# Workflow
idx = TimedeltaIndex(['4day', '1day', '2day'], name='idx')
result = idx.insert(2, timedelta(days=5))
exp = TimedeltaIndex(['4day', '1day', '5day', '2day'], name='idx')
tm.assert_index_equal(result, exp)
result = idx.insert(1, 'inserted')
expected = Index([Timedelta('4day'), 'inserted', Timedelta('1day'), Timedelta('2day')], name='idx')
assert not isinstance(result, TimedeltaIndex)
tm.assert_index_equal(result, expected)
assert result.name == expected.name
idx = timedelta_range('1day 00:00:01', periods=3, freq='s', name='idx')
expected_0 = TimedeltaIndex(['1day', '1day 00:00:01', '1day 00:00:02', '1day 00:00:03'], name='idx', freq='s')
expected_3 = TimedeltaIndex(['1day 00:00:01', '1day 00:00:02', '1day 00:00:03', '1day 00:00:04'], name='idx', freq='s')
expected_1_nofreq = TimedeltaIndex(['1day 00:00:01', '1day 00:00:01', '1day 00:00:02', '1day 00:00:03'], name='idx', freq=None)
expected_3_nofreq = TimedeltaIndex(['1day 00:00:01', '1day 00:00:02', '1day 00:00:03', '1day 00:00:05'], name='idx', freq=None)
cases = [(0, Timedelta('1day'), expected_0), (-3, Timedelta('1day'), expected_0), (3, Timedelta('1day 00:00:04'), expected_3), (1, Timedelta('1day 00:00:01'), expected_1_nofreq), (3, Timedelta('1day 00:00:05'), expected_3_nofreq)]
for n, d, expected in cases:
    result = idx.insert(n, d)
    tm.assert_index_equal(result, expected)
    assert result.name == expected.name
    assert result.freq == expected.freq
```

## Next Steps


---

*Source: test_insert.py:19 | Complexity: Advanced | Last updated: 2026-06-02*