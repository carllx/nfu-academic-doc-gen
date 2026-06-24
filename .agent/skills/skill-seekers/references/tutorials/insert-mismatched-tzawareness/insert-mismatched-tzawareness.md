# How To: Insert Mismatched Tzawareness

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test insert mismatched tzawareness

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

### Step 2: Assign item = Timestamp(...)

```python
item = Timestamp('2000-01-04')
```

### Step 3: Assign result = idx.insert(...)

```python
result = idx.insert(3, item)
```

### Step 4: Assign expected = Index(...)

```python
expected = Index(list(idx[:3]) + [item] + list(idx[3:]), dtype=object, name='idx')
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 6: Assign item = datetime(...)

```python
item = datetime(2000, 1, 4)
```

### Step 7: Assign result = idx.insert(...)

```python
result = idx.insert(3, item)
```

### Step 8: Assign expected = Index(...)

```python
expected = Index(list(idx[:3]) + [item] + list(idx[3:]), dtype=object, name='idx')
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx = date_range('1/1/2000', periods=3, freq='D', tz='Asia/Tokyo', name='idx')
item = Timestamp('2000-01-04')
result = idx.insert(3, item)
expected = Index(list(idx[:3]) + [item] + list(idx[3:]), dtype=object, name='idx')
tm.assert_index_equal(result, expected)
item = datetime(2000, 1, 4)
result = idx.insert(3, item)
expected = Index(list(idx[:3]) + [item] + list(idx[3:]), dtype=object, name='idx')
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_insert.py:181 | Complexity: Advanced | Last updated: 2026-06-02*