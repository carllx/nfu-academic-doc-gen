# How To: Random State Np Random Randomstate

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test random state np random RandomState

## Prerequisites

**Required Modules:**
- `os`
- `pathlib`
- `random`
- `tempfile`
- `pytest`
- `networkx`
- `networkx.utils.decorators`
- `networkx.utils.misc`


## Step-by-Step Guide

### Step 1: Call np.random.seed()

```python
np.random.seed(42)
```

**Verification:**
```python
assert rval == rval_expected
```

### Step 2: Assign np_rv = np.random.random(...)

```python
np_rv = np.random.random()
```

**Verification:**
```python
assert rval == rval_expected
```

### Step 3: Call np.random.seed()

```python
np.random.seed(42)
```

**Verification:**
```python
assert np_rv == np.random.random()
```

### Step 4: Assign seed = 1

```python
seed = 1
```

### Step 5: Assign rng = np.random.RandomState(...)

```python
rng = np.random.RandomState(seed)
```

### Step 6: Assign rval = self.instantiate_np_random_state(...)

```python
rval = self.instantiate_np_random_state(rng)
```

### Step 7: Assign rval_expected = np.random.RandomState.random(...)

```python
rval_expected = np.random.RandomState(seed).random()
```

**Verification:**
```python
assert rval == rval_expected
```

### Step 8: Assign rval = self.instantiate_py_random_state(...)

```python
rval = self.instantiate_py_random_state(rng)
```

### Step 9: Assign rval_expected = value

```python
rval_expected = np.random.RandomState(seed).random(size=2)[1]
```

**Verification:**
```python
assert rval == rval_expected
```


## Complete Example

```python
# Workflow
np.random.seed(42)
np_rv = np.random.random()
np.random.seed(42)
seed = 1
rng = np.random.RandomState(seed)
rval = self.instantiate_np_random_state(rng)
rval_expected = np.random.RandomState(seed).random()
assert rval == rval_expected
rval = self.instantiate_py_random_state(rng)
rval_expected = np.random.RandomState(seed).random(size=2)[1]
assert rval == rval_expected
assert np_rv == np.random.random()
```

## Next Steps


---

*Source: test_decorators.py:282 | Complexity: Advanced | Last updated: 2026-06-02*