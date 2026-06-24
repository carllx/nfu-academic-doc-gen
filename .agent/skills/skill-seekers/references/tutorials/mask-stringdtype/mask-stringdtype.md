# How To: Mask Stringdtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mask stringdtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign obj = DataFrame(...)

```python
obj = DataFrame({'A': ['foo', 'bar', 'baz', NA]}, index=['id1', 'id2', 'id3', 'id4'], dtype=StringDtype())
```

### Step 2: Assign filtered_obj = DataFrame(...)

```python
filtered_obj = DataFrame({'A': ['this', 'that']}, index=['id2', 'id3'], dtype=StringDtype())
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [NA, 'this', 'that', NA]}, index=['id1', 'id2', 'id3', 'id4'], dtype=StringDtype())
```

### Step 4: Assign filter_ser = Series(...)

```python
filter_ser = Series([False, True, True, False])
```

### Step 5: Assign result = obj.mask(...)

```python
result = obj.mask(filter_ser, filtered_obj)
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 7: Assign obj = value

```python
obj = obj['A']
```

### Step 8: Assign filtered_obj = value

```python
filtered_obj = filtered_obj['A']
```

### Step 9: Assign expected = value

```python
expected = expected['A']
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
obj = DataFrame({'A': ['foo', 'bar', 'baz', NA]}, index=['id1', 'id2', 'id3', 'id4'], dtype=StringDtype())
filtered_obj = DataFrame({'A': ['this', 'that']}, index=['id2', 'id3'], dtype=StringDtype())
expected = DataFrame({'A': [NA, 'this', 'that', NA]}, index=['id1', 'id2', 'id3', 'id4'], dtype=StringDtype())
if frame_or_series is Series:
    obj = obj['A']
    filtered_obj = filtered_obj['A']
    expected = expected['A']
filter_ser = Series([False, True, True, False])
result = obj.mask(filter_ser, filtered_obj)
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_mask.py:97 | Complexity: Advanced | Last updated: 2026-06-02*