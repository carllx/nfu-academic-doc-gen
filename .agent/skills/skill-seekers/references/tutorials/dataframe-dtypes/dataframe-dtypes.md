# How To: Dataframe Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dataframe dtypes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: method, expected_data, dtypes, min_periods, step
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.arange(10).reshape((5, 2)), dtype=get_dtype(dtypes))
```

### Step 2: Assign rolled = df.rolling(...)

```python
rolled = df.rolling(2, min_periods=min_periods, step=step)
```

### Step 3: Assign msg = 'Cannot aggregate non-numeric type'

```python
msg = 'Cannot aggregate non-numeric type'
```

### Step 4: Assign result = getattr(...)

```python
result = getattr(rolled, method)()
```

### Step 5: Assign expected = value

```python
expected = DataFrame(expected_data, dtype='float64')[::step]
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Call getattr()

```python
getattr(rolled, method)()
```


## Complete Example

```python
# Setup
# Fixtures: method, expected_data, dtypes, min_periods, step

# Workflow
df = DataFrame(np.arange(10).reshape((5, 2)), dtype=get_dtype(dtypes))
rolled = df.rolling(2, min_periods=min_periods, step=step)
if dtypes in ('m8[ns]', 'M8[ns]', 'datetime64[ns, UTC]') and method != 'count':
    msg = 'Cannot aggregate non-numeric type'
    with pytest.raises(DataError, match=msg):
        getattr(rolled, method)()
else:
    result = getattr(rolled, method)()
    expected = DataFrame(expected_data, dtype='float64')[::step]
    tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_dtypes.py:162 | Complexity: Intermediate | Last updated: 2026-06-02*