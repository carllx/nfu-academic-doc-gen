# How To: Converter With Structured Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test converter with structured dtype

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
txt = StringIO('1.5,2.5,Abc\n3.0,4.0,dEf\n5.5,6.0,ghI\n')
```

**Verification:**
```python
assert_equal(res, expected)
```

### Step 2: Assign dt = np.dtype(...)

```python
dt = np.dtype([('m', np.int32), ('r', np.float32), ('code', 'U8')])
```

### Step 3: Assign conv = value

```python
conv = {0: lambda s: int(10 * float(s)), -1: lambda s: s.upper()}
```

### Step 4: Assign res = np.loadtxt(...)

```python
res = np.loadtxt(txt, dtype=dt, delimiter=',', converters=conv)
```

### Step 5: Assign expected = np.array(...)

```python
expected = np.array([(15, 2.5, 'ABC'), (30, 4.0, 'DEF'), (55, 6.0, 'GHI')], dtype=dt)
```

### Step 6: Call assert_equal()

```python
assert_equal(res, expected)
```


## Complete Example

```python
# Workflow
txt = StringIO('1.5,2.5,Abc\n3.0,4.0,dEf\n5.5,6.0,ghI\n')
dt = np.dtype([('m', np.int32), ('r', np.float32), ('code', 'U8')])
conv = {0: lambda s: int(10 * float(s)), -1: lambda s: s.upper()}
res = np.loadtxt(txt, dtype=dt, delimiter=',', converters=conv)
expected = np.array([(15, 2.5, 'ABC'), (30, 4.0, 'DEF'), (55, 6.0, 'GHI')], dtype=dt)
assert_equal(res, expected)
```

## Next Steps


---

*Source: test_loadtxt.py:299 | Complexity: Intermediate | Last updated: 2026-06-02*