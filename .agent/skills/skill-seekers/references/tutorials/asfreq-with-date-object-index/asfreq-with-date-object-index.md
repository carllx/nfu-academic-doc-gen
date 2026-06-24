# How To: Asfreq With Date Object Index

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test asfreq with date object index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.offsets`
- `pandas`
- `pandas._testing`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('1/1/2000', periods=20)
```

### Step 2: Assign ts = frame_or_series(...)

```python
ts = frame_or_series(np.random.default_rng(2).standard_normal(20), index=rng)
```

### Step 3: Assign ts2 = ts.copy(...)

```python
ts2 = ts.copy()
```

### Step 4: Assign ts2.index = value

```python
ts2.index = [x.date() for x in ts2.index]
```

### Step 5: Assign result = ts2.asfreq(...)

```python
result = ts2.asfreq('4h', method='ffill')
```

### Step 6: Assign expected = ts.asfreq(...)

```python
expected = ts.asfreq('4h', method='ffill')
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
rng = date_range('1/1/2000', periods=20)
ts = frame_or_series(np.random.default_rng(2).standard_normal(20), index=rng)
ts2 = ts.copy()
ts2.index = [x.date() for x in ts2.index]
result = ts2.asfreq('4h', method='ffill')
expected = ts.asfreq('4h', method='ffill')
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_asfreq.py:191 | Complexity: Intermediate | Last updated: 2026-06-02*