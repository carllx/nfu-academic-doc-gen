# How To: Getitem Numeric Column Names

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem numeric column names

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({0: list('abcd') * 2, 2: np.random.default_rng(2).standard_normal(8), 4: np.random.default_rng(2).standard_normal(8), 6: np.random.default_rng(2).standard_normal(8)})
```

### Step 2: Assign result = unknown.mean(...)

```python
result = df.groupby(0)[df.columns[1:3]].mean()
```

### Step 3: Assign result2 = unknown.mean(...)

```python
result2 = df.groupby(0)[[2, 4]].mean()
```

### Step 4: Assign expected = unknown.groupby.mean(...)

```python
expected = df.loc[:, [0, 2, 4]].groupby(0).mean()
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result2, expected)
```

### Step 7: Call unknown.mean()

```python
df.groupby(0)[2, 4].mean()
```


## Complete Example

```python
# Workflow
df = DataFrame({0: list('abcd') * 2, 2: np.random.default_rng(2).standard_normal(8), 4: np.random.default_rng(2).standard_normal(8), 6: np.random.default_rng(2).standard_normal(8)})
result = df.groupby(0)[df.columns[1:3]].mean()
result2 = df.groupby(0)[[2, 4]].mean()
expected = df.loc[:, [0, 2, 4]].groupby(0).mean()
tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(result2, expected)
with pytest.raises(ValueError, match='Cannot subset columns with a tuple'):
    df.groupby(0)[2, 4].mean()
```

## Next Steps


---

*Source: test_grouping.py:89 | Complexity: Intermediate | Last updated: 2026-06-02*