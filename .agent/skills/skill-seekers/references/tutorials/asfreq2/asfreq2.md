# How To: Asfreq2

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate frame_or_series: test asfreq2

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

### Step 1: Assign ts = frame_or_series(...)

```python
ts = frame_or_series([0.0, 1.0, 2.0], index=DatetimeIndex([datetime(2009, 10, 30), datetime(2009, 11, 30), datetime(2009, 12, 31)], dtype='M8[ns]', freq='BME'))
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
ts = frame_or_series([0.0, 1.0, 2.0], index=DatetimeIndex([datetime(2009, 10, 30), datetime(2009, 11, 30), datetime(2009, 12, 31)], dtype='M8[ns]', freq='BME'))
```

## Next Steps


---

*Source: test_asfreq.py:27 | Complexity: Beginner | Last updated: 2026-06-02*