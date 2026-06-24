# How To: Large Header

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test large header

## Prerequisites

**Required Modules:**
- `os`
- `sys`
- `warnings`
- `io`
- `pytest`
- `numpy`
- `numpy.lib`
- `numpy.testing`
- `numpy.testing._private.utils`
- `numpy.lib._utils_impl`
- `random`
- `subprocess`


## Step-by-Step Guide

### Step 1: Assign s = BytesIO(...)

```python
s = BytesIO()
```

**Verification:**
```python
assert_raises(ValueError, format.write_array_header_1_0, s, d)
```

### Step 2: Assign d = value

```python
d = {'shape': (), 'fortran_order': False, 'descr': '<i8'}
```

### Step 3: Call format.write_array_header_1_0()

```python
format.write_array_header_1_0(s, d)
```

### Step 4: Assign s = BytesIO(...)

```python
s = BytesIO()
```

### Step 5: Assign unknown = value

```python
d['descr'] = [('x' * 256 * 256, '<i8')]
```

### Step 6: Call assert_raises()

```python
assert_raises(ValueError, format.write_array_header_1_0, s, d)
```


## Complete Example

```python
# Workflow
s = BytesIO()
d = {'shape': (), 'fortran_order': False, 'descr': '<i8'}
format.write_array_header_1_0(s, d)
s = BytesIO()
d['descr'] = [('x' * 256 * 256, '<i8')]
assert_raises(ValueError, format.write_array_header_1_0, s, d)
```

## Next Steps


---

*Source: test_format.py:866 | Complexity: Intermediate | Last updated: 2026-06-02*