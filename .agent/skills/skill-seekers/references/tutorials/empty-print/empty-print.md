# How To: Empty Print

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test empty print

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign factor = Categorical(...)

```python
factor = Categorical([], Index(['a', 'b', 'c'], dtype=object))
```

**Verification:**
```python
assert actual == expected
```

### Step 2: Assign expected = "[], Categories (3, object): ['a', 'b', 'c']"

```python
expected = "[], Categories (3, object): ['a', 'b', 'c']"
```

**Verification:**
```python
assert expected == actual
```

### Step 3: Assign actual = repr(...)

```python
actual = repr(factor)
```

**Verification:**
```python
assert expected == actual
```

### Step 4: Assign factor = Categorical(...)

```python
factor = Categorical([], Index(['a', 'b', 'c'], dtype=object), ordered=True)
```

**Verification:**
```python
assert expected == repr(factor)
```

### Step 5: Assign expected = "[], Categories (3, object): ['a' < 'b' < 'c']"

```python
expected = "[], Categories (3, object): ['a' < 'b' < 'c']"
```

### Step 6: Assign actual = repr(...)

```python
actual = repr(factor)
```

**Verification:**
```python
assert expected == actual
```

### Step 7: Assign factor = Categorical(...)

```python
factor = Categorical([], [])
```

### Step 8: Assign expected = '[], Categories (0, object): []'

```python
expected = '[], Categories (0, object): []'
```

**Verification:**
```python
assert expected == repr(factor)
```


## Complete Example

```python
# Workflow
factor = Categorical([], Index(['a', 'b', 'c'], dtype=object))
expected = "[], Categories (3, object): ['a', 'b', 'c']"
actual = repr(factor)
assert actual == expected
assert expected == actual
factor = Categorical([], Index(['a', 'b', 'c'], dtype=object), ordered=True)
expected = "[], Categories (3, object): ['a' < 'b' < 'c']"
actual = repr(factor)
assert expected == actual
factor = Categorical([], [])
expected = '[], Categories (0, object): []'
assert expected == repr(factor)
```

## Next Steps


---

*Source: test_repr.py:48 | Complexity: Advanced | Last updated: 2026-06-02*