# How To: Flex Method Subclass Metadata Preservation

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test flex method subclass metadata preservation

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.computation`
- `pandas.core.computation.check`

**Setup Required:**
```python
# Fixtures: all_arithmetic_operators
```

## Step-by-Step Guide

### Step 1: Assign opname = all_arithmetic_operators

```python
opname = all_arithmetic_operators
```

**Verification:**
```python
assert result.x == 42
```

### Step 2: Assign op = getattr(...)

```python
op = getattr(Series, opname)
```

### Step 3: Assign m = MySeries(...)

```python
m = MySeries([1, 2, 3], name='test')
```

### Step 4: Assign m.x = 42

```python
m.x = 42
```

### Step 5: Assign result = op(...)

```python
result = op(m, 1)
```

**Verification:**
```python
assert result.x == 42
```

### Step 6: Assign _metadata = value

```python
_metadata = ['x']
```


## Complete Example

```python
# Setup
# Fixtures: all_arithmetic_operators

# Workflow
class MySeries(Series):
    _metadata = ['x']

    @property
    def _constructor(self):
        return MySeries
opname = all_arithmetic_operators
op = getattr(Series, opname)
m = MySeries([1, 2, 3], name='test')
m.x = 42
result = op(m, 1)
assert result.x == 42
```

## Next Steps


---

*Source: test_arithmetic.py:84 | Complexity: Intermediate | Last updated: 2026-06-02*