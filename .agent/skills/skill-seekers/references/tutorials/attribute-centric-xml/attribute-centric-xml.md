# How To: Attribute Centric Xml

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test attribute centric xml

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

### Step 2: Assign xml = '<?xml version="1.0" encoding="UTF-8"?>\n<TrainSchedule>\n      <Stations>\n         <station Name="Manhattan" coords="31,460,195,498"/>\n         <station Name="Laraway Road" coords="63,409,194,455"/>\n         <station Name="179th St (Orland Park)" coords="0,364,110,395"/>\n         <station Name="153rd St (Orland Park)" coords="7,333,113,362"/>\n         <station Name="143rd St (Orland Park)" coords="17,297,115,330"/>\n         <station Name="Palos Park" coords="128,281,239,303"/>\n         <station Name="Palos Heights" coords="148,257,283,279"/>\n         <station Name="Worth" coords="170,230,248,255"/>\n         <station Name="Chicago Ridge" coords="70,187,208,214"/>\n         <station Name="Oak Lawn" coords="166,159,266,185"/>\n         <station Name="Ashburn" coords="197,133,336,157"/>\n         <station Name="Wrightwood" coords="219,106,340,133"/>\n         <station Name="Chicago Union Sta" coords="220,0,360,43"/>\n      </Stations>\n</TrainSchedule>'

```python
xml = '<?xml version="1.0" encoding="UTF-8"?>\n<TrainSchedule>\n      <Stations>\n         <station Name="Manhattan" coords="31,460,195,498"/>\n         <station Name="Laraway Road" coords="63,409,194,455"/>\n         <station Name="179th St (Orland Park)" coords="0,364,110,395"/>\n         <station Name="153rd St (Orland Park)" coords="7,333,113,362"/>\n         <station Name="143rd St (Orland Park)" coords="17,297,115,330"/>\n         <station Name="Palos Park" coords="128,281,239,303"/>\n         <station Name="Palos Heights" coords="148,257,283,279"/>\n         <station Name="Worth" coords="170,230,248,255"/>\n         <station Name="Chicago Ridge" coords="70,187,208,214"/>\n         <station Name="Oak Lawn" coords="166,159,266,185"/>\n         <station Name="Ashburn" coords="197,133,336,157"/>\n         <station Name="Wrightwood" coords="219,106,340,133"/>\n         <station Name="Chicago Union Sta" coords="220,0,360,43"/>\n      </Stations>\n</TrainSchedule>'
```

### Step 3: Assign df_lxml = read_xml(...)

```python
df_lxml = read_xml(StringIO(xml), xpath='.//station')
```

### Step 4: Assign df_etree = read_xml(...)

```python
df_etree = read_xml(StringIO(xml), xpath='.//station', parser='etree')
```

### Step 5: Assign df_iter_lx = read_xml_iterparse(...)

```python
df_iter_lx = read_xml_iterparse(xml, iterparse={'station': ['Name', 'coords']})
```

### Step 6: Assign df_iter_et = read_xml_iterparse(...)

```python
df_iter_et = read_xml_iterparse(xml, parser='etree', iterparse={'station': ['Name', 'coords']})
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_lxml, df_etree)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_iter_lx, df_iter_et)
```


## Complete Example

```python
# Workflow
pytest.importorskip('lxml')
xml = '<?xml version="1.0" encoding="UTF-8"?>\n<TrainSchedule>\n      <Stations>\n         <station Name="Manhattan" coords="31,460,195,498"/>\n         <station Name="Laraway Road" coords="63,409,194,455"/>\n         <station Name="179th St (Orland Park)" coords="0,364,110,395"/>\n         <station Name="153rd St (Orland Park)" coords="7,333,113,362"/>\n         <station Name="143rd St (Orland Park)" coords="17,297,115,330"/>\n         <station Name="Palos Park" coords="128,281,239,303"/>\n         <station Name="Palos Heights" coords="148,257,283,279"/>\n         <station Name="Worth" coords="170,230,248,255"/>\n         <station Name="Chicago Ridge" coords="70,187,208,214"/>\n         <station Name="Oak Lawn" coords="166,159,266,185"/>\n         <station Name="Ashburn" coords="197,133,336,157"/>\n         <station Name="Wrightwood" coords="219,106,340,133"/>\n         <station Name="Chicago Union Sta" coords="220,0,360,43"/>\n      </Stations>\n</TrainSchedule>'
df_lxml = read_xml(StringIO(xml), xpath='.//station')
df_etree = read_xml(StringIO(xml), xpath='.//station', parser='etree')
df_iter_lx = read_xml_iterparse(xml, iterparse={'station': ['Name', 'coords']})
df_iter_et = read_xml_iterparse(xml, parser='etree', iterparse={'station': ['Name', 'coords']})
tm.assert_frame_equal(df_lxml, df_etree)
tm.assert_frame_equal(df_iter_lx, df_iter_et)
```

## Next Steps


---

*Source: test_xml.py:828 | Complexity: Advanced | Last updated: 2026-06-02*