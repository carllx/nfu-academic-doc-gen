# How To: Difference Sort

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test difference sort

## Prerequisites

**Required Modules:**
- `datetime`
- `hypothesis`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = value

```python
idx = Index(range(4))[::-1]
```

### Step 2: Assign other = Index(...)

```python
other = Index(range(3, 4))
```

### Step 3: Assign result = idx.difference(...)

```python
result = idx.difference(other)
```

### Step 4: Assign expected = Index(...)

```python
expected = Index(range(3))
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```

### Step 6: Assign result = idx.difference(...)

```python
result = idx.difference(other, sort=False)
```

### Step 7: Assign expected = value

```python
expected = expected[::-1]
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```

### Step 9: Assign other = range(...)

```python
other = range(10, 12)
```

### Step 10: Assign result = idx.difference(...)

```python
result = idx.difference(other, sort=None)
```

### Step 11: Assign expected = value

```python
expected = idx[::-1]
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```


## Complete Example

```python
# Workflow
idx = Index(range(4))[::-1]
other = Index(range(3, 4))
result = idx.difference(other)
expected = Index(range(3))
tm.assert_index_equal(result, expected, exact=True)
result = idx.difference(other, sort=False)
expected = expected[::-1]
tm.assert_index_equal(result, expected, exact=True)
other = range(10, 12)
result = idx.difference(other, sort=None)
expected = idx[::-1]
tm.assert_index_equal(result, expected, exact=True)
```

## Next Steps


---

*Source: test_setops.py:343 | Complexity: Advanced | Last updated: 2026-06-02*