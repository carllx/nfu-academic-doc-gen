# How To: Tab Delimiter

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test tab delimiter

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

### Step 1: 'Test tab delimiter'

```python
'Test tab delimiter'
```

**Verification:**
```python
assert_equal(test, ['1', '2', '3', '4', '5  6'])
```

### Step 2: Assign strg = ' 1\t 2\t 3\t 4\t 5  6'

```python
strg = ' 1\t 2\t 3\t 4\t 5  6'
```

**Verification:**
```python
assert_equal(test, ['1  2', '3  4', '5  6'])
```

### Step 3: Assign test = LineSplitter(...)

```python
test = LineSplitter('\t')(strg)
```

### Step 4: Call assert_equal()

```python
assert_equal(test, ['1', '2', '3', '4', '5  6'])
```

### Step 5: Assign strg = ' 1  2\t 3  4\t 5  6'

```python
strg = ' 1  2\t 3  4\t 5  6'
```

### Step 6: Assign test = LineSplitter(...)

```python
test = LineSplitter('\t')(strg)
```

### Step 7: Call assert_equal()

```python
assert_equal(test, ['1  2', '3  4', '5  6'])
```


## Complete Example

```python
# Workflow
'Test tab delimiter'
strg = ' 1\t 2\t 3\t 4\t 5  6'
test = LineSplitter('\t')(strg)
assert_equal(test, ['1', '2', '3', '4', '5  6'])
strg = ' 1  2\t 3  4\t 5  6'
test = LineSplitter('\t')(strg)
assert_equal(test, ['1  2', '3  4', '5  6'])
```

## Next Steps


---

*Source: test__iotools.py:37 | Complexity: Intermediate | Last updated: 2026-06-02*