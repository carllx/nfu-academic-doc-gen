# How To: Info Verbose Check Header Separator Body

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test info verbose check header separator body

## Prerequisites

**Required Modules:**
- `io`
- `re`
- `string`
- `sys`
- `textwrap`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign buf = StringIO(...)

```python
buf = StringIO()
```

**Verification:**
```python
assert header in res
```

### Step 2: Assign size = 1001

```python
size = 1001
```

**Verification:**
```python
assert len(lines) > 0
```

### Step 3: Assign start = 5

```python
start = 5
```

**Verification:**
```python
assert line.startswith(line_nr)
```

### Step 4: Assign frame = DataFrame(...)

```python
frame = DataFrame(np.random.default_rng(2).standard_normal((3, size)))
```

### Step 5: Call frame.info()

```python
frame.info(verbose=True, buf=buf)
```

### Step 6: Assign res = buf.getvalue(...)

```python
res = buf.getvalue()
```

### Step 7: Assign header = ' #     Column  Dtype  \n---    ------  -----  '

```python
header = ' #     Column  Dtype  \n---    ------  -----  '
```

**Verification:**
```python
assert header in res
```

### Step 8: Call frame.info()

```python
frame.info(verbose=True, buf=buf)
```

### Step 9: Call buf.seek()

```python
buf.seek(0)
```

### Step 10: Assign lines = buf.readlines(...)

```python
lines = buf.readlines()
```

**Verification:**
```python
assert len(lines) > 0
```

### Step 11: Assign line_nr = value

```python
line_nr = f' {i - start} '
```

**Verification:**
```python
assert line.startswith(line_nr)
```


## Complete Example

```python
# Workflow
buf = StringIO()
size = 1001
start = 5
frame = DataFrame(np.random.default_rng(2).standard_normal((3, size)))
frame.info(verbose=True, buf=buf)
res = buf.getvalue()
header = ' #     Column  Dtype  \n---    ------  -----  '
assert header in res
frame.info(verbose=True, buf=buf)
buf.seek(0)
lines = buf.readlines()
assert len(lines) > 0
for i, line in enumerate(lines):
    if start <= i < start + size:
        line_nr = f' {i - start} '
        assert line.startswith(line_nr)
```

## Next Steps


---

*Source: test_info.py:128 | Complexity: Advanced | Last updated: 2026-06-02*