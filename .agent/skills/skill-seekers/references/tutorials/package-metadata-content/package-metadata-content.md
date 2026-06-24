# How To: Package Metadata Content

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test package metadata content

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `json`
- `tempfile`
- `zipfile`
- `pathlib`
- `unittest.mock`
- `pytest`
- `skill_seekers.cli.adaptors`
- `skill_seekers.cli.adaptors.base`

**Setup Required:**
```python
# Fixtures: platform
```

## Step-by-Step Guide

### Step 1: Assign adaptor = get_adaptor(...)

```python
adaptor = get_adaptor(platform)
```

**Verification:**
```python
assert metadata['platform'] == platform
```

### Step 2: Assign expected = value

```python
expected = PLATFORM_EXPECTED[platform]
```

**Verification:**
```python
assert metadata['name'] == 'test-skill'
```

### Step 3: Assign skill_dir = value

```python
skill_dir = Path(temp_dir) / 'test-skill'
```

**Verification:**
```python
assert expected['api_base_contains'] in metadata['api_base'].lower()
```

### Step 4: Call skill_dir.mkdir()

```python
skill_dir.mkdir()
```

### Step 5: Call unknown.write_text()

```python
(skill_dir / 'SKILL.md').write_text('Test instructions')
```

### Step 6: Call unknown.mkdir()

```python
(skill_dir / 'references').mkdir()
```

### Step 7: Call unknown.write_text()

```python
(skill_dir / 'references' / 'guide.md').write_text('# User Guide')
```

### Step 8: Assign output_dir = value

```python
output_dir = Path(temp_dir) / 'output'
```

### Step 9: Call output_dir.mkdir()

```python
output_dir.mkdir()
```

### Step 10: Assign package_path = adaptor.package(...)

```python
package_path = adaptor.package(skill_dir, output_dir)
```

### Step 11: Assign metadata_name = value

```python
metadata_name = f'{platform}_metadata.json'
```

### Step 12: Assign metadata_content = zf.read.decode(...)

```python
metadata_content = zf.read(metadata_name).decode('utf-8')
```

### Step 13: Assign metadata = json.loads(...)

```python
metadata = json.loads(metadata_content)
```

**Verification:**
```python
assert metadata['platform'] == platform
```


## Complete Example

```python
# Setup
# Fixtures: platform

# Workflow
adaptor = get_adaptor(platform)
expected = PLATFORM_EXPECTED[platform]
with tempfile.TemporaryDirectory() as temp_dir:
    skill_dir = Path(temp_dir) / 'test-skill'
    skill_dir.mkdir()
    (skill_dir / 'SKILL.md').write_text('Test instructions')
    (skill_dir / 'references').mkdir()
    (skill_dir / 'references' / 'guide.md').write_text('# User Guide')
    output_dir = Path(temp_dir) / 'output'
    output_dir.mkdir()
    package_path = adaptor.package(skill_dir, output_dir)
    with zipfile.ZipFile(package_path, 'r') as zf:
        metadata_name = f'{platform}_metadata.json'
        metadata_content = zf.read(metadata_name).decode('utf-8')
        metadata = json.loads(metadata_content)
        assert metadata['platform'] == platform
        assert metadata['name'] == 'test-skill'
        assert expected['api_base_contains'] in metadata['api_base'].lower()
```

## Next Steps


---

*Source: test_openai_compatible_shared.py:179 | Complexity: Advanced | Last updated: 2026-06-02*