# How To: Parse Dates List

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test parse dates list

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
# Fixtures: flavor_read_html
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'date': date_range('1/1/2001', periods=10)})
```

### Step 2: Assign expected = df.to_html(...)

```python
expected = df.to_html()
```

### Step 3: Assign res = flavor_read_html(...)

```python
res = flavor_read_html(StringIO(expected), parse_dates=[1], index_col=0)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, res[0])
```

### Step 5: Assign res = flavor_read_html(...)

```python
res = flavor_read_html(StringIO(expected), parse_dates=['date'], index_col=0)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, res[0])
```


## Complete Example

```python
# Setup
# Fixtures: flavor_read_html

# Workflow
df = DataFrame({'date': date_range('1/1/2001', periods=10)})
expected = df.to_html()
res = flavor_read_html(StringIO(expected), parse_dates=[1], index_col=0)
tm.assert_frame_equal(df, res[0])
res = flavor_read_html(StringIO(expected), parse_dates=['date'], index_col=0)
tm.assert_frame_equal(df, res[0])
```

## Next Steps


---

*Source: test_html.py:1039 | Complexity: Intermediate | Last updated: 2026-06-02*