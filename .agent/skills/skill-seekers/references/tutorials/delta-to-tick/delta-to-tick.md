# How To: Delta To Tick

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test delta to tick

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

### Step 1: Assign delta = timedelta(...)

```python
delta = timedelta(3)
```

**Verification:**
```python
assert tick == offsets.Day(3)
```

### Step 2: Assign tick = delta_to_tick(...)

```python
tick = delta_to_tick(delta)
```

**Verification:**
```python
assert tick == Nano(5)
```

### Step 3: Assign td = Timedelta(...)

```python
td = Timedelta(nanoseconds=5)
```

### Step 4: Assign tick = delta_to_tick(...)

```python
tick = delta_to_tick(td)
```

**Verification:**
```python
assert tick == Nano(5)
```


## Complete Example

```python
# Workflow
delta = timedelta(3)
tick = delta_to_tick(delta)
assert tick == offsets.Day(3)
td = Timedelta(nanoseconds=5)
tick = delta_to_tick(td)
assert tick == Nano(5)
```

## Next Steps


---

*Source: test_ticks.py:53 | Complexity: Intermediate | Last updated: 2026-06-02*