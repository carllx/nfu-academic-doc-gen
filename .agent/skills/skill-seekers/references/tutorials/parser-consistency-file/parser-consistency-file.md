# How To: Parser Consistency File

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test parser consistency file

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
# Fixtures: xml_books
```

## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('lxml')
```

### Step 2: Assign df_file_lxml = read_xml(...)

```python
df_file_lxml = read_xml(xml_books, parser='lxml')
```

### Step 3: Assign df_file_etree = read_xml(...)

```python
df_file_etree = read_xml(xml_books, parser='etree')
```

### Step 4: Assign df_iter_lxml = read_xml(...)

```python
df_iter_lxml = read_xml(xml_books, parser='lxml', iterparse={'book': ['category', 'title', 'year', 'author', 'price']})
```

### Step 5: Assign df_iter_etree = read_xml(...)

```python
df_iter_etree = read_xml(xml_books, parser='etree', iterparse={'book': ['category', 'title', 'year', 'author', 'price']})
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_file_lxml, df_file_etree)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_file_lxml, df_iter_lxml)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_iter_lxml, df_iter_etree)
```


## Complete Example

```python
# Setup
# Fixtures: xml_books

# Workflow
pytest.importorskip('lxml')
df_file_lxml = read_xml(xml_books, parser='lxml')
df_file_etree = read_xml(xml_books, parser='etree')
df_iter_lxml = read_xml(xml_books, parser='lxml', iterparse={'book': ['category', 'title', 'year', 'author', 'price']})
df_iter_etree = read_xml(xml_books, parser='etree', iterparse={'book': ['category', 'title', 'year', 'author', 'price']})
tm.assert_frame_equal(df_file_lxml, df_file_etree)
tm.assert_frame_equal(df_file_lxml, df_iter_lxml)
tm.assert_frame_equal(df_iter_lxml, df_iter_etree)
```

## Next Steps


---

*Source: test_xml.py:286 | Complexity: Advanced | Last updated: 2026-06-02*