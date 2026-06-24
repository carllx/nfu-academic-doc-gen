# How To: Pyarrow Engine

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pyarrow engine

## Prerequisites

**Required Modules:**
- `io`
- `os`
- `pathlib`
- `pytest`
- `pandas.errors`
- `pandas._testing`
- `pandas.io.parsers`
- `pandas.io.parsers.readers`
- `pandas.io.parsers.readers`
- `pandas.io.parsers.readers`


## Step-by-Step Guide

### Step 1: Assign data = '1,2,3,,\n        1,2,3,4,\n        1,2,3,4,5\n        1,2,,,\n        1,2,3,4,'

```python
data = '1,2,3,,\n        1,2,3,4,\n        1,2,3,4,5\n        1,2,,,\n        1,2,3,4,'
```

### Step 2: Assign msg = value

```python
msg = f"The {repr(default)} option is not supported with the 'pyarrow' engine"
```

### Step 3: Assign kwargs = value

```python
kwargs = {default: object()}
```

### Step 4: Assign default_needs_bool = value

```python
default_needs_bool = {'warn_bad_lines', 'error_bad_lines'}
```

### Step 5: Assign warn = None

```python
warn = None
```

### Step 6: Assign depr_msg = None

```python
depr_msg = None
```

### Step 7: Assign unknown = 'excel'

```python
kwargs[default] = 'excel'
```

### Step 8: Assign depr_msg = "The 'delim_whitespace' keyword in pd.read_csv is deprecated"

```python
depr_msg = "The 'delim_whitespace' keyword in pd.read_csv is deprecated"
```

### Step 9: Assign warn = FutureWarning

```python
warn = FutureWarning
```

### Step 10: Assign depr_msg = "The 'verbose' keyword in pd.read_csv is deprecated"

```python
depr_msg = "The 'verbose' keyword in pd.read_csv is deprecated"
```

### Step 11: Assign warn = FutureWarning

```python
warn = FutureWarning
```

### Step 12: Assign unknown = True

```python
kwargs[default] = True
```

### Step 13: Call read_csv()

```python
read_csv(StringIO(data), engine='pyarrow', **kwargs)
```

### Step 14: Assign unknown = 'warn'

```python
kwargs[default] = 'warn'
```


## Complete Example

```python
# Workflow
from pandas.io.parsers.readers import _pyarrow_unsupported as pa_unsupported
data = '1,2,3,,\n        1,2,3,4,\n        1,2,3,4,5\n        1,2,,,\n        1,2,3,4,'
for default in pa_unsupported:
    msg = f"The {repr(default)} option is not supported with the 'pyarrow' engine"
    kwargs = {default: object()}
    default_needs_bool = {'warn_bad_lines', 'error_bad_lines'}
    if default == 'dialect':
        kwargs[default] = 'excel'
    elif default in default_needs_bool:
        kwargs[default] = True
    elif default == 'on_bad_lines':
        kwargs[default] = 'warn'
    warn = None
    depr_msg = None
    if 'delim_whitespace' in kwargs:
        depr_msg = "The 'delim_whitespace' keyword in pd.read_csv is deprecated"
        warn = FutureWarning
    if 'verbose' in kwargs:
        depr_msg = "The 'verbose' keyword in pd.read_csv is deprecated"
        warn = FutureWarning
    with pytest.raises(ValueError, match=msg):
        with tm.assert_produces_warning(warn, match=depr_msg):
            read_csv(StringIO(data), engine='pyarrow', **kwargs)
```

## Next Steps


---

*Source: test_unsupported.py:136 | Complexity: Advanced | Last updated: 2026-06-02*