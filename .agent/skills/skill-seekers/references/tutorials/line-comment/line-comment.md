# How To: Line Comment

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test line comment

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
# Fixtures: all_parsers, read_kwargs, request
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = '# empty\nA,B,C\n1,2.,4.#hello world\n#ignore this line\n5.,NaN,10.0\n'

```python
data = '# empty\nA,B,C\n1,2.,4.#hello world\n#ignore this line\n5.,NaN,10.0\n'
```

### Step 3: Assign warn = None

```python
warn = None
```

### Step 4: Assign depr_msg = "The 'delim_whitespace' keyword in pd.read_csv is deprecated"

```python
depr_msg = "The 'delim_whitespace' keyword in pd.read_csv is deprecated"
```

### Step 5: Assign unknown = '#'

```python
read_kwargs['comment'] = '#'
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1.0, 2.0, 4.0], [5.0, np.nan, 10.0]], columns=['A', 'B', 'C'])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign data = data.replace(...)

```python
data = data.replace(',', ' ')
```

### Step 9: Assign warn = FutureWarning

```python
warn = FutureWarning
```

### Step 10: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), **read_kwargs)
```

### Step 11: Assign data = data.replace(...)

```python
data = data.replace('\n', read_kwargs.get('lineterminator'))
```

### Step 12: Assign msg = "The 'lineterminator' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'lineterminator' option is not supported with the 'pyarrow' engine"
```

### Step 13: Assign msg = "The 'comment' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'comment' option is not supported with the 'pyarrow' engine"
```

### Step 14: Assign msg = 'Custom line terminators not supported in python parser \\(yet\\)'

```python
msg = 'Custom line terminators not supported in python parser \\(yet\\)'
```

### Step 15: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), **read_kwargs)
```

### Step 16: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), **read_kwargs)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, read_kwargs, request

# Workflow
parser = all_parsers
data = '# empty\nA,B,C\n1,2.,4.#hello world\n#ignore this line\n5.,NaN,10.0\n'
warn = None
depr_msg = "The 'delim_whitespace' keyword in pd.read_csv is deprecated"
if read_kwargs.get('delim_whitespace'):
    data = data.replace(',', ' ')
    warn = FutureWarning
elif read_kwargs.get('lineterminator'):
    data = data.replace('\n', read_kwargs.get('lineterminator'))
read_kwargs['comment'] = '#'
if parser.engine == 'pyarrow':
    if 'lineterminator' in read_kwargs:
        msg = "The 'lineterminator' option is not supported with the 'pyarrow' engine"
    else:
        msg = "The 'comment' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        with tm.assert_produces_warning(warn, match=depr_msg, check_stacklevel=False):
            parser.read_csv(StringIO(data), **read_kwargs)
    return
elif parser.engine == 'python' and read_kwargs.get('lineterminator'):
    msg = 'Custom line terminators not supported in python parser \\(yet\\)'
    with pytest.raises(ValueError, match=msg):
        with tm.assert_produces_warning(warn, match=depr_msg, check_stacklevel=False):
            parser.read_csv(StringIO(data), **read_kwargs)
    return
with tm.assert_produces_warning(warn, match=depr_msg, check_stacklevel=False):
    result = parser.read_csv(StringIO(data), **read_kwargs)
expected = DataFrame([[1.0, 2.0, 4.0], [5.0, np.nan, 10.0]], columns=['A', 'B', 'C'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_comment.py:36 | Complexity: Advanced | Last updated: 2026-06-02*