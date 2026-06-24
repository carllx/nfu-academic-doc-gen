# How To: Delete Base

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test delete base

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `weakref`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: index
```

## Step-by-Step Guide

### Step 1: Assign expected = value

```python
expected = index[1:]
```

**Verification:**
```python
assert result.equals(expected)
```

### Step 2: Assign result = index.delete(...)

```python
result = index.delete(0)
```

**Verification:**
```python
assert result.name == expected.name
```

### Step 3: Assign expected = value

```python
expected = index[:-1]
```

**Verification:**
```python
assert result.equals(expected)
```

### Step 4: Assign result = index.delete(...)

```python
result = index.delete(-1)
```

**Verification:**
```python
assert result.name == expected.name
```

### Step 5: Assign length = len(...)

```python
length = len(index)
```

### Step 6: Assign msg = value

```python
msg = f'index {length} is out of bounds for axis 0 with size {length}'
```

### Step 7: Call pytest.skip()

```python
pytest.skip('Not applicable for empty index')
```

### Step 8: Call pytest.skip()

```python
pytest.skip(f'{type(self).__name__} tested elsewhere')
```

### Step 9: Call index.delete()

```python
index.delete(length)
```


## Complete Example

```python
# Setup
# Fixtures: index

# Workflow
if not len(index):
    pytest.skip('Not applicable for empty index')
if isinstance(index, RangeIndex):
    pytest.skip(f'{type(self).__name__} tested elsewhere')
expected = index[1:]
result = index.delete(0)
assert result.equals(expected)
assert result.name == expected.name
expected = index[:-1]
result = index.delete(-1)
assert result.equals(expected)
assert result.name == expected.name
length = len(index)
msg = f'index {length} is out of bounds for axis 0 with size {length}'
with pytest.raises(IndexError, match=msg):
    index.delete(length)
```

## Next Steps


---

*Source: test_old_base.py:467 | Complexity: Advanced | Last updated: 2026-06-02*