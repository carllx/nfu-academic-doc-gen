# How To: Set Levels Categorical

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test set levels categorical

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
# Fixtures: ordered
```

## Step-by-Step Guide

### Step 1: Assign index = MultiIndex.from_arrays(...)

```python
index = MultiIndex.from_arrays([list('xyzx'), [0, 1, 2, 3]])
```

### Step 2: Assign cidx = CategoricalIndex(...)

```python
cidx = CategoricalIndex(list('bac'), ordered=ordered)
```

### Step 3: Assign result = index.set_levels(...)

```python
result = index.set_levels(cidx, level=0)
```

### Step 4: Assign expected = MultiIndex(...)

```python
expected = MultiIndex(levels=[cidx, [0, 1, 2, 3]], codes=index.codes)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 6: Assign result_lvl = result.get_level_values(...)

```python
result_lvl = result.get_level_values(0)
```

### Step 7: Assign expected_lvl = CategoricalIndex(...)

```python
expected_lvl = CategoricalIndex(list('bacb'), categories=cidx.categories, ordered=cidx.ordered)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result_lvl, expected_lvl)
```


## Complete Example

```python
# Setup
# Fixtures: ordered

# Workflow
index = MultiIndex.from_arrays([list('xyzx'), [0, 1, 2, 3]])
cidx = CategoricalIndex(list('bac'), ordered=ordered)
result = index.set_levels(cidx, level=0)
expected = MultiIndex(levels=[cidx, [0, 1, 2, 3]], codes=index.codes)
tm.assert_index_equal(result, expected)
result_lvl = result.get_level_values(0)
expected_lvl = CategoricalIndex(list('bacb'), categories=cidx.categories, ordered=cidx.ordered)
tm.assert_index_equal(result_lvl, expected_lvl)
```

## Next Steps


---

*Source: test_get_set.py:308 | Complexity: Advanced | Last updated: 2026-06-02*