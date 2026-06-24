# How To: Is Unique

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test is unique

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array(self.values, dtype=self.dtype)
```

**Verification:**
```python
assert engine.is_unique is True
```

### Step 2: Assign engine = self.engine_type(...)

```python
engine = self.engine_type(arr)
```

**Verification:**
```python
assert engine.is_unique is False
```

### Step 3: Assign arr = np.array(...)

```python
arr = np.array(['a', 'b', 'a'], dtype=self.dtype)
```

### Step 4: Assign engine = self.engine_type(...)

```python
engine = self.engine_type(arr)
```

**Verification:**
```python
assert engine.is_unique is False
```


## Complete Example

```python
# Workflow
arr = np.array(self.values, dtype=self.dtype)
engine = self.engine_type(arr)
assert engine.is_unique is True
arr = np.array(['a', 'b', 'a'], dtype=self.dtype)
engine = self.engine_type(arr)
assert engine.is_unique is False
```

## Next Steps


---

*Source: test_engines.py:164 | Complexity: Intermediate | Last updated: 2026-06-02*