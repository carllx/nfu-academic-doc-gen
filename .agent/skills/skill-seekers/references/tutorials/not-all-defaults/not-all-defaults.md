# How To: Not All Defaults

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test not all defaults

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas.util._validators`

**Setup Required:**
```python
# Fixtures: i, _fname
```

## Step-by-Step Guide

### Step 1: Assign bad_arg = 'foo'

```python
bad_arg = 'foo'
```

### Step 2: Assign msg = value

```python
msg = f"the '{bad_arg}' parameter is not supported in the pandas implementation of {_fname}\\(\\)"
```

### Step 3: Assign compat_args = value

```python
compat_args = {'foo': 2, 'bar': -1, 'baz': 3}
```

### Step 4: Assign arg_vals = value

```python
arg_vals = (1, -1, 3)
```

### Step 5: Call validate_args()

```python
validate_args(_fname, arg_vals[:i], 2, compat_args)
```


## Complete Example

```python
# Setup
# Fixtures: i, _fname

# Workflow
bad_arg = 'foo'
msg = f"the '{bad_arg}' parameter is not supported in the pandas implementation of {_fname}\\(\\)"
compat_args = {'foo': 2, 'bar': -1, 'baz': 3}
arg_vals = (1, -1, 3)
with pytest.raises(ValueError, match=msg):
    validate_args(_fname, arg_vals[:i], 2, compat_args)
```

## Next Steps


---

*Source: test_validate_args.py:51 | Complexity: Intermediate | Last updated: 2026-06-02*