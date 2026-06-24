# How To: Empty Decimal Marker

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test empty decimal marker

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `codecs`
- `csv`
- `io`
- `os`
- `pathlib`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign data = 'A|B|C\n1|2,334|5\n10|13|10.\n'

```python
data = 'A|B|C\n1|2,334|5\n10|13|10.\n'
```

### Step 2: Assign msg = 'Only length-1 decimal markers supported'

```python
msg = 'Only length-1 decimal markers supported'
```

### Step 3: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 4: Assign msg = 'only single character unicode strings can be converted to Py_UCS4, got length 0'

```python
msg = 'only single character unicode strings can be converted to Py_UCS4, got length 0'
```

### Step 5: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), decimal='')
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
data = 'A|B|C\n1|2,334|5\n10|13|10.\n'
msg = 'Only length-1 decimal markers supported'
parser = all_parsers
if parser.engine == 'pyarrow':
    msg = 'only single character unicode strings can be converted to Py_UCS4, got length 0'
with pytest.raises(ValueError, match=msg):
    parser.read_csv(StringIO(data), decimal='')
```

## Next Steps


---

*Source: test_read_errors.py:28 | Complexity: Intermediate | Last updated: 2026-06-02*