# How To: To String With Formatters

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to string with formatters

## Prerequisites

**Required Modules:**
- `datetime`
- `io`
- `re`
- `sys`
- `textwrap`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'int': [1, 2, 3], 'float': [1.0, 2.0, 3.0], 'object': [(1, 2), True, False]}, columns=['int', 'float', 'object'])
```

**Verification:**
```python
assert result == '  int  float    object\n0 0x1 [ 1.0]  -(1, 2)-\n1 0x2 [ 2.0]    -True-\n2 0x3 [ 3.0]   -False-'
```

### Step 2: Assign formatters = value

```python
formatters = [('int', lambda x: f'0x{x:x}'), ('float', lambda x: f'[{x: 4.1f}]'), ('object', lambda x: f'-{x!s}-')]
```

**Verification:**
```python
assert result == result2
```

### Step 3: Assign result = df.to_string(...)

```python
result = df.to_string(formatters=dict(formatters))
```

### Step 4: Assign result2 = df.to_string(...)

```python
result2 = df.to_string(formatters=list(zip(*formatters))[1])
```

**Verification:**
```python
assert result == '  int  float    object\n0 0x1 [ 1.0]  -(1, 2)-\n1 0x2 [ 2.0]    -True-\n2 0x3 [ 3.0]   -False-'
```


## Complete Example

```python
# Workflow
df = DataFrame({'int': [1, 2, 3], 'float': [1.0, 2.0, 3.0], 'object': [(1, 2), True, False]}, columns=['int', 'float', 'object'])
formatters = [('int', lambda x: f'0x{x:x}'), ('float', lambda x: f'[{x: 4.1f}]'), ('object', lambda x: f'-{x!s}-')]
result = df.to_string(formatters=dict(formatters))
result2 = df.to_string(formatters=list(zip(*formatters))[1])
assert result == '  int  float    object\n0 0x1 [ 1.0]  -(1, 2)-\n1 0x2 [ 2.0]    -True-\n2 0x3 [ 3.0]   -False-'
assert result == result2
```

## Next Steps


---

*Source: test_to_string.py:55 | Complexity: Intermediate | Last updated: 2026-06-02*