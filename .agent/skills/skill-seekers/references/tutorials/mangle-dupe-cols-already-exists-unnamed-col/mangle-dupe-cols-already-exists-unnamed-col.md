# How To: Mangle Dupe Cols Already Exists Unnamed Col

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mangle dupe cols already exists unnamed col

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
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

### Step 2: Assign data = ',Unnamed: 0,,Unnamed: 2\n1,2,3,4'

```python
data = ',Unnamed: 0,,Unnamed: 2\n1,2,3,4'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data))
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 2, 3, 4]], columns=['Unnamed: 0.1', 'Unnamed: 0', 'Unnamed: 2.1', 'Unnamed: 2'])
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
data = ',Unnamed: 0,,Unnamed: 2\n1,2,3,4'
result = parser.read_csv(StringIO(data))
expected = DataFrame([[1, 2, 3, 4]], columns=['Unnamed: 0.1', 'Unnamed: 0', 'Unnamed: 2.1', 'Unnamed: 2'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_mangle_dupes.py:162 | Complexity: Intermediate | Last updated: 2026-06-02*