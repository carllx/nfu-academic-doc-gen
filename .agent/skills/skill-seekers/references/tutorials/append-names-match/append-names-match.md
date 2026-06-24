# How To: Append Names Match

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test append names match

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: name, exp
```

## Step-by-Step Guide

### Step 1: Assign midx = MultiIndex.from_arrays(...)

```python
midx = MultiIndex.from_arrays([[1, 2], [3, 4]], names=['a', 'b'])
```

### Step 2: Assign midx2 = MultiIndex.from_arrays(...)

```python
midx2 = MultiIndex.from_arrays([[3], [5]], names=['a', name])
```

### Step 3: Assign result = midx.append(...)

```python
result = midx.append(midx2)
```

### Step 4: Assign expected = MultiIndex.from_arrays(...)

```python
expected = MultiIndex.from_arrays([[1, 2, 3], [3, 4, 5]], names=['a', exp])
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: name, exp

# Workflow
midx = MultiIndex.from_arrays([[1, 2], [3, 4]], names=['a', 'b'])
midx2 = MultiIndex.from_arrays([[3], [5]], names=['a', name])
result = midx.append(midx2)
expected = MultiIndex.from_arrays([[1, 2, 3], [3, 4, 5]], names=['a', exp])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_reshape.py:154 | Complexity: Intermediate | Last updated: 2026-06-02*