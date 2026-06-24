# How To: Assert Frame Equal Checking Allow Dups Flag

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test assert frame equal checking allow dups flag

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign left = DataFrame(...)

```python
left = DataFrame([[1, 2], [3, 4]])
```

### Step 2: Assign left.flags.allows_duplicate_labels = False

```python
left.flags.allows_duplicate_labels = False
```

### Step 3: Assign right = DataFrame(...)

```python
right = DataFrame([[1, 2], [3, 4]])
```

### Step 4: Assign right.flags.allows_duplicate_labels = True

```python
right.flags.allows_duplicate_labels = True
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(left, right, check_flags=False)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(left, right, check_flags=True)
```


## Complete Example

```python
# Workflow
left = DataFrame([[1, 2], [3, 4]])
left.flags.allows_duplicate_labels = False
right = DataFrame([[1, 2], [3, 4]])
right.flags.allows_duplicate_labels = True
tm.assert_frame_equal(left, right, check_flags=False)
with pytest.raises(AssertionError, match='allows_duplicate_labels'):
    tm.assert_frame_equal(left, right, check_flags=True)
```

## Next Steps


---

*Source: test_assert_frame_equal.py:310 | Complexity: Intermediate | Last updated: 2026-06-02*