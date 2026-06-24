# How To: Delete

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test delete

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = RangeIndex(...)

```python
idx = RangeIndex(5, name='Foo')
```

**Verification:**
```python
assert result.name == expected.name
```

### Step 2: Assign expected = value

```python
expected = idx[1:]
```

**Verification:**
```python
assert result.name == expected.name
```

### Step 3: Assign result = idx.delete(...)

```python
result = idx.delete(0)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```

**Verification:**
```python
assert result.name == expected.name
```

### Step 5: Assign expected = value

```python
expected = idx[:-1]
```

### Step 6: Assign result = idx.delete(...)

```python
result = idx.delete(-1)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```

**Verification:**
```python
assert result.name == expected.name
```

### Step 8: Assign msg = 'index 5 is out of bounds for axis 0 with size 5'

```python
msg = 'index 5 is out of bounds for axis 0 with size 5'
```

### Step 9: Assign result = idx.delete(...)

```python
result = idx.delete(len(idx))
```


## Complete Example

```python
# Workflow
idx = RangeIndex(5, name='Foo')
expected = idx[1:]
result = idx.delete(0)
tm.assert_index_equal(result, expected, exact=True)
assert result.name == expected.name
expected = idx[:-1]
result = idx.delete(-1)
tm.assert_index_equal(result, expected, exact=True)
assert result.name == expected.name
msg = 'index 5 is out of bounds for axis 0 with size 5'
with pytest.raises((IndexError, ValueError), match=msg):
    result = idx.delete(len(idx))
```

## Next Steps


---

*Source: test_range.py:114 | Complexity: Advanced | Last updated: 2026-06-02*