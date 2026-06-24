# How To: Indices Grouped By Tuple With Lambda

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test indices grouped by tuple with lambda

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
df = DataFrame({'Tuples': ((x, y) for x in [0, 1] for y in np.random.default_rng(2).integers(3, 5, 5))})
```

### Step 2: Assign gb = df.groupby(...)

```python
gb = df.groupby('Tuples')
```

### Step 3: Assign gb_lambda = df.groupby(...)

```python
gb_lambda = df.groupby(lambda x: df.iloc[x, 0])
```

### Step 4: Assign expected = value

```python
expected = gb.indices
```

### Step 5: Assign result = value

```python
result = gb_lambda.indices
```

### Step 6: Call tm.assert_dict_equal()

```python
tm.assert_dict_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'Tuples': ((x, y) for x in [0, 1] for y in np.random.default_rng(2).integers(3, 5, 5))})
gb = df.groupby('Tuples')
gb_lambda = df.groupby(lambda x: df.iloc[x, 0])
expected = gb.indices
result = gb_lambda.indices
tm.assert_dict_equal(result, expected)
```

## Next Steps


---

*Source: test_grouping.py:149 | Complexity: Intermediate | Last updated: 2026-06-02*