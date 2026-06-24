# How To: Read With Where Tz Aware Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read with where tz aware index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.timezones`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.io.pytables.common`

**Setup Required:**
```python
# Fixtures: tmp_path, setup_path
```

## Step-by-Step Guide

### Step 1: Assign periods = 10

```python
periods = 10
```

### Step 2: Assign dts = date_range(...)

```python
dts = date_range('20151201', periods=periods, freq='D', tz='UTC')
```

### Step 3: Assign mi = pd.MultiIndex.from_arrays(...)

```python
mi = pd.MultiIndex.from_arrays([dts, range(periods)], names=['DATE', 'NO'])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'MYCOL': 0}, index=mi)
```

### Step 5: Assign key = 'mykey'

```python
key = 'mykey'
```

### Step 6: Assign path = value

```python
path = tmp_path / setup_path
```

### Step 7: Assign result = pd.read_hdf(...)

```python
result = pd.read_hdf(path, key, where='DATE > 20151130')
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Call store.append()

```python
store.append(key, expected, format='table', append=True)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, setup_path

# Workflow
periods = 10
dts = date_range('20151201', periods=periods, freq='D', tz='UTC')
mi = pd.MultiIndex.from_arrays([dts, range(periods)], names=['DATE', 'NO'])
expected = DataFrame({'MYCOL': 0}, index=mi)
key = 'mykey'
path = tmp_path / setup_path
with pd.HDFStore(path) as store:
    store.append(key, expected, format='table', append=True)
result = pd.read_hdf(path, key, where='DATE > 20151130')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_timezones.py:352 | Complexity: Advanced | Last updated: 2026-06-02*