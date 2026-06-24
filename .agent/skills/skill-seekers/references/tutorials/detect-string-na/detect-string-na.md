# How To: Detect String Na

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test detect string na

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

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'A,B\nfoo,bar\nNA,baz\nNaN,nan\n'

```python
data = 'A,B\nfoo,bar\nNA,baz\nNaN,nan\n'
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([['foo', 'bar'], [np.nan, 'baz'], [np.nan, np.nan]], columns=['A', 'B'])
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign unknown = None

```python
expected.loc[[1, 2], 'A'] = None
```

### Step 7: Assign unknown = None

```python
expected.loc[2, 'B'] = None
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = 'A,B\nfoo,bar\nNA,baz\nNaN,nan\n'
expected = DataFrame([['foo', 'bar'], [np.nan, 'baz'], [np.nan, np.nan]], columns=['A', 'B'])
if parser.engine == 'pyarrow':
    expected.loc[[1, 2], 'A'] = None
    expected.loc[2, 'B'] = None
result = parser.read_csv(StringIO(data))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_na_values.py:45 | Complexity: Intermediate | Last updated: 2026-06-02*