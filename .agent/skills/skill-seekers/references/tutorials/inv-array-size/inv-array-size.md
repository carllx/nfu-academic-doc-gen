# How To: Inv Array Size

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test inv array size

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `importlib`
- `io`
- `textwrap`
- `time`
- `pytest`
- `numpy`
- `numpy.f2py`
- `numpy.f2py.crackfortran`

**Setup Required:**
```python
# Fixtures: dimspec
```

## Step-by-Step Guide

### Step 1: Assign count = self.all_dimspecs.index(...)

```python
count = self.all_dimspecs.index(dimspec)
```

**Verification:**
```python
assert sz == sz1, (n, n1, sz, sz1)
```

### Step 2: Assign get_arr_size = getattr(...)

```python
get_arr_size = getattr(self.module, f'get_arr_size_{count}')
```

### Step 3: Assign get_inv_arr_size = getattr(...)

```python
get_inv_arr_size = getattr(self.module, f'get_inv_arr_size_{count}')
```

### Step 4: Assign unknown = get_arr_size(...)

```python
sz, a = get_arr_size(n)
```

### Step 5: Assign unknown = get_arr_size(...)

```python
sz1, _ = get_arr_size(n1)
```

**Verification:**
```python
assert sz == sz1, (n, n1, sz, sz1)
```

### Step 6: Assign n1 = get_inv_arr_size(...)

```python
n1 = get_inv_arr_size(a, n)
```

### Step 7: Assign n1 = get_inv_arr_size(...)

```python
n1 = get_inv_arr_size(a)
```


## Complete Example

```python
# Setup
# Fixtures: dimspec

# Workflow
count = self.all_dimspecs.index(dimspec)
get_arr_size = getattr(self.module, f'get_arr_size_{count}')
get_inv_arr_size = getattr(self.module, f'get_inv_arr_size_{count}')
for n in [1, 2, 3, 4, 5]:
    sz, a = get_arr_size(n)
    if dimspec in self.nonlinear_dimspecs:
        n1 = get_inv_arr_size(a, n)
    else:
        n1 = get_inv_arr_size(a)
    sz1, _ = get_arr_size(n1)
    assert sz == sz1, (n, n1, sz, sz1)
```

## Next Steps


---

*Source: test_crackfortran.py:232 | Complexity: Intermediate | Last updated: 2026-06-02*