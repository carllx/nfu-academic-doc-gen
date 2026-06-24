# How To: Numpy To List Of Ints

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test numpy to list of ints

## Prerequisites

**Required Modules:**
- `random`
- `copy`
- `pytest`
- `networkx`
- `networkx.utils`
- `networkx.utils.misc`


## Step-by-Step Guide

### Step 1: Assign a = np.array(...)

```python
a = np.array([1, 2, 3], dtype=np.int64)
```

**Verification:**
```python
assert isinstance(make_list_of_ints(a), list)
```

### Step 2: Assign b = np.array(...)

```python
b = np.array([1.0, 2, 3])
```

**Verification:**
```python
assert make_list_of_ints(b) == list(b)
```

### Step 3: Assign c = np.array(...)

```python
c = np.array([1.1, 2, 3])
```

**Verification:**
```python
assert isinstance(B[0], int)
```

### Step 4: Assign B = make_list_of_ints(...)

```python
B = make_list_of_ints(b)
```

**Verification:**
```python
assert isinstance(B[0], int)
```

### Step 5: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, make_list_of_ints, c)
```


## Complete Example

```python
# Workflow
a = np.array([1, 2, 3], dtype=np.int64)
b = np.array([1.0, 2, 3])
c = np.array([1.1, 2, 3])
assert isinstance(make_list_of_ints(a), list)
assert make_list_of_ints(b) == list(b)
B = make_list_of_ints(b)
assert isinstance(B[0], int)
pytest.raises(nx.NetworkXError, make_list_of_ints, c)
```

## Next Steps


---

*Source: test_misc.py:84 | Complexity: Intermediate | Last updated: 2026-06-02*