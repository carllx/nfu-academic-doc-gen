# How To: Difference Mismatched Step

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test difference mismatched step

## Prerequisites

**Required Modules:**
- `datetime`
- `hypothesis`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign obj = RangeIndex.from_range(...)

```python
obj = RangeIndex.from_range(range(1, 10), name='foo')
```

### Step 2: Assign result = obj.difference(...)

```python
result = obj.difference(obj[::2])
```

### Step 3: Assign expected = value

```python
expected = obj[1::2]
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```

### Step 5: Assign result = unknown.difference(...)

```python
result = obj[::-1].difference(obj[::2], sort=False)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected[::-1], exact=True)
```

### Step 7: Assign result = obj.difference(...)

```python
result = obj.difference(obj[1::2])
```

### Step 8: Assign expected = value

```python
expected = obj[::2]
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```

### Step 10: Assign result = unknown.difference(...)

```python
result = obj[::-1].difference(obj[1::2], sort=False)
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected[::-1], exact=True)
```


## Complete Example

```python
# Workflow
obj = RangeIndex.from_range(range(1, 10), name='foo')
result = obj.difference(obj[::2])
expected = obj[1::2]
tm.assert_index_equal(result, expected, exact=True)
result = obj[::-1].difference(obj[::2], sort=False)
tm.assert_index_equal(result, expected[::-1], exact=True)
result = obj.difference(obj[1::2])
expected = obj[::2]
tm.assert_index_equal(result, expected, exact=True)
result = obj[::-1].difference(obj[1::2], sort=False)
tm.assert_index_equal(result, expected[::-1], exact=True)
```

## Next Steps


---

*Source: test_setops.py:363 | Complexity: Advanced | Last updated: 2026-06-02*