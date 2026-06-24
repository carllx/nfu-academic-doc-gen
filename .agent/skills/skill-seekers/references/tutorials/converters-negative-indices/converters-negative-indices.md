# How To: Converters Negative Indices

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test converters negative indices

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
txt = StringIO('1.5,2.5\n3.0,XXX\n5.5,6.0')
```

**Verification:**
```python
assert_equal(res, expected)
```

### Step 2: Assign conv = value

```python
conv = {-1: lambda s: np.nan if s == 'XXX' else float(s)}
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array([[1.5, 2.5], [3.0, np.nan], [5.5, 6.0]])
```

### Step 4: Assign res = np.loadtxt(...)

```python
res = np.loadtxt(txt, dtype=np.float64, delimiter=',', converters=conv)
```

### Step 5: Call assert_equal()

```python
assert_equal(res, expected)
```


## Complete Example

```python
# Workflow
txt = StringIO('1.5,2.5\n3.0,XXX\n5.5,6.0')
conv = {-1: lambda s: np.nan if s == 'XXX' else float(s)}
expected = np.array([[1.5, 2.5], [3.0, np.nan], [5.5, 6.0]])
res = np.loadtxt(txt, dtype=np.float64, delimiter=',', converters=conv)
assert_equal(res, expected)
```

## Next Steps


---

*Source: test_loadtxt.py:217 | Complexity: Intermediate | Last updated: 2026-06-02*