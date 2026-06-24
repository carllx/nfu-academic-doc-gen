# How To: String Io

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test string io

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections.abc`
- `functools`
- `io`
- `os`
- `pathlib`
- `re`
- `threading`
- `urllib.error`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.common`
- `pandas.io.html`
- `pyarrow`
- `pandas.arrays`

**Setup Required:**
```python
# Fixtures: spam_data, flavor_read_html
```

## Step-by-Step Guide

### Step 1: Assign df1 = flavor_read_html(...)

```python
df1 = flavor_read_html(data1, match='.*Water.*')
```

**Verification:**
```python
assert_framelist_equal(df1, df2)
```

### Step 2: Assign df2 = flavor_read_html(...)

```python
df2 = flavor_read_html(data2, match='Unit')
```

### Step 3: Call assert_framelist_equal()

```python
assert_framelist_equal(df1, df2)
```

### Step 4: Assign data1 = StringIO(...)

```python
data1 = StringIO(f.read())
```

### Step 5: Assign data2 = StringIO(...)

```python
data2 = StringIO(f.read())
```


## Complete Example

```python
# Setup
# Fixtures: spam_data, flavor_read_html

# Workflow
with open(spam_data, encoding='UTF-8') as f:
    data1 = StringIO(f.read())
with open(spam_data, encoding='UTF-8') as f:
    data2 = StringIO(f.read())
df1 = flavor_read_html(data1, match='.*Water.*')
df2 = flavor_read_html(data2, match='Unit')
assert_framelist_equal(df1, df2)
```

## Next Steps


---

*Source: test_html.py:353 | Complexity: Intermediate | Last updated: 2026-06-02*