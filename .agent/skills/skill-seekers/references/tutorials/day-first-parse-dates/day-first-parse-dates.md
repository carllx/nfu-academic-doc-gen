# How To: Day First Parse Dates

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test day first parse dates

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

### Step 1: Assign xml = "<?xml version='1.0' encoding='utf-8'?>\n<data>\n  <row>\n    <shape>square</shape>\n    <degrees>00360</degrees>\n    <sides>4.0</sides>\n    <date>31/12/2020</date>\n   </row>\n  <row>\n    <shape>circle</shape>\n    <degrees>00360</degrees>\n    <sides/>\n    <date>31/12/2021</date>\n  </row>\n  <row>\n    <shape>triangle</shape>\n    <degrees>00180</degrees>\n    <sides>3.0</sides>\n    <date>31/12/2022</date>\n  </row>\n</data>"

```python
xml = "<?xml version='1.0' encoding='utf-8'?>\n<data>\n  <row>\n    <shape>square</shape>\n    <degrees>00360</degrees>\n    <sides>4.0</sides>\n    <date>31/12/2020</date>\n   </row>\n  <row>\n    <shape>circle</shape>\n    <degrees>00360</degrees>\n    <sides/>\n    <date>31/12/2021</date>\n  </row>\n  <row>\n    <shape>triangle</shape>\n    <degrees>00180</degrees>\n    <sides>3.0</sides>\n    <date>31/12/2022</date>\n  </row>\n</data>"
```

### Step 2: Assign df_expected = DataFrame(...)

```python
df_expected = DataFrame({'shape': ['square', 'circle', 'triangle'], 'degrees': [360, 360, 180], 'sides': [4.0, float('nan'), 3.0], 'date': to_datetime(['2020-12-31', '2021-12-31', '2022-12-31'])})
```

### Step 3: Assign df_result = read_xml(...)

```python
df_result = read_xml(StringIO(xml), parse_dates=['date'], parser=parser)
```

### Step 4: Assign df_iter = read_xml_iterparse(...)

```python
df_iter = read_xml_iterparse(xml, parse_dates=['date'], parser=parser, iterparse={'row': ['shape', 'degrees', 'sides', 'date']})
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
xml = "<?xml version='1.0' encoding='utf-8'?>\n<data>\n  <row>\n    <shape>square</shape>\n    <degrees>00360</degrees>\n    <sides>4.0</sides>\n    <date>31/12/2020</date>\n   </row>\n  <row>\n    <shape>circle</shape>\n    <degrees>00360</degrees>\n    <sides/>\n    <date>31/12/2021</date>\n  </row>\n  <row>\n    <shape>triangle</shape>\n    <degrees>00180</degrees>\n    <sides>3.0</sides>\n    <date>31/12/2022</date>\n  </row>\n</data>"
df_expected = DataFrame({'shape': ['square', 'circle', 'triangle'], 'degrees': [360, 360, 180], 'sides': [4.0, float('nan'), 3.0], 'date': to_datetime(['2020-12-31', '2021-12-31', '2022-12-31'])})
with tm.assert_produces_warning(UserWarning, match='Parsing dates in %d/%m/%Y format'):
    df_result = read_xml(StringIO(xml), parse_dates=['date'], parser=parser)
    df_iter = read_xml_iterparse(xml, parse_dates=['date'], parser=parser, iterparse={'row': ['shape', 'degrees', 'sides', 'date']})
    tm.assert_frame_equal(df_result, df_expected)
    tm.assert_frame_equal(df_iter, df_expected)
```

## Next Steps


---

*Source: test_xml_dtypes.py:433 | Complexity: Intermediate | Last updated: 2026-06-02*