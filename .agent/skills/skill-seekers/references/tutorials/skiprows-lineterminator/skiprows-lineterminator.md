# How To: Skiprows Lineterminator

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test skiprows lineterminator

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `io`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, lineterminator, request
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = unknown.join(...)

```python
data = '\n'.join(['SMOSMANIA ThetaProbe-ML2X ', '2007/01/01 01:00   0.2140 U M ', '2007/01/01 02:00   0.2141 M O ', '2007/01/01 04:00   0.2142 D M '])
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([['2007/01/01', '01:00', 0.214, 'U', 'M'], ['2007/01/01', '02:00', 0.2141, 'M', 'O'], ['2007/01/01', '04:00', 0.2142, 'D', 'M']], columns=['date', 'time', 'var', 'flag', 'oflag'])
```

### Step 4: Assign data = data.replace(...)

```python
data = data.replace('\n', lineterminator)
```

### Step 5: Assign depr_msg = "The 'delim_whitespace' keyword in pd.read_csv is deprecated"

```python
depr_msg = "The 'delim_whitespace' keyword in pd.read_csv is deprecated"
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign mark = pytest.mark.xfail(...)

```python
mark = pytest.mark.xfail(reason="'CR' not respect with the Python parser yet")
```

### Step 8: Call request.applymarker()

```python
request.applymarker(mark)
```

### Step 9: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), skiprows=1, delim_whitespace=True, names=['date', 'time', 'var', 'flag', 'oflag'])
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, lineterminator, request

# Workflow
parser = all_parsers
data = '\n'.join(['SMOSMANIA ThetaProbe-ML2X ', '2007/01/01 01:00   0.2140 U M ', '2007/01/01 02:00   0.2141 M O ', '2007/01/01 04:00   0.2142 D M '])
expected = DataFrame([['2007/01/01', '01:00', 0.214, 'U', 'M'], ['2007/01/01', '02:00', 0.2141, 'M', 'O'], ['2007/01/01', '04:00', 0.2142, 'D', 'M']], columns=['date', 'time', 'var', 'flag', 'oflag'])
if parser.engine == 'python' and lineterminator == '\r':
    mark = pytest.mark.xfail(reason="'CR' not respect with the Python parser yet")
    request.applymarker(mark)
data = data.replace('\n', lineterminator)
depr_msg = "The 'delim_whitespace' keyword in pd.read_csv is deprecated"
with tm.assert_produces_warning(FutureWarning, match=depr_msg, check_stacklevel=False):
    result = parser.read_csv(StringIO(data), skiprows=1, delim_whitespace=True, names=['date', 'time', 'var', 'flag', 'oflag'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_skiprows.py:194 | Complexity: Advanced | Last updated: 2026-06-02*