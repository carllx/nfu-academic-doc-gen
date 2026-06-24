# How To: Integer Overflow Bug

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test integer overflow bug

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
# Fixtures: all_parsers, sep
```

## Step-by-Step Guide

### Step 1: Assign data = '65248E10 11\n55555E55 22\n'

```python
data = '65248E10 11\n55555E55 22\n'
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), header=None, sep=sep)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[652480000000000.0, 11], [5.5555e+59, 22]])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign msg = "the 'pyarrow' engine does not support regex separators"

```python
msg = "the 'pyarrow' engine does not support regex separators"
```

### Step 7: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), header=None, sep=sep)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, sep

# Workflow
data = '65248E10 11\n55555E55 22\n'
parser = all_parsers
if parser.engine == 'pyarrow' and sep != ' ':
    msg = "the 'pyarrow' engine does not support regex separators"
    with pytest.raises(ValueError, match=msg):
        parser.read_csv(StringIO(data), header=None, sep=sep)
    return
result = parser.read_csv(StringIO(data), header=None, sep=sep)
expected = DataFrame([[652480000000000.0, 11], [5.5555e+59, 22]])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_ints.py:105 | Complexity: Intermediate | Last updated: 2026-06-02*