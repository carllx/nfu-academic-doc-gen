# How To: Append Same Columns Type

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test append same columns type

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `dateutil`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: index
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 2, 3], [4, 5, 6]], columns=index)
```

**Verification:**
```python
assert expected.dtypes.iloc[0].kind == 'i'
```

### Step 2: Assign ser_index = value

```python
ser_index = index[:2]
```

**Verification:**
```python
assert expected.dtypes.iloc[1].kind == 'i'
```

### Step 3: Assign ser = Series(...)

```python
ser = Series([7, 8], index=ser_index, name=2)
```

### Step 4: Assign result = df._append(...)

```python
result = df._append(ser)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 2, 3.0], [4, 5, 6], [7, 8, np.nan]], index=[0, 1, 2], columns=index)
```

**Verification:**
```python
assert expected.dtypes.iloc[0].kind == 'i'
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign ser_index = index

```python
ser_index = index
```

### Step 8: Assign index = value

```python
index = index[:2]
```

### Step 9: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 2], [4, 5]], columns=index)
```

### Step 10: Assign ser = Series(...)

```python
ser = Series([7, 8, 9], index=ser_index, name=2)
```

### Step 11: Assign result = df._append(...)

```python
result = df._append(ser)
```

### Step 12: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 2, np.nan], [4, 5, np.nan], [7, 8, 9]], index=[0, 1, 2], columns=ser_index)
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: index

# Workflow
df = DataFrame([[1, 2, 3], [4, 5, 6]], columns=index)
ser_index = index[:2]
ser = Series([7, 8], index=ser_index, name=2)
result = df._append(ser)
expected = DataFrame([[1, 2, 3.0], [4, 5, 6], [7, 8, np.nan]], index=[0, 1, 2], columns=index)
assert expected.dtypes.iloc[0].kind == 'i'
assert expected.dtypes.iloc[1].kind == 'i'
tm.assert_frame_equal(result, expected)
ser_index = index
index = index[:2]
df = DataFrame([[1, 2], [4, 5]], columns=index)
ser = Series([7, 8, 9], index=ser_index, name=2)
result = df._append(ser)
expected = DataFrame([[1, 2, np.nan], [4, 5, np.nan], [7, 8, 9]], index=[0, 1, 2], columns=ser_index)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_append.py:191 | Complexity: Advanced | Last updated: 2026-06-02*