# How To: Numeric Range Too Wide

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test numeric range too wide

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
# Fixtures: all_parsers, exp_data
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = unknown.join(...)

```python
data = '\n'.join(exp_data)
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame(exp_data)
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), header=None)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, exp_data

# Workflow
parser = all_parsers
data = '\n'.join(exp_data)
expected = DataFrame(exp_data)
result = parser.read_csv(StringIO(data), header=None)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_ints.py:213 | Complexity: Intermediate | Last updated: 2026-06-02*