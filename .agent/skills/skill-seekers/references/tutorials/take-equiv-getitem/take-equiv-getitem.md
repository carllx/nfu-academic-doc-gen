# How To: Take Equiv Getitem

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test take equiv getitem

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign tds = value

```python
tds = ['1day 02:00:00', '1 day 04:00:00', '1 day 10:00:00']
```

**Verification:**
```python
assert isinstance(taken, TimedeltaIndex)
```

### Step 2: Assign idx = timedelta_range(...)

```python
idx = timedelta_range(start='1d', end='2d', freq='h', name='idx')
```

**Verification:**
```python
assert taken.freq is None
```

### Step 3: Assign expected = TimedeltaIndex(...)

```python
expected = TimedeltaIndex(tds, freq=None, name='idx')
```

**Verification:**
```python
assert taken.name == expected.name
```

### Step 4: Assign taken1 = idx.take(...)

```python
taken1 = idx.take([2, 4, 10])
```

### Step 5: Assign taken2 = value

```python
taken2 = idx[[2, 4, 10]]
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(taken, expected)
```

**Verification:**
```python
assert isinstance(taken, TimedeltaIndex)
```


## Complete Example

```python
# Workflow
tds = ['1day 02:00:00', '1 day 04:00:00', '1 day 10:00:00']
idx = timedelta_range(start='1d', end='2d', freq='h', name='idx')
expected = TimedeltaIndex(tds, freq=None, name='idx')
taken1 = idx.take([2, 4, 10])
taken2 = idx[[2, 4, 10]]
for taken in [taken1, taken2]:
    tm.assert_index_equal(taken, expected)
    assert isinstance(taken, TimedeltaIndex)
    assert taken.freq is None
    assert taken.name == expected.name
```

## Next Steps


---

*Source: test_indexing.py:231 | Complexity: Intermediate | Last updated: 2026-06-02*