# How To: Variable Fixed Width

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test variable fixed width

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

### Step 1: Assign strg = '  1     3  4  5  6# test'

```python
strg = '  1     3  4  5  6# test'
```

**Verification:**
```python
assert_equal(test, ['1', '3', '4  5', '6'])
```

### Step 2: Assign test = LineSplitter(...)

```python
test = LineSplitter((3, 6, 6, 3))(strg)
```

**Verification:**
```python
assert_equal(test, ['1', '3  4', '5  6'])
```

### Step 3: Call assert_equal()

```python
assert_equal(test, ['1', '3', '4  5', '6'])
```

### Step 4: Assign strg = '  1     3  4  5  6# test'

```python
strg = '  1     3  4  5  6# test'
```

### Step 5: Assign test = LineSplitter(...)

```python
test = LineSplitter((6, 6, 9))(strg)
```

### Step 6: Call assert_equal()

```python
assert_equal(test, ['1', '3  4', '5  6'])
```


## Complete Example

```python
# Workflow
strg = '  1     3  4  5  6# test'
test = LineSplitter((3, 6, 6, 3))(strg)
assert_equal(test, ['1', '3', '4  5', '6'])
strg = '  1     3  4  5  6# test'
test = LineSplitter((6, 6, 9))(strg)
assert_equal(test, ['1', '3  4', '5  6'])
```

## Next Steps


---

*Source: test__iotools.py:75 | Complexity: Intermediate | Last updated: 2026-06-02*