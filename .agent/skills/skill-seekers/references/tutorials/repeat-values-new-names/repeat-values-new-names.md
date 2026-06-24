# How To: Repeat Values New Names

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test repeat values new names

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

### Step 1: Assign xml = '<shapes>\n  <shape>\n    <name>rectangle</name>\n    <family>rectangle</family>\n  </shape>\n  <shape>\n    <name>square</name>\n    <family>rectangle</family>\n  </shape>\n  <shape>\n    <name>ellipse</name>\n    <family>ellipse</family>\n  </shape>\n  <shape>\n    <name>circle</name>\n    <family>ellipse</family>\n  </shape>\n</shapes>'

```python
xml = '<shapes>\n  <shape>\n    <name>rectangle</name>\n    <family>rectangle</family>\n  </shape>\n  <shape>\n    <name>square</name>\n    <family>rectangle</family>\n  </shape>\n  <shape>\n    <name>ellipse</name>\n    <family>ellipse</family>\n  </shape>\n  <shape>\n    <name>circle</name>\n    <family>ellipse</family>\n  </shape>\n</shapes>'
```

### Step 2: Assign df_xpath = read_xml(...)

```python
df_xpath = read_xml(StringIO(xml), xpath='.//shape', parser=parser, names=['name', 'group'])
```

### Step 3: Assign df_iter = read_xml_iterparse(...)

```python
df_iter = read_xml_iterparse(xml, parser=parser, iterparse={'shape': ['name', 'family']}, names=['name', 'group'])
```

### Step 4: Assign df_expected = DataFrame(...)

```python
df_expected = DataFrame({'name': ['rectangle', 'square', 'ellipse', 'circle'], 'group': ['rectangle', 'rectangle', 'ellipse', 'ellipse']})
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
xml = '<shapes>\n  <shape>\n    <name>rectangle</name>\n    <family>rectangle</family>\n  </shape>\n  <shape>\n    <name>square</name>\n    <family>rectangle</family>\n  </shape>\n  <shape>\n    <name>ellipse</name>\n    <family>ellipse</family>\n  </shape>\n  <shape>\n    <name>circle</name>\n    <family>ellipse</family>\n  </shape>\n</shapes>'
df_xpath = read_xml(StringIO(xml), xpath='.//shape', parser=parser, names=['name', 'group'])
df_iter = read_xml_iterparse(xml, parser=parser, iterparse={'shape': ['name', 'family']}, names=['name', 'group'])
df_expected = DataFrame({'name': ['rectangle', 'square', 'ellipse', 'circle'], 'group': ['rectangle', 'rectangle', 'ellipse', 'ellipse']})
tm.assert_frame_equal(df_xpath, df_expected)
tm.assert_frame_equal(df_iter, df_expected)
```

## Next Steps


---

*Source: test_xml.py:928 | Complexity: Intermediate | Last updated: 2026-06-02*