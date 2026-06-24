# How To: Integer Thousands

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test integer thousands

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

### Step 1: Assign data = '123,456\n12,500'

```python
data = '123,456\n12,500'
```

### Step 2: Assign reader = TextReader(...)

```python
reader = TextReader(StringIO(data), delimiter=':', thousands=',', header=None)
```

### Step 3: Assign result = reader.read(...)

```python
result = reader.read()
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([123456, 12500], dtype=np.int64)
```

### Step 5: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result[0], expected)
```


## Complete Example

```python
# Workflow
data = '123,456\n12,500'
reader = TextReader(StringIO(data), delimiter=':', thousands=',', header=None)
result = reader.read()
expected = np.array([123456, 12500], dtype=np.int64)
tm.assert_almost_equal(result[0], expected)
```

## Next Steps


---

*Source: test_textreader.py:109 | Complexity: Intermediate | Last updated: 2026-06-02*