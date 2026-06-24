# How To: Print

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test print

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`

**Setup Required:**
```python
# Fixtures: using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign factor = Categorical(...)

```python
factor = Categorical(['a', 'b', 'b', 'a', 'a', 'c', 'c', 'c'], ordered=True)
```

**Verification:**
```python
assert actual == expected
```

### Step 2: Assign dtype = value

```python
dtype = 'str' if using_infer_string else 'object'
```

### Step 3: Assign expected = value

```python
expected = ["['a', 'b', 'b', 'a', 'a', 'c', 'c', 'c']", f"Categories (3, {dtype}): ['a' < 'b' < 'c']"]
```

### Step 4: Assign expected = unknown.join(...)

```python
expected = '\n'.join(expected)
```

### Step 5: Assign actual = repr(...)

```python
actual = repr(factor)
```

**Verification:**
```python
assert actual == expected
```


## Complete Example

```python
# Setup
# Fixtures: using_infer_string

# Workflow
factor = Categorical(['a', 'b', 'b', 'a', 'a', 'c', 'c', 'c'], ordered=True)
dtype = 'str' if using_infer_string else 'object'
expected = ["['a', 'b', 'b', 'a', 'a', 'c', 'c', 'c']", f"Categories (3, {dtype}): ['a' < 'b' < 'c']"]
expected = '\n'.join(expected)
actual = repr(factor)
assert actual == expected
```

## Next Steps


---

*Source: test_repr.py:20 | Complexity: Intermediate | Last updated: 2026-06-02*