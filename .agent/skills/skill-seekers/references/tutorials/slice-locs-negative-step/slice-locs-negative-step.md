# How To: Slice Locs Negative Step

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test slice locs negative step

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: in_slice, expected, any_string_dtype
```

## Step-by-Step Guide

### Step 1: Assign index = Index(...)

```python
index = Index(list('bcdxy'), dtype=any_string_dtype)
```

### Step 2: Assign unknown = index.slice_locs(...)

```python
s_start, s_stop = index.slice_locs(in_slice.start, in_slice.stop, in_slice.step)
```

### Step 3: Assign result = value

```python
result = index[s_start:s_stop:in_slice.step]
```

### Step 4: Assign expected = Index(...)

```python
expected = Index(list(expected), dtype=any_string_dtype)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: in_slice, expected, any_string_dtype

# Workflow
index = Index(list('bcdxy'), dtype=any_string_dtype)
s_start, s_stop = index.slice_locs(in_slice.start, in_slice.stop, in_slice.step)
result = index[s_start:s_stop:in_slice.step]
expected = Index(list(expected), dtype=any_string_dtype)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:170 | Complexity: Intermediate | Last updated: 2026-06-02*