# How To: Loc Axis Single Level Single Col Indexing Multiindex Col Df

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc axis single level single col indexing multiindex col df

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.indexing.common`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.arange(27).reshape(3, 9), columns=MultiIndex.from_product([['a1', 'a2', 'a3'], ['b1', 'b2', 'b3']]))
```

### Step 2: Assign result = value

```python
result = df.loc(axis=1)['a1']
```

### Step 3: Assign expected = value

```python
expected = df.iloc[:, :3]
```

### Step 4: Assign expected.columns = value

```python
expected.columns = ['b1', 'b2', 'b3']
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.arange(27).reshape(3, 9), columns=MultiIndex.from_product([['a1', 'a2', 'a3'], ['b1', 'b2', 'b3']]))
result = df.loc(axis=1)['a1']
expected = df.iloc[:, :3]
expected.columns = ['b1', 'b2', 'b3']
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_slice.py:537 | Complexity: Intermediate | Last updated: 2026-06-02*