# How To: Bar Align Height

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test bar align height

## Prerequisites

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign data = DataFrame(...)

```python
data = DataFrame([[1], [2]])
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign result = value

```python
result = data.style.bar(align='left', height=50)._compute().ctx
```

### Step 3: Assign bg_s = 'linear-gradient(90deg, #d65f5f 100.0%, transparent 100.0%) no-repeat center'

```python
bg_s = 'linear-gradient(90deg, #d65f5f 100.0%, transparent 100.0%) no-repeat center'
```

### Step 4: Assign expected = value

```python
expected = {(0, 0): [('width', '10em')], (1, 0): [('width', '10em'), ('background', bg_s), ('background-size', '100% 50.0%')]}
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
data = DataFrame([[1], [2]])
result = data.style.bar(align='left', height=50)._compute().ctx
bg_s = 'linear-gradient(90deg, #d65f5f 100.0%, transparent 100.0%) no-repeat center'
expected = {(0, 0): [('width', '10em')], (1, 0): [('width', '10em'), ('background', bg_s), ('background-size', '100% 50.0%')]}
assert result == expected
```

## Next Steps


---

*Source: test_bar.py:284 | Complexity: Intermediate | Last updated: 2026-06-02*