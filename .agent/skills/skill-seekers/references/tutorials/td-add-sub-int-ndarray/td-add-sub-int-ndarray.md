# How To: Td Add Sub Int Ndarray

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test td add sub int ndarray

## Prerequisites

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`


## Step-by-Step Guide

### Step 1: Assign td = Timedelta(...)

```python
td = Timedelta('1 day')
```

### Step 2: Assign other = np.array(...)

```python
other = np.array([1])
```

### Step 3: Assign msg = "unsupported operand type\\(s\\) for \\+: 'Timedelta' and 'int'"

```python
msg = "unsupported operand type\\(s\\) for \\+: 'Timedelta' and 'int'"
```

### Step 4: Assign msg = unknown.join(...)

```python
msg = '|'.join(["unsupported operand type\\(s\\) for \\+: 'numpy.ndarray' and 'Timedelta'", 'Concatenation operation is not implemented for NumPy arrays'])
```

### Step 5: Assign msg = "unsupported operand type\\(s\\) for -: 'Timedelta' and 'int'"

```python
msg = "unsupported operand type\\(s\\) for -: 'Timedelta' and 'int'"
```

### Step 6: Assign msg = "unsupported operand type\\(s\\) for -: 'numpy.ndarray' and 'Timedelta'"

```python
msg = "unsupported operand type\\(s\\) for -: 'numpy.ndarray' and 'Timedelta'"
```

### Step 7: td + np.array([1])

```python
td + np.array([1])
```

### Step 8: other + td

```python
other + td
```

### Step 9: td - other

```python
td - other
```

### Step 10: other - td

```python
other - td
```


## Complete Example

```python
# Workflow
td = Timedelta('1 day')
other = np.array([1])
msg = "unsupported operand type\\(s\\) for \\+: 'Timedelta' and 'int'"
with pytest.raises(TypeError, match=msg):
    td + np.array([1])
msg = '|'.join(["unsupported operand type\\(s\\) for \\+: 'numpy.ndarray' and 'Timedelta'", 'Concatenation operation is not implemented for NumPy arrays'])
with pytest.raises(TypeError, match=msg):
    other + td
msg = "unsupported operand type\\(s\\) for -: 'Timedelta' and 'int'"
with pytest.raises(TypeError, match=msg):
    td - other
msg = "unsupported operand type\\(s\\) for -: 'numpy.ndarray' and 'Timedelta'"
with pytest.raises(TypeError, match=msg):
    other - td
```

## Next Steps


---

*Source: test_arithmetic.py:207 | Complexity: Advanced | Last updated: 2026-06-02*