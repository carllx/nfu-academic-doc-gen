# How To: Float Subtype

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test float subtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: start, end, freq
```

## Step-by-Step Guide

### Step 1: Assign index = interval_range(...)

```python
index = interval_range(start=start, end=end, freq=freq)
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign result = value

```python
result = index.dtype.subtype
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign expected = value

```python
expected = 'int64' if is_integer(start + end + freq) else 'float64'
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign index = interval_range(...)

```python
index = interval_range(start=start, periods=5, freq=freq)
```

**Verification:**
```python
assert result == expected
```

### Step 5: Assign result = value

```python
result = index.dtype.subtype
```

### Step 6: Assign expected = value

```python
expected = 'int64' if is_integer(start + freq) else 'float64'
```

**Verification:**
```python
assert result == expected
```

### Step 7: Assign index = interval_range(...)

```python
index = interval_range(end=end, periods=5, freq=freq)
```

### Step 8: Assign result = value

```python
result = index.dtype.subtype
```

### Step 9: Assign expected = value

```python
expected = 'int64' if is_integer(end + freq) else 'float64'
```

**Verification:**
```python
assert result == expected
```

### Step 10: Assign index = interval_range(...)

```python
index = interval_range(start=start, end=end, periods=5)
```

### Step 11: Assign result = value

```python
result = index.dtype.subtype
```

### Step 12: Assign expected = value

```python
expected = 'int64' if is_integer(start + end) else 'float64'
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: start, end, freq

# Workflow
index = interval_range(start=start, end=end, freq=freq)
result = index.dtype.subtype
expected = 'int64' if is_integer(start + end + freq) else 'float64'
assert result == expected
index = interval_range(start=start, periods=5, freq=freq)
result = index.dtype.subtype
expected = 'int64' if is_integer(start + freq) else 'float64'
assert result == expected
index = interval_range(end=end, periods=5, freq=freq)
result = index.dtype.subtype
expected = 'int64' if is_integer(end + freq) else 'float64'
assert result == expected
index = interval_range(start=start, end=end, periods=5)
result = index.dtype.subtype
expected = 'int64' if is_integer(start + end) else 'float64'
assert result == expected
```

## Next Steps


---

*Source: test_interval_range.py:195 | Complexity: Advanced | Last updated: 2026-06-02*