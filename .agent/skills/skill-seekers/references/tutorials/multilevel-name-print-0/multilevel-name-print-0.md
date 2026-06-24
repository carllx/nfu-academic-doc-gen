# How To: Multilevel Name Print 0

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multilevel name print 0

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign mi = pd.MultiIndex.from_product(...)

```python
mi = pd.MultiIndex.from_product([range(2, 3), range(3, 4)], names=[0, None])
```

**Verification:**
```python
assert res == expected
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(1.5, index=mi)
```

### Step 3: Assign res = repr(...)

```python
res = repr(ser)
```

### Step 4: Assign expected = '0   \n2  3    1.5\ndtype: float64'

```python
expected = '0   \n2  3    1.5\ndtype: float64'
```

**Verification:**
```python
assert res == expected
```


## Complete Example

```python
# Workflow
mi = pd.MultiIndex.from_product([range(2, 3), range(3, 4)], names=[0, None])
ser = Series(1.5, index=mi)
res = repr(ser)
expected = '0   \n2  3    1.5\ndtype: float64'
assert res == expected
```

## Next Steps


---

*Source: test_formats.py:24 | Complexity: Intermediate | Last updated: 2026-06-02*