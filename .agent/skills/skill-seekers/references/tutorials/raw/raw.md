# How To: Raw

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test raw

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

### Step 1: Assign bit_generator = self.bit_generator(...)

```python
bit_generator = self.bit_generator(*self.data1['seed'])
```

**Verification:**
```python
assert_equal(uints, self.data1['data'])
```

### Step 2: Assign uints = bit_generator.random_raw(...)

```python
uints = bit_generator.random_raw(1000)
```

**Verification:**
```python
assert_equal(uints, self.data1['data'][0])
```

### Step 3: Call assert_equal()

```python
assert_equal(uints, self.data1['data'])
```

**Verification:**
```python
assert_equal(uints, self.data2['data'])
```

### Step 4: Assign bit_generator = self.bit_generator(...)

```python
bit_generator = self.bit_generator(*self.data1['seed'])
```

### Step 5: Assign uints = bit_generator.random_raw(...)

```python
uints = bit_generator.random_raw()
```

### Step 6: Call assert_equal()

```python
assert_equal(uints, self.data1['data'][0])
```

### Step 7: Assign bit_generator = self.bit_generator(...)

```python
bit_generator = self.bit_generator(*self.data2['seed'])
```

### Step 8: Assign uints = bit_generator.random_raw(...)

```python
uints = bit_generator.random_raw(1000)
```

### Step 9: Call assert_equal()

```python
assert_equal(uints, self.data2['data'])
```


## Complete Example

```python
# Workflow
bit_generator = self.bit_generator(*self.data1['seed'])
uints = bit_generator.random_raw(1000)
assert_equal(uints, self.data1['data'])
bit_generator = self.bit_generator(*self.data1['seed'])
uints = bit_generator.random_raw()
assert_equal(uints, self.data1['data'][0])
bit_generator = self.bit_generator(*self.data2['seed'])
uints = bit_generator.random_raw(1000)
assert_equal(uints, self.data2['data'])
```

## Next Steps


---

*Source: test_direct.py:228 | Complexity: Advanced | Last updated: 2026-06-02*