# How To: Values Mixed Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test values mixed dtypes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: float_frame, float_string_frame
```

## Step-by-Step Guide

### Step 1: Assign frame = float_frame

```python
frame = float_frame
```

**Verification:**
```python
assert np.isnan(frame[col].iloc[i])
```

### Step 2: Assign arr = value

```python
arr = frame.values
```

**Verification:**
```python
assert value == frame[col].iloc[i]
```

### Step 3: Assign frame_cols = value

```python
frame_cols = frame.columns
```

**Verification:**
```python
assert arr[0, 0] == 'bar'
```

### Step 4: Assign arr = value

```python
arr = float_string_frame[['foo', 'A']].values
```

**Verification:**
```python
assert arr[0, 0] == 1j
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame({'complex': [1j, 2j, 3j], 'real': [1, 2, 3]})
```

### Step 6: Assign arr = value

```python
arr = df.values
```

**Verification:**
```python
assert arr[0, 0] == 1j
```

### Step 7: Assign col = value

```python
col = frame_cols[j]
```

**Verification:**
```python
assert np.isnan(frame[col].iloc[i])
```


## Complete Example

```python
# Setup
# Fixtures: float_frame, float_string_frame

# Workflow
frame = float_frame
arr = frame.values
frame_cols = frame.columns
for i, row in enumerate(arr):
    for j, value in enumerate(row):
        col = frame_cols[j]
        if np.isnan(value):
            assert np.isnan(frame[col].iloc[i])
        else:
            assert value == frame[col].iloc[i]
arr = float_string_frame[['foo', 'A']].values
assert arr[0, 0] == 'bar'
df = DataFrame({'complex': [1j, 2j, 3j], 'real': [1, 2, 3]})
arr = df.values
assert arr[0, 0] == 1j
```

## Next Steps


---

*Source: test_values.py:32 | Complexity: Intermediate | Last updated: 2026-06-02*