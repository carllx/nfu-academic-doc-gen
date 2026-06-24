# How To: Uniform Double

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test uniform double

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

### Step 1: Assign rs = Generator(...)

```python
rs = Generator(self.bit_generator(*self.data1['seed']))
```

**Verification:**
```python
assert_allclose(uniforms, vals)
```

### Step 2: Assign vals = uniform_from_uint(...)

```python
vals = uniform_from_uint(self.data1['data'], self.bits)
```

**Verification:**
```python
assert_equal(uniforms.dtype, np.float64)
```

### Step 3: Assign uniforms = rs.random(...)

```python
uniforms = rs.random(len(vals))
```

**Verification:**
```python
assert_allclose(uniforms, vals)
```

### Step 4: Call assert_allclose()

```python
assert_allclose(uniforms, vals)
```

**Verification:**
```python
assert_equal(uniforms.dtype, np.float64)
```

### Step 5: Call assert_equal()

```python
assert_equal(uniforms.dtype, np.float64)
```

### Step 6: Assign rs = Generator(...)

```python
rs = Generator(self.bit_generator(*self.data2['seed']))
```

### Step 7: Assign vals = uniform_from_uint(...)

```python
vals = uniform_from_uint(self.data2['data'], self.bits)
```

### Step 8: Assign uniforms = rs.random(...)

```python
uniforms = rs.random(len(vals))
```

### Step 9: Call assert_allclose()

```python
assert_allclose(uniforms, vals)
```

### Step 10: Call assert_equal()

```python
assert_equal(uniforms.dtype, np.float64)
```


## Complete Example

```python
# Workflow
rs = Generator(self.bit_generator(*self.data1['seed']))
vals = uniform_from_uint(self.data1['data'], self.bits)
uniforms = rs.random(len(vals))
assert_allclose(uniforms, vals)
assert_equal(uniforms.dtype, np.float64)
rs = Generator(self.bit_generator(*self.data2['seed']))
vals = uniform_from_uint(self.data2['data'], self.bits)
uniforms = rs.random(len(vals))
assert_allclose(uniforms, vals)
assert_equal(uniforms.dtype, np.float64)
```

## Next Steps


---

*Source: test_direct.py:260 | Complexity: Advanced | Last updated: 2026-06-02*