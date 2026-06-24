# How To: Empty Pass Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test empty pass dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'one,two'

```python
data = 'one,two'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), dtype={'one': 'u1'})
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'one': np.empty(0, dtype='u1'), 'two': np.empty(0, dtype=object)})
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
data = 'one,two'
result = parser.read_csv(StringIO(data), dtype={'one': 'u1'})
expected = DataFrame({'one': np.empty(0, dtype='u1'), 'two': np.empty(0, dtype=object)})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_empty.py:34 | Complexity: Intermediate | Last updated: 2026-06-02*