# How To: Str Size

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test str size

## Prerequisites

**Required Modules:**
- `collections`
- `functools`
- `string`
- `subprocess`
- `sys`
- `textwrap`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.common`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign a = 'a'

```python
a = 'a'
```

**Verification:**
```python
assert int(result) == int(expected)
```

### Step 2: Assign expected = sys.getsizeof(...)

```python
expected = sys.getsizeof(a)
```

### Step 3: Assign pyexe = sys.executable.replace(...)

```python
pyexe = sys.executable.replace('\\', '/')
```

### Step 4: Assign call = value

```python
call = [pyexe, '-c', "a='a';import sys;sys.getsizeof(a);import pandas;print(sys.getsizeof(a));"]
```

### Step 5: Assign result = unknown.strip(...)

```python
result = subprocess.check_output(call).decode()[-4:-1].strip('\n')
```

**Verification:**
```python
assert int(result) == int(expected)
```


## Complete Example

```python
# Workflow
a = 'a'
expected = sys.getsizeof(a)
pyexe = sys.executable.replace('\\', '/')
call = [pyexe, '-c', "a='a';import sys;sys.getsizeof(a);import pandas;print(sys.getsizeof(a));"]
result = subprocess.check_output(call).decode()[-4:-1].strip('\n')
assert int(result) == int(expected)
```

## Next Steps


---

*Source: test_common.py:238 | Complexity: Intermediate | Last updated: 2026-06-02*