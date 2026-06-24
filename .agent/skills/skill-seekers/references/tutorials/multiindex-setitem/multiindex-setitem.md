# How To: Multiindex Setitem

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiindex setitem

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arrays = value

```python
arrays = [np.array(['bar', 'bar', 'baz', 'qux', 'qux', 'bar']), np.array(['one', 'two', 'one', 'one', 'two', 'one']), np.arange(0, 6, 1)]
```

### Step 2: Assign df_orig = DataFrame.sort_index(...)

```python
df_orig = DataFrame(np.random.default_rng(2).standard_normal((6, 3)), index=arrays, columns=['A', 'B', 'C']).sort_index()
```

### Step 3: Assign expected = value

```python
expected = df_orig.loc[['bar']] * 2
```

### Step 4: Assign df = df_orig.copy(...)

```python
df = df_orig.copy()
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df.loc[['bar']], expected)
```

### Step 6: Assign msg = 'cannot align on a multi-index with out specifying the join levels'

```python
msg = 'cannot align on a multi-index with out specifying the join levels'
```


## Complete Example

```python
# Workflow
arrays = [np.array(['bar', 'bar', 'baz', 'qux', 'qux', 'bar']), np.array(['one', 'two', 'one', 'one', 'two', 'one']), np.arange(0, 6, 1)]
df_orig = DataFrame(np.random.default_rng(2).standard_normal((6, 3)), index=arrays, columns=['A', 'B', 'C']).sort_index()
expected = df_orig.loc[['bar']] * 2
df = df_orig.copy()
df.loc[['bar']] *= 2
tm.assert_frame_equal(df.loc[['bar']], expected)
msg = 'cannot align on a multi-index with out specifying the join levels'
with pytest.raises(TypeError, match=msg):
    df.loc['bar'] *= 2
```

## Next Steps


---

*Source: test_setitem.py:132 | Complexity: Intermediate | Last updated: 2026-06-02*