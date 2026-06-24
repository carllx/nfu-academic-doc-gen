# How To: Rename Fields

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rename fields

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

### Step 1: Assign a = np.array(...)

```python
a = np.array([(1, (2, [3.0, 30.0])), (4, (5, [6.0, 60.0]))], dtype=[('a', int), ('b', [('ba', float), ('bb', (float, 2))])])
```

**Verification:**
```python
assert_equal(test.dtype, newdtype)
```

### Step 2: Assign test = rename_fields(...)

```python
test = rename_fields(a, {'a': 'A', 'bb': 'BB'})
```

**Verification:**
```python
assert_equal(test, control)
```

### Step 3: Assign newdtype = value

```python
newdtype = [('A', int), ('b', [('ba', float), ('BB', (float, 2))])]
```

### Step 4: Assign control = a.view(...)

```python
control = a.view(newdtype)
```

### Step 5: Call assert_equal()

```python
assert_equal(test.dtype, newdtype)
```

### Step 6: Call assert_equal()

```python
assert_equal(test, control)
```


## Complete Example

```python
# Workflow
a = np.array([(1, (2, [3.0, 30.0])), (4, (5, [6.0, 60.0]))], dtype=[('a', int), ('b', [('ba', float), ('bb', (float, 2))])])
test = rename_fields(a, {'a': 'A', 'bb': 'BB'})
newdtype = [('A', int), ('b', [('ba', float), ('BB', (float, 2))])]
control = a.view(newdtype)
assert_equal(test.dtype, newdtype)
assert_equal(test, control)
```

## Next Steps


---

*Source: test_recfunctions.py:105 | Complexity: Intermediate | Last updated: 2026-06-02*