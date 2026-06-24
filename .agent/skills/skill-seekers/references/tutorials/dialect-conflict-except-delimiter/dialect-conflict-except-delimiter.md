# How To: Dialect Conflict Except Delimiter

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dialect conflict except delimiter

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `csv`
- `io`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.io.parsers.base_parser`

**Setup Required:**
```python
# Fixtures: all_parsers, custom_dialect, arg, value
```

## Step-by-Step Guide

### Step 1: Assign unknown = custom_dialect

```python
dialect_name, dialect_kwargs = custom_dialect
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1], 'b': [2]})
```

### Step 4: Assign data = 'a:b\n1:2'

```python
data = 'a:b\n1:2'
```

### Step 5: Assign warning_klass = None

```python
warning_klass = None
```

### Step 6: Assign kwds = value

```python
kwds = {}
```

### Step 7: Assign result = parser.read_csv_check_warnings(...)

```python
result = parser.read_csv_check_warnings(warning_klass, 'Conflicting values for', StringIO(data), dialect=dialect_name, **kwds)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign unknown = value

```python
kwds[arg] = dialect_kwargs[arg]
```

### Step 10: Assign msg = "The 'dialect' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'dialect' option is not supported with the 'pyarrow' engine"
```

### Step 11: Assign unknown = value

```python
kwds[arg] = parser_defaults[arg]
```

### Step 12: Assign warning_klass = ParserWarning

```python
warning_klass = ParserWarning
```

### Step 13: Assign unknown = 'blah'

```python
kwds[arg] = 'blah'
```

### Step 14: Call parser.read_csv_check_warnings()

```python
parser.read_csv_check_warnings(None, 'Conflicting values for', StringIO(data), dialect=dialect_name, **kwds)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, custom_dialect, arg, value

# Workflow
dialect_name, dialect_kwargs = custom_dialect
parser = all_parsers
expected = DataFrame({'a': [1], 'b': [2]})
data = 'a:b\n1:2'
warning_klass = None
kwds = {}
if arg is not None:
    if value == 'dialect':
        kwds[arg] = dialect_kwargs[arg]
    elif value == 'default':
        from pandas.io.parsers.base_parser import parser_defaults
        kwds[arg] = parser_defaults[arg]
    else:
        warning_klass = ParserWarning
        kwds[arg] = 'blah'
with tm.with_csv_dialect(dialect_name, **dialect_kwargs):
    if parser.engine == 'pyarrow':
        msg = "The 'dialect' option is not supported with the 'pyarrow' engine"
        with pytest.raises(ValueError, match=msg):
            parser.read_csv_check_warnings(None, 'Conflicting values for', StringIO(data), dialect=dialect_name, **kwds)
        return
    result = parser.read_csv_check_warnings(warning_klass, 'Conflicting values for', StringIO(data), dialect=dialect_name, **kwds)
    tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_dialect.py:102 | Complexity: Advanced | Last updated: 2026-06-02*