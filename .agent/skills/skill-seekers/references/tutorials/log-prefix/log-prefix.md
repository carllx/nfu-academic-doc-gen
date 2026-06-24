# How To: Log Prefix

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test log prefix

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `re`
- `contextlib`
- `pytest`
- `numpy.distutils`

**Setup Required:**
```python
# Fixtures: func_name
```

## Step-by-Step Guide

### Step 1: Assign func = getattr(...)

```python
func = getattr(log, func_name)
```

**Verification:**
```python
assert out
```

### Step 2: Assign msg = value

```python
msg = f'{func_name} message'
```

**Verification:**
```python
assert line == f'{func_name.upper()}: {msg}'
```

### Step 3: Assign f = io.StringIO(...)

```python
f = io.StringIO()
```

### Step 4: Assign out = f.getvalue(...)

```python
out = f.getvalue()
```

**Verification:**
```python
assert out
```

### Step 5: Assign clean_out = r_ansi.sub(...)

```python
clean_out = r_ansi.sub('', out)
```

### Step 6: Assign line = next(...)

```python
line = next((line for line in clean_out.splitlines()))
```

**Verification:**
```python
assert line == f'{func_name.upper()}: {msg}'
```

### Step 7: Call func()

```python
func(msg)
```


## Complete Example

```python
# Setup
# Fixtures: func_name

# Workflow
func = getattr(log, func_name)
msg = f'{func_name} message'
f = io.StringIO()
with redirect_stdout(f):
    func(msg)
out = f.getvalue()
assert out
clean_out = r_ansi.sub('', out)
line = next((line for line in clean_out.splitlines()))
assert line == f'{func_name.upper()}: {msg}'
```

## Next Steps


---

*Source: test_log.py:24 | Complexity: Intermediate | Last updated: 2026-06-02*