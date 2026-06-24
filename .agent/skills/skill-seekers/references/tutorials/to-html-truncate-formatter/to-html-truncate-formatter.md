# How To: To Html Truncate Formatter

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to html truncate formatter

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `io`
- `itertools`
- `re`
- `textwrap`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.formats.format`

**Setup Required:**
```python
# Fixtures: datapath
```

## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = [{'A': 1, 'B': 2, 'C': 3, 'D': 4}, {'A': 5, 'B': 6, 'C': 7, 'D': 8}, {'A': 9, 'B': 10, 'C': 11, 'D': 12}, {'A': 13, 'B': 14, 'C': 15, 'D': 16}]
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(data)
```

### Step 3: Assign fmt = value

```python
fmt = lambda x: str(x) + '_mod'
```

### Step 4: Assign formatters = value

```python
formatters = [fmt, fmt, None, None]
```

### Step 5: Assign result = df.to_html(...)

```python
result = df.to_html(formatters=formatters, max_cols=3)
```

### Step 6: Assign expected = expected_html(...)

```python
expected = expected_html(datapath, 'truncate_formatter')
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: datapath

# Workflow
data = [{'A': 1, 'B': 2, 'C': 3, 'D': 4}, {'A': 5, 'B': 6, 'C': 7, 'D': 8}, {'A': 9, 'B': 10, 'C': 11, 'D': 12}, {'A': 13, 'B': 14, 'C': 15, 'D': 16}]
df = DataFrame(data)
fmt = lambda x: str(x) + '_mod'
formatters = [fmt, fmt, None, None]
result = df.to_html(formatters=formatters, max_cols=3)
expected = expected_html(datapath, 'truncate_formatter')
assert result == expected
```

## Next Steps


---

*Source: test_to_html.py:319 | Complexity: Intermediate | Last updated: 2026-06-02*