# How To: Encode String Conversion

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test encode string conversion

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `calendar`
- `datetime`
- `decimal`
- `json`
- `locale`
- `math`
- `re`
- `time`
- `dateutil`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.json`
- `pandas.compat`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: ensure_ascii
```

## Step-by-Step Guide

### Step 1: Assign string_input = 'A string \\ / \x08 \x0c \n \r \t </script> &'

```python
string_input = 'A string \\ / \x08 \x0c \n \r \t </script> &'
```

**Verification:**
```python
assert output == expected_output
```

### Step 2: Assign not_html_encoded = '"A string \\\\ \\/ \\b \\f \\n \\r \\t <\\/script> &"'

```python
not_html_encoded = '"A string \\\\ \\/ \\b \\f \\n \\r \\t <\\/script> &"'
```

**Verification:**
```python
assert string_input == json.loads(output)
```

### Step 3: Assign html_encoded = '"A string \\\\ \\/ \\b \\f \\n \\r \\t \\u003c\\/script\\u003e \\u0026"'

```python
html_encoded = '"A string \\\\ \\/ \\b \\f \\n \\r \\t \\u003c\\/script\\u003e \\u0026"'
```

**Verification:**
```python
assert string_input == ujson.ujson_loads(output)
```

### Step 4: Call helper()

```python
helper(not_html_encoded)
```

### Step 5: Call helper()

```python
helper(not_html_encoded, encode_html_chars=False)
```

### Step 6: Call helper()

```python
helper(html_encoded, encode_html_chars=True)
```

### Step 7: Assign output = ujson.ujson_dumps(...)

```python
output = ujson.ujson_dumps(string_input, ensure_ascii=ensure_ascii, **encode_kwargs)
```

**Verification:**
```python
assert output == expected_output
```


## Complete Example

```python
# Setup
# Fixtures: ensure_ascii

# Workflow
string_input = 'A string \\ / \x08 \x0c \n \r \t </script> &'
not_html_encoded = '"A string \\\\ \\/ \\b \\f \\n \\r \\t <\\/script> &"'
html_encoded = '"A string \\\\ \\/ \\b \\f \\n \\r \\t \\u003c\\/script\\u003e \\u0026"'

def helper(expected_output, **encode_kwargs):
    output = ujson.ujson_dumps(string_input, ensure_ascii=ensure_ascii, **encode_kwargs)
    assert output == expected_output
    assert string_input == json.loads(output)
    assert string_input == ujson.ujson_loads(output)
helper(not_html_encoded)
helper(not_html_encoded, encode_html_chars=False)
helper(html_encoded, encode_html_chars=True)
```

## Next Steps


---

*Source: test_ujson.py:113 | Complexity: Intermediate | Last updated: 2026-06-02*