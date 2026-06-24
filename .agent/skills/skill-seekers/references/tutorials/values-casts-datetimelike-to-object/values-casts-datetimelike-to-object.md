# How To: Values Casts Datetimelike To Object

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test values casts datetimelike to object

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: constructor
```

## Step-by-Step Guide

### Step 1: Assign series = Series(...)

```python
series = Series(constructor('2000-01-01', periods=10, freq='D'))
```

**Verification:**
```python
assert (result[:, 0] == expected.values).all()
```

### Step 2: Assign expected = series.astype(...)

```python
expected = series.astype('object')
```

**Verification:**
```python
assert (result[:, 0] == expected.values).all()
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'a': series, 'b': np.random.default_rng(2).standard_normal(len(series))})
```

### Step 4: Assign result = df.values.squeeze(...)

```python
result = df.values.squeeze()
```

**Verification:**
```python
assert (result[:, 0] == expected.values).all()
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame({'a': series, 'b': ['foo'] * len(series)})
```

### Step 6: Assign result = df.values.squeeze(...)

```python
result = df.values.squeeze()
```

**Verification:**
```python
assert (result[:, 0] == expected.values).all()
```


## Complete Example

```python
# Setup
# Fixtures: constructor

# Workflow
series = Series(constructor('2000-01-01', periods=10, freq='D'))
expected = series.astype('object')
df = DataFrame({'a': series, 'b': np.random.default_rng(2).standard_normal(len(series))})
result = df.values.squeeze()
assert (result[:, 0] == expected.values).all()
df = DataFrame({'a': series, 'b': ['foo'] * len(series)})
result = df.values.squeeze()
assert (result[:, 0] == expected.values).all()
```

## Next Steps


---

*Source: test_values.py:70 | Complexity: Intermediate | Last updated: 2026-06-02*