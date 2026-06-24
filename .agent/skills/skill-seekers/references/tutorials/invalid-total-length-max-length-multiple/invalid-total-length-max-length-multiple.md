# How To: Invalid Total Length Max Length Multiple

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test invalid total length max length multiple

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas.util._validators`

**Setup Required:**
```python
# Fixtures: _fname
```

## Step-by-Step Guide

### Step 1: Assign compat_args = value

```python
compat_args = ('foo', 'bar', 'baz')
```

### Step 2: Assign kwargs = value

```python
kwargs = {'foo': 'FOO', 'bar': 'BAR'}
```

### Step 3: Assign args = value

```python
args = ('FoO', 'BaZ')
```

### Step 4: Assign min_fname_arg_count = 2

```python
min_fname_arg_count = 2
```

### Step 5: Assign max_length = value

```python
max_length = len(compat_args) + min_fname_arg_count
```

### Step 6: Assign actual_length = value

```python
actual_length = len(kwargs) + len(args) + min_fname_arg_count
```

### Step 7: Assign msg = value

```python
msg = f'{_fname}\\(\\) takes at most {max_length} arguments \\({actual_length} given\\)'
```

### Step 8: Call validate_args_and_kwargs()

```python
validate_args_and_kwargs(_fname, args, kwargs, min_fname_arg_count, compat_args)
```


## Complete Example

```python
# Setup
# Fixtures: _fname

# Workflow
compat_args = ('foo', 'bar', 'baz')
kwargs = {'foo': 'FOO', 'bar': 'BAR'}
args = ('FoO', 'BaZ')
min_fname_arg_count = 2
max_length = len(compat_args) + min_fname_arg_count
actual_length = len(kwargs) + len(args) + min_fname_arg_count
msg = f'{_fname}\\(\\) takes at most {max_length} arguments \\({actual_length} given\\)'
with pytest.raises(TypeError, match=msg):
    validate_args_and_kwargs(_fname, args, kwargs, min_fname_arg_count, compat_args)
```

## Next Steps


---

*Source: test_validate_args_and_kwargs.py:29 | Complexity: Advanced | Last updated: 2026-06-02*