# How To: Unbalanced Quoting

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test unbalanced quoting

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `csv`
- `io`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, balanced, request
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'a,b,c\n1,2,"3'

```python
data = 'a,b,c\n1,2,"3'
```

### Step 3: Assign mark = pytest.mark.xfail(...)

```python
mark = pytest.mark.xfail(reason='Mismatched result')
```

### Step 4: Call request.applymarker()

```python
request.applymarker(mark)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 2, 3]], columns=['a', 'b', 'c'])
```

### Step 6: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data + '"'))
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign msg = value

```python
msg = 'EOF inside string starting at row 1' if parser.engine == 'c' else 'unexpected end of data'
```

### Step 9: Call parser.read_csv()

```python
parser.read_csv(StringIO(data))
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, balanced, request

# Workflow
parser = all_parsers
data = 'a,b,c\n1,2,"3'
if parser.engine == 'pyarrow' and (not balanced):
    mark = pytest.mark.xfail(reason='Mismatched result')
    request.applymarker(mark)
if balanced:
    expected = DataFrame([[1, 2, 3]], columns=['a', 'b', 'c'])
    result = parser.read_csv(StringIO(data + '"'))
    tm.assert_frame_equal(result, expected)
else:
    msg = 'EOF inside string starting at row 1' if parser.engine == 'c' else 'unexpected end of data'
    with pytest.raises(ParserError, match=msg):
        parser.read_csv(StringIO(data))
```

## Next Steps


---

*Source: test_quoting.py:177 | Complexity: Advanced | Last updated: 2026-06-02*