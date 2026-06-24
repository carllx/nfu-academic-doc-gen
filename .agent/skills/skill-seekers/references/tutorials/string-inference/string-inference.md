# How To: String Inference

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test string inference

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.pyarrow`
- `pandas`
- `pandas._testing`
- `pandas.io.feather_format`
- `pyarrow`
- `pyarrow`
- `pandas.arrays`

**Setup Required:**
```python
# Fixtures: tmp_path, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign path = value

```python
path = tmp_path / 'test_string_inference.p'
```

### Step 2: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame(data={'a': ['x', 'y']})
```

### Step 3: Call df.to_feather()

```python
df.to_feather(path)
```

### Step 4: Assign dtype = pd.StringDtype(...)

```python
dtype = pd.StringDtype(na_value=np.nan)
```

### Step 5: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame(data={'a': ['x', 'y']}, dtype=pd.StringDtype(na_value=np.nan))
```

### Step 6: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame(data={'a': ['x', 'y']}, dtype=dtype, columns=pd.Index(['a'], dtype=object if pa_version_under19p0 and (not using_infer_string) else dtype))
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = read_feather(...)

```python
result = read_feather(path)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, using_infer_string

# Workflow
path = tmp_path / 'test_string_inference.p'
df = pd.DataFrame(data={'a': ['x', 'y']})
df.to_feather(path)
with pd.option_context('future.infer_string', True):
    result = read_feather(path)
dtype = pd.StringDtype(na_value=np.nan)
expected = pd.DataFrame(data={'a': ['x', 'y']}, dtype=pd.StringDtype(na_value=np.nan))
expected = pd.DataFrame(data={'a': ['x', 'y']}, dtype=dtype, columns=pd.Index(['a'], dtype=object if pa_version_under19p0 and (not using_infer_string) else dtype))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_feather.py:247 | Complexity: Advanced | Last updated: 2026-06-02*