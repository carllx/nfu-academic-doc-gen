# How To: Malformed Chunks

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test malformed chunks

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
# Fixtures: all_parsers, nrows
```

## Step-by-Step Guide

### Step 1: Assign data = 'ignore\nA,B,C\nskip\n1,2,3\n3,5,10 # comment\n1,2,3,4,5\n2,3,4\n'

```python
data = 'ignore\nA,B,C\nskip\n1,2,3\n3,5,10 # comment\n1,2,3,4,5\n2,3,4\n'
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign msg = 'Expected 3 fields in line 6, saw 5'

```python
msg = 'Expected 3 fields in line 6, saw 5'
```

### Step 4: Assign msg = "The 'iterator' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'iterator' option is not supported with the 'pyarrow' engine"
```

### Step 5: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), header=1, comment='#', iterator=True, chunksize=1, skiprows=[2])
```

### Step 6: Call reader.read()

```python
reader.read(nrows)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, nrows

# Workflow
data = 'ignore\nA,B,C\nskip\n1,2,3\n3,5,10 # comment\n1,2,3,4,5\n2,3,4\n'
parser = all_parsers
if parser.engine == 'pyarrow':
    msg = "The 'iterator' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        parser.read_csv(StringIO(data), header=1, comment='#', iterator=True, chunksize=1, skiprows=[2])
    return
msg = 'Expected 3 fields in line 6, saw 5'
with parser.read_csv(StringIO(data), header=1, comment='#', iterator=True, chunksize=1, skiprows=[2]) as reader:
    with pytest.raises(ParserError, match=msg):
        reader.read(nrows)
```

## Next Steps


---

*Source: test_read_errors.py:86 | Complexity: Intermediate | Last updated: 2026-06-02*