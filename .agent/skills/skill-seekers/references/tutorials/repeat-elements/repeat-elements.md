# How To: Repeat Elements

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test repeat elements

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `io`
- `lzma`
- `os`
- `tarfile`
- `urllib.error`
- `xml.etree.ElementTree`
- `zipfile`
- `numpy`
- `pytest`
- `pandas.compat._optional`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.common`
- `pandas.io.xml`
- `pandas.arrays`

**Setup Required:**
```python
# Fixtures: parser
```

## Step-by-Step Guide

### Step 1: Assign xml = '<shapes>\n  <shape>\n    <value item="name">circle</value>\n    <value item="family">ellipse</value>\n    <value item="degrees">360</value>\n    <value item="sides">0</value>\n  </shape>\n  <shape>\n    <value item="name">triangle</value>\n    <value item="family">polygon</value>\n    <value item="degrees">180</value>\n    <value item="sides">3</value>\n  </shape>\n  <shape>\n    <value item="name">square</value>\n    <value item="family">polygon</value>\n    <value item="degrees">360</value>\n    <value item="sides">4</value>\n  </shape>\n</shapes>'

```python
xml = '<shapes>\n  <shape>\n    <value item="name">circle</value>\n    <value item="family">ellipse</value>\n    <value item="degrees">360</value>\n    <value item="sides">0</value>\n  </shape>\n  <shape>\n    <value item="name">triangle</value>\n    <value item="family">polygon</value>\n    <value item="degrees">180</value>\n    <value item="sides">3</value>\n  </shape>\n  <shape>\n    <value item="name">square</value>\n    <value item="family">polygon</value>\n    <value item="degrees">360</value>\n    <value item="sides">4</value>\n  </shape>\n</shapes>'
```

### Step 2: Assign df_xpath = read_xml(...)

```python
df_xpath = read_xml(StringIO(xml), xpath='.//shape', parser=parser, names=['name', 'family', 'degrees', 'sides'])
```

### Step 3: Assign df_iter = read_xml_iterparse(...)

```python
df_iter = read_xml_iterparse(xml, parser=parser, iterparse={'shape': ['value', 'value', 'value', 'value']}, names=['name', 'family', 'degrees', 'sides'])
```

### Step 4: Assign df_expected = DataFrame(...)

```python
df_expected = DataFrame({'name': ['circle', 'triangle', 'square'], 'family': ['ellipse', 'polygon', 'polygon'], 'degrees': [360, 180, 360], 'sides': [0, 3, 4]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_xpath, df_expected)
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
xml = '<shapes>\n  <shape>\n    <value item="name">circle</value>\n    <value item="family">ellipse</value>\n    <value item="degrees">360</value>\n    <value item="sides">0</value>\n  </shape>\n  <shape>\n    <value item="name">triangle</value>\n    <value item="family">polygon</value>\n    <value item="degrees">180</value>\n    <value item="sides">3</value>\n  </shape>\n  <shape>\n    <value item="name">square</value>\n    <value item="family">polygon</value>\n    <value item="degrees">360</value>\n    <value item="sides">4</value>\n  </shape>\n</shapes>'
df_xpath = read_xml(StringIO(xml), xpath='.//shape', parser=parser, names=['name', 'family', 'degrees', 'sides'])
df_iter = read_xml_iterparse(xml, parser=parser, iterparse={'shape': ['value', 'value', 'value', 'value']}, names=['name', 'family', 'degrees', 'sides'])
df_expected = DataFrame({'name': ['circle', 'triangle', 'square'], 'family': ['ellipse', 'polygon', 'polygon'], 'degrees': [360, 180, 360], 'sides': [0, 3, 4]})
tm.assert_frame_equal(df_xpath, df_expected)
tm.assert_frame_equal(df_iter, df_expected)
```

## Next Steps


---

*Source: test_xml.py:970 | Complexity: Intermediate | Last updated: 2026-06-02*