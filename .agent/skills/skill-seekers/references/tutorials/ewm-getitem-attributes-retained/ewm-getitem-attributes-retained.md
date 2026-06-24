# How To: Ewm Getitem Attributes Retained

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test ewm getitem attributes retained

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: arg, adjust, ignore_na
```

## Step-by-Step Guide

### Step 1: Assign kwargs = value

```python
kwargs = {arg: 1, 'adjust': adjust, 'ignore_na': ignore_na}
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign ewm = DataFrame.ewm(...)

```python
ewm = DataFrame({'A': range(1), 'B': range(1)}).ewm(**kwargs)
```

### Step 3: Assign expected = value

```python
expected = {attr: getattr(ewm, attr) for attr in ewm._attributes}
```

### Step 4: Assign ewm_slice = value

```python
ewm_slice = ewm['A']
```

### Step 5: Assign result = value

```python
result = {attr: getattr(ewm, attr) for attr in ewm_slice._attributes}
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: arg, adjust, ignore_na

# Workflow
kwargs = {arg: 1, 'adjust': adjust, 'ignore_na': ignore_na}
ewm = DataFrame({'A': range(1), 'B': range(1)}).ewm(**kwargs)
expected = {attr: getattr(ewm, attr) for attr in ewm._attributes}
ewm_slice = ewm['A']
result = {attr: getattr(ewm, attr) for attr in ewm_slice._attributes}
assert result == expected
```

## Next Steps


---

*Source: test_ewm.py:141 | Complexity: Intermediate | Last updated: 2026-06-02*