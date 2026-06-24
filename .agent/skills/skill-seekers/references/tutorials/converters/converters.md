# How To: Converters

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test converters

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `dateutil.parser`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, column, converter
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'A,B,C,D\na,1,2,01/01/2009\nb,3,4,01/02/2009\nc,4,5,01/03/2009\n'

```python
data = 'A,B,C,D\na,1,2,01/01/2009\nb,3,4,01/02/2009\nc,4,5,01/03/2009\n'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), converters={column: converter})
```

### Step 4: Assign expected = parser.read_csv(...)

```python
expected = parser.read_csv(StringIO(data))
```

### Step 5: Assign unknown = unknown.map(...)

```python
expected['D'] = expected['D'].map(converter)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign msg = "The 'converters' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'converters' option is not supported with the 'pyarrow' engine"
```

### Step 8: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), converters={column: converter})
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, column, converter

# Workflow
parser = all_parsers
data = 'A,B,C,D\na,1,2,01/01/2009\nb,3,4,01/02/2009\nc,4,5,01/03/2009\n'
if parser.engine == 'pyarrow':
    msg = "The 'converters' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        parser.read_csv(StringIO(data), converters={column: converter})
    return
result = parser.read_csv(StringIO(data), converters={column: converter})
expected = parser.read_csv(StringIO(data))
expected['D'] = expected['D'].map(converter)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_converters.py:37 | Complexity: Advanced | Last updated: 2026-06-02*