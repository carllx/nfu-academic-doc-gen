# How To: Unary Binary

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test unary binary

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `functools`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.api.types`

**Setup Required:**
```python
# Fixtures: request, dtype
```

## Step-by-Step Guide

### Step 1: Assign values = np.array(...)

```python
values = np.array([[-1, -1], [1, 1]], dtype='int64')
```

**Verification:**
```python
assert isinstance(result_pandas, tuple)
```

### Step 2: Assign df = pd.DataFrame.astype(...)

```python
df = pd.DataFrame(values, columns=['A', 'B'], index=['a', 'b']).astype(dtype=dtype)
```

**Verification:**
```python
assert len(result_pandas) == 2
```

### Step 3: Assign result_pandas = np.modf(...)

```python
result_pandas = np.modf(df)
```

**Verification:**
```python
assert isinstance(result_pandas, tuple)
```

### Step 4: Assign expected_numpy = np.modf(...)

```python
expected_numpy = np.modf(values)
```

### Step 5: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(reason='Extension / mixed with multiple outputs not implemented.'))
```

### Step 6: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame(b, index=df.index, columns=df.columns)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: request, dtype

# Workflow
if is_extension_array_dtype(dtype) or isinstance(dtype, dict):
    request.applymarker(pytest.mark.xfail(reason='Extension / mixed with multiple outputs not implemented.'))
values = np.array([[-1, -1], [1, 1]], dtype='int64')
df = pd.DataFrame(values, columns=['A', 'B'], index=['a', 'b']).astype(dtype=dtype)
result_pandas = np.modf(df)
assert isinstance(result_pandas, tuple)
assert len(result_pandas) == 2
expected_numpy = np.modf(values)
for result, b in zip(result_pandas, expected_numpy):
    expected = pd.DataFrame(b, index=df.index, columns=df.columns)
    tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_ufunc.py:31 | Complexity: Intermediate | Last updated: 2026-06-02*