# How To: Agg Str With Kwarg Axis 1 Raises

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test agg str with kwarg axis 1 raises

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
# Fixtures: df, reduction_func
```

## Step-by-Step Guide

### Step 1: Assign gb = df.groupby(...)

```python
gb = df.groupby(level=0)
```

### Step 2: Assign warn_msg = value

```python
warn_msg = f'DataFrameGroupBy.{reduction_func} with axis=1 is deprecated'
```

### Step 3: Assign error = TypeError

```python
error = TypeError
```

### Step 4: Assign msg = "'[<>]' not supported between instances of 'float' and 'str'"

```python
msg = "'[<>]' not supported between instances of 'float' and 'str'"
```

### Step 5: Assign warn = FutureWarning

```python
warn = FutureWarning
```

### Step 6: Assign error = ValueError

```python
error = ValueError
```

### Step 7: Assign msg = value

```python
msg = f'Operation {reduction_func} does not support axis=1'
```

### Step 8: Assign warn = None

```python
warn = None
```

### Step 9: Call gb.agg()

```python
gb.agg(reduction_func, axis=1)
```


## Complete Example

```python
# Setup
# Fixtures: df, reduction_func

# Workflow
gb = df.groupby(level=0)
warn_msg = f'DataFrameGroupBy.{reduction_func} with axis=1 is deprecated'
if reduction_func in ('idxmax', 'idxmin'):
    error = TypeError
    msg = "'[<>]' not supported between instances of 'float' and 'str'"
    warn = FutureWarning
else:
    error = ValueError
    msg = f'Operation {reduction_func} does not support axis=1'
    warn = None
with pytest.raises(error, match=msg):
    with tm.assert_produces_warning(warn, match=warn_msg):
        gb.agg(reduction_func, axis=1)
```

## Next Steps


---

*Source: test_aggregate.py:237 | Complexity: Advanced | Last updated: 2026-06-02*