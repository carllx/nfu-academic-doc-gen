# How To: Compare Zerodim Array

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test compare zerodim array

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: fixed_now_ts
```

## Step-by-Step Guide

### Step 1: Assign ts = fixed_now_ts

```python
ts = fixed_now_ts
```

**Verification:**
```python
assert arr.ndim == 0
```

### Step 2: Assign dt64 = np.datetime64(...)

```python
dt64 = np.datetime64('2016-01-01', 'ns')
```

**Verification:**
```python
assert result is np.bool_(True)
```

### Step 3: Assign arr = np.array(...)

```python
arr = np.array(dt64)
```

**Verification:**
```python
assert result is np.bool_(False)
```

### Step 4: Assign result = value

```python
result = arr < ts
```

**Verification:**
```python
assert result is np.bool_(True)
```

### Step 5: Assign result = value

```python
result = arr > ts
```

**Verification:**
```python
assert result is np.bool_(False)
```


## Complete Example

```python
# Setup
# Fixtures: fixed_now_ts

# Workflow
ts = fixed_now_ts
dt64 = np.datetime64('2016-01-01', 'ns')
arr = np.array(dt64)
assert arr.ndim == 0
result = arr < ts
assert result is np.bool_(True)
result = arr > ts
assert result is np.bool_(False)
```

## Next Steps


---

*Source: test_comparisons.py:273 | Complexity: Intermediate | Last updated: 2026-06-02*