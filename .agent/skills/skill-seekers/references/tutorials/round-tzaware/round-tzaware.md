# How To: Round Tzaware

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test round tzaware

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign dt = Timestamp(...)

```python
dt = Timestamp('20130101 09:10:11', tz='US/Eastern')
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign result = dt.round(...)

```python
result = dt.round('D')
```

**Verification:**
```python
assert result == dt
```

### Step 3: Assign expected = Timestamp(...)

```python
expected = Timestamp('20130101', tz='US/Eastern')
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign dt = Timestamp(...)

```python
dt = Timestamp('20130101 09:10:11', tz='US/Eastern')
```

### Step 5: Assign result = dt.round(...)

```python
result = dt.round('s')
```

**Verification:**
```python
assert result == dt
```


## Complete Example

```python
# Workflow
dt = Timestamp('20130101 09:10:11', tz='US/Eastern')
result = dt.round('D')
expected = Timestamp('20130101', tz='US/Eastern')
assert result == expected
dt = Timestamp('20130101 09:10:11', tz='US/Eastern')
result = dt.round('s')
assert result == dt
```

## Next Steps


---

*Source: test_round.py:50 | Complexity: Intermediate | Last updated: 2026-06-02*