# How To: Get Fieldstructure

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get fieldstructure

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.ma`
- `numpy.lib.recfunctions`
- `numpy.ma.mrecords`
- `numpy.ma.testutils`
- `numpy.testing`
- `datetime`


## Step-by-Step Guide

### Step 1: Assign ndtype = np.dtype(...)

```python
ndtype = np.dtype([('A', '|S3'), ('B', float)])
```

**Verification:**
```python
assert_equal(test, {'A': [], 'B': []})
```

### Step 2: Assign test = get_fieldstructure(...)

```python
test = get_fieldstructure(ndtype)
```

**Verification:**
```python
assert_equal(test, {'A': [], 'B': [], 'BA': ['B'], 'BB': ['B']})
```

### Step 3: Call assert_equal()

```python
assert_equal(test, {'A': [], 'B': []})
```

**Verification:**
```python
assert_equal(test, control)
```

### Step 4: Assign ndtype = np.dtype(...)

```python
ndtype = np.dtype([('A', int), ('B', [('BA', float), ('BB', '|S1')])])
```

**Verification:**
```python
assert_equal(test, {})
```

### Step 5: Assign test = get_fieldstructure(...)

```python
test = get_fieldstructure(ndtype)
```

### Step 6: Call assert_equal()

```python
assert_equal(test, {'A': [], 'B': [], 'BA': ['B'], 'BB': ['B']})
```

### Step 7: Assign ndtype = np.dtype(...)

```python
ndtype = np.dtype([('A', int), ('B', [('BA', int), ('BB', [('BBA', int), ('BBB', int)])])])
```

### Step 8: Assign test = get_fieldstructure(...)

```python
test = get_fieldstructure(ndtype)
```

### Step 9: Assign control = value

```python
control = {'A': [], 'B': [], 'BA': ['B'], 'BB': ['B'], 'BBA': ['B', 'BB'], 'BBB': ['B', 'BB']}
```

### Step 10: Call assert_equal()

```python
assert_equal(test, control)
```

### Step 11: Assign ndtype = np.dtype(...)

```python
ndtype = np.dtype([])
```

### Step 12: Assign test = get_fieldstructure(...)

```python
test = get_fieldstructure(ndtype)
```

### Step 13: Call assert_equal()

```python
assert_equal(test, {})
```


## Complete Example

```python
# Workflow
ndtype = np.dtype([('A', '|S3'), ('B', float)])
test = get_fieldstructure(ndtype)
assert_equal(test, {'A': [], 'B': []})
ndtype = np.dtype([('A', int), ('B', [('BA', float), ('BB', '|S1')])])
test = get_fieldstructure(ndtype)
assert_equal(test, {'A': [], 'B': [], 'BA': ['B'], 'BB': ['B']})
ndtype = np.dtype([('A', int), ('B', [('BA', int), ('BB', [('BBA', int), ('BBB', int)])])])
test = get_fieldstructure(ndtype)
control = {'A': [], 'B': [], 'BA': ['B'], 'BB': ['B'], 'BBA': ['B', 'BB'], 'BBB': ['B', 'BB']}
assert_equal(test, control)
ndtype = np.dtype([])
test = get_fieldstructure(ndtype)
assert_equal(test, {})
```

## Next Steps


---

*Source: test_recfunctions.py:152 | Complexity: Advanced | Last updated: 2026-06-02*