# How To: Selection

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test selection

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `warnings`
- `dateutil`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.ccalendar`
- `pandas._libs.tslibs.period`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.datetimes`
- `pandas.core.indexes.period`
- `pandas.core.resample`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: index, freq, kind, kwargs
```

## Step-by-Step Guide

### Step 1: Assign rng = np.arange(...)

```python
rng = np.arange(len(index), dtype=np.int64)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'date': index, 'a': rng}, index=pd.MultiIndex.from_arrays([rng, index], names=['v', 'd']))
```

### Step 3: Assign msg = 'Resampling from level= or on= selection with a PeriodIndex is not currently supported, use \\.set_index\\(\\.\\.\\.\\) to explicitly set index'

```python
msg = 'Resampling from level= or on= selection with a PeriodIndex is not currently supported, use \\.set_index\\(\\.\\.\\.\\) to explicitly set index'
```

### Step 4: Assign depr_msg = "The 'kind' keyword in DataFrame.resample is deprecated"

```python
depr_msg = "The 'kind' keyword in DataFrame.resample is deprecated"
```

### Step 5: Call df.resample()

```python
df.resample(freq, kind=kind, **kwargs)
```


## Complete Example

```python
# Setup
# Fixtures: index, freq, kind, kwargs

# Workflow
rng = np.arange(len(index), dtype=np.int64)
df = DataFrame({'date': index, 'a': rng}, index=pd.MultiIndex.from_arrays([rng, index], names=['v', 'd']))
msg = 'Resampling from level= or on= selection with a PeriodIndex is not currently supported, use \\.set_index\\(\\.\\.\\.\\) to explicitly set index'
depr_msg = "The 'kind' keyword in DataFrame.resample is deprecated"
with pytest.raises(NotImplementedError, match=msg):
    with tm.assert_produces_warning(FutureWarning, match=depr_msg):
        df.resample(freq, kind=kind, **kwargs)
```

## Next Steps


---

*Source: test_period_index.py:115 | Complexity: Intermediate | Last updated: 2026-06-02*