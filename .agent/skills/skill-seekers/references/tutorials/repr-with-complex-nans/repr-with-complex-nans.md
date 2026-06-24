# How To: Repr With Complex Nans

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test repr with complex nans

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `io`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: data, output, as_frame
```

## Step-by-Step Guide

### Step 1: Assign obj = Series(...)

```python
obj = Series(np.array(data))
```

**Verification:**
```python
assert str(obj) == expected, f'\n{str(obj)}\n\n{expected}'
```

### Step 2: Assign obj = obj.to_frame(...)

```python
obj = obj.to_frame(name='val')
```

### Step 3: Assign reprs = value

```python
reprs = [f'{i} {val}' for i, val in enumerate(output)]
```

### Step 4: Assign expected = value

```python
expected = f"{'val': >{len(reprs[0])}}\n" + '\n'.join(reprs)
```

### Step 5: Assign reprs = value

```python
reprs = [f'{i}   {val}' for i, val in enumerate(output)]
```

### Step 6: Assign expected = value

```python
expected = '\n'.join(reprs) + '\ndtype: complex128'
```


## Complete Example

```python
# Setup
# Fixtures: data, output, as_frame

# Workflow
obj = Series(np.array(data))
if as_frame:
    obj = obj.to_frame(name='val')
    reprs = [f'{i} {val}' for i, val in enumerate(output)]
    expected = f"{'val': >{len(reprs[0])}}\n" + '\n'.join(reprs)
else:
    reprs = [f'{i}   {val}' for i, val in enumerate(output)]
    expected = '\n'.join(reprs) + '\ndtype: complex128'
assert str(obj) == expected, f'\n{str(obj)}\n\n{expected}'
```

## Next Steps


---

*Source: test_repr.py:508 | Complexity: Intermediate | Last updated: 2026-06-02*