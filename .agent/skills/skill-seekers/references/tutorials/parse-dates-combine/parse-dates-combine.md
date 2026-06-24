# How To: Parse Dates Combine

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test parse dates combine

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

### Step 1: Assign raw_dates = Series(...)

```python
raw_dates = Series(date_range('1/1/2001', periods=10))
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'date': raw_dates.map(lambda x: str(x.date())), 'time': raw_dates.map(lambda x: str(x.time()))})
```

### Step 3: Assign res = flavor_read_html(...)

```python
res = flavor_read_html(StringIO(df.to_html()), parse_dates={'datetime': [1, 2]}, index_col=1)
```

### Step 4: Assign newdf = DataFrame(...)

```python
newdf = DataFrame({'datetime': raw_dates})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(newdf, res[0])
```


## Complete Example

```python
# Setup
# Fixtures: flavor_read_html

# Workflow
raw_dates = Series(date_range('1/1/2001', periods=10))
df = DataFrame({'date': raw_dates.map(lambda x: str(x.date())), 'time': raw_dates.map(lambda x: str(x.time()))})
res = flavor_read_html(StringIO(df.to_html()), parse_dates={'datetime': [1, 2]}, index_col=1)
newdf = DataFrame({'datetime': raw_dates})
tm.assert_frame_equal(newdf, res[0])
```

## Next Steps


---

*Source: test_html.py:1047 | Complexity: Intermediate | Last updated: 2026-06-02*