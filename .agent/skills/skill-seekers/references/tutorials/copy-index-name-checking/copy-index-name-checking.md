# How To: Copy Index Name Checking

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test copy index name checking

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
# Fixtures: float_frame, attr
```

## Step-by-Step Guide

### Step 1: Assign ind = getattr(...)

```python
ind = getattr(float_frame, attr)
```

**Verification:**
```python
assert getattr(float_frame, attr).name is None
```

### Step 2: Assign ind.name = None

```python
ind.name = None
```

### Step 3: Assign cp = float_frame.copy(...)

```python
cp = float_frame.copy()
```

### Step 4: Assign getattr.name = 'foo'

```python
getattr(cp, attr).name = 'foo'
```

**Verification:**
```python
assert getattr(float_frame, attr).name is None
```


## Complete Example

```python
# Setup
# Fixtures: float_frame, attr

# Workflow
ind = getattr(float_frame, attr)
ind.name = None
cp = float_frame.copy()
getattr(cp, attr).name = 'foo'
assert getattr(float_frame, attr).name is None
```

## Next Steps


---

*Source: test_copy.py:12 | Complexity: Intermediate | Last updated: 2026-06-02*