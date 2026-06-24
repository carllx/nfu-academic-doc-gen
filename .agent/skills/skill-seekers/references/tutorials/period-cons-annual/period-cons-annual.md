# How To: Period Cons Annual

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test period cons annual

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.ccalendar`
- `pandas._libs.tslibs.np_datetime`
- `pandas._libs.tslibs.parsing`
- `pandas._libs.tslibs.period`
- `pandas.compat`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: month
```

## Step-by-Step Guide

### Step 1: Assign freq = value

```python
freq = f'Y-{month}'
```

**Verification:**
```python
assert p == exp + 1
```

### Step 2: Assign exp = Period(...)

```python
exp = Period('1989', freq=freq)
```

**Verification:**
```python
assert isinstance(p, Period)
```

### Step 3: Assign stamp = value

```python
stamp = exp.to_timestamp('D', how='end') + timedelta(days=30)
```

### Step 4: Assign p = Period(...)

```python
p = Period(stamp, freq=freq)
```

**Verification:**
```python
assert p == exp + 1
```


## Complete Example

```python
# Setup
# Fixtures: month

# Workflow
freq = f'Y-{month}'
exp = Period('1989', freq=freq)
stamp = exp.to_timestamp('D', how='end') + timedelta(days=30)
p = Period(stamp, freq=freq)
assert p == exp + 1
assert isinstance(p, Period)
```

## Next Steps


---

*Source: test_period.py:421 | Complexity: Intermediate | Last updated: 2026-06-02*