# How To: Logical Ops Categorical Columns

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test logical ops categorical columns

## Prerequisites

**Required Modules:**
- `operator`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign intervals = value

```python
intervals = [Interval(1, 2), Interval(3, 4)]
```

### Step 2: Assign data = DataFrame(...)

```python
data = DataFrame([[1, np.nan], [2, np.nan]], columns=CategoricalIndex(intervals, categories=intervals + [Interval(5, 6)]))
```

### Step 3: Assign mask = DataFrame(...)

```python
mask = DataFrame([[False, False], [False, False]], columns=data.columns, dtype=bool)
```

### Step 4: Assign result = value

```python
result = mask | isnull(data)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame([[False, True], [False, True]], columns=CategoricalIndex(intervals, categories=intervals + [Interval(5, 6)]))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
intervals = [Interval(1, 2), Interval(3, 4)]
data = DataFrame([[1, np.nan], [2, np.nan]], columns=CategoricalIndex(intervals, categories=intervals + [Interval(5, 6)]))
mask = DataFrame([[False, False], [False, False]], columns=data.columns, dtype=bool)
result = mask | isnull(data)
expected = DataFrame([[False, True], [False, True]], columns=CategoricalIndex(intervals, categories=intervals + [Interval(5, 6)]))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_logical_ops.py:178 | Complexity: Intermediate | Last updated: 2026-06-02*