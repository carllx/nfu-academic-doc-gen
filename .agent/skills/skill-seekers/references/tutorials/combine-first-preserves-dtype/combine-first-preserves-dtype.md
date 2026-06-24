# How To: Combine First Preserves Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test combine first preserves dtype

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s1 = Series(...)

```python
s1 = Series([1666880195890293744, 1666880195890293837])
```

### Step 2: Assign s2 = Series(...)

```python
s2 = Series([1, 2, 3])
```

### Step 3: Assign result = s1.combine_first(...)

```python
result = s1.combine_first(s2)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([1666880195890293744, 1666880195890293837, 3])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
s1 = Series([1666880195890293744, 1666880195890293837])
s2 = Series([1, 2, 3])
result = s1.combine_first(s2)
expected = Series([1666880195890293744, 1666880195890293837, 3])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_combine_first.py:121 | Complexity: Intermediate | Last updated: 2026-06-02*