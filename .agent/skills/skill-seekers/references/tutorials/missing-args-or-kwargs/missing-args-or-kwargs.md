# How To: Missing Args Or Kwargs

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test missing args or kwargs

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas.util._validators`

**Setup Required:**
```python
# Fixtures: args, kwargs, _fname
```

## Step-by-Step Guide

### Step 1: Assign bad_arg = 'bar'

```python
bad_arg = 'bar'
```

### Step 2: Assign min_fname_arg_count = 2

```python
min_fname_arg_count = 2
```

### Step 3: Assign compat_args = value

```python
compat_args = {'foo': -5, bad_arg: 1}
```

### Step 4: Assign msg = value

```python
msg = f"the '{bad_arg}' parameter is not supported in the pandas implementation of {_fname}\\(\\)"
```

### Step 5: Call validate_args_and_kwargs()

```python
validate_args_and_kwargs(_fname, args, kwargs, min_fname_arg_count, compat_args)
```


## Complete Example

```python
# Setup
# Fixtures: args, kwargs, _fname

# Workflow
bad_arg = 'bar'
min_fname_arg_count = 2
compat_args = {'foo': -5, bad_arg: 1}
msg = f"the '{bad_arg}' parameter is not supported in the pandas implementation of {_fname}\\(\\)"
with pytest.raises(ValueError, match=msg):
    validate_args_and_kwargs(_fname, args, kwargs, min_fname_arg_count, compat_args)
```

## Next Steps


---

*Source: test_validate_args_and_kwargs.py:48 | Complexity: Intermediate | Last updated: 2026-06-02*