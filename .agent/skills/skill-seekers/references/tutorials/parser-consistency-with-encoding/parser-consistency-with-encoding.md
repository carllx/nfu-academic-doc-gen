# How To: Parser Consistency With Encoding

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test parser consistency with encoding

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
# Fixtures: xml_baby_names
```

## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('lxml')
```

### Step 2: Assign df_xpath_lxml = read_xml(...)

```python
df_xpath_lxml = read_xml(xml_baby_names, parser='lxml', encoding='ISO-8859-1')
```

### Step 3: Assign df_xpath_etree = read_xml(...)

```python
df_xpath_etree = read_xml(xml_baby_names, parser='etree', encoding='iso-8859-1')
```

### Step 4: Assign df_iter_lxml = read_xml(...)

```python
df_iter_lxml = read_xml(xml_baby_names, parser='lxml', encoding='ISO-8859-1', iterparse={'row': ['rank', 'malename', 'femalename']})
```

### Step 5: Assign df_iter_etree = read_xml(...)

```python
df_iter_etree = read_xml(xml_baby_names, parser='etree', encoding='ISO-8859-1', iterparse={'row': ['rank', 'malename', 'femalename']})
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_xpath_lxml, df_xpath_etree)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_xpath_etree, df_iter_etree)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_iter_lxml, df_iter_etree)
```


## Complete Example

```python
# Setup
# Fixtures: xml_baby_names

# Workflow
pytest.importorskip('lxml')
df_xpath_lxml = read_xml(xml_baby_names, parser='lxml', encoding='ISO-8859-1')
df_xpath_etree = read_xml(xml_baby_names, parser='etree', encoding='iso-8859-1')
df_iter_lxml = read_xml(xml_baby_names, parser='lxml', encoding='ISO-8859-1', iterparse={'row': ['rank', 'malename', 'femalename']})
df_iter_etree = read_xml(xml_baby_names, parser='etree', encoding='ISO-8859-1', iterparse={'row': ['rank', 'malename', 'femalename']})
tm.assert_frame_equal(df_xpath_lxml, df_xpath_etree)
tm.assert_frame_equal(df_xpath_etree, df_iter_etree)
tm.assert_frame_equal(df_iter_lxml, df_iter_etree)
```

## Next Steps


---

*Source: test_xml.py:1058 | Complexity: Advanced | Last updated: 2026-06-02*