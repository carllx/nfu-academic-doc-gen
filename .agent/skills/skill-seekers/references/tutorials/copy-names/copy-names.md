# How To: Copy Names

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test copy names

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign multi_idx = MultiIndex.from_tuples(...)

```python
multi_idx = MultiIndex.from_tuples([(1, 2), (3, 4)], names=['MyName1', 'MyName2'])
```

**Verification:**
```python
assert multi_idx.equals(multi_idx1)
```

### Step 2: Assign multi_idx1 = multi_idx.copy(...)

```python
multi_idx1 = multi_idx.copy()
```

**Verification:**
```python
assert multi_idx.names == ['MyName1', 'MyName2']
```

### Step 3: Assign multi_idx2 = multi_idx.copy(...)

```python
multi_idx2 = multi_idx.copy(names=['NewName1', 'NewName2'])
```

**Verification:**
```python
assert multi_idx1.names == ['MyName1', 'MyName2']
```

### Step 4: Assign multi_idx3 = multi_idx.copy(...)

```python
multi_idx3 = multi_idx.copy(name=['NewName1', 'NewName2'])
```

**Verification:**
```python
assert multi_idx.equals(multi_idx2)
```

### Step 5: Call multi_idx.copy()

```python
multi_idx.copy(names=['mario'])
```

**Verification:**
```python
assert multi_idx.names == ['MyName1', 'MyName2']
```

### Step 6: Call multi_idx.copy()

```python
multi_idx.copy(names=[['mario'], ['luigi']])
```

**Verification:**
```python
assert multi_idx2.names == ['NewName1', 'NewName2']
```


## Complete Example

```python
# Workflow
multi_idx = MultiIndex.from_tuples([(1, 2), (3, 4)], names=['MyName1', 'MyName2'])
multi_idx1 = multi_idx.copy()
assert multi_idx.equals(multi_idx1)
assert multi_idx.names == ['MyName1', 'MyName2']
assert multi_idx1.names == ['MyName1', 'MyName2']
multi_idx2 = multi_idx.copy(names=['NewName1', 'NewName2'])
assert multi_idx.equals(multi_idx2)
assert multi_idx.names == ['MyName1', 'MyName2']
assert multi_idx2.names == ['NewName1', 'NewName2']
multi_idx3 = multi_idx.copy(name=['NewName1', 'NewName2'])
assert multi_idx.equals(multi_idx3)
assert multi_idx.names == ['MyName1', 'MyName2']
assert multi_idx3.names == ['NewName1', 'NewName2']
with pytest.raises(ValueError, match='Length of new names must be 2, got 1'):
    multi_idx.copy(names=['mario'])
with pytest.raises(TypeError, match='MultiIndex.name must be a hashable type'):
    multi_idx.copy(names=[['mario'], ['luigi']])
```

## Next Steps


---

*Source: test_names.py:56 | Complexity: Intermediate | Last updated: 2026-06-02*