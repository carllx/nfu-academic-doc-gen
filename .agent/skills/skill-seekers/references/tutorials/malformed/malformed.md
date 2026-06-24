# How To: Malformed

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test malformed

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

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'ignore\nA,B,C\n1,2,3 # comment\n1,2,3,4,5\n2,3,4\n'

```python
data = 'ignore\nA,B,C\n1,2,3 # comment\n1,2,3,4,5\n2,3,4\n'
```

### Step 3: Assign msg = 'Expected 3 fields in line 4, saw 5'

```python
msg = 'Expected 3 fields in line 4, saw 5'
```

### Step 4: Assign err = ParserError

```python
err = ParserError
```

### Step 5: Assign msg = "The 'comment' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'comment' option is not supported with the 'pyarrow' engine"
```

### Step 6: Assign err = ValueError

```python
err = ValueError
```

### Step 7: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), header=1, comment='#')
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = 'ignore\nA,B,C\n1,2,3 # comment\n1,2,3,4,5\n2,3,4\n'
msg = 'Expected 3 fields in line 4, saw 5'
err = ParserError
if parser.engine == 'pyarrow':
    msg = "The 'comment' option is not supported with the 'pyarrow' engine"
    err = ValueError
with pytest.raises(err, match=msg):
    parser.read_csv(StringIO(data), header=1, comment='#')
```

## Next Steps


---

*Source: test_read_errors.py:67 | Complexity: Intermediate | Last updated: 2026-06-02*