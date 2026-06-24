# How To: Non String Na Values

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test non string na values

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
# Fixtures: all_parsers, data, na_values, request
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame([[np.nan, 1.2], [2.0, np.nan], [3.0, 4.5]], columns=['A', 'B'])
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), na_values=na_values)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign msg = "The 'pyarrow' engine requires all na_values to be strings"

```python
msg = "The 'pyarrow' engine requires all na_values to be strings"
```

### Step 6: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), na_values=na_values)
```

### Step 7: Assign mark = pytest.mark.xfail(...)

```python
mark = pytest.mark.xfail(reason='pyarrow engined does not recognize equivalent floats')
```

### Step 8: Call request.applymarker()

```python
request.applymarker(mark)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, data, na_values, request

# Workflow
parser = all_parsers
expected = DataFrame([[np.nan, 1.2], [2.0, np.nan], [3.0, 4.5]], columns=['A', 'B'])
if parser.engine == 'pyarrow' and (not all((isinstance(x, str) for x in na_values))):
    msg = "The 'pyarrow' engine requires all na_values to be strings"
    with pytest.raises(TypeError, match=msg):
        parser.read_csv(StringIO(data), na_values=na_values)
    return
elif parser.engine == 'pyarrow' and '-999.000' in data:
    mark = pytest.mark.xfail(reason='pyarrow engined does not recognize equivalent floats')
    request.applymarker(mark)
result = parser.read_csv(StringIO(data), na_values=na_values)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_na_values.py:89 | Complexity: Advanced | Last updated: 2026-06-02*