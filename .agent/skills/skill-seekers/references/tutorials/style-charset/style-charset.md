# How To: Style Charset

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test style charset

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('lxml')
```

### Step 2: Assign xml = '<中文標籤><row><c1>1</c1><c2>2</c2></row></中文標籤>'

```python
xml = '<中文標籤><row><c1>1</c1><c2>2</c2></row></中文標籤>'
```

### Step 3: Assign xsl = '<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">\n <xsl:output omit-xml-declaration="yes" indent="yes"/>\n <xsl:strip-space elements="*"/>\n\n <xsl:template match="node()|@*">\n     <xsl:copy>\n       <xsl:apply-templates select="node()|@*"/>\n     </xsl:copy>\n </xsl:template>\n\n <xsl:template match="中文標籤">\n     <根>\n       <xsl:apply-templates />\n     </根>\n </xsl:template>\n\n</xsl:stylesheet>'

```python
xsl = '<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">\n <xsl:output omit-xml-declaration="yes" indent="yes"/>\n <xsl:strip-space elements="*"/>\n\n <xsl:template match="node()|@*">\n     <xsl:copy>\n       <xsl:apply-templates select="node()|@*"/>\n     </xsl:copy>\n </xsl:template>\n\n <xsl:template match="中文標籤">\n     <根>\n       <xsl:apply-templates />\n     </根>\n </xsl:template>\n\n</xsl:stylesheet>'
```

### Step 4: Assign df_orig = read_xml(...)

```python
df_orig = read_xml(StringIO(xml))
```

### Step 5: Assign df_style = read_xml(...)

```python
df_style = read_xml(StringIO(xml), stylesheet=xsl)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_orig, df_style)
```


## Complete Example

```python
# Workflow
pytest.importorskip('lxml')
xml = '<中文標籤><row><c1>1</c1><c2>2</c2></row></中文標籤>'
xsl = '<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">\n <xsl:output omit-xml-declaration="yes" indent="yes"/>\n <xsl:strip-space elements="*"/>\n\n <xsl:template match="node()|@*">\n     <xsl:copy>\n       <xsl:apply-templates select="node()|@*"/>\n     </xsl:copy>\n </xsl:template>\n\n <xsl:template match="中文標籤">\n     <根>\n       <xsl:apply-templates />\n     </根>\n </xsl:template>\n\n</xsl:stylesheet>'
df_orig = read_xml(StringIO(xml))
df_style = read_xml(StringIO(xml), stylesheet=xsl)
tm.assert_frame_equal(df_orig, df_style)
```

## Next Steps


---

*Source: test_xml.py:1205 | Complexity: Intermediate | Last updated: 2026-06-02*