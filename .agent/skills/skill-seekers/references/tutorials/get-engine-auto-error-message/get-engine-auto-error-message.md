# How To: Get Engine Auto Error Message

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get engine auto error message

## Prerequisites

**Required Modules:**
- `datetime`
- `decimal`
- `io`
- `os`
- `pathlib`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._config.config`
- `pandas.compat`
- `pandas.compat.pyarrow`
- `pandas`
- `pandas._testing`
- `pandas.util.version`
- `pandas.io.parquet`
- `pyarrow`
- `fastparquet`
- `pyarrow.dataset`
- `pandas.compat._optional`
- `pyarrow`
- `pyarrow`
- `pyarrow`
- `pyarrow`
- `pyarrow`
- `pyarrow.parquet`
- `fastparquet`
- `fastparquet`
- `fastparquet`
- `fastparquet`
- `fastparquet`
- `pytz`


## Step-by-Step Guide

### Step 1: Assign pa_min_ver = VERSIONS.get(...)

```python
pa_min_ver = VERSIONS.get('pyarrow')
```

### Step 2: Assign fp_min_ver = VERSIONS.get(...)

```python
fp_min_ver = VERSIONS.get('fastparquet')
```

### Step 3: Assign have_pa_bad_version = value

```python
have_pa_bad_version = False if not _HAVE_PYARROW else Version(pyarrow.__version__) < Version(pa_min_ver)
```

### Step 4: Assign have_fp_bad_version = value

```python
have_fp_bad_version = False if not _HAVE_FASTPARQUET else Version(fastparquet.__version__) < Version(fp_min_ver)
```

### Step 5: Assign have_usable_pa = value

```python
have_usable_pa = _HAVE_PYARROW and (not have_pa_bad_version)
```

### Step 6: Assign have_usable_fp = value

```python
have_usable_fp = _HAVE_FASTPARQUET and (not have_fp_bad_version)
```

### Step 7: Assign match = value

```python
match = f'Pandas requires version .{pa_min_ver}. or newer of .pyarrow.'
```

### Step 8: Assign match = 'Missing optional dependency .pyarrow.'

```python
match = 'Missing optional dependency .pyarrow.'
```

### Step 9: Assign match = value

```python
match = f'Pandas requires version .{fp_min_ver}. or newer of .fastparquet.'
```

### Step 10: Assign match = 'Missing optional dependency .fastparquet.'

```python
match = 'Missing optional dependency .fastparquet.'
```

### Step 11: Call get_engine()

```python
get_engine('auto')
```

### Step 12: Call get_engine()

```python
get_engine('auto')
```

### Step 13: Call get_engine()

```python
get_engine('auto')
```

### Step 14: Call get_engine()

```python
get_engine('auto')
```


## Complete Example

```python
# Workflow
from pandas.compat._optional import VERSIONS
pa_min_ver = VERSIONS.get('pyarrow')
fp_min_ver = VERSIONS.get('fastparquet')
have_pa_bad_version = False if not _HAVE_PYARROW else Version(pyarrow.__version__) < Version(pa_min_ver)
have_fp_bad_version = False if not _HAVE_FASTPARQUET else Version(fastparquet.__version__) < Version(fp_min_ver)
have_usable_pa = _HAVE_PYARROW and (not have_pa_bad_version)
have_usable_fp = _HAVE_FASTPARQUET and (not have_fp_bad_version)
if not have_usable_pa and (not have_usable_fp):
    if have_pa_bad_version:
        match = f'Pandas requires version .{pa_min_ver}. or newer of .pyarrow.'
        with pytest.raises(ImportError, match=match):
            get_engine('auto')
    else:
        match = 'Missing optional dependency .pyarrow.'
        with pytest.raises(ImportError, match=match):
            get_engine('auto')
    if have_fp_bad_version:
        match = f'Pandas requires version .{fp_min_ver}. or newer of .fastparquet.'
        with pytest.raises(ImportError, match=match):
            get_engine('auto')
    else:
        match = 'Missing optional dependency .fastparquet.'
        with pytest.raises(ImportError, match=match):
            get_engine('auto')
```

## Next Steps


---

*Source: test_parquet.py:306 | Complexity: Advanced | Last updated: 2026-06-02*