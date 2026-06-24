# How To: Na Values Uint64

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test na values uint64

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas._libs.parsers`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, data, kwargs, expected, request
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), header=None, **kwargs)
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 4: Assign msg = "The 'pyarrow' engine requires all na_values to be strings"

```python
msg = "The 'pyarrow' engine requires all na_values to be strings"
```

### Step 5: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), header=None, **kwargs)
```

### Step 6: Assign mark = pytest.mark.xfail(...)

```python
mark = pytest.mark.xfail(reason='Returns float64 instead of object')
```

### Step 7: Call request.applymarker()

```python
request.applymarker(mark)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, data, kwargs, expected, request

# Workflow
parser = all_parsers
if parser.engine == 'pyarrow' and 'na_values' in kwargs:
    msg = "The 'pyarrow' engine requires all na_values to be strings"
    with pytest.raises(TypeError, match=msg):
        parser.read_csv(StringIO(data), header=None, **kwargs)
    return
elif parser.engine == 'pyarrow':
    mark = pytest.mark.xfail(reason='Returns float64 instead of object')
    request.applymarker(mark)
result = parser.read_csv(StringIO(data), header=None, **kwargs)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_na_values.py:579 | Complexity: Intermediate | Last updated: 2026-06-02*