# How To: Unary Unary

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test unary unary

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
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign values = np.array(...)

```python
values = np.array([[-1, -1], [1, 1]], dtype='int64')
```

### Step 2: Assign df = pd.DataFrame.astype(...)

```python
df = pd.DataFrame(values, columns=['A', 'B'], index=['a', 'b']).astype(dtype=dtype)
```

### Step 3: Assign result = np.positive(...)

```python
result = np.positive(df)
```

### Step 4: Assign expected = pd.DataFrame.astype(...)

```python
expected = pd.DataFrame(np.positive(values), index=df.index, columns=df.columns).astype(dtype)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
values = np.array([[-1, -1], [1, 1]], dtype='int64')
df = pd.DataFrame(values, columns=['A', 'B'], index=['a', 'b']).astype(dtype=dtype)
result = np.positive(df)
expected = pd.DataFrame(np.positive(values), index=df.index, columns=df.columns).astype(dtype)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_ufunc.py:19 | Complexity: Intermediate | Last updated: 2026-06-02*