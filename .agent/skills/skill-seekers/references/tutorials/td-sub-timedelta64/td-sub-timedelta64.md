# How To: Td Sub Timedelta64

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test td sub timedelta64

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
result = td - td.to_timedelta64()
```

**Verification:**
```python
assert isinstance(result, Timedelta)
```

### Step 4: Assign result = value

```python
result = td.to_timedelta64() - td
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
result = td - td.to_timedelta64()
assert isinstance(result, Timedelta)
assert result == expected
result = td.to_timedelta64() - td
assert isinstance(result, Timedelta)
assert result == expected
```

## Next Steps


---

*Source: test_arithmetic.py:160 | Complexity: Intermediate | Last updated: 2026-06-02*