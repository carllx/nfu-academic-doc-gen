# How To: Index Repr Bool Nan

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test index repr bool nan

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._config.config`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arr = Index(...)

```python
arr = Index([True, False, np.nan], dtype=object)
```

**Verification:**
```python
assert out1 == exp1
```

### Step 2: Assign msg = 'Index.format is deprecated'

```python
msg = 'Index.format is deprecated'
```

**Verification:**
```python
assert out2 == exp2
```

### Step 3: Assign out1 = value

```python
out1 = ['True', 'False', 'NaN']
```

**Verification:**
```python
assert out1 == exp1
```

### Step 4: Assign exp2 = repr(...)

```python
exp2 = repr(arr)
```

### Step 5: Assign out2 = "Index([True, False, nan], dtype='object')"

```python
out2 = "Index([True, False, nan], dtype='object')"
```

**Verification:**
```python
assert out2 == exp2
```

### Step 6: Assign exp1 = arr.format(...)

```python
exp1 = arr.format()
```


## Complete Example

```python
# Workflow
arr = Index([True, False, np.nan], dtype=object)
msg = 'Index.format is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    exp1 = arr.format()
out1 = ['True', 'False', 'NaN']
assert out1 == exp1
exp2 = repr(arr)
out2 = "Index([True, False, nan], dtype='object')"
assert out2 == exp2
```

## Next Steps


---

*Source: test_formats.py:144 | Complexity: Intermediate | Last updated: 2026-06-02*