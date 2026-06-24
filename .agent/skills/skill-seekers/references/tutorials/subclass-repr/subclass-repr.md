# How To: Subclass Repr

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test that repr uses the name of the subclass
and 'array' for np.ndarray

## Prerequisites

**Required Modules:**
- `numpy`
- `numpy.lib.mixins`
- `numpy.ma.core`
- `numpy.ma.testutils`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: "test that repr uses the name of the subclass\n        and 'array' for np.ndarray"

```python
"test that repr uses the name of the subclass\n        and 'array' for np.ndarray"
```

**Verification:**
```python
assert_startswith(repr(mx), 'masked_array')
```

### Step 2: Assign x = np.arange(...)

```python
x = np.arange(5)
```

**Verification:**
```python
assert_startswith(repr(mxsub), f'masked_{SubArray.__name__}(data=[--, 1, --, 3, 4]')
```

### Step 3: Assign mx = masked_array(...)

```python
mx = masked_array(x, mask=[True, False, True, False, False])
```

### Step 4: Call assert_startswith()

```python
assert_startswith(repr(mx), 'masked_array')
```

### Step 5: Assign xsub = SubArray(...)

```python
xsub = SubArray(x)
```

### Step 6: Assign mxsub = masked_array(...)

```python
mxsub = masked_array(xsub, mask=[True, False, True, False, False])
```

### Step 7: Call assert_startswith()

```python
assert_startswith(repr(mxsub), f'masked_{SubArray.__name__}(data=[--, 1, --, 3, 4]')
```


## Complete Example

```python
# Workflow
"test that repr uses the name of the subclass\n        and 'array' for np.ndarray"
x = np.arange(5)
mx = masked_array(x, mask=[True, False, True, False, False])
assert_startswith(repr(mx), 'masked_array')
xsub = SubArray(x)
mxsub = masked_array(xsub, mask=[True, False, True, False, False])
assert_startswith(repr(mxsub), f'masked_{SubArray.__name__}(data=[--, 1, --, 3, 4]')
```

## Next Steps


---

*Source: test_subclassing.py:347 | Complexity: Intermediate | Last updated: 2026-06-02*