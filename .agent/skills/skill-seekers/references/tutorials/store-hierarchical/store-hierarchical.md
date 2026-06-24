# How To: Store Hierarchical

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test store hierarchical

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.compat`
- `pandas`
- `pandas`
- `pandas.tests.io.pytables.common`
- `pandas.util`

**Setup Required:**
```python
# Fixtures: setup_path, using_infer_string, multiindex_dataframe_random_data
```

## Step-by-Step Guide

### Step 1: Assign frame = multiindex_dataframe_random_data

```python
frame = multiindex_dataframe_random_data
```

### Step 2: Call _check_roundtrip()

```python
_check_roundtrip(frame, tm.assert_frame_equal, path=setup_path)
```

### Step 3: Call _check_roundtrip()

```python
_check_roundtrip(frame.T, tm.assert_frame_equal, path=setup_path)
```

### Step 4: Call _check_roundtrip()

```python
_check_roundtrip(frame['A'], tm.assert_series_equal, path=setup_path)
```

### Step 5: Assign msg = 'Saving a MultiIndex with an extension dtype is not supported.'

```python
msg = 'Saving a MultiIndex with an extension dtype is not supported.'
```

### Step 6: Assign unknown = frame

```python
store['frame'] = frame
```

### Step 7: Assign recons = value

```python
recons = store['frame']
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(recons, frame)
```

### Step 9: Call _check_roundtrip()

```python
_check_roundtrip(frame, tm.assert_frame_equal, path=setup_path)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path, using_infer_string, multiindex_dataframe_random_data

# Workflow
frame = multiindex_dataframe_random_data
if using_infer_string:
    msg = 'Saving a MultiIndex with an extension dtype is not supported.'
    with pytest.raises(NotImplementedError, match=msg):
        _check_roundtrip(frame, tm.assert_frame_equal, path=setup_path)
    return
_check_roundtrip(frame, tm.assert_frame_equal, path=setup_path)
_check_roundtrip(frame.T, tm.assert_frame_equal, path=setup_path)
_check_roundtrip(frame['A'], tm.assert_series_equal, path=setup_path)
with ensure_clean_store(setup_path) as store:
    store['frame'] = frame
    recons = store['frame']
    tm.assert_frame_equal(recons, frame)
```

## Next Steps


---

*Source: test_round_trip.py:432 | Complexity: Advanced | Last updated: 2026-06-02*