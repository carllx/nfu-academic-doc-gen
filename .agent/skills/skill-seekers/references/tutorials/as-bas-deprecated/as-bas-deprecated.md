# How To: As Bas Deprecated

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test AS BAS deprecated

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: freq_depr, expected_values, expected_freq
```

## Step-by-Step Guide

### Step 1: Assign freq_msg = value

```python
freq_msg = re.split('[0-9]*', freq_depr, maxsplit=1)[1]
```

### Step 2: Assign msg = value

```python
msg = f"'{freq_msg}' is deprecated and will be removed in a future version."
```

### Step 3: Assign result = DatetimeIndex(...)

```python
result = DatetimeIndex(expected_values, dtype='datetime64[ns]', freq=expected_freq)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign expected = date_range(...)

```python
expected = date_range(dt.datetime(2020, 12, 1), dt.datetime(2023, 12, 1), freq=freq_depr)
```


## Complete Example

```python
# Setup
# Fixtures: freq_depr, expected_values, expected_freq

# Workflow
freq_msg = re.split('[0-9]*', freq_depr, maxsplit=1)[1]
msg = f"'{freq_msg}' is deprecated and will be removed in a future version."
with tm.assert_produces_warning(FutureWarning, match=msg):
    expected = date_range(dt.datetime(2020, 12, 1), dt.datetime(2023, 12, 1), freq=freq_depr)
result = DatetimeIndex(expected_values, dtype='datetime64[ns]', freq=expected_freq)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_datetime.py:176 | Complexity: Intermediate | Last updated: 2026-06-02*