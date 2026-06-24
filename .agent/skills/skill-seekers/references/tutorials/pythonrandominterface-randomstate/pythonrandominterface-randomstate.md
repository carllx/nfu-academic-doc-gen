# How To: Pythonrandominterface Randomstate

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test PythonRandomInterface RandomState

## Prerequisites

**Required Modules:**
- `random`
- `copy`
- `pytest`
- `networkx`
- `networkx.utils`
- `networkx.utils.misc`


## Step-by-Step Guide

### Step 1: Assign np = pytest.importorskip(...)

```python
np = pytest.importorskip('numpy')
```

**Verification:**
```python
assert rng.randrange(3, 5) == rs42.randint(3, 5)
```

### Step 2: Assign seed = 42

```python
seed = 42
```

**Verification:**
```python
assert rng.randrange(2) == rs42.randint(0, 2)
```

### Step 3: Assign rs = value

```python
rs = np.random.RandomState
```

**Verification:**
```python
assert rng.uniform(1, 10) == rs42.uniform(1, 10)
```

### Step 4: Assign rng = PythonRandomInterface(...)

```python
rng = PythonRandomInterface(rs(seed))
```

**Verification:**
```python
assert rng.choice([1, 2, 3]) == rs42.choice([1, 2, 3])
```

### Step 5: Assign rs42 = rs(...)

```python
rs42 = rs(seed)
```

**Verification:**
```python
assert rng.gauss(0, 1) == rs42.normal(0, 1)
```


## Complete Example

```python
# Workflow
np = pytest.importorskip('numpy')
seed = 42
rs = np.random.RandomState
rng = PythonRandomInterface(rs(seed))
rs42 = rs(seed)
assert rng.randrange(3, 5) == rs42.randint(3, 5)
assert rng.randrange(2) == rs42.randint(0, 2)
assert rng.uniform(1, 10) == rs42.uniform(1, 10)
assert rng.choice([1, 2, 3]) == rs42.choice([1, 2, 3])
assert rng.gauss(0, 1) == rs42.normal(0, 1)
assert rng.expovariate(1.5) == rs42.exponential(1 / 1.5)
assert rng.paretovariate(2) == rs42.pareto(2)
assert np.all(rng.shuffle([1, 2, 3]) == rs42.shuffle([1, 2, 3]))
assert np.all(rng.sample([1, 2, 3], 2) == rs42.choice([1, 2, 3], (2,), replace=False))
assert np.all([rng.randint(3, 5) for _ in range(100)] == [rs42.randint(3, 6) for _ in range(100)])
assert rng.random() == rs42.random_sample()
```

## Next Steps


---

*Source: test_misc.py:211 | Complexity: Intermediate | Last updated: 2026-06-02*