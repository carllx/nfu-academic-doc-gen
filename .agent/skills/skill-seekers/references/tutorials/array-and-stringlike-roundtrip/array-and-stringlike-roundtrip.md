# How To: Array And Stringlike Roundtrip

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Test that string representations of long-double roundtrip both
for array casting and scalar coercion, see also gh-15608.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `platform`
- `warnings`
- `pytest`
- `numpy`
- `numpy._core.tests._locales`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: strtype
```

## Step-by-Step Guide

### Step 1: '\n    Test that string representations of long-double roundtrip both\n    for array casting and scalar coercion, see also gh-15608.\n    '

```python
'\n    Test that string representations of long-double roundtrip both\n    for array casting and scalar coercion, see also gh-15608.\n    '
```

**Verification:**
```python
assert o == np.longdouble(o_str)
```

### Step 2: Assign o = value

```python
o = 1 + LD_INFO.eps
```

**Verification:**
```python
assert (o == o_strarr.astype(np.longdouble)).all()
```

### Step 3: Assign o_strarr = np.asarray(...)

```python
o_strarr = np.asarray([o] * 3, dtype=strtype)
```

**Verification:**
```python
assert (o_strarr == o_str).all()
```

### Step 4: Assign o_str = strtype(...)

```python
o_str = strtype(str(o).encode('ascii'))
```

**Verification:**
```python
assert (np.asarray([o] * 3).astype(strtype) == o_str).all()
```

### Step 5: Assign o_str = strtype(...)

```python
o_str = strtype(str(o))
```


## Complete Example

```python
# Setup
# Fixtures: strtype

# Workflow
'\n    Test that string representations of long-double roundtrip both\n    for array casting and scalar coercion, see also gh-15608.\n    '
o = 1 + LD_INFO.eps
if strtype in (np.bytes_, bytes):
    o_str = strtype(str(o).encode('ascii'))
else:
    o_str = strtype(str(o))
assert o == np.longdouble(o_str)
o_strarr = np.asarray([o] * 3, dtype=strtype)
assert (o == o_strarr.astype(np.longdouble)).all()
assert (o_strarr == o_str).all()
assert (np.asarray([o] * 3).astype(strtype) == o_str).all()
```

## Next Steps


---

*Source: test_longdouble.py:58 | Complexity: Intermediate | Last updated: 2026-06-02*