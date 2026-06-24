# How To: Get Datetime64 Unit

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get datetime64 unit

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `subprocess`
- `sys`
- `sysconfig`
- `datetime`
- `pytest`
- `numpy`
- `numpy.testing`
- `cython`
- `Cython.Compiler.Version`
- `numpy._utils`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`
- `checks`

**Setup Required:**
```python
# Fixtures: install_temp
```

## Step-by-Step Guide

### Step 1: Assign dt64 = np.datetime64(...)

```python
dt64 = np.datetime64('2016-01-01', 'ns')
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign result = checks.get_dt64_unit(...)

```python
result = checks.get_dt64_unit(dt64)
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign expected = 10

```python
expected = 10
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign td64 = np.timedelta64(...)

```python
td64 = np.timedelta64(12345, 'h')
```

### Step 5: Assign result = checks.get_dt64_unit(...)

```python
result = checks.get_dt64_unit(td64)
```

### Step 6: Assign expected = 5

```python
expected = 5
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: install_temp

# Workflow
import checks
dt64 = np.datetime64('2016-01-01', 'ns')
result = checks.get_dt64_unit(dt64)
expected = 10
assert result == expected
td64 = np.timedelta64(12345, 'h')
result = checks.get_dt64_unit(td64)
expected = 5
assert result == expected
```

## Next Steps


---

*Source: test_cython.py:133 | Complexity: Intermediate | Last updated: 2026-06-02*