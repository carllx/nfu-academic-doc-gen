# How To: Not All None

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test not all none

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
compat_args = {'foo': 1, 'bar': 's', 'baz': None}
```

### Step 4: Assign kwarg_keys = value

```python
kwarg_keys = ('foo', 'bar', 'baz')
```

### Step 5: Assign kwarg_vals = value

```python
kwarg_vals = (2, 's', None)
```

### Step 6: Assign kwargs = dict(...)

```python
kwargs = dict(zip(kwarg_keys[:i], kwarg_vals[:i]))
```

### Step 7: Call validate_kwargs()

```python
validate_kwargs(_fname, kwargs, compat_args)
```


## Complete Example

```python
# Setup
# Fixtures: i, _fname

# Workflow
bad_arg = 'foo'
msg = f"the '{bad_arg}' parameter is not supported in the pandas implementation of {_fname}\\(\\)"
compat_args = {'foo': 1, 'bar': 's', 'baz': None}
kwarg_keys = ('foo', 'bar', 'baz')
kwarg_vals = (2, 's', None)
kwargs = dict(zip(kwarg_keys[:i], kwarg_vals[:i]))
with pytest.raises(ValueError, match=msg):
    validate_kwargs(_fname, kwargs, compat_args)
```

## Next Steps


---

*Source: test_validate_kwargs.py:28 | Complexity: Intermediate | Last updated: 2026-06-02*