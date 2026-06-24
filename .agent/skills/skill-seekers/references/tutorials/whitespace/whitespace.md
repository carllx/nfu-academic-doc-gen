# How To: Whitespace

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test whitespace

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

### Step 1: Assign xml = '\n      <data>\n        <row sides=" 4 ">\n          <shape>\n              square\n          </shape>\n          <degrees>&#009;360&#009;</degrees>\n        </row>\n        <row sides=" 0 ">\n          <shape>\n              circle\n          </shape>\n          <degrees>&#009;360&#009;</degrees>\n        </row>\n        <row sides=" 3 ">\n          <shape>\n              triangle\n          </shape>\n          <degrees>&#009;180&#009;</degrees>\n        </row>\n      </data>'

```python
xml = '\n      <data>\n        <row sides=" 4 ">\n          <shape>\n              square\n          </shape>\n          <degrees>&#009;360&#009;</degrees>\n        </row>\n        <row sides=" 0 ">\n          <shape>\n              circle\n          </shape>\n          <degrees>&#009;360&#009;</degrees>\n        </row>\n        <row sides=" 3 ">\n          <shape>\n              triangle\n          </shape>\n          <degrees>&#009;180&#009;</degrees>\n        </row>\n      </data>'
```

### Step 2: Assign df_xpath = read_xml(...)

```python
df_xpath = read_xml(StringIO(xml), parser=parser, dtype='string')
```

### Step 3: Assign df_iter = read_xml_iterparse(...)

```python
df_iter = read_xml_iterparse(xml, parser=parser, iterparse={'row': ['sides', 'shape', 'degrees']}, dtype='string')
```

### Step 4: Assign df_expected = DataFrame(...)

```python
df_expected = DataFrame({'sides': [' 4 ', ' 0 ', ' 3 '], 'shape': ['\n              square\n          ', '\n              circle\n          ', '\n              triangle\n          '], 'degrees': ['\t360\t', '\t360\t', '\t180\t']}, dtype='string')
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
xml = '\n      <data>\n        <row sides=" 4 ">\n          <shape>\n              square\n          </shape>\n          <degrees>&#009;360&#009;</degrees>\n        </row>\n        <row sides=" 0 ">\n          <shape>\n              circle\n          </shape>\n          <degrees>&#009;360&#009;</degrees>\n        </row>\n        <row sides=" 3 ">\n          <shape>\n              triangle\n          </shape>\n          <degrees>&#009;180&#009;</degrees>\n        </row>\n      </data>'
df_xpath = read_xml(StringIO(xml), parser=parser, dtype='string')
df_iter = read_xml_iterparse(xml, parser=parser, iterparse={'row': ['sides', 'shape', 'degrees']}, dtype='string')
df_expected = DataFrame({'sides': [' 4 ', ' 0 ', ' 3 '], 'shape': ['\n              square\n          ', '\n              circle\n          ', '\n              triangle\n          '], 'degrees': ['\t360\t', '\t360\t', '\t180\t']}, dtype='string')
tm.assert_frame_equal(df_xpath, df_expected)
tm.assert_frame_equal(df_iter, df_expected)
```

## Next Steps


---

*Source: test_xml.py:532 | Complexity: Intermediate | Last updated: 2026-06-02*