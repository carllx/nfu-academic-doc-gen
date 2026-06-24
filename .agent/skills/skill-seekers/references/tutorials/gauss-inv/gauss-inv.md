# How To: Gauss Inv

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test gauss inv

## Prerequisites

**Required Modules:**
- `os`
- `sys`
- `os.path`
- `pytest`
- `numpy`
- `numpy.random`
- `numpy.random._common`
- `numpy.testing`
- `cffi`
- `ctypes`
- `numpy.random.bit_generator`
- `numpy.random.bit_generator`
- `pickle`
- `pickle`
- `gzip`
- `pickle`


## Step-by-Step Guide

### Step 1: Assign n = 25

```python
n = 25
```

**Verification:**
```python
assert_allclose(gauss, gauss_from_uint(self.data1['data'], n, self.bits))
```

### Step 2: Assign rs = RandomState(...)

```python
rs = RandomState(self.bit_generator(*self.data1['seed']))
```

**Verification:**
```python
assert_allclose(gauss, gauss_from_uint(self.data2['data'], n, self.bits))
```

### Step 3: Assign gauss = rs.standard_normal(...)

```python
gauss = rs.standard_normal(n)
```

### Step 4: Call assert_allclose()

```python
assert_allclose(gauss, gauss_from_uint(self.data1['data'], n, self.bits))
```

### Step 5: Assign rs = RandomState(...)

```python
rs = RandomState(self.bit_generator(*self.data2['seed']))
```

### Step 6: Assign gauss = rs.standard_normal(...)

```python
gauss = rs.standard_normal(25)
```

### Step 7: Call assert_allclose()

```python
assert_allclose(gauss, gauss_from_uint(self.data2['data'], n, self.bits))
```


## Complete Example

```python
# Workflow
n = 25
rs = RandomState(self.bit_generator(*self.data1['seed']))
gauss = rs.standard_normal(n)
assert_allclose(gauss, gauss_from_uint(self.data1['data'], n, self.bits))
rs = RandomState(self.bit_generator(*self.data2['seed']))
gauss = rs.standard_normal(25)
assert_allclose(gauss, gauss_from_uint(self.data2['data'], n, self.bits))
```

## Next Steps


---

*Source: test_direct.py:248 | Complexity: Intermediate | Last updated: 2026-06-02*