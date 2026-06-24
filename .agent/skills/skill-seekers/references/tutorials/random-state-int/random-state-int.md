# How To: Random State Int

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test random state int

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
assert np_rv == np.random.random()
```

### Step 3: Call random.seed()

```python
random.seed(42)
```

**Verification:**
```python
assert rval == rval_expected
```

### Step 4: Assign py_rv = random.random(...)

```python
py_rv = random.random()
```

**Verification:**
```python
assert py_rv == random.random()
```

### Step 5: Call np.random.seed()

```python
np.random.seed(42)
```

### Step 6: Assign seed = 1

```python
seed = 1
```

### Step 7: Assign rval = self.instantiate_np_random_state(...)

```python
rval = self.instantiate_np_random_state(seed)
```

### Step 8: Assign rval_expected = np.random.RandomState.rand(...)

```python
rval_expected = np.random.RandomState(seed).rand()
```

**Verification:**
```python
assert rval == rval_expected
```

### Step 9: Call random.seed()

```python
random.seed(42)
```

### Step 10: Assign rval = self.instantiate_py_random_state(...)

```python
rval = self.instantiate_py_random_state(seed)
```

### Step 11: Assign rval_expected = random.Random.random(...)

```python
rval_expected = random.Random(seed).random()
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
random.seed(42)
py_rv = random.random()
np.random.seed(42)
seed = 1
rval = self.instantiate_np_random_state(seed)
rval_expected = np.random.RandomState(seed).rand()
assert rval == rval_expected
assert np_rv == np.random.random()
random.seed(42)
rval = self.instantiate_py_random_state(seed)
rval_expected = random.Random(seed).random()
assert rval == rval_expected
assert py_rv == random.random()
```

## Next Steps


---

*Source: test_decorators.py:244 | Complexity: Advanced | Last updated: 2026-06-02*