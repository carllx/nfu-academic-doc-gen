# How To: Autocorr

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test autocorr

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`

**Setup Required:**
```python
# Fixtures: datetime_series
```

## Step-by-Step Guide

### Step 1: Assign corr1 = datetime_series.autocorr(...)

```python
corr1 = datetime_series.autocorr()
```

**Verification:**
```python
assert np.isnan(corr1)
```

### Step 2: Assign corr2 = datetime_series.autocorr(...)

```python
corr2 = datetime_series.autocorr(lag=1)
```

**Verification:**
```python
assert np.isnan(corr2)
```

### Step 3: Assign n = value

```python
n = 1 + np.random.default_rng(2).integers(max(1, len(datetime_series) - 2))
```

**Verification:**
```python
assert corr1 == corr2
```

### Step 4: Assign corr1 = datetime_series.corr(...)

```python
corr1 = datetime_series.corr(datetime_series.shift(n))
```

**Verification:**
```python
assert np.isnan(corr1)
```

### Step 5: Assign corr2 = datetime_series.autocorr(...)

```python
corr2 = datetime_series.autocorr(lag=n)
```

**Verification:**
```python
assert np.isnan(corr2)
```


## Complete Example

```python
# Setup
# Fixtures: datetime_series

# Workflow
corr1 = datetime_series.autocorr()
corr2 = datetime_series.autocorr(lag=1)
if len(datetime_series) <= 2:
    assert np.isnan(corr1)
    assert np.isnan(corr2)
else:
    assert corr1 == corr2
n = 1 + np.random.default_rng(2).integers(max(1, len(datetime_series) - 2))
corr1 = datetime_series.corr(datetime_series.shift(n))
corr2 = datetime_series.autocorr(lag=n)
if len(datetime_series) <= 2:
    assert np.isnan(corr1)
    assert np.isnan(corr2)
else:
    assert corr1 == corr2
```

## Next Steps


---

*Source: test_autocorr.py:5 | Complexity: Intermediate | Last updated: 2026-06-02*