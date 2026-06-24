# How To: First Last Valid

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test first last valid

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`

**Setup Required:**
```python
# Fixtures: index
```

## Step-by-Step Guide

### Step 1: Assign mat = np.random.default_rng.standard_normal(...)

```python
mat = np.random.default_rng(2).standard_normal(len(index))
```

**Verification:**
```python
assert frame.first_valid_index() == frame.index[5]
```

### Step 2: Assign unknown = value

```python
mat[:5] = np.nan
```

**Verification:**
```python
assert frame.last_valid_index() == frame.index[-6]
```

### Step 3: Assign unknown = value

```python
mat[-5:] = np.nan
```

**Verification:**
```python
assert ser.first_valid_index() == frame.index[5]
```

### Step 4: Assign frame = DataFrame(...)

```python
frame = DataFrame({'foo': mat}, index=index)
```

**Verification:**
```python
assert ser.last_valid_index() == frame.index[-6]
```

### Step 5: Assign ser = value

```python
ser = frame['foo']
```

**Verification:**
```python
assert ser.first_valid_index() == frame.index[5]
```


## Complete Example

```python
# Setup
# Fixtures: index

# Workflow
mat = np.random.default_rng(2).standard_normal(len(index))
mat[:5] = np.nan
mat[-5:] = np.nan
frame = DataFrame({'foo': mat}, index=index)
assert frame.first_valid_index() == frame.index[5]
assert frame.last_valid_index() == frame.index[-6]
ser = frame['foo']
assert ser.first_valid_index() == frame.index[5]
assert ser.last_valid_index() == frame.index[-6]
```

## Next Steps


---

*Source: test_first_valid_index.py:52 | Complexity: Intermediate | Last updated: 2026-06-02*