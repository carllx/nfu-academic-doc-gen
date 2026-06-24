# How To: Too Many Exponent Digits

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test too many exponent digits

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers_all_precisions, exp, request
```

## Step-by-Step Guide

### Step 1: Assign unknown = all_parsers_all_precisions

```python
parser, precision = all_parsers_all_precisions
```

### Step 2: Assign data = value

```python
data = f'data\n10E{exp}'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), float_precision=precision)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign value = value

```python
value = np.inf if exp > 0 else 0.0
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame({'data': [value]})
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({'data': [f'10E{exp}']})
```

### Step 8: Assign mark = pytest.mark.xfail(...)

```python
mark = pytest.mark.xfail(reason='GH38794, on Linux gives object result')
```

### Step 9: Call request.applymarker()

```python
request.applymarker(mark)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers_all_precisions, exp, request

# Workflow
parser, precision = all_parsers_all_precisions
data = f'data\n10E{exp}'
result = parser.read_csv(StringIO(data), float_precision=precision)
if precision == 'round_trip':
    if exp == 999999999999999999 and is_platform_linux():
        mark = pytest.mark.xfail(reason='GH38794, on Linux gives object result')
        request.applymarker(mark)
    value = np.inf if exp > 0 else 0.0
    expected = DataFrame({'data': [value]})
else:
    expected = DataFrame({'data': [f'10E{exp}']})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_float.py:64 | Complexity: Advanced | Last updated: 2026-06-02*