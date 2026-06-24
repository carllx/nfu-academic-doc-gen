# How To: Dateoffset Add Sub Timestamp Series With Nano

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dateoffset add sub timestamp series with nano

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.period`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.tests.tseries.offsets.common`
- `pandas.tseries`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: offset, expected
```

## Step-by-Step Guide

### Step 1: Assign start_time = Timestamp(...)

```python
start_time = Timestamp('2022-01-01')
```

**Verification:**
```python
assert testseries[0] == expected
```

### Step 2: Assign teststamp = start_time

```python
teststamp = start_time
```

**Verification:**
```python
assert testseries[0] == teststamp
```

### Step 3: Assign testseries = Series(...)

```python
testseries = Series([start_time])
```

**Verification:**
```python
assert testseries[0] == expected
```

### Step 4: Assign testseries = value

```python
testseries = testseries + offset
```

**Verification:**
```python
assert testseries[0] == expected
```

### Step 5: Assign testseries = value

```python
testseries = offset + testseries
```

**Verification:**
```python
assert testseries[0] == expected
```


## Complete Example

```python
# Setup
# Fixtures: offset, expected

# Workflow
start_time = Timestamp('2022-01-01')
teststamp = start_time
testseries = Series([start_time])
testseries = testseries + offset
assert testseries[0] == expected
testseries -= offset
assert testseries[0] == teststamp
testseries = offset + testseries
assert testseries[0] == expected
```

## Next Steps


---

*Source: test_offsets.py:1079 | Complexity: Intermediate | Last updated: 2026-06-02*