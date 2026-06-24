# How To: Dtype With Converters

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dtype with converters

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `io`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'a,b\n1.1,2.2\n1.2,2.3'

```python
data = 'a,b\n1.1,2.2\n1.2,2.3'
```

### Step 3: Assign result = parser.read_csv_check_warnings(...)

```python
result = parser.read_csv_check_warnings(ParserWarning, 'Both a converter and dtype were specified for column a - only the converter will be used.', StringIO(data), dtype={'a': 'i8'}, converters={'a': lambda x: str(x)})
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': ['1.1', '1.2'], 'b': [2.2, 2.3]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign msg = "The 'converters' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'converters' option is not supported with the 'pyarrow' engine"
```

### Step 7: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), dtype={'a': 'i8'}, converters={'a': lambda x: str(x)})
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = 'a,b\n1.1,2.2\n1.2,2.3'
if parser.engine == 'pyarrow':
    msg = "The 'converters' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        parser.read_csv(StringIO(data), dtype={'a': 'i8'}, converters={'a': lambda x: str(x)})
    return
result = parser.read_csv_check_warnings(ParserWarning, 'Both a converter and dtype were specified for column a - only the converter will be used.', StringIO(data), dtype={'a': 'i8'}, converters={'a': lambda x: str(x)})
expected = DataFrame({'a': ['1.1', '1.2'], 'b': [2.2, 2.3]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_dtypes_basic.py:107 | Complexity: Intermediate | Last updated: 2026-06-02*