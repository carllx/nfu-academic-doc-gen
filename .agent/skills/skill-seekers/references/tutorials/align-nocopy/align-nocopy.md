# How To: Align Nocopy

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test align nocopy

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datetime_series, using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign b = unknown.copy(...)

```python
b = datetime_series[:5].copy()
```

**Verification:**
```python
assert not (a[:5] == 5).any()
```

### Step 2: Assign a = datetime_series.copy(...)

```python
a = datetime_series.copy()
```

**Verification:**
```python
assert not (a[:5] == 5).any()
```

### Step 3: Assign unknown = a.align(...)

```python
ra, _ = a.align(b, join='left')
```

**Verification:**
```python
assert (a[:5] == 5).all()
```

### Step 4: Assign unknown = 5

```python
ra[:5] = 5
```

**Verification:**
```python
assert not (b[:3] == 5).any()
```

### Step 5: Assign a = datetime_series.copy(...)

```python
a = datetime_series.copy()
```

**Verification:**
```python
assert not (b[:2] == 5).any()
```

### Step 6: Assign unknown = a.align(...)

```python
ra, _ = a.align(b, join='left', copy=False)
```

**Verification:**
```python
assert (b[:2] == 5).all()
```

### Step 7: Assign unknown = 5

```python
ra[:5] = 5
```

### Step 8: Assign a = datetime_series.copy(...)

```python
a = datetime_series.copy()
```

### Step 9: Assign b = unknown.copy(...)

```python
b = datetime_series[:5].copy()
```

### Step 10: Assign unknown = a.align(...)

```python
_, rb = a.align(b, join='right')
```

### Step 11: Assign unknown = 5

```python
rb[:3] = 5
```

**Verification:**
```python
assert not (b[:3] == 5).any()
```

### Step 12: Assign a = datetime_series.copy(...)

```python
a = datetime_series.copy()
```

### Step 13: Assign b = unknown.copy(...)

```python
b = datetime_series[:5].copy()
```

### Step 14: Assign unknown = a.align(...)

```python
_, rb = a.align(b, join='right', copy=False)
```

### Step 15: Assign unknown = 5

```python
rb[:2] = 5
```

**Verification:**
```python
assert not (a[:5] == 5).any()
```


## Complete Example

```python
# Setup
# Fixtures: datetime_series, using_copy_on_write

# Workflow
b = datetime_series[:5].copy()
a = datetime_series.copy()
ra, _ = a.align(b, join='left')
ra[:5] = 5
assert not (a[:5] == 5).any()
a = datetime_series.copy()
ra, _ = a.align(b, join='left', copy=False)
ra[:5] = 5
if using_copy_on_write:
    assert not (a[:5] == 5).any()
else:
    assert (a[:5] == 5).all()
a = datetime_series.copy()
b = datetime_series[:5].copy()
_, rb = a.align(b, join='right')
rb[:3] = 5
assert not (b[:3] == 5).any()
a = datetime_series.copy()
b = datetime_series[:5].copy()
_, rb = a.align(b, join='right', copy=False)
rb[:2] = 5
if using_copy_on_write:
    assert not (b[:2] == 5).any()
else:
    assert (b[:2] == 5).all()
```

## Next Steps


---

*Source: test_align.py:92 | Complexity: Advanced | Last updated: 2026-06-02*