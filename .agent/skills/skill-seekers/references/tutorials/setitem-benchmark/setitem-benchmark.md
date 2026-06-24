# How To: Setitem Benchmark

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem benchmark

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.base`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign N = 10

```python
N = 10
```

### Step 2: Assign K = 5

```python
K = 5
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(index=range(N))
```

### Step 4: Assign new_col = np.random.default_rng.standard_normal(...)

```python
new_col = np.random.default_rng(2).standard_normal(N)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame(np.repeat(new_col, K).reshape(N, K), index=range(N))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 7: Assign unknown = new_col

```python
df[i] = new_col
```


## Complete Example

```python
# Workflow
N = 10
K = 5
df = DataFrame(index=range(N))
new_col = np.random.default_rng(2).standard_normal(N)
for i in range(K):
    df[i] = new_col
expected = DataFrame(np.repeat(new_col, K).reshape(N, K), index=range(N))
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_setitem.py:102 | Complexity: Intermediate | Last updated: 2026-06-02*