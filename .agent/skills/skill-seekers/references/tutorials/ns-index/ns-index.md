# How To: Ns Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ns index

## Prerequisites

**Required Modules:**
- `datetime`
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign nsamples = 400

```python
nsamples = 400
```

### Step 2: Assign ns = int(...)

```python
ns = int(1000000000.0 / 24414)
```

### Step 3: Assign dtstart = np.datetime64(...)

```python
dtstart = np.datetime64('2012-09-20T00:00:00')
```

### Step 4: Assign dt = value

```python
dt = dtstart + np.arange(nsamples) * np.timedelta64(ns, 'ns')
```

### Step 5: Assign freq = value

```python
freq = ns * offsets.Nano()
```

### Step 6: Assign index = DatetimeIndex(...)

```python
index = DatetimeIndex(dt, freq=freq, name='time')
```

### Step 7: Call self.assert_index_parameters()

```python
self.assert_index_parameters(index)
```

### Step 8: Assign new_index = date_range(...)

```python
new_index = date_range(start=index[0], end=index[-1], freq=index.freq)
```

### Step 9: Call self.assert_index_parameters()

```python
self.assert_index_parameters(new_index)
```


## Complete Example

```python
# Workflow
nsamples = 400
ns = int(1000000000.0 / 24414)
dtstart = np.datetime64('2012-09-20T00:00:00')
dt = dtstart + np.arange(nsamples) * np.timedelta64(ns, 'ns')
freq = ns * offsets.Nano()
index = DatetimeIndex(dt, freq=freq, name='time')
self.assert_index_parameters(index)
new_index = date_range(start=index[0], end=index[-1], freq=index.freq)
self.assert_index_parameters(new_index)
```

## Next Steps


---

*Source: test_datetime.py:88 | Complexity: Advanced | Last updated: 2026-06-02*