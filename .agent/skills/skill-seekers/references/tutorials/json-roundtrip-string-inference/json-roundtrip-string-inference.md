# How To: Json Roundtrip String Inference

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test json roundtrip string inference

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `datetime`
- `decimal`
- `io`
- `json`
- `os`
- `sys`
- `time`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.json`
- `pandas.arrays`
- `pandas.arrays`

**Setup Required:**
```python
# Fixtures: orient
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([['a', 'b'], ['c', 'd']], index=['row 1', 'row 2'], columns=['col 1', 'col 2'])
```

### Step 2: Assign out = df.to_json(...)

```python
out = df.to_json()
```

### Step 3: Assign dtype = pd.StringDtype(...)

```python
dtype = pd.StringDtype(na_value=np.nan)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([['a', 'b'], ['c', 'd']], dtype=dtype, index=Index(['row 1', 'row 2'], dtype=dtype), columns=Index(['col 1', 'col 2'], dtype=dtype))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = read_json(...)

```python
result = read_json(StringIO(out))
```


## Complete Example

```python
# Setup
# Fixtures: orient

# Workflow
df = DataFrame([['a', 'b'], ['c', 'd']], index=['row 1', 'row 2'], columns=['col 1', 'col 2'])
out = df.to_json()
with pd.option_context('future.infer_string', True):
    result = read_json(StringIO(out))
dtype = pd.StringDtype(na_value=np.nan)
expected = DataFrame([['a', 'b'], ['c', 'd']], dtype=dtype, index=Index(['row 1', 'row 2'], dtype=dtype), columns=Index(['col 1', 'col 2'], dtype=dtype))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_pandas.py:2135 | Complexity: Intermediate | Last updated: 2026-06-02*