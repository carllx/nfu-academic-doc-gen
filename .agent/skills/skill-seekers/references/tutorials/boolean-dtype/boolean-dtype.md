# How To: Boolean Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test boolean dtype

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

### Step 2: Assign data = unknown.join(...)

```python
data = '\n'.join(['a', 'True', 'TRUE', 'true', '1', '1.0', 'False', 'FALSE', 'false', '0', '0.0', 'NaN', 'nan', 'NA', 'null', 'NULL'])
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), dtype='boolean')
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': pd.array([True, True, True, True, True, False, False, False, False, False, None, None, None, None, None], dtype='boolean')})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = '\n'.join(['a', 'True', 'TRUE', 'true', '1', '1.0', 'False', 'FALSE', 'false', '0', '0.0', 'NaN', 'nan', 'NA', 'null', 'NULL'])
result = parser.read_csv(StringIO(data), dtype='boolean')
expected = DataFrame({'a': pd.array([True, True, True, True, True, False, False, False, False, False, None, None, None, None, None], dtype='boolean')})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_dtypes_basic.py:147 | Complexity: Intermediate | Last updated: 2026-06-02*