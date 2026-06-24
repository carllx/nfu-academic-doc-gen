# How To: Ensure String List

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ensure string list

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `distutils`
- `distutils.cmd`
- `distutils.dist`
- `distutils.errors`
- `pytest`

**Setup Required:**
```python
# Fixtures: cmd
```

## Step-by-Step Guide

### Step 1: Assign cmd.not_string_list = value

```python
cmd.not_string_list = ['one', 2, 'three']
```

**Verification:**
```python
assert cmd.option1 == ['ok', 'dok']
```

### Step 2: Assign cmd.yes_string_list = value

```python
cmd.yes_string_list = ['one', 'two', 'three']
```

### Step 3: Assign cmd.not_string_list2 = object(...)

```python
cmd.not_string_list2 = object()
```

### Step 4: Assign cmd.yes_string_list2 = 'ok'

```python
cmd.yes_string_list2 = 'ok'
```

### Step 5: Call cmd.ensure_string_list()

```python
cmd.ensure_string_list('yes_string_list')
```

### Step 6: Call cmd.ensure_string_list()

```python
cmd.ensure_string_list('yes_string_list2')
```

### Step 7: Assign cmd.option1 = 'ok,dok'

```python
cmd.option1 = 'ok,dok'
```

### Step 8: Call cmd.ensure_string_list()

```python
cmd.ensure_string_list('option1')
```

**Verification:**
```python
assert cmd.option1 == ['ok', 'dok']
```

### Step 9: Assign cmd.option2 = value

```python
cmd.option2 = ['xxx', 'www']
```

### Step 10: Call cmd.ensure_string_list()

```python
cmd.ensure_string_list('option2')
```

### Step 11: Assign cmd.option3 = value

```python
cmd.option3 = ['ok', 2]
```

### Step 12: Call cmd.ensure_string_list()

```python
cmd.ensure_string_list('not_string_list')
```

### Step 13: Call cmd.ensure_string_list()

```python
cmd.ensure_string_list('not_string_list2')
```

### Step 14: Call cmd.ensure_string_list()

```python
cmd.ensure_string_list('option3')
```


## Complete Example

```python
# Setup
# Fixtures: cmd

# Workflow
cmd.not_string_list = ['one', 2, 'three']
cmd.yes_string_list = ['one', 'two', 'three']
cmd.not_string_list2 = object()
cmd.yes_string_list2 = 'ok'
cmd.ensure_string_list('yes_string_list')
cmd.ensure_string_list('yes_string_list2')
with pytest.raises(DistutilsOptionError):
    cmd.ensure_string_list('not_string_list')
with pytest.raises(DistutilsOptionError):
    cmd.ensure_string_list('not_string_list2')
cmd.option1 = 'ok,dok'
cmd.ensure_string_list('option1')
assert cmd.option1 == ['ok', 'dok']
cmd.option2 = ['xxx', 'www']
cmd.ensure_string_list('option2')
cmd.option3 = ['ok', 2]
with pytest.raises(DistutilsOptionError):
    cmd.ensure_string_list('option3')
```

## Next Steps


---

*Source: test_cmd.py:23 | Complexity: Advanced | Last updated: 2026-06-02*