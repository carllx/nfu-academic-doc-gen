# How To: Subtype Integer With Non Integer Borders

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test subtype integer with non integer borders

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: subtype
```

## Step-by-Step Guide

### Step 1: Assign index = interval_range(...)

```python
index = interval_range(0.0, 3.0, freq=0.25)
```

### Step 2: Assign dtype = IntervalDtype(...)

```python
dtype = IntervalDtype(subtype, 'right')
```

### Step 3: Assign result = index.astype(...)

```python
result = index.astype(dtype)
```

### Step 4: Assign expected = IntervalIndex.from_arrays(...)

```python
expected = IntervalIndex.from_arrays(index.left.astype(subtype), index.right.astype(subtype), closed=index.closed)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: subtype

# Workflow
index = interval_range(0.0, 3.0, freq=0.25)
dtype = IntervalDtype(subtype, 'right')
result = index.astype(dtype)
expected = IntervalIndex.from_arrays(index.left.astype(subtype), index.right.astype(subtype), closed=index.closed)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_astype.py:162 | Complexity: Intermediate | Last updated: 2026-06-02*