# How To: Td Sub Pytimedelta

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test td sub pytimedelta

## Prerequisites

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`


## Step-by-Step Guide

### Step 1: Assign td = Timedelta(...)

```python
td = Timedelta(10, unit='d')
```

**Verification:**
```python
assert isinstance(result, Timedelta)
```

### Step 2: Assign expected = Timedelta(...)

```python
expected = Timedelta(0, unit='ns')
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign result = value

```python
result = td - td.to_pytimedelta()
```

**Verification:**
```python
assert isinstance(result, Timedelta)
```

### Step 4: Assign result = value

```python
result = td.to_pytimedelta() - td
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
td = Timedelta(10, unit='d')
expected = Timedelta(0, unit='ns')
result = td - td.to_pytimedelta()
assert isinstance(result, Timedelta)
assert result == expected
result = td.to_pytimedelta() - td
assert isinstance(result, Timedelta)
assert result == expected
```

## Next Steps


---

*Source: test_arithmetic.py:148 | Complexity: Intermediate | Last updated: 2026-06-02*