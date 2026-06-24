# How To: Tick Addition

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test tick addition

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: kls, expected
```

## Step-by-Step Guide

### Step 1: Assign offset = kls(...)

```python
offset = kls(3)
```

**Verification:**
```python
assert isinstance(result, Timedelta)
```

### Step 2: Assign td = Timedelta(...)

```python
td = Timedelta(hours=2)
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign result = value

```python
result = offset + other
```

**Verification:**
```python
assert isinstance(result, Timedelta)
```

### Step 4: Assign result = value

```python
result = other + offset
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: kls, expected

# Workflow
offset = kls(3)
td = Timedelta(hours=2)
for other in [td, td.to_pytimedelta(), td.to_timedelta64()]:
    result = offset + other
    assert isinstance(result, Timedelta)
    assert result == expected
    result = other + offset
    assert isinstance(result, Timedelta)
    assert result == expected
```

## Next Steps


---

*Source: test_ticks.py:227 | Complexity: Intermediate | Last updated: 2026-06-02*