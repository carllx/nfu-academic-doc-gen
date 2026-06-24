# How To: Pure Subclass Info Preservation

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pure subclass info preservation

## Prerequisites

**Required Modules:**
- `numpy`
- `numpy.lib.mixins`
- `numpy.ma.core`
- `numpy.ma.testutils`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign arr1 = SubMaskedArray(...)

```python
arr1 = SubMaskedArray('test', data=[1, 2, 3, 4, 5, 6])
```

**Verification:**
```python
assert_('info' in diff1._optinfo)
```

### Step 2: Assign arr2 = SubMaskedArray(...)

```python
arr2 = SubMaskedArray(data=[0, 1, 2, 3, 4, 5])
```

**Verification:**
```python
assert_(diff1._optinfo['info'] == 'test')
```

### Step 3: Assign diff1 = np.subtract(...)

```python
diff1 = np.subtract(arr1, arr2)
```

**Verification:**
```python
assert_('info' in diff2._optinfo)
```

### Step 4: Call assert_()

```python
assert_('info' in diff1._optinfo)
```

**Verification:**
```python
assert_(diff2._optinfo['info'] == 'test')
```

### Step 5: Call assert_()

```python
assert_(diff1._optinfo['info'] == 'test')
```

### Step 6: Assign diff2 = value

```python
diff2 = arr1 - arr2
```

### Step 7: Call assert_()

```python
assert_('info' in diff2._optinfo)
```

### Step 8: Call assert_()

```python
assert_(diff2._optinfo['info'] == 'test')
```


## Complete Example

```python
# Workflow
arr1 = SubMaskedArray('test', data=[1, 2, 3, 4, 5, 6])
arr2 = SubMaskedArray(data=[0, 1, 2, 3, 4, 5])
diff1 = np.subtract(arr1, arr2)
assert_('info' in diff1._optinfo)
assert_(diff1._optinfo['info'] == 'test')
diff2 = arr1 - arr2
assert_('info' in diff2._optinfo)
assert_(diff2._optinfo['info'] == 'test')
```

## Next Steps


---

*Source: test_subclassing.py:372 | Complexity: Advanced | Last updated: 2026-06-02*