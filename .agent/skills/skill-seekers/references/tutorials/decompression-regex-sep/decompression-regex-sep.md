# How To: Decompression Regex Sep

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test decompression regex sep

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `csv`
- `io`
- `typing`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `collections.abc`

**Setup Required:**
```python
# Fixtures: python_parser_only, csv1, compression, klass
```

## Step-by-Step Guide

### Step 1: Assign parser = python_parser_only

```python
parser = python_parser_only
```

### Step 2: Assign data = data.replace(...)

```python
data = data.replace(b',', b'::')
```

### Step 3: Assign expected = parser.read_csv(...)

```python
expected = parser.read_csv(csv1)
```

### Step 4: Assign module = pytest.importorskip(...)

```python
module = pytest.importorskip(compression)
```

### Step 5: Assign klass = getattr(...)

```python
klass = getattr(module, klass)
```

### Step 6: Assign data = f.read(...)

```python
data = f.read()
```

### Step 7: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(path, sep='::', compression=compression)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Call tmp.write()

```python
tmp.write(data)
```


## Complete Example

```python
# Setup
# Fixtures: python_parser_only, csv1, compression, klass

# Workflow
parser = python_parser_only
with open(csv1, 'rb') as f:
    data = f.read()
data = data.replace(b',', b'::')
expected = parser.read_csv(csv1)
module = pytest.importorskip(compression)
klass = getattr(module, klass)
with tm.ensure_clean() as path:
    with klass(path, mode='wb') as tmp:
        tmp.write(data)
    result = parser.read_csv(path, sep='::', compression=compression)
    tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_python_parser_only.py:160 | Complexity: Advanced | Last updated: 2026-06-02*