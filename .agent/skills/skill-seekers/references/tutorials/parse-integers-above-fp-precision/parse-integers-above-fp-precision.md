# How To: Parse Integers Above Fp Precision

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test parse integers above fp precision

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

### Step 1: Assign data = 'Numbers\n17007000002000191\n17007000002000191\n17007000002000191\n17007000002000191\n17007000002000192\n17007000002000192\n17007000002000192\n17007000002000192\n17007000002000192\n17007000002000194'

```python
data = 'Numbers\n17007000002000191\n17007000002000191\n17007000002000191\n17007000002000191\n17007000002000192\n17007000002000192\n17007000002000192\n17007000002000192\n17007000002000192\n17007000002000194'
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data))
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'Numbers': [17007000002000191, 17007000002000191, 17007000002000191, 17007000002000191, 17007000002000192, 17007000002000192, 17007000002000192, 17007000002000192, 17007000002000192, 17007000002000194]})
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
data = 'Numbers\n17007000002000191\n17007000002000191\n17007000002000191\n17007000002000191\n17007000002000192\n17007000002000192\n17007000002000192\n17007000002000192\n17007000002000192\n17007000002000194'
parser = all_parsers
result = parser.read_csv(StringIO(data))
expected = DataFrame({'Numbers': [17007000002000191, 17007000002000191, 17007000002000191, 17007000002000191, 17007000002000192, 17007000002000192, 17007000002000192, 17007000002000192, 17007000002000192, 17007000002000194]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_ints.py:71 | Complexity: Intermediate | Last updated: 2026-06-02*