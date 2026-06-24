# How To: Random State

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test random state

## Prerequisites

**Required Modules:**
- `collections`
- `functools`
- `string`
- `subprocess`
- `sys`
- `textwrap`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.common`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign state = com.random_state(...)

```python
state = com.random_state(5)
```

**Verification:**
```python
assert state.uniform() == np.random.RandomState(5).uniform()
```

### Step 2: Assign state2 = np.random.RandomState(...)

```python
state2 = np.random.RandomState(10)
```

**Verification:**
```python
assert com.random_state(state2).uniform() == np.random.RandomState(10).uniform()
```

### Step 3: Assign state_arr_like = np.random.default_rng.integers(...)

```python
state_arr_like = np.random.default_rng(None).integers(0, 2 ** 31, size=624, dtype='uint32')
```

**Verification:**
```python
assert com.random_state() is np.random
```

### Step 4: Assign msg = 'random_state must be an integer, array-like, a BitGenerator, Generator, a numpy RandomState, or None'

```python
msg = 'random_state must be an integer, array-like, a BitGenerator, Generator, a numpy RandomState, or None'
```

**Verification:**
```python
assert com.random_state(state_arr_like).uniform() == np.random.RandomState(state_arr_like).uniform()
```

### Step 5: Call com.random_state()

```python
com.random_state('test')
```

**Verification:**
```python
assert com.random_state(np.random.MT19937(3)).uniform() == np.random.RandomState(np.random.MT19937(3)).uniform()
```

### Step 6: Call com.random_state()

```python
com.random_state(5.5)
```

**Verification:**
```python
assert com.random_state(np.random.PCG64(11)).uniform() == np.random.RandomState(np.random.PCG64(11)).uniform()
```


## Complete Example

```python
# Workflow
state = com.random_state(5)
assert state.uniform() == np.random.RandomState(5).uniform()
state2 = np.random.RandomState(10)
assert com.random_state(state2).uniform() == np.random.RandomState(10).uniform()
assert com.random_state() is np.random
state_arr_like = np.random.default_rng(None).integers(0, 2 ** 31, size=624, dtype='uint32')
assert com.random_state(state_arr_like).uniform() == np.random.RandomState(state_arr_like).uniform()
assert com.random_state(np.random.MT19937(3)).uniform() == np.random.RandomState(np.random.MT19937(3)).uniform()
assert com.random_state(np.random.PCG64(11)).uniform() == np.random.RandomState(np.random.PCG64(11)).uniform()
msg = 'random_state must be an integer, array-like, a BitGenerator, Generator, a numpy RandomState, or None'
with pytest.raises(ValueError, match=msg):
    com.random_state('test')
with pytest.raises(ValueError, match=msg):
    com.random_state(5.5)
```

## Next Steps


---

*Source: test_common.py:54 | Complexity: Intermediate | Last updated: 2026-06-02*