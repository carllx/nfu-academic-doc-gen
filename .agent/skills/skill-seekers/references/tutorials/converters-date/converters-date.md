# How To: Converters Date

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test converters date

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `io`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.io.xml`

**Setup Required:**
```python
# Fixtures: parser
```

## Step-by-Step Guide

### Step 1: Assign convert_to_datetime = value

```python
convert_to_datetime = lambda x: to_datetime(x)
```

### Step 2: Assign df_result = read_xml(...)

```python
df_result = read_xml(StringIO(xml_dates), converters={'date': convert_to_datetime}, parser=parser)
```

### Step 3: Assign df_iter = read_xml_iterparse(...)

```python
df_iter = read_xml_iterparse(xml_dates, parser=parser, converters={'date': convert_to_datetime}, iterparse={'row': ['shape', 'degrees', 'sides', 'date']})
```

### Step 4: Assign df_expected = DataFrame(...)

```python
df_expected = DataFrame({'shape': ['square', 'circle', 'triangle'], 'degrees': [360, 360, 180], 'sides': [4.0, float('nan'), 3.0], 'date': to_datetime(['2020-01-01', '2021-01-01', '2022-01-01'])})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_result, df_expected)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_iter, df_expected)
```


## Complete Example

```python
# Setup
# Fixtures: parser

# Workflow
convert_to_datetime = lambda x: to_datetime(x)
df_result = read_xml(StringIO(xml_dates), converters={'date': convert_to_datetime}, parser=parser)
df_iter = read_xml_iterparse(xml_dates, parser=parser, converters={'date': convert_to_datetime}, iterparse={'row': ['shape', 'degrees', 'sides', 'date']})
df_expected = DataFrame({'shape': ['square', 'circle', 'triangle'], 'degrees': [360, 360, 180], 'sides': [4.0, float('nan'), 3.0], 'date': to_datetime(['2020-01-01', '2021-01-01', '2022-01-01'])})
tm.assert_frame_equal(df_result, df_expected)
tm.assert_frame_equal(df_iter, df_expected)
```

## Next Steps


---

*Source: test_xml_dtypes.py:265 | Complexity: Intermediate | Last updated: 2026-06-02*