# How To: Read Csv With Use Inf As Na

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read csv with use inf as na

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = '1.0\nNaN\n3.0'

```python
data = '1.0\nNaN\n3.0'
```

### Step 3: Assign msg = 'use_inf_as_na option is deprecated'

```python
msg = 'use_inf_as_na option is deprecated'
```

### Step 4: Assign warn = FutureWarning

```python
warn = FutureWarning
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame([1.0, np.nan, 3.0])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign warn = value

```python
warn = (FutureWarning, DeprecationWarning)
```

### Step 8: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), header=None)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = '1.0\nNaN\n3.0'
msg = 'use_inf_as_na option is deprecated'
warn = FutureWarning
if parser.engine == 'pyarrow':
    warn = (FutureWarning, DeprecationWarning)
with tm.assert_produces_warning(warn, match=msg, check_stacklevel=False):
    with option_context('use_inf_as_na', True):
        result = parser.read_csv(StringIO(data), header=None)
expected = DataFrame([1.0, np.nan, 3.0])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_inf.py:65 | Complexity: Advanced | Last updated: 2026-06-02*