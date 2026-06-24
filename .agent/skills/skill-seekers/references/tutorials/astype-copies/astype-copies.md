# How To: Astype Copies

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test astype copies

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('pyarrow')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3]}, dtype=dtype)
```

### Step 3: Assign result = df.astype(...)

```python
result = df.astype('int64[pyarrow]', copy=True)
```

### Step 4: Assign unknown = 100

```python
df.iloc[0, 0] = 100
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 2, 3]}, dtype='int64[pyarrow]')
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
pytest.importorskip('pyarrow')
df = DataFrame({'a': [1, 2, 3]}, dtype=dtype)
result = df.astype('int64[pyarrow]', copy=True)
df.iloc[0, 0] = 100
expected = DataFrame({'a': [1, 2, 3]}, dtype='int64[pyarrow]')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_astype.py:898 | Complexity: Intermediate | Last updated: 2026-06-02*