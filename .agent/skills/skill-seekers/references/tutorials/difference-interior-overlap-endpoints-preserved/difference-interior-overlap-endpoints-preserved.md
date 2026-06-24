# How To: Difference Interior Overlap Endpoints Preserved

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test difference interior overlap endpoints preserved

## Prerequisites

**Required Modules:**
- `datetime`
- `hypothesis`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign left = RangeIndex(...)

```python
left = RangeIndex(range(4))
```

**Verification:**
```python
assert expected.tolist() == [0, 3]
```

### Step 2: Assign right = RangeIndex(...)

```python
right = RangeIndex(range(1, 3))
```

### Step 3: Assign result = left.difference(...)

```python
result = left.difference(right)
```

### Step 4: Assign expected = RangeIndex(...)

```python
expected = RangeIndex(0, 4, 3)
```

**Verification:**
```python
assert expected.tolist() == [0, 3]
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```


## Complete Example

```python
# Workflow
left = RangeIndex(range(4))
right = RangeIndex(range(1, 3))
result = left.difference(right)
expected = RangeIndex(0, 4, 3)
assert expected.tolist() == [0, 3]
tm.assert_index_equal(result, expected, exact=True)
```

## Next Steps


---

*Source: test_setops.py:380 | Complexity: Intermediate | Last updated: 2026-06-02*