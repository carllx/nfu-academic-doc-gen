# How To: Tick Mul Float

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tick mul float

## Prerequisites

**Required Modules:**
- `datetime`
- `hypothesis`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.offsets`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas._testing._hypothesis`
- `pandas.tests.tseries.offsets.common`
- `pandas.tseries`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign off = Micro(...)

```python
off = Micro(2)
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign result = value

```python
result = off * 1.5
```

**Verification:**
```python
assert isinstance(result, Micro)
```

### Step 3: Assign expected = Micro(...)

```python
expected = Micro(3)
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign result = value

```python
result = off * 1.25
```

**Verification:**
```python
assert isinstance(result, Nano)
```

### Step 5: Assign expected = Nano(...)

```python
expected = Nano(2500)
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
off = Micro(2)
result = off * 1.5
expected = Micro(3)
assert result == expected
assert isinstance(result, Micro)
result = off * 1.25
expected = Nano(2500)
assert result == expected
assert isinstance(result, Nano)
```

## Next Steps


---

*Source: test_ticks.py:279 | Complexity: Intermediate | Last updated: 2026-06-02*