# How To: Math Max Min

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test math max min

## Prerequisites

**Required Modules:**
- `itertools`
- `math`
- `operator`
- `re`
- `pytest`
- `numpy._core._multiarray_umath`
- `numpy._core._simd`


## Step-by-Step Guide

### Step 1: Assign data_a = self._data(...)

```python
data_a = self._data()
```

**Verification:**
```python
assert simd_max == data_max
```

### Step 2: Assign data_b = self._data(...)

```python
data_b = self._data(self.nlanes)
```

**Verification:**
```python
assert simd_min == data_min
```

### Step 3: Assign unknown = value

```python
vdata_a, vdata_b = (self.load(data_a), self.load(data_b))
```

### Step 4: Assign data_max = value

```python
data_max = [max(a, b) for a, b in zip(data_a, data_b)]
```

### Step 5: Assign simd_max = self.max(...)

```python
simd_max = self.max(vdata_a, vdata_b)
```

**Verification:**
```python
assert simd_max == data_max
```

### Step 6: Assign data_min = value

```python
data_min = [min(a, b) for a, b in zip(data_a, data_b)]
```

### Step 7: Assign simd_min = self.min(...)

```python
simd_min = self.min(vdata_a, vdata_b)
```

**Verification:**
```python
assert simd_min == data_min
```


## Complete Example

```python
# Workflow
data_a = self._data()
data_b = self._data(self.nlanes)
vdata_a, vdata_b = (self.load(data_a), self.load(data_b))
data_max = [max(a, b) for a, b in zip(data_a, data_b)]
simd_max = self.max(vdata_a, vdata_b)
assert simd_max == data_max
data_min = [min(a, b) for a, b in zip(data_a, data_b)]
simd_min = self.min(vdata_a, vdata_b)
assert simd_min == data_min
```

## Next Steps


---

*Source: test_simd.py:304 | Complexity: Intermediate | Last updated: 2026-06-02*