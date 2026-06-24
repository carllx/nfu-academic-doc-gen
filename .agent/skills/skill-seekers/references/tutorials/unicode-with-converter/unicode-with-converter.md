# How To: Unicode With Converter

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unicode with converter

## Prerequisites

**Required Modules:**
- `os`
- `sys`
- `io`
- `tempfile`
- `pytest`
- `numpy`
- `numpy.ma.testutils`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign txt = StringIO(...)

```python
txt = StringIO('cat,dog\nαβγ,δεζ\nabc,def\n')
```

**Verification:**
```python
assert_equal(res, expected)
```

### Step 2: Assign conv = value

```python
conv = {0: lambda s: s.upper()}
```

### Step 3: Assign res = np.loadtxt(...)

```python
res = np.loadtxt(txt, dtype=np.dtype('U12'), converters=conv, delimiter=',', encoding=None)
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([['CAT', 'dog'], ['ΑΒΓ', 'δεζ'], ['ABC', 'def']])
```

### Step 5: Call assert_equal()

```python
assert_equal(res, expected)
```


## Complete Example

```python
# Workflow
txt = StringIO('cat,dog\nαβγ,δεζ\nabc,def\n')
conv = {0: lambda s: s.upper()}
res = np.loadtxt(txt, dtype=np.dtype('U12'), converters=conv, delimiter=',', encoding=None)
expected = np.array([['CAT', 'dog'], ['ΑΒΓ', 'δεζ'], ['ABC', 'def']])
assert_equal(res, expected)
```

## Next Steps


---

*Source: test_loadtxt.py:285 | Complexity: Intermediate | Last updated: 2026-06-02*