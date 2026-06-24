# How To: Infer Freq Non Nano Tzaware

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test infer freq non nano tzaware

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
# Fixtures: tz_aware_fixture
```

## Step-by-Step Guide

### Step 1: Assign tz = tz_aware_fixture

```python
tz = tz_aware_fixture
```

**Verification:**
```python
assert res == 'B'
```

### Step 2: Assign dti = date_range(...)

```python
dti = date_range('2016-01-01', periods=365, freq='B', tz=tz)
```

### Step 3: Assign dta = dti._data.as_unit(...)

```python
dta = dti._data.as_unit('s')
```

### Step 4: Assign res = frequencies.infer_freq(...)

```python
res = frequencies.infer_freq(dta)
```

**Verification:**
```python
assert res == 'B'
```


## Complete Example

```python
# Setup
# Fixtures: tz_aware_fixture

# Workflow
tz = tz_aware_fixture
dti = date_range('2016-01-01', periods=365, freq='B', tz=tz)
dta = dti._data.as_unit('s')
res = frequencies.infer_freq(dta)
assert res == 'B'
```

## Next Steps


---

*Source: test_inference.py:551 | Complexity: Intermediate | Last updated: 2026-06-02*