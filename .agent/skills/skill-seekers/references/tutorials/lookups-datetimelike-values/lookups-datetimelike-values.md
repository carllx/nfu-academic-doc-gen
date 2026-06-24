# How To: Lookups Datetimelike Values

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test lookups datetimelike values

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: vals, dtype
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(vals, index=range(3, 6))
```

**Verification:**
```python
assert isinstance(result, type(expected)) and result == expected
```

### Step 2: Assign ser.index = ser.index.astype(...)

```python
ser.index = ser.index.astype(dtype)
```

**Verification:**
```python
assert isinstance(result, type(expected)) and result == expected
```

### Step 3: Assign expected = value

```python
expected = vals[1]
```

**Verification:**
```python
assert isinstance(result, type(expected)) and result == expected
```

### Step 4: Assign result = value

```python
result = ser[4.0]
```

**Verification:**
```python
assert isinstance(result, type(expected)) and result == expected
```

### Step 5: Assign result = value

```python
result = ser[4]
```

**Verification:**
```python
assert isinstance(result, type(expected)) and result == expected
```

### Step 6: Assign result = value

```python
result = ser.loc[4.0]
```

**Verification:**
```python
assert isinstance(result, type(expected)) and result == expected
```

### Step 7: Assign result = value

```python
result = ser.loc[4]
```

**Verification:**
```python
assert isinstance(result, type(expected)) and result == expected
```

### Step 8: Assign result = value

```python
result = ser.at[4.0]
```

**Verification:**
```python
assert isinstance(result, type(expected)) and result == expected
```

### Step 9: Assign result = value

```python
result = ser.at[4]
```

**Verification:**
```python
assert isinstance(result, type(expected)) and result == expected
```

### Step 10: Assign result = value

```python
result = ser.iloc[1]
```

**Verification:**
```python
assert isinstance(result, type(expected)) and result == expected
```

### Step 11: Assign result = value

```python
result = ser.iat[1]
```

**Verification:**
```python
assert isinstance(result, type(expected)) and result == expected
```


## Complete Example

```python
# Setup
# Fixtures: vals, dtype

# Workflow
ser = Series(vals, index=range(3, 6))
ser.index = ser.index.astype(dtype)
expected = vals[1]
result = ser[4.0]
assert isinstance(result, type(expected)) and result == expected
result = ser[4]
assert isinstance(result, type(expected)) and result == expected
result = ser.loc[4.0]
assert isinstance(result, type(expected)) and result == expected
result = ser.loc[4]
assert isinstance(result, type(expected)) and result == expected
result = ser.at[4.0]
assert isinstance(result, type(expected)) and result == expected
result = ser.at[4]
assert isinstance(result, type(expected)) and result == expected
result = ser.iloc[1]
assert isinstance(result, type(expected)) and result == expected
result = ser.iat[1]
assert isinstance(result, type(expected)) and result == expected
```

## Next Steps


---

*Source: test_numeric.py:167 | Complexity: Advanced | Last updated: 2026-06-02*