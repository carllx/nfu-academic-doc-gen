# How To: Build Index

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test building index with both checksums.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `shutil`
- `unittest.mock`
- `nltk`
- `nltk.downloader`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: 'Test building index with both checksums.'

```python
'Test building index with both checksums.'
```

**Verification:**
```python
assert package_element.get('id') == 'test_package'
```

### Step 2: Assign test_pkg_dir = str(...)

```python
test_pkg_dir = str(tmp_path.joinpath('packages'))
```

**Verification:**
```python
assert isinstance(md5_checksum, str)
```

### Step 3: Assign test_pkg_name = 'test_package'

```python
test_pkg_name = 'test_package'
```

**Verification:**
```python
assert len(md5_checksum) > 5
```

### Step 4: Assign test_pkg_path = os.path.join(...)

```python
test_pkg_path = os.path.join(test_pkg_dir, f'{test_pkg_name}')
```

**Verification:**
```python
assert isinstance(sha256_checksum, str)
```

### Step 5: Call os.makedirs()

```python
os.makedirs(test_pkg_path, exist_ok=True)
```

**Verification:**
```python
assert len(sha256_checksum) > 5
```

### Step 6: Assign test_xml_path = os.path.join(...)

```python
test_xml_path = os.path.join(test_pkg_path, f'{test_pkg_name}.xml')
```

### Step 7: Assign zip_path = os.path.join(...)

```python
zip_path = os.path.join(test_pkg_path, f'{test_pkg_name}')
```

### Step 8: Call shutil.make_archive()

```python
shutil.make_archive(base_name=zip_path, format='zip', root_dir=test_pkg_dir, base_dir=os.path.basename(test_pkg_path))
```

### Step 9: Assign xml_index = build_index(...)

```python
xml_index = build_index(root=os.path.dirname(test_pkg_dir), base_url='https://someurl')
```

### Step 10: Assign package_element = value

```python
package_element = xml_index[0][0]
```

**Verification:**
```python
assert package_element.get('id') == 'test_package'
```

### Step 11: Assign md5_checksum = package_element.get(...)

```python
md5_checksum = package_element.get('checksum')
```

**Verification:**
```python
assert isinstance(md5_checksum, str)
```

### Step 12: Assign sha256_checksum = package_element.get(...)

```python
sha256_checksum = package_element.get('sha256_checksum')
```

**Verification:**
```python
assert isinstance(sha256_checksum, str)
```

### Step 13: Call fi.write()

```python
fi.write(f'<package id="{test_pkg_name}" name="A Test Package" webpage="http://www.somefake.url/" unzip="1"/>')
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
'Test building index with both checksums.'
test_pkg_dir = str(tmp_path.joinpath('packages'))
test_pkg_name = 'test_package'
test_pkg_path = os.path.join(test_pkg_dir, f'{test_pkg_name}')
os.makedirs(test_pkg_path, exist_ok=True)
test_xml_path = os.path.join(test_pkg_path, f'{test_pkg_name}.xml')
with open(test_xml_path, 'w') as fi:
    fi.write(f'<package id="{test_pkg_name}" name="A Test Package" webpage="http://www.somefake.url/" unzip="1"/>')
zip_path = os.path.join(test_pkg_path, f'{test_pkg_name}')
shutil.make_archive(base_name=zip_path, format='zip', root_dir=test_pkg_dir, base_dir=os.path.basename(test_pkg_path))
xml_index = build_index(root=os.path.dirname(test_pkg_dir), base_url='https://someurl')
package_element = xml_index[0][0]
assert package_element.get('id') == 'test_package'
md5_checksum = package_element.get('checksum')
assert isinstance(md5_checksum, str)
assert len(md5_checksum) > 5
sha256_checksum = package_element.get('sha256_checksum')
assert isinstance(sha256_checksum, str)
assert len(sha256_checksum) > 5
```

## Next Steps


---

*Source: test_downloader.py:52 | Complexity: Advanced | Last updated: 2026-06-02*