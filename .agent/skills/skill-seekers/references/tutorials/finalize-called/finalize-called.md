# How To: Finalize Called

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test finalize called

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: ndframe_method
```

## Step-by-Step Guide

### Step 1: Assign unknown = ndframe_method

```python
cls, init_args, method = ndframe_method
```

**Verification:**
```python
assert result.attrs == {'a': 1}
```

### Step 2: Assign ndframe = cls(...)

```python
ndframe = cls(*init_args)
```

### Step 3: Assign ndframe.attrs = value

```python
ndframe.attrs = {'a': 1}
```

### Step 4: Assign result = method(...)

```python
result = method(ndframe)
```

**Verification:**
```python
assert result.attrs == {'a': 1}
```


## Complete Example

```python
# Setup
# Fixtures: ndframe_method

# Workflow
cls, init_args, method = ndframe_method
ndframe = cls(*init_args)
ndframe.attrs = {'a': 1}
result = method(ndframe)
assert result.attrs == {'a': 1}
```

## Next Steps


---

*Source: test_finalize.py:401 | Complexity: Intermediate | Last updated: 2026-06-02*