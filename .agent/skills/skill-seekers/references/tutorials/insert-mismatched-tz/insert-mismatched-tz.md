# How To: Insert Mismatched Tz

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test insert mismatched tz

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = date_range(...)

```python
idx = date_range('1/1/2000', periods=3, freq='D', tz='Asia/Tokyo', name='idx')
```

**Verification:**
```python
assert expected.dtype == idx.dtype
```

### Step 2: Assign item = Timestamp(...)

```python
item = Timestamp('2000-01-04', tz='US/Eastern')
```

**Verification:**
```python
assert expected.dtype == idx.dtype
```

### Step 3: Assign result = idx.insert(...)

```python
result = idx.insert(3, item)
```

### Step 4: Assign expected = Index(...)

```python
expected = Index(list(idx[:3]) + [item.tz_convert(idx.tz)] + list(idx[3:]), name='idx')
```

**Verification:**
```python
assert expected.dtype == idx.dtype
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 6: Assign item = datetime(...)

```python
item = datetime(2000, 1, 4, tzinfo=pytz.timezone('US/Eastern'))
```

### Step 7: Assign result = idx.insert(...)

```python
result = idx.insert(3, item)
```

### Step 8: Assign expected = Index(...)

```python
expected = Index(list(idx[:3]) + [item.astimezone(idx.tzinfo)] + list(idx[3:]), name='idx')
```

**Verification:**
```python
assert expected.dtype == idx.dtype
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx = date_range('1/1/2000', periods=3, freq='D', tz='Asia/Tokyo', name='idx')
item = Timestamp('2000-01-04', tz='US/Eastern')
result = idx.insert(3, item)
expected = Index(list(idx[:3]) + [item.tz_convert(idx.tz)] + list(idx[3:]), name='idx')
assert expected.dtype == idx.dtype
tm.assert_index_equal(result, expected)
item = datetime(2000, 1, 4, tzinfo=pytz.timezone('US/Eastern'))
result = idx.insert(3, item)
expected = Index(list(idx[:3]) + [item.astimezone(idx.tzinfo)] + list(idx[3:]), name='idx')
assert expected.dtype == idx.dtype
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_insert.py:202 | Complexity: Advanced | Last updated: 2026-06-02*