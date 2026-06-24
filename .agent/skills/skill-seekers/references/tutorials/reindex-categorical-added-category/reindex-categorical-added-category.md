# How To: Reindex Categorical Added Category

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex categorical added category

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ci = CategoricalIndex(...)

```python
ci = CategoricalIndex([Interval(0, 1, closed='right'), Interval(1, 2, closed='right')], ordered=True)
```

### Step 2: Assign ci_add = CategoricalIndex(...)

```python
ci_add = CategoricalIndex([Interval(0, 1, closed='right'), Interval(1, 2, closed='right'), Interval(2, 3, closed='right'), Interval(3, 4, closed='right')], ordered=True)
```

### Step 3: Assign unknown = ci.reindex(...)

```python
result, _ = ci.reindex(ci_add)
```

### Step 4: Assign expected = ci_add

```python
expected = ci_add
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(expected, result)
```


## Complete Example

```python
# Workflow
ci = CategoricalIndex([Interval(0, 1, closed='right'), Interval(1, 2, closed='right')], ordered=True)
ci_add = CategoricalIndex([Interval(0, 1, closed='right'), Interval(1, 2, closed='right'), Interval(2, 3, closed='right'), Interval(3, 4, closed='right')], ordered=True)
result, _ = ci.reindex(ci_add)
expected = ci_add
tm.assert_index_equal(expected, result)
```

## Next Steps


---

*Source: test_reindex.py:61 | Complexity: Intermediate | Last updated: 2026-06-02*