# How To: Info Verbose With Counts Spacing

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Test header column, spacer, first line and last line in verbose mode.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `re`
- `string`
- `sys`
- `textwrap`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.util.version`

**Setup Required:**
```python
# Fixtures: size, header_exp, separator_exp, first_line_exp, last_line_exp
```

## Step-by-Step Guide

### Step 1: 'Test header column, spacer, first line and last line in verbose mode.'

```python
'Test header column, spacer, first line and last line in verbose mode.'
```

**Verification:**
```python
assert header == header_exp
```

### Step 2: Assign frame = DataFrame(...)

```python
frame = DataFrame(np.random.default_rng(2).standard_normal((3, size)))
```

**Verification:**
```python
assert separator == separator_exp
```

### Step 3: Assign table = value

```python
table = all_lines[3:-2]
```

**Verification:**
```python
assert first_line == first_line_exp
```

### Step 4: Assign unknown = table

```python
header, separator, first_line, *rest, last_line = table
```

**Verification:**
```python
assert last_line == last_line_exp
```

### Step 5: Call frame.info()

```python
frame.info(verbose=True, show_counts=True, buf=buf)
```

### Step 6: Assign all_lines = buf.getvalue.splitlines(...)

```python
all_lines = buf.getvalue().splitlines()
```


## Complete Example

```python
# Setup
# Fixtures: size, header_exp, separator_exp, first_line_exp, last_line_exp

# Workflow
'Test header column, spacer, first line and last line in verbose mode.'
frame = DataFrame(np.random.default_rng(2).standard_normal((3, size)))
with StringIO() as buf:
    frame.info(verbose=True, show_counts=True, buf=buf)
    all_lines = buf.getvalue().splitlines()
table = all_lines[3:-2]
header, separator, first_line, *rest, last_line = table
assert header == header_exp
assert separator == separator_exp
assert first_line == first_line_exp
assert last_line == last_line_exp
```

## Next Steps


---

*Source: test_info.py:190 | Complexity: Intermediate | Last updated: 2026-06-02*