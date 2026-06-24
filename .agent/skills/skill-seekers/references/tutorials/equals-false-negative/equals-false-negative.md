# How To: Equals False Negative

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test equals false negative

## Prerequisites

**Required Modules:**
- `contextlib`
- `copy`
- `numpy`
- `pytest`
- `pandas._libs.missing`
- `pandas.compat.numpy`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arr = value

```python
arr = [False, np.nan]
```

**Verification:**
```python
assert s1.equals(s1)
```

### Step 2: Assign s1 = Series(...)

```python
s1 = Series(arr)
```

**Verification:**
```python
assert s1.equals(s2)
```

### Step 3: Assign s2 = s1.copy(...)

```python
s2 = s1.copy()
```

**Verification:**
```python
assert s1.equals(s3)
```

### Step 4: Assign s3 = Series(...)

```python
s3 = Series(index=range(2), dtype=object)
```

**Verification:**
```python
assert s1.equals(s4)
```

### Step 5: Assign s4 = s3.copy(...)

```python
s4 = s3.copy()
```

**Verification:**
```python
assert s1.equals(s5)
```

### Step 6: Assign s5 = s3.copy(...)

```python
s5 = s3.copy()
```

**Verification:**
```python
assert s5.equals(s6)
```

### Step 7: Assign s6 = s3.copy(...)

```python
s6 = s3.copy()
```

### Step 8: Assign unknown, unknown, unknown, unknown = False

```python
s3[:-1] = s4[:-1] = s5[0] = s6[0] = False
```

**Verification:**
```python
assert s1.equals(s1)
```


## Complete Example

```python
# Workflow
arr = [False, np.nan]
s1 = Series(arr)
s2 = s1.copy()
s3 = Series(index=range(2), dtype=object)
s4 = s3.copy()
s5 = s3.copy()
s6 = s3.copy()
s3[:-1] = s4[:-1] = s5[0] = s6[0] = False
assert s1.equals(s1)
assert s1.equals(s2)
assert s1.equals(s3)
assert s1.equals(s4)
assert s1.equals(s5)
assert s5.equals(s6)
```

## Next Steps


---

*Source: test_equals.py:61 | Complexity: Advanced | Last updated: 2026-06-02*