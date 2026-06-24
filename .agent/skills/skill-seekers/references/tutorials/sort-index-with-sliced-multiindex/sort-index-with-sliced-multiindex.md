# How To: Sort Index With Sliced Multiindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort index with sliced multiindex

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign mi = MultiIndex.from_tuples(...)

```python
mi = MultiIndex.from_tuples([('a', '10'), ('a', '18'), ('a', '25'), ('b', '16'), ('b', '26'), ('a', '45'), ('b', '28'), ('a', '5'), ('a', '50'), ('a', '51'), ('b', '4')], names=['group', 'str'])
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'x': range(len(mi))}, index=mi)
```

### Step 3: Assign result = unknown.sort_index(...)

```python
result = df.iloc[0:6].sort_index()
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'x': [0, 1, 2, 5, 3, 4]}, index=MultiIndex.from_tuples([('a', '10'), ('a', '18'), ('a', '25'), ('a', '45'), ('b', '16'), ('b', '26')], names=['group', 'str']))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
mi = MultiIndex.from_tuples([('a', '10'), ('a', '18'), ('a', '25'), ('b', '16'), ('b', '26'), ('a', '45'), ('b', '28'), ('a', '5'), ('a', '50'), ('a', '51'), ('b', '4')], names=['group', 'str'])
df = DataFrame({'x': range(len(mi))}, index=mi)
result = df.iloc[0:6].sort_index()
expected = DataFrame({'x': [0, 1, 2, 5, 3, 4]}, index=MultiIndex.from_tuples([('a', '10'), ('a', '18'), ('a', '25'), ('a', '45'), ('b', '16'), ('b', '26')], names=['group', 'str']))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_sort_index.py:960 | Complexity: Intermediate | Last updated: 2026-06-02*