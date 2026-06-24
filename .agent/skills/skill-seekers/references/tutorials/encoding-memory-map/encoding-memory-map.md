# How To: Encoding Memory Map

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test encoding memory map

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `os`
- `tempfile`
- `uuid`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, encoding
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame({'name': ['Raphael', 'Donatello', 'Miguel Angel', 'Leonardo'], 'mask': ['red', 'purple', 'orange', 'blue'], 'weapon': ['sai', 'bo staff', 'nunchunk', 'katana']})
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 4: Call expected.to_csv()

```python
expected.to_csv(file, index=False, encoding=encoding)
```

### Step 5: Assign df = parser.read_csv(...)

```python
df = parser.read_csv(file, encoding=encoding, memory_map=True)
```

### Step 6: Assign msg = "The 'memory_map' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'memory_map' option is not supported with the 'pyarrow' engine"
```

### Step 7: Call parser.read_csv()

```python
parser.read_csv(file, encoding=encoding, memory_map=True)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, encoding

# Workflow
parser = all_parsers
expected = DataFrame({'name': ['Raphael', 'Donatello', 'Miguel Angel', 'Leonardo'], 'mask': ['red', 'purple', 'orange', 'blue'], 'weapon': ['sai', 'bo staff', 'nunchunk', 'katana']})
with tm.ensure_clean() as file:
    expected.to_csv(file, index=False, encoding=encoding)
    if parser.engine == 'pyarrow':
        msg = "The 'memory_map' option is not supported with the 'pyarrow' engine"
        with pytest.raises(ValueError, match=msg):
            parser.read_csv(file, encoding=encoding, memory_map=True)
        return
    df = parser.read_csv(file, encoding=encoding, memory_map=True)
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_encoding.py:241 | Complexity: Intermediate | Last updated: 2026-06-02*