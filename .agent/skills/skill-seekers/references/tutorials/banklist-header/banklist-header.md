# How To: Banklist Header

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test banklist header

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
# Fixtures: banklist_data, datapath, flavor_read_html
```

## Step-by-Step Guide

### Step 1: Assign df = value

```python
df = flavor_read_html(banklist_data, match='Metcalf', attrs={'id': 'table'})[0]
```

**Verification:**
```python
assert df.shape == ground_truth.shape
```

### Step 2: Assign ground_truth = read_csv(...)

```python
ground_truth = read_csv(datapath('io', 'data', 'csv', 'banklist.csv'), converters={'Updated Date': Timestamp, 'Closing Date': Timestamp})
```

**Verification:**
```python
assert df.shape == ground_truth.shape
```

### Step 3: Assign old = value

```python
old = ['First Vietnamese American Bank In Vietnamese', 'Westernbank Puerto Rico En Espanol', 'R-G Premier Bank of Puerto Rico En Espanol', 'Eurobank En Espanol', 'Sanderson State Bank En Espanol', 'Washington Mutual Bank (Including its subsidiary Washington Mutual Bank FSB)', 'Silver State Bank En Espanol', 'AmTrade International Bank En Espanol', 'Hamilton Bank, NA En Espanol', 'The Citizens Savings Bank Pioneer Community Bank, Inc.']
```

### Step 4: Assign new = value

```python
new = ['First Vietnamese American Bank', 'Westernbank Puerto Rico', 'R-G Premier Bank of Puerto Rico', 'Eurobank', 'Sanderson State Bank', 'Washington Mutual Bank', 'Silver State Bank', 'AmTrade International Bank', 'Hamilton Bank, NA', 'The Citizens Savings Bank']
```

### Step 5: Assign dfnew = df.map.replace(...)

```python
dfnew = df.map(try_remove_ws).replace(old, new)
```

### Step 6: Assign gtnew = ground_truth.map(...)

```python
gtnew = ground_truth.map(try_remove_ws)
```

### Step 7: Assign converted = dfnew

```python
converted = dfnew
```

### Step 8: Assign date_cols = value

```python
date_cols = ['Closing Date', 'Updated Date']
```

### Step 9: Assign unknown = unknown.apply(...)

```python
converted[date_cols] = converted[date_cols].apply(to_datetime)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(converted, gtnew)
```


## Complete Example

```python
# Setup
# Fixtures: banklist_data, datapath, flavor_read_html

# Workflow
from pandas.io.html import _remove_whitespace

def try_remove_ws(x):
    try:
        return _remove_whitespace(x)
    except AttributeError:
        return x
df = flavor_read_html(banklist_data, match='Metcalf', attrs={'id': 'table'})[0]
ground_truth = read_csv(datapath('io', 'data', 'csv', 'banklist.csv'), converters={'Updated Date': Timestamp, 'Closing Date': Timestamp})
assert df.shape == ground_truth.shape
old = ['First Vietnamese American Bank In Vietnamese', 'Westernbank Puerto Rico En Espanol', 'R-G Premier Bank of Puerto Rico En Espanol', 'Eurobank En Espanol', 'Sanderson State Bank En Espanol', 'Washington Mutual Bank (Including its subsidiary Washington Mutual Bank FSB)', 'Silver State Bank En Espanol', 'AmTrade International Bank En Espanol', 'Hamilton Bank, NA En Espanol', 'The Citizens Savings Bank Pioneer Community Bank, Inc.']
new = ['First Vietnamese American Bank', 'Westernbank Puerto Rico', 'R-G Premier Bank of Puerto Rico', 'Eurobank', 'Sanderson State Bank', 'Washington Mutual Bank', 'Silver State Bank', 'AmTrade International Bank', 'Hamilton Bank, NA', 'The Citizens Savings Bank']
dfnew = df.map(try_remove_ws).replace(old, new)
gtnew = ground_truth.map(try_remove_ws)
converted = dfnew
date_cols = ['Closing Date', 'Updated Date']
converted[date_cols] = converted[date_cols].apply(to_datetime)
tm.assert_frame_equal(converted, gtnew)
```

## Next Steps


---

*Source: test_html.py:738 | Complexity: Advanced | Last updated: 2026-06-02*