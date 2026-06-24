# How To: Style To Csv

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test style to csv

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `io`
- `os`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.io.common`
- `pandas.io.xml`

**Setup Required:**
```python
# Fixtures: geom_df
```

## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('lxml')
```

**Verification:**
```python
assert out_csv == out_xml
```

### Step 2: Assign xsl = '<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">\n    <xsl:output method="text" indent="yes" />\n    <xsl:strip-space elements="*"/>\n\n    <xsl:param name="delim">,</xsl:param>\n    <xsl:template match="/data">\n        <xsl:text>,shape,degrees,sides&#xa;</xsl:text>\n        <xsl:apply-templates select="row"/>\n    </xsl:template>\n\n    <xsl:template match="row">\n        <xsl:value-of select="concat(index, $delim, shape, $delim,\n                                     degrees, $delim, sides)"/>\n         <xsl:text>&#xa;</xsl:text>\n    </xsl:template>\n</xsl:stylesheet>'

```python
xsl = '<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">\n    <xsl:output method="text" indent="yes" />\n    <xsl:strip-space elements="*"/>\n\n    <xsl:param name="delim">,</xsl:param>\n    <xsl:template match="/data">\n        <xsl:text>,shape,degrees,sides&#xa;</xsl:text>\n        <xsl:apply-templates select="row"/>\n    </xsl:template>\n\n    <xsl:template match="row">\n        <xsl:value-of select="concat(index, $delim, shape, $delim,\n                                     degrees, $delim, sides)"/>\n         <xsl:text>&#xa;</xsl:text>\n    </xsl:template>\n</xsl:stylesheet>'
```

### Step 3: Assign out_csv = geom_df.to_csv(...)

```python
out_csv = geom_df.to_csv(lineterminator='\n')
```

### Step 4: Assign out_xml = geom_df.to_xml(...)

```python
out_xml = geom_df.to_xml(stylesheet=xsl)
```

**Verification:**
```python
assert out_csv == out_xml
```

### Step 5: Assign out_csv = out_csv.strip(...)

```python
out_csv = out_csv.strip()
```


## Complete Example

```python
# Setup
# Fixtures: geom_df

# Workflow
pytest.importorskip('lxml')
xsl = '<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">\n    <xsl:output method="text" indent="yes" />\n    <xsl:strip-space elements="*"/>\n\n    <xsl:param name="delim">,</xsl:param>\n    <xsl:template match="/data">\n        <xsl:text>,shape,degrees,sides&#xa;</xsl:text>\n        <xsl:apply-templates select="row"/>\n    </xsl:template>\n\n    <xsl:template match="row">\n        <xsl:value-of select="concat(index, $delim, shape, $delim,\n                                     degrees, $delim, sides)"/>\n         <xsl:text>&#xa;</xsl:text>\n    </xsl:template>\n</xsl:stylesheet>'
out_csv = geom_df.to_csv(lineterminator='\n')
if out_csv is not None:
    out_csv = out_csv.strip()
out_xml = geom_df.to_xml(stylesheet=xsl)
assert out_csv == out_xml
```

## Next Steps


---

*Source: test_to_xml.py:1171 | Complexity: Intermediate | Last updated: 2026-06-02*