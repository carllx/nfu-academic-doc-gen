# How To: Range Difference

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test range difference

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `hypothesis`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: start1, stop1, step1, start2, stop2, step2
```

## Step-by-Step Guide

### Step 1: Call assume()

```python
assume(step1 != 0)
```

**Verification:**
```python
assert_range_or_not_is_rangelike(result)
```

### Step 2: Call assume()

```python
assume(step2 != 0)
```

**Verification:**
```python
assert_range_or_not_is_rangelike(result)
```

### Step 3: Assign left = RangeIndex(...)

```python
left = RangeIndex(start1, stop1, step1)
```

### Step 4: Assign right = RangeIndex(...)

```python
right = RangeIndex(start2, stop2, step2)
```

### Step 5: Assign result = left.difference(...)

```python
result = left.difference(right, sort=None)
```

### Step 6: Call assert_range_or_not_is_rangelike()

```python
assert_range_or_not_is_rangelike(result)
```

### Step 7: Assign left_int64 = Index(...)

```python
left_int64 = Index(left.to_numpy())
```

### Step 8: Assign right_int64 = Index(...)

```python
right_int64 = Index(right.to_numpy())
```

### Step 9: Assign alt = left_int64.difference(...)

```python
alt = left_int64.difference(right_int64, sort=None)
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, alt, exact='equiv')
```

### Step 11: Assign result = left.difference(...)

```python
result = left.difference(right, sort=False)
```

### Step 12: Call assert_range_or_not_is_rangelike()

```python
assert_range_or_not_is_rangelike(result)
```

### Step 13: Assign alt = left_int64.difference(...)

```python
alt = left_int64.difference(right_int64, sort=False)
```

### Step 14: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, alt, exact='equiv')
```


## Complete Example

```python
# Setup
# Fixtures: start1, stop1, step1, start2, stop2, step2

# Workflow
assume(step1 != 0)
assume(step2 != 0)
left = RangeIndex(start1, stop1, step1)
right = RangeIndex(start2, stop2, step2)
result = left.difference(right, sort=None)
assert_range_or_not_is_rangelike(result)
left_int64 = Index(left.to_numpy())
right_int64 = Index(right.to_numpy())
alt = left_int64.difference(right_int64, sort=None)
tm.assert_index_equal(result, alt, exact='equiv')
result = left.difference(right, sort=False)
assert_range_or_not_is_rangelike(result)
alt = left_int64.difference(right_int64, sort=False)
tm.assert_index_equal(result, alt, exact='equiv')
```

## Next Steps


---

*Source: test_setops.py:470 | Complexity: Advanced | Last updated: 2026-06-02*