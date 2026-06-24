# How To: Dataframe Sub Numexpr Path

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dataframe sub numexpr path

## Prerequisites

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.computation.check`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': np.random.default_rng(2).standard_normal(25000)})
```

### Step 2: Assign unknown = value

```python
df.iloc[0:5] = np.nan
```

### Step 3: Assign expected = value

```python
expected = 1 - np.isnan(df.iloc[0:25])
```

### Step 4: Assign result = value

```python
result = (1 - np.isnan(df)).iloc[0:25]
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': np.random.default_rng(2).standard_normal(25000)})
df.iloc[0:5] = np.nan
expected = 1 - np.isnan(df.iloc[0:25])
result = (1 - np.isnan(df)).iloc[0:25]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_query_eval.py:133 | Complexity: Intermediate | Last updated: 2026-06-02*