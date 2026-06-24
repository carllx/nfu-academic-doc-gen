# How To: Astype Object Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test astype object tz

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `dateutil`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz
```

## Step-by-Step Guide

### Step 1: Assign idx = date_range(...)

```python
idx = date_range(start='2013-01-01', periods=4, freq='ME', name='idx', tz=tz)
```

**Verification:**
```python
assert idx.tolist() == expected_list
```

### Step 2: Assign expected_list = value

```python
expected_list = [Timestamp('2013-01-31', tz=tz), Timestamp('2013-02-28', tz=tz), Timestamp('2013-03-31', tz=tz), Timestamp('2013-04-30', tz=tz)]
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
# Setup
# Fixtures: tz

# Workflow
idx = date_range(start='2013-01-01', periods=4, freq='ME', name='idx', tz=tz)
expected_list = [Timestamp('2013-01-31', tz=tz), Timestamp('2013-02-28', tz=tz), Timestamp('2013-03-31', tz=tz), Timestamp('2013-04-30', tz=tz)]
expected = Index(expected_list, dtype=object, name='idx')
result = idx.astype(object)
tm.assert_index_equal(result, expected)
assert idx.tolist() == expected_list
```

## Next Steps


---

*Source: test_astype.py:197 | Complexity: Intermediate | Last updated: 2026-06-02*