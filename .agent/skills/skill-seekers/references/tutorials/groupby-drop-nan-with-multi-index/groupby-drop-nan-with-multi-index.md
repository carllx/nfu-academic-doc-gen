# How To: Groupby Drop Nan With Multi Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby drop nan with multi index

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.pyarrow`
- `pandas.core.dtypes.missing`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`


## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame([[np.nan, 0, 1]], columns=['a', 'b', 'c'])
```

### Step 2: Assign df = df.set_index(...)

```python
df = df.set_index(['a', 'b'])
```

### Step 3: Assign result = df.groupby.first(...)

```python
result = df.groupby(['a', 'b'], dropna=False).first()
```

### Step 4: Assign expected = df

```python
expected = df
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = pd.DataFrame([[np.nan, 0, 1]], columns=['a', 'b', 'c'])
df = df.set_index(['a', 'b'])
result = df.groupby(['a', 'b'], dropna=False).first()
expected = df
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_groupby_dropna.py:390 | Complexity: Intermediate | Last updated: 2026-06-02*