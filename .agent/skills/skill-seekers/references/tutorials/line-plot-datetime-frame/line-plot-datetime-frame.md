# How To: Line Plot Datetime Frame

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test line plot datetime frame

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `pickle`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.datetimes`
- `pandas.core.indexes.period`
- `pandas.core.indexes.timedeltas`
- `pandas.tests.plotting.common`
- `pandas.tseries.offsets`
- `matplotlib.pyplot`
- `pandas.plotting._matplotlib.converter`
- `pandas.plotting._matplotlib.converter`
- `pandas.plotting._matplotlib.converter`
- `pandas.plotting._matplotlib.converter`
- `pandas.plotting._matplotlib.converter`

**Setup Required:**
```python
# Fixtures: freq
```

## Step-by-Step Guide

### Step 1: Assign idx = date_range(...)

```python
idx = date_range('12/31/1999', freq=freq, periods=100)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((len(idx), 3)), index=idx, columns=['A', 'B', 'C'])
```

### Step 3: Assign freq = freq_to_period_freqstr(...)

```python
freq = freq_to_period_freqstr(1, df.index.freq.rule_code)
```

### Step 4: Assign freq = value

```python
freq = df.index.to_period(freq).freq
```

### Step 5: Call _check_plot_works()

```python
_check_plot_works(df.plot, freq)
```


## Complete Example

```python
# Setup
# Fixtures: freq

# Workflow
idx = date_range('12/31/1999', freq=freq, periods=100)
df = DataFrame(np.random.default_rng(2).standard_normal((len(idx), 3)), index=idx, columns=['A', 'B', 'C'])
freq = freq_to_period_freqstr(1, df.index.freq.rule_code)
freq = df.index.to_period(freq).freq
_check_plot_works(df.plot, freq)
```

## Next Steps


---

*Source: test_datetimelike.py:249 | Complexity: Intermediate | Last updated: 2026-06-02*