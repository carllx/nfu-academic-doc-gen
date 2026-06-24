# How To: Other Delimiter

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test LineSplitter on delimiter

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

### Step 1: 'Test LineSplitter on delimiter'

```python
'Test LineSplitter on delimiter'
```

**Verification:**
```python
assert_equal(test, ['1', '2', '3', '4', '', '5'])
```

### Step 2: Assign strg = '1,2,3,4,,5'

```python
strg = '1,2,3,4,,5'
```

**Verification:**
```python
assert_equal(test, ['1', '2', '3', '4', '', '5'])
```

### Step 3: Assign test = LineSplitter(...)

```python
test = LineSplitter(',')(strg)
```

**Verification:**
```python
assert_equal(test, ['1', '2', '3', '4', '', '5'])
```

### Step 4: Call assert_equal()

```python
assert_equal(test, ['1', '2', '3', '4', '', '5'])
```

### Step 5: Assign strg = ' 1,2,3,4,,5 # test'

```python
strg = ' 1,2,3,4,,5 # test'
```

### Step 6: Assign test = LineSplitter(...)

```python
test = LineSplitter(',')(strg)
```

### Step 7: Call assert_equal()

```python
assert_equal(test, ['1', '2', '3', '4', '', '5'])
```

### Step 8: Assign strg = b' 1,2,3,4,,5 % test'

```python
strg = b' 1,2,3,4,,5 % test'
```

### Step 9: Assign test = LineSplitter(...)

```python
test = LineSplitter(delimiter=b',', comments=b'%')(strg)
```

### Step 10: Call assert_equal()

```python
assert_equal(test, ['1', '2', '3', '4', '', '5'])
```


## Complete Example

```python
# Workflow
'Test LineSplitter on delimiter'
strg = '1,2,3,4,,5'
test = LineSplitter(',')(strg)
assert_equal(test, ['1', '2', '3', '4', '', '5'])
strg = ' 1,2,3,4,,5 # test'
test = LineSplitter(',')(strg)
assert_equal(test, ['1', '2', '3', '4', '', '5'])
strg = b' 1,2,3,4,,5 % test'
test = LineSplitter(delimiter=b',', comments=b'%')(strg)
assert_equal(test, ['1', '2', '3', '4', '', '5'])
```

## Next Steps


---

*Source: test__iotools.py:46 | Complexity: Advanced | Last updated: 2026-06-02*