# How To: Constructor Mismatched Codes Levels

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor mismatched codes levels

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.core.dtypes.cast`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: idx
```

## Step-by-Step Guide

### Step 1: Assign codes = value

```python
codes = [np.array([1]), np.array([2]), np.array([3])]
```

### Step 2: Assign levels = value

```python
levels = ['a']
```

### Step 3: Assign msg = 'Length of levels and codes must be the same'

```python
msg = 'Length of levels and codes must be the same'
```

### Step 4: Assign length_error = 'On level 0, code max \\(3\\) >= length of level \\(1\\)\\. NOTE: this index is in an inconsistent state'

```python
length_error = 'On level 0, code max \\(3\\) >= length of level \\(1\\)\\. NOTE: this index is in an inconsistent state'
```

### Step 5: Assign label_error = 'Unequal code lengths: \\[4, 2\\]'

```python
label_error = 'Unequal code lengths: \\[4, 2\\]'
```

### Step 6: Assign code_value_error = 'On level 0, code value \\(-2\\) < -1'

```python
code_value_error = 'On level 0, code value \\(-2\\) < -1'
```

### Step 7: Call idx.copy.set_codes()

```python
idx.copy().set_codes(codes=[[0, 0, 0, 0], [0, 0]], verify_integrity=False)
```

### Step 8: Call MultiIndex()

```python
MultiIndex(levels=levels, codes=codes)
```

### Step 9: Call MultiIndex()

```python
MultiIndex(levels=[['a'], ['b']], codes=[[0, 1, 2, 3], [0, 3, 4, 1]])
```

### Step 10: Call MultiIndex()

```python
MultiIndex(levels=[['a'], ['b']], codes=[[0, 0, 0, 0], [0, 0]])
```

### Step 11: Call idx.copy.set_levels()

```python
idx.copy().set_levels([['a'], ['b']])
```

### Step 12: Call idx.copy.set_codes()

```python
idx.copy().set_codes([[0, 0, 0, 0], [0, 0]])
```

### Step 13: Call MultiIndex()

```python
MultiIndex(levels=[['a'], ['b']], codes=[[0, -2], [0, 0]])
```


## Complete Example

```python
# Setup
# Fixtures: idx

# Workflow
codes = [np.array([1]), np.array([2]), np.array([3])]
levels = ['a']
msg = 'Length of levels and codes must be the same'
with pytest.raises(ValueError, match=msg):
    MultiIndex(levels=levels, codes=codes)
length_error = 'On level 0, code max \\(3\\) >= length of level \\(1\\)\\. NOTE: this index is in an inconsistent state'
label_error = 'Unequal code lengths: \\[4, 2\\]'
code_value_error = 'On level 0, code value \\(-2\\) < -1'
with pytest.raises(ValueError, match=length_error):
    MultiIndex(levels=[['a'], ['b']], codes=[[0, 1, 2, 3], [0, 3, 4, 1]])
with pytest.raises(ValueError, match=label_error):
    MultiIndex(levels=[['a'], ['b']], codes=[[0, 0, 0, 0], [0, 0]])
with pytest.raises(ValueError, match=length_error):
    idx.copy().set_levels([['a'], ['b']])
with pytest.raises(ValueError, match=label_error):
    idx.copy().set_codes([[0, 0, 0, 0], [0, 0]])
idx.copy().set_codes(codes=[[0, 0, 0, 0], [0, 0]], verify_integrity=False)
with pytest.raises(ValueError, match=code_value_error):
    MultiIndex(levels=[['a'], ['b']], codes=[[0, -2], [0, 0]])
```

## Next Steps


---

*Source: test_constructors.py:69 | Complexity: Advanced | Last updated: 2026-06-02*