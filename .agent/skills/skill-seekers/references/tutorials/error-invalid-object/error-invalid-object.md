# How To: Error Invalid Object

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test error invalid object

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `typing`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: data, all_arithmetic_operators
```

## Step-by-Step Guide

### Step 1: Assign unknown = data

```python
data, _ = data
```

**Verification:**
```python
assert result is NotImplemented
```

### Step 2: Assign op = all_arithmetic_operators

```python
op = all_arithmetic_operators
```

### Step 3: Assign opa = getattr(...)

```python
opa = getattr(data, op)
```

### Step 4: Assign result = opa(...)

```python
result = opa(pd.DataFrame({'A': data}))
```

**Verification:**
```python
assert result is NotImplemented
```

### Step 5: Assign msg = 'can only perform ops with 1-d structures'

```python
msg = 'can only perform ops with 1-d structures'
```

### Step 6: Call opa()

```python
opa(np.arange(len(data)).reshape(-1, len(data)))
```


## Complete Example

```python
# Setup
# Fixtures: data, all_arithmetic_operators

# Workflow
data, _ = data
op = all_arithmetic_operators
opa = getattr(data, op)
result = opa(pd.DataFrame({'A': data}))
assert result is NotImplemented
msg = 'can only perform ops with 1-d structures'
with pytest.raises(NotImplementedError, match=msg):
    opa(np.arange(len(data)).reshape(-1, len(data)))
```

## Next Steps


---

*Source: test_arithmetic.py:175 | Complexity: Intermediate | Last updated: 2026-06-02*