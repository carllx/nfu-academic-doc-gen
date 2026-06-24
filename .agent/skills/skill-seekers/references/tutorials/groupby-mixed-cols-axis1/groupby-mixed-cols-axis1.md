# How To: Groupby Mixed Cols Axis1

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test groupby mixed cols axis1

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `functools`
- `functools`
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`

**Setup Required:**
```python
# Fixtures: func, expected_data, result_dtype_dict
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame.astype(...)

```python
df = DataFrame(np.arange(12).reshape(3, 4), index=Index([0, 1, 0], name='y'), columns=Index([10, 20, 10, 20], name='x'), dtype='int64').astype({10: 'Int64'})
```

### Step 2: Assign msg = 'DataFrame.groupby with axis=1 is deprecated'

```python
msg = 'DataFrame.groupby with axis=1 is deprecated'
```

### Step 3: Assign result = gb.agg(...)

```python
result = gb.agg(func)
```

### Step 4: Assign expected = DataFrame.astype(...)

```python
expected = DataFrame(data=expected_data, index=Index([0, 1, 0], name='y'), columns=Index([10, 20], name='x')).astype(result_dtype_dict)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign gb = df.groupby(...)

```python
gb = df.groupby('x', axis=1)
```


## Complete Example

```python
# Setup
# Fixtures: func, expected_data, result_dtype_dict

# Workflow
df = DataFrame(np.arange(12).reshape(3, 4), index=Index([0, 1, 0], name='y'), columns=Index([10, 20, 10, 20], name='x'), dtype='int64').astype({10: 'Int64'})
msg = 'DataFrame.groupby with axis=1 is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    gb = df.groupby('x', axis=1)
result = gb.agg(func)
expected = DataFrame(data=expected_data, index=Index([0, 1, 0], name='y'), columns=Index([10, 20], name='x')).astype(result_dtype_dict)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_aggregate.py:291 | Complexity: Intermediate | Last updated: 2026-06-02*