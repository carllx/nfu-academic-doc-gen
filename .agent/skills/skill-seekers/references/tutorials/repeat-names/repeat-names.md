# How To: Repeat Names

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test repeat names

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

### Step 1: Assign xml = '<shapes>\n  <shape type="2D">\n    <name>circle</name>\n    <type>curved</type>\n  </shape>\n  <shape type="3D">\n    <name>sphere</name>\n    <type>curved</type>\n  </shape>\n</shapes>'

```python
xml = '<shapes>\n  <shape type="2D">\n    <name>circle</name>\n    <type>curved</type>\n  </shape>\n  <shape type="3D">\n    <name>sphere</name>\n    <type>curved</type>\n  </shape>\n</shapes>'
```

### Step 2: Assign df_xpath = read_xml(...)

```python
df_xpath = read_xml(StringIO(xml), xpath='.//shape', parser=parser, names=['type_dim', 'shape', 'type_edge'])
```

### Step 3: Assign df_iter = read_xml_iterparse(...)

```python
df_iter = read_xml_iterparse(xml, parser=parser, iterparse={'shape': ['type', 'name', 'type']}, names=['type_dim', 'shape', 'type_edge'])
```

### Step 4: Assign df_expected = DataFrame(...)

```python
df_expected = DataFrame({'type_dim': ['2D', '3D'], 'shape': ['circle', 'sphere'], 'type_edge': ['curved', 'curved']})
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
xml = '<shapes>\n  <shape type="2D">\n    <name>circle</name>\n    <type>curved</type>\n  </shape>\n  <shape type="3D">\n    <name>sphere</name>\n    <type>curved</type>\n  </shape>\n</shapes>'
df_xpath = read_xml(StringIO(xml), xpath='.//shape', parser=parser, names=['type_dim', 'shape', 'type_edge'])
df_iter = read_xml_iterparse(xml, parser=parser, iterparse={'shape': ['type', 'name', 'type']}, names=['type_dim', 'shape', 'type_edge'])
df_expected = DataFrame({'type_dim': ['2D', '3D'], 'shape': ['circle', 'sphere'], 'type_edge': ['curved', 'curved']})
tm.assert_frame_equal(df_xpath, df_expected)
tm.assert_frame_equal(df_iter, df_expected)
```

## Next Steps


---

*Source: test_xml.py:890 | Complexity: Intermediate | Last updated: 2026-06-02*