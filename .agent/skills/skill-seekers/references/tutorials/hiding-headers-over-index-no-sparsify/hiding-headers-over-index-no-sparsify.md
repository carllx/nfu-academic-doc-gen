# How To: Hiding Headers Over Index No Sparsify

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test hiding headers over index no sparsify

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

### Step 1: Assign midx = MultiIndex.from_product(...)

```python
midx = MultiIndex.from_product([[1, 2], ['a', 'a', 'b']])
```

**Verification:**
```python
assert len(ctx['body']) == 6
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(9, index=midx, columns=[0])
```

**Verification:**
```python
assert len(ctx['body']) == 4
```

### Step 3: Assign ctx = df.style._translate(...)

```python
ctx = df.style._translate(False, False)
```

**Verification:**
```python
assert 'row2' in ctx['body'][0][0]['class']
```

### Step 4: Assign ctx = df.style.hide._translate(...)

```python
ctx = df.style.hide((1, 'a'), axis=0)._translate(False, False)
```

**Verification:**
```python
assert len(ctx['body']) == 4
```


## Complete Example

```python
# Workflow
midx = MultiIndex.from_product([[1, 2], ['a', 'a', 'b']])
df = DataFrame(9, index=midx, columns=[0])
ctx = df.style._translate(False, False)
assert len(ctx['body']) == 6
ctx = df.style.hide((1, 'a'), axis=0)._translate(False, False)
assert len(ctx['body']) == 4
assert 'row2' in ctx['body'][0][0]['class']
```

## Next Steps


---

*Source: test_style.py:1486 | Complexity: Intermediate | Last updated: 2026-06-02*