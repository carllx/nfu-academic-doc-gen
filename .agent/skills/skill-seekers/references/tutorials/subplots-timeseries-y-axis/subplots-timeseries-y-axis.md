# How To: Subplots Timeseries Y Axis

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test subplots timeseries y axis

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `string`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.plotting.common`
- `pandas.io.formats.printing`

**Setup Required:**
```python
# Fixtures: col
```

## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = {'numeric': np.array([1, 2, 5]), 'timedelta': [pd.Timedelta(-10, unit='s'), pd.Timedelta(10, unit='m'), pd.Timedelta(10, unit='h')], 'datetime_no_tz': [pd.to_datetime('2017-08-01 00:00:00'), pd.to_datetime('2017-08-01 02:00:00'), pd.to_datetime('2017-08-02 00:00:00')], 'datetime_all_tz': [pd.to_datetime('2017-08-01 00:00:00', utc=True), pd.to_datetime('2017-08-01 02:00:00', utc=True), pd.to_datetime('2017-08-02 00:00:00', utc=True)], 'text': ['This', 'should', 'fail']}
```

**Verification:**
```python
assert (result == expected).all()
```

### Step 2: Assign testdata = DataFrame(...)

```python
testdata = DataFrame(data)
```

### Step 3: Assign ax = testdata.plot(...)

```python
ax = testdata.plot(y=col)
```

### Step 4: Assign result = value

```python
result = ax.get_lines()[0].get_data()[1]
```

### Step 5: Assign expected = value

```python
expected = testdata[col].values
```

**Verification:**
```python
assert (result == expected).all()
```


## Complete Example

```python
# Setup
# Fixtures: col

# Workflow
data = {'numeric': np.array([1, 2, 5]), 'timedelta': [pd.Timedelta(-10, unit='s'), pd.Timedelta(10, unit='m'), pd.Timedelta(10, unit='h')], 'datetime_no_tz': [pd.to_datetime('2017-08-01 00:00:00'), pd.to_datetime('2017-08-01 02:00:00'), pd.to_datetime('2017-08-02 00:00:00')], 'datetime_all_tz': [pd.to_datetime('2017-08-01 00:00:00', utc=True), pd.to_datetime('2017-08-01 02:00:00', utc=True), pd.to_datetime('2017-08-02 00:00:00', utc=True)], 'text': ['This', 'should', 'fail']}
testdata = DataFrame(data)
ax = testdata.plot(y=col)
result = ax.get_lines()[0].get_data()[1]
expected = testdata[col].values
assert (result == expected).all()
```

## Next Steps


---

*Source: test_frame_subplots.py:129 | Complexity: Intermediate | Last updated: 2026-06-02*