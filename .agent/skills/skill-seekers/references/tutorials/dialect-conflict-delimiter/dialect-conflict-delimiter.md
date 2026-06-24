# How To: Dialect Conflict Delimiter

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dialect conflict delimiter

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
# Fixtures: all_parsers, custom_dialect, kwargs, warning_klass
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

### Step 5: Assign result = parser.read_csv_check_warnings(...)

```python
result = parser.read_csv_check_warnings(warning_klass, "Conflicting values for 'delimiter'", StringIO(data), dialect=dialect_name, **kwargs)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign msg = "The 'dialect' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'dialect' option is not supported with the 'pyarrow' engine"
```

### Step 8: Call parser.read_csv_check_warnings()

```python
parser.read_csv_check_warnings(None, "Conflicting values for 'delimiter'", StringIO(data), dialect=dialect_name, **kwargs)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, custom_dialect, kwargs, warning_klass

# Workflow
dialect_name, dialect_kwargs = custom_dialect
parser = all_parsers
expected = DataFrame({'a': [1], 'b': [2]})
data = 'a:b\n1:2'
with tm.with_csv_dialect(dialect_name, **dialect_kwargs):
    if parser.engine == 'pyarrow':
        msg = "The 'dialect' option is not supported with the 'pyarrow' engine"
        with pytest.raises(ValueError, match=msg):
            parser.read_csv_check_warnings(None, "Conflicting values for 'delimiter'", StringIO(data), dialect=dialect_name, **kwargs)
        return
    result = parser.read_csv_check_warnings(warning_klass, "Conflicting values for 'delimiter'", StringIO(data), dialect=dialect_name, **kwargs)
    tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_dialect.py:167 | Complexity: Advanced | Last updated: 2026-06-02*