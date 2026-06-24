# How To: Conversions

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test conversions

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.arrays`
- `pandas.core.arrays.integer`

**Setup Required:**
```python
# Fixtures: data_missing
```

## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'A': data_missing})
```

**Verification:**
```python
assert pd.isnull(e)
```

### Step 2: Assign result = unknown.astype(...)

```python
result = df['A'].astype('object')
```

**Verification:**
```python
assert r == e
```

### Step 3: Assign expected = pd.Series(...)

```python
expected = pd.Series(np.array([pd.NA, 1], dtype=object), name='A')
```

**Verification:**
```python
assert is_integer(e)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

**Verification:**
```python
assert r == e
```

### Step 5: Assign result = value

```python
result = df['A'].astype('object').values
```

**Verification:**
```python
assert type(r) == type(e)
```

### Step 6: Assign expected = np.array(...)

```python
expected = np.array([pd.NA, 1], dtype=object)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

**Verification:**
```python
assert pd.isnull(e)
```


## Complete Example

```python
# Setup
# Fixtures: data_missing

# Workflow
df = pd.DataFrame({'A': data_missing})
result = df['A'].astype('object')
expected = pd.Series(np.array([pd.NA, 1], dtype=object), name='A')
tm.assert_series_equal(result, expected)
result = df['A'].astype('object').values
expected = np.array([pd.NA, 1], dtype=object)
tm.assert_numpy_array_equal(result, expected)
for r, e in zip(result, expected):
    if pd.isnull(r):
        assert pd.isnull(e)
    elif is_integer(r):
        assert r == e
        assert is_integer(e)
    else:
        assert r == e
        assert type(r) == type(e)
```

## Next Steps


---

*Source: test_construction.py:50 | Complexity: Intermediate | Last updated: 2026-06-02*