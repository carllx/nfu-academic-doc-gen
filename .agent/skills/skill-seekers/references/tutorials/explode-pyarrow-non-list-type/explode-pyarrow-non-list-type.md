# How To: Explode Pyarrow Non List Type

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test explode pyarrow non list type

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: ignore_index
```

## Step-by-Step Guide

### Step 1: Assign pa = pytest.importorskip(...)

```python
pa = pytest.importorskip('pyarrow')
```

### Step 2: Assign data = value

```python
data = [1, 2, 3]
```

### Step 3: Assign ser = pd.Series(...)

```python
ser = pd.Series(data, dtype=pd.ArrowDtype(pa.int64()))
```

### Step 4: Assign result = ser.explode(...)

```python
result = ser.explode(ignore_index=ignore_index)
```

### Step 5: Assign expected = pd.Series(...)

```python
expected = pd.Series([1, 2, 3], dtype='int64[pyarrow]', index=[0, 1, 2])
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: ignore_index

# Workflow
pa = pytest.importorskip('pyarrow')
data = [1, 2, 3]
ser = pd.Series(data, dtype=pd.ArrowDtype(pa.int64()))
result = ser.explode(ignore_index=ignore_index)
expected = pd.Series([1, 2, 3], dtype='int64[pyarrow]', index=[0, 1, 2])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_explode.py:169 | Complexity: Intermediate | Last updated: 2026-06-02*