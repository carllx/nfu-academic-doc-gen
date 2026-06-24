# How To: Unique Level

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test unique level

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: idx, level
```

## Step-by-Step Guide

### Step 1: Assign result = idx.unique(...)

```python
result = idx.unique(level=level)
```

### Step 2: Assign expected = idx.get_level_values.unique(...)

```python
expected = idx.get_level_values(level).unique()
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 4: Assign mi = MultiIndex.from_arrays(...)

```python
mi = MultiIndex.from_arrays([[1, 3, 2, 4], [1, 3, 2, 5]], names=['first', 'second'])
```

### Step 5: Assign result = mi.unique(...)

```python
result = mi.unique(level=level)
```

### Step 6: Assign expected = mi.get_level_values(...)

```python
expected = mi.get_level_values(level)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 8: Assign mi = MultiIndex.from_arrays(...)

```python
mi = MultiIndex.from_arrays([[], []], names=['first', 'second'])
```

### Step 9: Assign result = mi.unique(...)

```python
result = mi.unique(level=level)
```

### Step 10: Assign expected = mi.get_level_values(...)

```python
expected = mi.get_level_values(level)
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: idx, level

# Workflow
result = idx.unique(level=level)
expected = idx.get_level_values(level).unique()
tm.assert_index_equal(result, expected)
mi = MultiIndex.from_arrays([[1, 3, 2, 4], [1, 3, 2, 5]], names=['first', 'second'])
result = mi.unique(level=level)
expected = mi.get_level_values(level)
tm.assert_index_equal(result, expected)
mi = MultiIndex.from_arrays([[], []], names=['first', 'second'])
result = mi.unique(level=level)
expected = mi.get_level_values(level)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_duplicates.py:82 | Complexity: Advanced | Last updated: 2026-06-02*