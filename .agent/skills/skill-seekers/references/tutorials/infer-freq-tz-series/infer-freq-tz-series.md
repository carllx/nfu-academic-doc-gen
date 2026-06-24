# How To: Infer Freq Tz Series

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test infer freq tz series

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.ccalendar`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.period`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.tools.datetimes`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: tz_naive_fixture
```

## Step-by-Step Guide

### Step 1: Assign tz = tz_naive_fixture

```python
tz = tz_naive_fixture
```

**Verification:**
```python
assert inferred_freq == 'D'
```

### Step 2: Assign idx = date_range(...)

```python
idx = date_range('2021-01-01', '2021-01-04', tz=tz)
```

### Step 3: Assign series = idx.to_series.reset_index(...)

```python
series = idx.to_series().reset_index(drop=True)
```

### Step 4: Assign inferred_freq = frequencies.infer_freq(...)

```python
inferred_freq = frequencies.infer_freq(series)
```

**Verification:**
```python
assert inferred_freq == 'D'
```


## Complete Example

```python
# Setup
# Fixtures: tz_naive_fixture

# Workflow
tz = tz_naive_fixture
idx = date_range('2021-01-01', '2021-01-04', tz=tz)
series = idx.to_series().reset_index(drop=True)
inferred_freq = frequencies.infer_freq(series)
assert inferred_freq == 'D'
```

## Next Steps


---

*Source: test_inference.py:242 | Complexity: Intermediate | Last updated: 2026-06-02*