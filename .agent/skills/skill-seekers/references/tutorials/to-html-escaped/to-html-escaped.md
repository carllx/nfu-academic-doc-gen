# How To: To Html Escaped

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test to html escaped

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
# Fixtures: kwargs, string, expected, datapath
```

## Step-by-Step Guide

### Step 1: Assign a = 'str<ing1 &amp;'

```python
a = 'str<ing1 &amp;'
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign b = 'stri>ng2 &amp;'

```python
b = 'stri>ng2 &amp;'
```

### Step 3: Assign test_dict = value

```python
test_dict = {'co<l1': {a: string, b: string}, 'co>l2': {a: string, b: string}}
```

### Step 4: Assign result = DataFrame.to_html(...)

```python
result = DataFrame(test_dict).to_html(**kwargs)
```

### Step 5: Assign expected = expected_html(...)

```python
expected = expected_html(datapath, expected)
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: kwargs, string, expected, datapath

# Workflow
a = 'str<ing1 &amp;'
b = 'stri>ng2 &amp;'
test_dict = {'co<l1': {a: string, b: string}, 'co>l2': {a: string, b: string}}
result = DataFrame(test_dict).to_html(**kwargs)
expected = expected_html(datapath, expected)
assert result == expected
```

## Next Steps


---

*Source: test_to_html.py:174 | Complexity: Intermediate | Last updated: 2026-06-02*