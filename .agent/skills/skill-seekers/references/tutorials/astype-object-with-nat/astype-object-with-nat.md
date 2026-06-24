# How To: Astype Object With Nat

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype object with nat

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = DatetimeIndex(...)

```python
idx = DatetimeIndex([datetime(2013, 1, 1), datetime(2013, 1, 2), NaT, datetime(2013, 1, 4)], name='idx')
```

**Verification:**
```python
assert idx.tolist() == expected_list
```

### Step 2: Assign expected_list = value

```python
expected_list = [Timestamp('2013-01-01'), Timestamp('2013-01-02'), NaT, Timestamp('2013-01-04')]
```

### Step 3: Assign expected = Index(...)

```python
expected = Index(expected_list, dtype=object, name='idx')
```

### Step 4: Assign result = idx.astype(...)

```python
result = idx.astype(object)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

**Verification:**
```python
assert idx.tolist() == expected_list
```


## Complete Example

```python
# Workflow
idx = DatetimeIndex([datetime(2013, 1, 1), datetime(2013, 1, 2), NaT, datetime(2013, 1, 4)], name='idx')
expected_list = [Timestamp('2013-01-01'), Timestamp('2013-01-02'), NaT, Timestamp('2013-01-04')]
expected = Index(expected_list, dtype=object, name='idx')
result = idx.astype(object)
tm.assert_index_equal(result, expected)
assert idx.tolist() == expected_list
```

## Next Steps


---

*Source: test_astype.py:210 | Complexity: Intermediate | Last updated: 2026-06-02*