# How To: Skip Bad Lines

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test skip bad lines

## Prerequisites

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas._libs.parsers`
- `pandas._libs.parsers`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.io.parsers`
- `pandas.io.parsers.c_parser_wrapper`


## Step-by-Step Guide

### Step 1: Assign data = 'a:b:c\nd:e:f\ng:h:i\nj:k:l:m\nl:m:n\no:p:q:r'

```python
data = 'a:b:c\nd:e:f\ng:h:i\nj:k:l:m\nl:m:n\no:p:q:r'
```

**Verification:**
```python
assert_array_dicts_equal(result, expected)
```

### Step 2: Assign reader = TextReader(...)

```python
reader = TextReader(StringIO(data), delimiter=':', header=None)
```

### Step 3: Assign msg = 'Error tokenizing data\\. C error: Expected 3 fields in line 4, saw 4'

```python
msg = 'Error tokenizing data\\. C error: Expected 3 fields in line 4, saw 4'
```

### Step 4: Assign reader = TextReader(...)

```python
reader = TextReader(StringIO(data), delimiter=':', header=None, on_bad_lines=2)
```

### Step 5: Assign result = reader.read(...)

```python
result = reader.read()
```

### Step 6: Assign expected = value

```python
expected = {0: np.array(['a', 'd', 'g', 'l'], dtype=object), 1: np.array(['b', 'e', 'h', 'm'], dtype=object), 2: np.array(['c', 'f', 'i', 'n'], dtype=object)}
```

### Step 7: Call assert_array_dicts_equal()

```python
assert_array_dicts_equal(result, expected)
```

### Step 8: Call reader.read()

```python
reader.read()
```

### Step 9: Assign reader = TextReader(...)

```python
reader = TextReader(StringIO(data), delimiter=':', header=None, on_bad_lines=1)
```

### Step 10: Call reader.read()

```python
reader.read()
```


## Complete Example

```python
# Workflow
data = 'a:b:c\nd:e:f\ng:h:i\nj:k:l:m\nl:m:n\no:p:q:r'
reader = TextReader(StringIO(data), delimiter=':', header=None)
msg = 'Error tokenizing data\\. C error: Expected 3 fields in line 4, saw 4'
with pytest.raises(parser.ParserError, match=msg):
    reader.read()
reader = TextReader(StringIO(data), delimiter=':', header=None, on_bad_lines=2)
result = reader.read()
expected = {0: np.array(['a', 'd', 'g', 'l'], dtype=object), 1: np.array(['b', 'e', 'h', 'm'], dtype=object), 2: np.array(['c', 'f', 'i', 'n'], dtype=object)}
assert_array_dicts_equal(result, expected)
with tm.assert_produces_warning(ParserWarning, match='Skipping line'):
    reader = TextReader(StringIO(data), delimiter=':', header=None, on_bad_lines=1)
    reader.read()
```

## Next Steps


---

*Source: test_textreader.py:129 | Complexity: Advanced | Last updated: 2026-06-02*