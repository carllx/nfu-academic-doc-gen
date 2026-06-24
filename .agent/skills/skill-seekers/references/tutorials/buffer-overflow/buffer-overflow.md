# How To: Buffer Overflow

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test buffer overflow

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `decimal`
- `io`
- `mmap`
- `os`
- `tarfile`
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: c_parser_only, malformed
```

## Step-by-Step Guide

### Step 1: Assign msg = 'Buffer overflow caught - possible malformed input file.'

```python
msg = 'Buffer overflow caught - possible malformed input file.'
```

### Step 2: Assign parser = c_parser_only

```python
parser = c_parser_only
```

### Step 3: Call parser.read_csv()

```python
parser.read_csv(StringIO(malformed))
```


## Complete Example

```python
# Setup
# Fixtures: c_parser_only, malformed

# Workflow
msg = 'Buffer overflow caught - possible malformed input file.'
parser = c_parser_only
with pytest.raises(ParserError, match=msg):
    parser.read_csv(StringIO(malformed))
```

## Next Steps


---

*Source: test_c_parser_only.py:39 | Complexity: Beginner | Last updated: 2026-06-02*