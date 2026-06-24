# How To: No Na Values No Keep Default

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test no na values no keep default

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas._libs.parsers`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign data = 'A,B,C\na,1,None\nb,2,two\n,3,None\nd,4,nan\ne,5,five\nnan,6,\ng,7,seven\n'

```python
data = 'A,B,C\na,1,None\nb,2,two\n,3,None\nd,4,nan\ne,5,five\nnan,6,\ng,7,seven\n'
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), keep_default_na=False)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': ['a', 'b', '', 'd', 'e', 'nan', 'g'], 'B': [1, 2, 3, 4, 5, 6, 7], 'C': ['None', 'two', 'None', 'nan', 'five', '', 'seven']})
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
data = 'A,B,C\na,1,None\nb,2,two\n,3,None\nd,4,nan\ne,5,five\nnan,6,\ng,7,seven\n'
parser = all_parsers
result = parser.read_csv(StringIO(data), keep_default_na=False)
expected = DataFrame({'A': ['a', 'b', '', 'd', 'e', 'nan', 'g'], 'B': [1, 2, 3, 4, 5, 6, 7], 'C': ['None', 'two', 'None', 'nan', 'five', '', 'seven']})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_na_values.py:334 | Complexity: Intermediate | Last updated: 2026-06-02*