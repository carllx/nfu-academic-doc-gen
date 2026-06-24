# How To: Logical Operators Int Dtype With Float

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test logical operators int dtype with float

## Prerequisites

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas._testing`
- `pandas.core`


## Step-by-Step Guide

### Step 1: Assign s_0123 = Series(...)

```python
s_0123 = Series(range(4), dtype='int64')
```

### Step 2: Assign warn_msg = 'Logical ops \\(and, or, xor\\) between Pandas objects and dtype-less sequences'

```python
warn_msg = 'Logical ops \\(and, or, xor\\) between Pandas objects and dtype-less sequences'
```

### Step 3: Assign msg = 'Cannot perform.+with a dtyped.+array and scalar of type'

```python
msg = 'Cannot perform.+with a dtyped.+array and scalar of type'
```

### Step 4: Assign msg = 'unsupported operand type.+for &:'

```python
msg = 'unsupported operand type.+for &:'
```

### Step 5: s_0123 & np.nan

```python
s_0123 & np.nan
```

### Step 6: s_0123 & 3.14

```python
s_0123 & 3.14
```

### Step 7: s_0123 & np.array([0.1, 4, 3.14, 2])

```python
s_0123 & np.array([0.1, 4, 3.14, 2])
```

### Step 8: s_0123 & Series([0.1, 4, -3.14, 2])

```python
s_0123 & Series([0.1, 4, -3.14, 2])
```

### Step 9: s_0123 & [0.1, 4, 3.14, 2]

```python
s_0123 & [0.1, 4, 3.14, 2]
```


## Complete Example

```python
# Workflow
s_0123 = Series(range(4), dtype='int64')
warn_msg = 'Logical ops \\(and, or, xor\\) between Pandas objects and dtype-less sequences'
msg = 'Cannot perform.+with a dtyped.+array and scalar of type'
with pytest.raises(TypeError, match=msg):
    s_0123 & np.nan
with pytest.raises(TypeError, match=msg):
    s_0123 & 3.14
msg = 'unsupported operand type.+for &:'
with pytest.raises(TypeError, match=msg):
    with tm.assert_produces_warning(FutureWarning, match=warn_msg):
        s_0123 & [0.1, 4, 3.14, 2]
with pytest.raises(TypeError, match=msg):
    s_0123 & np.array([0.1, 4, 3.14, 2])
with pytest.raises(TypeError, match=msg):
    s_0123 & Series([0.1, 4, -3.14, 2])
```

## Next Steps


---

*Source: test_logical_ops.py:90 | Complexity: Advanced | Last updated: 2026-06-02*