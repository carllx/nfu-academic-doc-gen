# How To: Corrwith Index Intersection

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test corrwith index intersection

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(np.random.default_rng(2).random(size=(10, 2)), columns=['a', 'b'])
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(np.random.default_rng(2).random(size=(10, 3)), columns=['a', 'b', 'c'])
```

### Step 3: Assign result = df1.corrwith.index.sort_values(...)

```python
result = df1.corrwith(df2, drop=True).index.sort_values()
```

### Step 4: Assign expected = df1.columns.intersection.sort_values(...)

```python
expected = df1.columns.intersection(df2.columns).sort_values()
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
df1 = DataFrame(np.random.default_rng(2).random(size=(10, 2)), columns=['a', 'b'])
df2 = DataFrame(np.random.default_rng(2).random(size=(10, 3)), columns=['a', 'b', 'c'])
result = df1.corrwith(df2, drop=True).index.sort_values()
expected = df1.columns.intersection(df2.columns).sort_values()
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_cov_corr.py:392 | Complexity: Intermediate | Last updated: 2026-06-02*