# How To: Constructor Range

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor range

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign result = RangeIndex.from_range(...)

```python
result = RangeIndex.from_range(range(1, 5, 2))
```

### Step 2: Assign expected = RangeIndex(...)

```python
expected = RangeIndex(1, 5, 2)
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```

### Step 4: Assign result = RangeIndex.from_range(...)

```python
result = RangeIndex.from_range(range(5, 6))
```

### Step 5: Assign expected = RangeIndex(...)

```python
expected = RangeIndex(5, 6, 1)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```

### Step 7: Assign result = RangeIndex.from_range(...)

```python
result = RangeIndex.from_range(range(5, 1))
```

### Step 8: Assign expected = RangeIndex(...)

```python
expected = RangeIndex(0, 0, 1)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```

### Step 10: Assign result = RangeIndex.from_range(...)

```python
result = RangeIndex.from_range(range(5))
```

### Step 11: Assign expected = RangeIndex(...)

```python
expected = RangeIndex(0, 5, 1)
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```

### Step 13: Assign result = Index(...)

```python
result = Index(range(1, 5, 2))
```

### Step 14: Assign expected = RangeIndex(...)

```python
expected = RangeIndex(1, 5, 2)
```

### Step 15: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```

### Step 16: Assign msg = "(RangeIndex.)?from_range\\(\\) got an unexpected keyword argument( 'copy')?"

```python
msg = "(RangeIndex.)?from_range\\(\\) got an unexpected keyword argument( 'copy')?"
```

### Step 17: Call RangeIndex.from_range()

```python
RangeIndex.from_range(range(10), copy=True)
```


## Complete Example

```python
# Workflow
result = RangeIndex.from_range(range(1, 5, 2))
expected = RangeIndex(1, 5, 2)
tm.assert_index_equal(result, expected, exact=True)
result = RangeIndex.from_range(range(5, 6))
expected = RangeIndex(5, 6, 1)
tm.assert_index_equal(result, expected, exact=True)
result = RangeIndex.from_range(range(5, 1))
expected = RangeIndex(0, 0, 1)
tm.assert_index_equal(result, expected, exact=True)
result = RangeIndex.from_range(range(5))
expected = RangeIndex(0, 5, 1)
tm.assert_index_equal(result, expected, exact=True)
result = Index(range(1, 5, 2))
expected = RangeIndex(1, 5, 2)
tm.assert_index_equal(result, expected, exact=True)
msg = "(RangeIndex.)?from_range\\(\\) got an unexpected keyword argument( 'copy')?"
with pytest.raises(TypeError, match=msg):
    RangeIndex.from_range(range(10), copy=True)
```

## Next Steps


---

*Source: test_constructors.py:98 | Complexity: Advanced | Last updated: 2026-06-02*