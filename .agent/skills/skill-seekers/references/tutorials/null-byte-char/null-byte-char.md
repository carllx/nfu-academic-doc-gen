# How To: Null Byte Char

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test null byte char

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `codecs`
- `csv`
- `io`
- `os`
- `pathlib`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: request, all_parsers
```

## Step-by-Step Guide

### Step 1: Assign data = '\x00,foo'

```python
data = '\x00,foo'
```

### Step 2: Assign names = value

```python
names = ['a', 'b']
```

### Step 3: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[np.nan, 'foo']], columns=names)
```

### Step 5: Assign out = parser.read_csv(...)

```python
out = parser.read_csv(StringIO(data), names=names)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(out, expected)
```

### Step 7: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(reason='In Python 3.11, this is read as an empty character not null'))
```

### Step 8: Call pytest.skip()

```python
pytest.skip(reason='https://github.com/apache/arrow/issues/38676')
```

### Step 9: Assign msg = 'NULL byte detected'

```python
msg = 'NULL byte detected'
```

### Step 10: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), names=names)
```


## Complete Example

```python
# Setup
# Fixtures: request, all_parsers

# Workflow
data = '\x00,foo'
names = ['a', 'b']
parser = all_parsers
if parser.engine == 'c' or (parser.engine == 'python' and PY311):
    if parser.engine == 'python' and PY311:
        request.applymarker(pytest.mark.xfail(reason='In Python 3.11, this is read as an empty character not null'))
    expected = DataFrame([[np.nan, 'foo']], columns=names)
    out = parser.read_csv(StringIO(data), names=names)
    tm.assert_frame_equal(out, expected)
else:
    if parser.engine == 'pyarrow':
        pytest.skip(reason='https://github.com/apache/arrow/issues/38676')
    else:
        msg = 'NULL byte detected'
    with pytest.raises(ParserError, match=msg):
        parser.read_csv(StringIO(data), names=names)
```

## Next Steps


---

*Source: test_read_errors.py:222 | Complexity: Advanced | Last updated: 2026-06-02*