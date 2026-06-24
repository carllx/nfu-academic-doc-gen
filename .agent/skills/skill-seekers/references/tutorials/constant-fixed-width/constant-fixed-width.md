# How To: Constant Fixed Width

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test LineSplitter w/ fixed-width fields

## Prerequisites

**Required Modules:**
- `time`
- `datetime`
- `pytest`
- `numpy`
- `numpy.lib._iotools`
- `numpy.testing`
- `numpy._core.numeric`


## Step-by-Step Guide

### Step 1: 'Test LineSplitter w/ fixed-width fields'

```python
'Test LineSplitter w/ fixed-width fields'
```

**Verification:**
```python
assert_equal(test, ['1', '2', '3', '4', '', '5', ''])
```

### Step 2: Assign strg = '  1  2  3  4     5   # test'

```python
strg = '  1  2  3  4     5   # test'
```

**Verification:**
```python
assert_equal(test, ['1     3  4  5  6'])
```

### Step 3: Assign test = LineSplitter(...)

```python
test = LineSplitter(3)(strg)
```

**Verification:**
```python
assert_equal(test, ['1     3  4  5  6'])
```

### Step 4: Call assert_equal()

```python
assert_equal(test, ['1', '2', '3', '4', '', '5', ''])
```

### Step 5: Assign strg = '  1     3  4  5  6# test'

```python
strg = '  1     3  4  5  6# test'
```

### Step 6: Assign test = LineSplitter(...)

```python
test = LineSplitter(20)(strg)
```

### Step 7: Call assert_equal()

```python
assert_equal(test, ['1     3  4  5  6'])
```

### Step 8: Assign strg = '  1     3  4  5  6# test'

```python
strg = '  1     3  4  5  6# test'
```

### Step 9: Assign test = LineSplitter(...)

```python
test = LineSplitter(30)(strg)
```

### Step 10: Call assert_equal()

```python
assert_equal(test, ['1     3  4  5  6'])
```


## Complete Example

```python
# Workflow
'Test LineSplitter w/ fixed-width fields'
strg = '  1  2  3  4     5   # test'
test = LineSplitter(3)(strg)
assert_equal(test, ['1', '2', '3', '4', '', '5', ''])
strg = '  1     3  4  5  6# test'
test = LineSplitter(20)(strg)
assert_equal(test, ['1     3  4  5  6'])
strg = '  1     3  4  5  6# test'
test = LineSplitter(30)(strg)
assert_equal(test, ['1     3  4  5  6'])
```

## Next Steps


---

*Source: test__iotools.py:61 | Complexity: Advanced | Last updated: 2026-06-02*