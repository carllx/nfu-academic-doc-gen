# How To: Set Properties

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set properties

## Prerequisites

**Required Modules:**
- `contextlib`
- `copy`
- `re`
- `textwrap`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.io.formats.style`
- `pandas.io.formats.style_render`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [0, 1]})
```

**Verification:**
```python
assert result.keys() == expected.keys()
```

### Step 2: Assign result = value

```python
result = df.style.set_properties(color='white', size='10px')._compute().ctx
```

**Verification:**
```python
assert sorted(v1) == sorted(v2)
```

### Step 3: Assign v = value

```python
v = [('color', 'white'), ('size', '10px')]
```

### Step 4: Assign expected = value

```python
expected = {(0, 0): v, (1, 0): v}
```

**Verification:**
```python
assert result.keys() == expected.keys()
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': [0, 1]})
result = df.style.set_properties(color='white', size='10px')._compute().ctx
v = [('color', 'white'), ('size', '10px')]
expected = {(0, 0): v, (1, 0): v}
assert result.keys() == expected.keys()
for v1, v2 in zip(result.values(), expected.values()):
    assert sorted(v1) == sorted(v2)
```

## Next Steps


---

*Source: test_style.py:542 | Complexity: Intermediate | Last updated: 2026-06-02*