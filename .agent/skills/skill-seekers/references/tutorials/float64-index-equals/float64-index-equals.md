# How To: Float64 Index Equals

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test float64 index equals

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign float_index = Index(...)

```python
float_index = Index([1.0, 2, 3])
```

**Verification:**
```python
assert result is False
```

### Step 2: Assign string_index = Index(...)

```python
string_index = Index(['1', '2', '3'])
```

**Verification:**
```python
assert result is False
```

### Step 3: Assign result = float_index.equals(...)

```python
result = float_index.equals(string_index)
```

**Verification:**
```python
assert result is False
```

### Step 4: Assign result = string_index.equals(...)

```python
result = string_index.equals(float_index)
```

**Verification:**
```python
assert result is False
```


## Complete Example

```python
# Workflow
float_index = Index([1.0, 2, 3])
string_index = Index(['1', '2', '3'])
result = float_index.equals(string_index)
assert result is False
result = string_index.equals(float_index)
assert result is False
```

## Next Steps


---

*Source: test_numeric.py:511 | Complexity: Intermediate | Last updated: 2026-06-02*