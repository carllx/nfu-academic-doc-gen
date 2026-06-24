# How To: Multiindex Groupby Mixed Cols Axis1

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test multiindex groupby mixed cols axis1

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
# Fixtures: func, expected, dtype, result_dtype_dict
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame.astype(...)

```python
df = DataFrame([[1, 2, 3, 4, 5, 6]] * 3, columns=MultiIndex.from_product([['a', 'b'], ['i', 'j', 'k']])).astype({('a', 'j'): dtype, ('b', 'j'): dtype})
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
expected = DataFrame([expected] * 3, columns=['i', 'j', 'k']).astype(result_dtype_dict)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign gb = df.groupby(...)

```python
gb = df.groupby(level=1, axis=1)
```


## Complete Example

```python
# Setup
# Fixtures: func, expected, dtype, result_dtype_dict

# Workflow
df = DataFrame([[1, 2, 3, 4, 5, 6]] * 3, columns=MultiIndex.from_product([['a', 'b'], ['i', 'j', 'k']])).astype({('a', 'j'): dtype, ('b', 'j'): dtype})
msg = 'DataFrame.groupby with axis=1 is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    gb = df.groupby(level=1, axis=1)
result = gb.agg(func)
expected = DataFrame([expected] * 3, columns=['i', 'j', 'k']).astype(result_dtype_dict)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_aggregate.py:264 | Complexity: Intermediate | Last updated: 2026-06-02*