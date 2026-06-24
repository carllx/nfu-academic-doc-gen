# How To: Multiple Header Rows

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiple header rows

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

### Step 1: Assign expected_df = DataFrame(...)

```python
expected_df = DataFrame(data=[('Hillary', 68, 'D'), ('Bernie', 74, 'D'), ('Donald', 69, 'R')])
```

### Step 2: Assign expected_df.columns = value

```python
expected_df.columns = [['Unnamed: 0_level_0', 'Age', 'Party'], ['Name', 'Unnamed: 1_level_1', 'Unnamed: 2_level_1']]
```

### Step 3: Assign html = expected_df.to_html(...)

```python
html = expected_df.to_html(index=False)
```

### Step 4: Assign html_df = value

```python
html_df = flavor_read_html(StringIO(html))[0]
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected_df, html_df)
```


## Complete Example

```python
# Setup
# Fixtures: flavor_read_html

# Workflow
expected_df = DataFrame(data=[('Hillary', 68, 'D'), ('Bernie', 74, 'D'), ('Donald', 69, 'R')])
expected_df.columns = [['Unnamed: 0_level_0', 'Age', 'Party'], ['Name', 'Unnamed: 1_level_1', 'Unnamed: 2_level_1']]
html = expected_df.to_html(index=False)
html_df = flavor_read_html(StringIO(html))[0]
tm.assert_frame_equal(expected_df, html_df)
```

## Next Steps


---

*Source: test_html.py:1272 | Complexity: Intermediate | Last updated: 2026-06-02*