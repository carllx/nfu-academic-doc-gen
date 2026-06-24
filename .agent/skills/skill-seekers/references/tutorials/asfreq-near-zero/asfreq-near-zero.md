# How To: Asfreq Near Zero

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test asfreq near zero

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas._libs.tslibs.period`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: freq
```

## Step-by-Step Guide

### Step 1: Assign per = Period(...)

```python
per = Period('0001-01-01', freq=freq)
```

**Verification:**
```python
assert prev.ordinal == per.ordinal - 1
```

### Step 2: Assign tup1 = value

```python
tup1 = (per.year, per.hour, per.day)
```

**Verification:**
```python
assert tup2 < tup1
```

### Step 3: Assign prev = value

```python
prev = per - 1
```

**Verification:**
```python
assert prev.ordinal == per.ordinal - 1
```

### Step 4: Assign tup2 = value

```python
tup2 = (prev.year, prev.month, prev.day)
```

**Verification:**
```python
assert tup2 < tup1
```


## Complete Example

```python
# Setup
# Fixtures: freq

# Workflow
per = Period('0001-01-01', freq=freq)
tup1 = (per.year, per.hour, per.day)
prev = per - 1
assert prev.ordinal == per.ordinal - 1
tup2 = (prev.year, prev.month, prev.day)
assert tup2 < tup1
```

## Next Steps


---

*Source: test_asfreq.py:21 | Complexity: Intermediate | Last updated: 2026-06-02*