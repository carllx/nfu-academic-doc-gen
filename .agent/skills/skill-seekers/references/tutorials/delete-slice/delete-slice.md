# How To: Delete Slice

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test delete slice

## Prerequisites

**Required Modules:**
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = timedelta_range(...)

```python
idx = timedelta_range(start='1 days', periods=10, freq='D', name='idx')
```

**Verification:**
```python
assert result.name == expected.name
```

### Step 2: Assign expected_0_2 = timedelta_range(...)

```python
expected_0_2 = timedelta_range(start='4 days', periods=7, freq='D', name='idx')
```

**Verification:**
```python
assert result.freq == expected.freq
```

### Step 3: Assign expected_7_9 = timedelta_range(...)

```python
expected_7_9 = timedelta_range(start='1 days', periods=7, freq='D', name='idx')
```

**Verification:**
```python
assert result.name == expected.name
```

### Step 4: Assign expected_3_5 = TimedeltaIndex(...)

```python
expected_3_5 = TimedeltaIndex(['1 d', '2 d', '3 d', '7 d', '8 d', '9 d', '10d'], freq=None, name='idx')
```

**Verification:**
```python
assert result.freq == expected.freq
```

### Step 5: Assign cases = value

```python
cases = {(0, 1, 2): expected_0_2, (7, 8, 9): expected_7_9, (3, 4, 5): expected_3_5}
```

### Step 6: Assign result = idx.delete(...)

```python
result = idx.delete(n)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

**Verification:**
```python
assert result.name == expected.name
```

### Step 8: Assign result = idx.delete(...)

```python
result = idx.delete(slice(n[0], n[-1] + 1))
```

### Step 9: Call tm.assert_index_equal()

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
idx = timedelta_range(start='1 days', periods=10, freq='D', name='idx')
expected_0_2 = timedelta_range(start='4 days', periods=7, freq='D', name='idx')
expected_7_9 = timedelta_range(start='1 days', periods=7, freq='D', name='idx')
expected_3_5 = TimedeltaIndex(['1 d', '2 d', '3 d', '7 d', '8 d', '9 d', '10d'], freq=None, name='idx')
cases = {(0, 1, 2): expected_0_2, (7, 8, 9): expected_7_9, (3, 4, 5): expected_3_5}
for n, expected in cases.items():
    result = idx.delete(n)
    tm.assert_index_equal(result, expected)
    assert result.name == expected.name
    assert result.freq == expected.freq
    result = idx.delete(slice(n[0], n[-1] + 1))
    tm.assert_index_equal(result, expected)
    assert result.name == expected.name
    assert result.freq == expected.freq
```

## Next Steps


---

*Source: test_delete.py:38 | Complexity: Advanced | Last updated: 2026-06-02*