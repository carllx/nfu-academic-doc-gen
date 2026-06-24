# How To: Unique

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unique

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([1.2345] * 100)
```

**Verification:**
```python
assert len(result) == 2
```

### Step 2: Assign unknown = value

```python
ser[::2] = np.nan
```

**Verification:**
```python
assert len(result) == 2
```

### Step 3: Assign result = ser.unique(...)

```python
result = ser.unique()
```

**Verification:**
```python
assert len(result) == 2
```

### Step 4: Assign ser = Series(...)

```python
ser = Series([1.2345] * 100, dtype='f4')
```

### Step 5: Assign unknown = value

```python
ser[::2] = np.nan
```

### Step 6: Assign result = ser.unique(...)

```python
result = ser.unique()
```

**Verification:**
```python
assert len(result) == 2
```


## Complete Example

```python
# Workflow
ser = Series([1.2345] * 100)
ser[::2] = np.nan
result = ser.unique()
assert len(result) == 2
ser = Series([1.2345] * 100, dtype='f4')
ser[::2] = np.nan
result = ser.unique()
assert len(result) == 2
```

## Next Steps


---

*Source: test_unique.py:23 | Complexity: Intermediate | Last updated: 2026-06-02*