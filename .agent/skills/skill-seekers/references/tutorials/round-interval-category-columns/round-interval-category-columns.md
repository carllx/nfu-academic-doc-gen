# How To: Round Interval Category Columns

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test round interval category columns

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign columns = pd.CategoricalIndex(...)

```python
columns = pd.CategoricalIndex(pd.interval_range(0, 2))
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame([[0.66, 1.1], [0.3, 0.25]], columns=columns)
```

### Step 3: Assign result = df.round(...)

```python
result = df.round()
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1.0, 1.0], [0.0, 0.0]], columns=columns)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
columns = pd.CategoricalIndex(pd.interval_range(0, 2))
df = DataFrame([[0.66, 1.1], [0.3, 0.25]], columns=columns)
result = df.round()
expected = DataFrame([[1.0, 1.0], [0.0, 0.0]], columns=columns)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_round.py:211 | Complexity: Intermediate | Last updated: 2026-06-02*