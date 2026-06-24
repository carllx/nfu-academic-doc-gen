# How To: Char Repeat

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test char repeat

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign np_s = np.bytes_(...)

```python
np_s = np.bytes_('abc')
```

**Verification:**
```python
assert_(np_s * 5 == res_s)
```

### Step 2: Assign np_u = np.str_(...)

```python
np_u = np.str_('abc')
```

**Verification:**
```python
assert_(np_u * 5 == res_u)
```

### Step 3: Assign res_s = value

```python
res_s = b'abc' * 5
```

### Step 4: Assign res_u = value

```python
res_u = 'abc' * 5
```

### Step 5: Call assert_()

```python
assert_(np_s * 5 == res_s)
```

### Step 6: Call assert_()

```python
assert_(np_u * 5 == res_u)
```


## Complete Example

```python
# Workflow
np_s = np.bytes_('abc')
np_u = np.str_('abc')
res_s = b'abc' * 5
res_u = 'abc' * 5
assert_(np_s * 5 == res_s)
assert_(np_u * 5 == res_u)
```

## Next Steps


---

*Source: test_scalarinherit.py:99 | Complexity: Intermediate | Last updated: 2026-06-02*