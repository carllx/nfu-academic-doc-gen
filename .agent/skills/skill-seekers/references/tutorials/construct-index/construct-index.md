# How To: Construct Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test construct index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.generic`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.integer`

**Setup Required:**
```python
# Fixtures: all_data, dropna
```

## Step-by-Step Guide

### Step 1: Assign all_data = value

```python
all_data = all_data[:10]
```

**Verification:**
```python
assert all_data.dtype == expected.dtype
```

### Step 2: Assign result = pd.Index(...)

```python
result = pd.Index(pd.array(other, dtype=all_data.dtype))
```

### Step 3: Assign expected = pd.Index(...)

```python
expected = pd.Index(other, dtype=all_data.dtype)
```

**Verification:**
```python
assert all_data.dtype == expected.dtype
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign other = np.array(...)

```python
other = np.array(all_data[~all_data.isna()])
```

### Step 6: Assign other = all_data

```python
other = all_data
```


## Complete Example

```python
# Setup
# Fixtures: all_data, dropna

# Workflow
all_data = all_data[:10]
if dropna:
    other = np.array(all_data[~all_data.isna()])
else:
    other = all_data
result = pd.Index(pd.array(other, dtype=all_data.dtype))
expected = pd.Index(other, dtype=all_data.dtype)
assert all_data.dtype == expected.dtype
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_dtypes.py:63 | Complexity: Intermediate | Last updated: 2026-06-02*