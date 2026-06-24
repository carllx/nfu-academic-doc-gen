# How To: Asfreq Mult Pi

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test asfreq mult pi

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: freq
```

## Step-by-Step Guide

### Step 1: Assign pi = PeriodIndex(...)

```python
pi = PeriodIndex(['2001-01', '2001-02', 'NaT', '2001-03'], freq='2M')
```

**Verification:**
```python
assert result.freq == exp.freq
```

### Step 2: Assign result = pi.asfreq(...)

```python
result = pi.asfreq(freq)
```

**Verification:**
```python
assert result.freq == exp.freq
```

### Step 3: Assign exp = PeriodIndex(...)

```python
exp = PeriodIndex(['2001-02-28', '2001-03-31', 'NaT', '2001-04-30'], freq=freq)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp)
```

**Verification:**
```python
assert result.freq == exp.freq
```

### Step 5: Assign result = pi.asfreq(...)

```python
result = pi.asfreq(freq, how='S')
```

### Step 6: Assign exp = PeriodIndex(...)

```python
exp = PeriodIndex(['2001-01-01', '2001-02-01', 'NaT', '2001-03-01'], freq=freq)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp)
```

**Verification:**
```python
assert result.freq == exp.freq
```


## Complete Example

```python
# Setup
# Fixtures: freq

# Workflow
pi = PeriodIndex(['2001-01', '2001-02', 'NaT', '2001-03'], freq='2M')
result = pi.asfreq(freq)
exp = PeriodIndex(['2001-02-28', '2001-03-31', 'NaT', '2001-04-30'], freq=freq)
tm.assert_index_equal(result, exp)
assert result.freq == exp.freq
result = pi.asfreq(freq, how='S')
exp = PeriodIndex(['2001-01-01', '2001-02-01', 'NaT', '2001-03-01'], freq=freq)
tm.assert_index_equal(result, exp)
assert result.freq == exp.freq
```

## Next Steps


---

*Source: test_asfreq.py:93 | Complexity: Intermediate | Last updated: 2026-06-02*