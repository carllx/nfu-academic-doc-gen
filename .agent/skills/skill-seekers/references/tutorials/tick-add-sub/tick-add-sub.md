# How To: Tick Add Sub

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test tick add sub

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
# Fixtures: cls, n, m
```

## Step-by-Step Guide

### Step 1: Assign left = cls(...)

```python
left = cls(n)
```

**Verification:**
```python
assert left + right == expected
```

### Step 2: Assign right = cls(...)

```python
right = cls(m)
```

**Verification:**
```python
assert left - right == expected
```

### Step 3: Assign expected = cls(...)

```python
expected = cls(n + m)
```

**Verification:**
```python
assert left + right == expected
```

### Step 4: Assign expected = cls(...)

```python
expected = cls(n - m)
```

**Verification:**
```python
assert left - right == expected
```


## Complete Example

```python
# Setup
# Fixtures: cls, n, m

# Workflow
left = cls(n)
right = cls(m)
expected = cls(n + m)
assert left + right == expected
expected = cls(n - m)
assert left - right == expected
```

## Next Steps


---

*Source: test_ticks.py:69 | Complexity: Intermediate | Last updated: 2026-06-02*