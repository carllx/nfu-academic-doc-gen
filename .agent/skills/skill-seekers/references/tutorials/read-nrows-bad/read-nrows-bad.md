# How To: Read Nrows Bad

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test read nrows bad

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `inspect`
- `io`
- `os`
- `pathlib`
- `sys`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.io.parsers`
- `pandas.io.parsers.c_parser_wrapper`

**Setup Required:**
```python
# Fixtures: all_parsers, nrows
```

## Step-by-Step Guide

### Step 1: Assign data = 'index,A,B,C,D\nfoo,2,3,4,5\nbar,7,8,9,10\nbaz,12,13,14,15\nqux,12,13,14,15\nfoo2,12,13,14,15\nbar2,12,13,14,15\n'

```python
data = 'index,A,B,C,D\nfoo,2,3,4,5\nbar,7,8,9,10\nbaz,12,13,14,15\nqux,12,13,14,15\nfoo2,12,13,14,15\nbar2,12,13,14,15\n'
```

### Step 2: Assign msg = "'nrows' must be an integer >=0"

```python
msg = "'nrows' must be an integer >=0"
```

### Step 3: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 4: Assign msg = "The 'nrows' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'nrows' option is not supported with the 'pyarrow' engine"
```

### Step 5: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), nrows=nrows)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, nrows

# Workflow
data = 'index,A,B,C,D\nfoo,2,3,4,5\nbar,7,8,9,10\nbaz,12,13,14,15\nqux,12,13,14,15\nfoo2,12,13,14,15\nbar2,12,13,14,15\n'
msg = "'nrows' must be an integer >=0"
parser = all_parsers
if parser.engine == 'pyarrow':
    msg = "The 'nrows' option is not supported with the 'pyarrow' engine"
with pytest.raises(ValueError, match=msg):
    parser.read_csv(StringIO(data), nrows=nrows)
```

## Next Steps


---

*Source: test_common_basic.py:258 | Complexity: Intermediate | Last updated: 2026-06-02*