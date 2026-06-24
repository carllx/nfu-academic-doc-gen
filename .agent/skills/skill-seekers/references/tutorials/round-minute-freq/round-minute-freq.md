# How To: Round Minute Freq

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test round minute freq

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `hypothesis`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.dtypes`
- `pandas._libs.tslibs.period`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: test_input, freq, expected, rounder
```

## Step-by-Step Guide

### Step 1: Assign dt = Timestamp(...)

```python
dt = Timestamp(test_input)
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign expected = Timestamp(...)

```python
expected = Timestamp(expected)
```

### Step 3: Assign func = getattr(...)

```python
func = getattr(dt, rounder)
```

### Step 4: Assign result = func(...)

```python
result = func(freq)
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: test_input, freq, expected, rounder

# Workflow
dt = Timestamp(test_input)
expected = Timestamp(expected)
func = getattr(dt, rounder)
result = func(freq)
assert result == expected
```

## Next Steps


---

*Source: test_round.py:140 | Complexity: Intermediate | Last updated: 2026-06-02*