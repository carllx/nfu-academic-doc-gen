# How To: Subplots Timeseries Y Axis Not Supported

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: This test will fail for:
    period:
        since period isn't yet implemented in ``select_dtypes``
        and because it will need a custom value converter +
        tick formatter (as was done for x-axis plots)

    categorical:
         because it will need a custom value converter +
         tick formatter (also doesn't work for x-axis, as of now)

    datetime_mixed_tz:
        because of the way how pandas handles ``Series`` of
        ``datetime`` objects with different timezone,
        generally converting ``datetime`` objects in a tz-aware
        form could help with this problem

## Prerequisites

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


## Step-by-Step Guide

### Step 1: "\n        This test will fail for:\n            period:\n                since period isn't yet implemented in ``select_dtypes``\n                and because it will need a custom value converter +\n                tick formatter (as was done for x-axis plots)\n\n            categorical:\n                 because it will need a custom value converter +\n                 tick formatter (also doesn't work for x-axis, as of now)\n\n            datetime_mixed_tz:\n                because of the way how pandas handles ``Series`` of\n                ``datetime`` objects with different timezone,\n                generally converting ``datetime`` objects in a tz-aware\n                form could help with this problem\n        "

```python
"\n        This test will fail for:\n            period:\n                since period isn't yet implemented in ``select_dtypes``\n                and because it will need a custom value converter +\n                tick formatter (as was done for x-axis plots)\n\n            categorical:\n                 because it will need a custom value converter +\n                 tick formatter (also doesn't work for x-axis, as of now)\n\n            datetime_mixed_tz:\n                because of the way how pandas handles ``Series`` of\n                ``datetime`` objects with different timezone,\n                generally converting ``datetime`` objects in a tz-aware\n                form could help with this problem\n        "
```

**Verification:**
```python
assert (ax_period.get_lines()[0].get_data()[1] == testdata['period'].values).all()
```

### Step 2: Assign data = value

```python
data = {'numeric': np.array([1, 2, 5]), 'period': [pd.Period('2017-08-01 00:00:00', freq='H'), pd.Period('2017-08-01 02:00', freq='H'), pd.Period('2017-08-02 00:00:00', freq='H')], 'categorical': pd.Categorical(['c', 'b', 'a'], categories=['a', 'b', 'c'], ordered=False), 'datetime_mixed_tz': [pd.to_datetime('2017-08-01 00:00:00', utc=True), pd.to_datetime('2017-08-01 02:00:00'), pd.to_datetime('2017-08-02 00:00:00')]}
```

**Verification:**
```python
assert (ax_categorical.get_lines()[0].get_data()[1] == testdata['categorical'].values).all()
```

### Step 3: Assign testdata = DataFrame(...)

```python
testdata = DataFrame(data)
```

**Verification:**
```python
assert (ax_datetime_mixed_tz.get_lines()[0].get_data()[1] == testdata['datetime_mixed_tz'].values).all()
```

### Step 4: Assign ax_period = testdata.plot(...)

```python
ax_period = testdata.plot(x='numeric', y='period')
```

**Verification:**
```python
assert (ax_period.get_lines()[0].get_data()[1] == testdata['period'].values).all()
```

### Step 5: Assign ax_categorical = testdata.plot(...)

```python
ax_categorical = testdata.plot(x='numeric', y='categorical')
```

**Verification:**
```python
assert (ax_categorical.get_lines()[0].get_data()[1] == testdata['categorical'].values).all()
```

### Step 6: Assign ax_datetime_mixed_tz = testdata.plot(...)

```python
ax_datetime_mixed_tz = testdata.plot(x='numeric', y='datetime_mixed_tz')
```

**Verification:**
```python
assert (ax_datetime_mixed_tz.get_lines()[0].get_data()[1] == testdata['datetime_mixed_tz'].values).all()
```


## Complete Example

```python
# Workflow
"\n        This test will fail for:\n            period:\n                since period isn't yet implemented in ``select_dtypes``\n                and because it will need a custom value converter +\n                tick formatter (as was done for x-axis plots)\n\n            categorical:\n                 because it will need a custom value converter +\n                 tick formatter (also doesn't work for x-axis, as of now)\n\n            datetime_mixed_tz:\n                because of the way how pandas handles ``Series`` of\n                ``datetime`` objects with different timezone,\n                generally converting ``datetime`` objects in a tz-aware\n                form could help with this problem\n        "
data = {'numeric': np.array([1, 2, 5]), 'period': [pd.Period('2017-08-01 00:00:00', freq='H'), pd.Period('2017-08-01 02:00', freq='H'), pd.Period('2017-08-02 00:00:00', freq='H')], 'categorical': pd.Categorical(['c', 'b', 'a'], categories=['a', 'b', 'c'], ordered=False), 'datetime_mixed_tz': [pd.to_datetime('2017-08-01 00:00:00', utc=True), pd.to_datetime('2017-08-01 02:00:00'), pd.to_datetime('2017-08-02 00:00:00')]}
testdata = DataFrame(data)
ax_period = testdata.plot(x='numeric', y='period')
assert (ax_period.get_lines()[0].get_data()[1] == testdata['period'].values).all()
ax_categorical = testdata.plot(x='numeric', y='categorical')
assert (ax_categorical.get_lines()[0].get_data()[1] == testdata['categorical'].values).all()
ax_datetime_mixed_tz = testdata.plot(x='numeric', y='datetime_mixed_tz')
assert (ax_datetime_mixed_tz.get_lines()[0].get_data()[1] == testdata['datetime_mixed_tz'].values).all()
```

## Next Steps


---

*Source: test_frame_subplots.py:169 | Complexity: Intermediate | Last updated: 2026-06-02*