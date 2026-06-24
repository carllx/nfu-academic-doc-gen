# How To: Integer Thousands Alt

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test integer thousands alt

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

### Step 1: Assign data = '123.456\n12.500'

```python
data = '123.456\n12.500'
```

### Step 2: Assign reader = TextFileReader(...)

```python
reader = TextFileReader(StringIO(data), delimiter=':', thousands='.', header=None)
```

### Step 3: Assign result = reader.read(...)

```python
result = reader.read()
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([123456, 12500])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
data = '123.456\n12.500'
reader = TextFileReader(StringIO(data), delimiter=':', thousands='.', header=None)
result = reader.read()
expected = DataFrame([123456, 12500])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_textreader.py:118 | Complexity: Intermediate | Last updated: 2026-06-02*