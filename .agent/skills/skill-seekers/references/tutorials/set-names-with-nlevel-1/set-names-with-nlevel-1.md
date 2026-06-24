# How To: Set Names With Nlevel 1

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test set names with nlevel 1

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: inplace
```

## Step-by-Step Guide

### Step 1: Assign expected = MultiIndex(...)

```python
expected = MultiIndex(levels=[[0, 1]], codes=[[0, 1]], names=['first'])
```

### Step 2: Assign m = MultiIndex.from_product(...)

```python
m = MultiIndex.from_product([[0, 1]])
```

### Step 3: Assign result = m.set_names(...)

```python
result = m.set_names('first', level=0, inplace=inplace)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign result = m

```python
result = m
```


## Complete Example

```python
# Setup
# Fixtures: inplace

# Workflow
expected = MultiIndex(levels=[[0, 1]], codes=[[0, 1]], names=['first'])
m = MultiIndex.from_product([[0, 1]])
result = m.set_names('first', level=0, inplace=inplace)
if inplace:
    result = m
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_get_set.py:293 | Complexity: Intermediate | Last updated: 2026-06-02*