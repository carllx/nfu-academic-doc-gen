# How To: Split With Name Series

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test split with name series

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas.tests.strings`

**Setup Required:**
```python
# Fixtures: any_string_dtype
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(['a,b', 'c,d'], name='xxx', dtype=any_string_dtype)
```

### Step 2: Assign res = s.str.split(...)

```python
res = s.str.split(',')
```

### Step 3: Assign exp = Series(...)

```python
exp = Series([['a', 'b'], ['c', 'd']], name='xxx')
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```

### Step 5: Assign res = s.str.split(...)

```python
res = s.str.split(',', expand=True)
```

### Step 6: Assign exp = DataFrame(...)

```python
exp = DataFrame([['a', 'b'], ['c', 'd']], dtype=any_string_dtype)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp)
```


## Complete Example

```python
# Setup
# Fixtures: any_string_dtype

# Workflow
s = Series(['a,b', 'c,d'], name='xxx', dtype=any_string_dtype)
res = s.str.split(',')
exp = Series([['a', 'b'], ['c', 'd']], name='xxx')
tm.assert_series_equal(res, exp)
res = s.str.split(',', expand=True)
exp = DataFrame([['a', 'b'], ['c', 'd']], dtype=any_string_dtype)
tm.assert_frame_equal(res, exp)
```

## Next Steps


---

*Source: test_split_partition.py:393 | Complexity: Intermediate | Last updated: 2026-06-02*