---
name: antivirus
description: >-
  Antivirus/EDR/XDR engineering and signature development skill. Use when user needs to build, configure, or optimize antivirus/endpoint protection solutions - including signature creation (YARA, ClamAV, OpenIOC), heuristic/behavioral engine tuning, scanning engine architecture, real-time protection, quarantine/remediation, performance optimization, and false positive reduction. Trigger on: "antivirus development", "AV signatures", "YARA rules", "ClamAV signatures", "heuristic engine", "behavioral detection", "real-time protection", "EDR development", "XDR rules", "file scanning", "quarantine", "false positive reduction", "AV performance".
---

# Antivirus/EDR Engineering Skill

Engineering skill for building, configuring, and optimizing antivirus, EDR (Endpoint Detection & Response), and XDR (Extended Detection & Response) solutions. Covers signature-based detection, heuristic/behavioral engines, scanning architectures, and response automation.

## Core Components

### 1. Signature-Based Detection
- **Hash Signatures**: MD5, SHA1, SHA256, SSDEEP (fuzzy), TLSH (locality-sensitive)
- **Pattern Signatures**: Byte sequences, regex, wildcard patterns
- **Structural Signatures**: PE/ELF section anomalies, import table hashes (impfuzzy), rich header
- **Format-Specific**: ClamAV (.hdb/.ndb/.ldb), YARA, OpenIOC, STIX patterns

### 2. Heuristic/Behavioral Engines
- **Static Heuristics**: Entropy analysis, packer detection, suspicious API combinations, string anomalies
- **Dynamic Heuristics**: API call sequences, syscall patterns, process tree anomalies, MITRE ATT&CK mapping
- **ML/AI Models**: Feature extraction (PE headers, imports, strings, entropy), classification (malware/benign/family)

### 3. Scanning Architecture
- **On-Demand**: Full, quick, custom, context-menu scanning
- **Real-Time/On-Access**: File system filter drivers (minifilter), kernel callbacks, ETW providers
- **Scheduled**: Idle-time, maintenance windows, cloud-assisted
- **Cloud-Assisted**: Hash lookup, reputation, ML inference offload

### 4. Remediation & Response
- **Actions**: Clean, quarantine, delete, block, allow, rollback
- **Quarantine**: Secure storage, metadata preservation, restore capability
- **Rollback**: Ransomware file recovery (VSS, journal), registry restoration
- **Network Isolation**: Host firewall, NAC integration

## Signature Development

### YARA Rules (Primary Format)
```yara
rule MALWARE_Family_Variant {
    meta:
        description = "Detects Family variant Variant"
        author = "analyst"
        date = "YYYY-MM-DD"
        version = "1.0"
        hash = "sha256:..."
        severity = "high"
        category = "trojan|ransomware|backdoor|etc"
        platform = "windows|linux|macos|multi"
        mitre = "T1055, T1547.001"
        
    strings:
        // Static strings
        $s1 = "unique_string" ascii wide nocase
        $s2 = { 4D 5A ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? }
        
        // Hex patterns with jumps
        $h1 = { 48 89 5C 24 ?? 48 89 74 24 ?? 57 48 83 EC 20 }
        
        // Regex for obfuscated patterns
        $r1 = /[A-Za-z0-9+\/]{20,}={0,2}/  // Base64
        
        // Entropy-based (high entropy sections)
        $entropy = { ?? ?? ?? ?? }  // placeholder for entropy condition
        
    condition:
        // File size constraints
        filesize < 50MB and
        
        // Primary detection logic
        (any of ($s*) and any of ($h*)) or
        (uint16(0) == 0x5A4D and any of ($s*)) or  // PE header + strings
        
        // High entropy + suspicious imports
        (math.entropy(0, filesize) > 7.5 and pe.imports("kernel32.dll", "VirtualAllocEx"))
}
```

### ClamAV Signatures
```bash
# Hash-based (.hdb)
<md5>:<size>:<malware_name>
d41d8cd98f00b204e9800998ecf8427e:0:Test.Empty.File

# Extended signatures (.ndb)
<name>:<target>:<offset>:<pattern>
Trojan.Test:*:0:{4d 5a ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ??}

# Logical signatures (.ldb) - complex logic
Trojan.Test {0} (0,0) 0:
    0:& (pe.entry_point > 0x1000)
    1:& (pe.sections[0].entropy > 7.0)
```

### OpenIOC / STIX Patterns
```xml
<!-- OpenIOC 1.1 -->
<Indicator>
  <IndicatorItem id="file_hash_sha256" condition="is">
    <Context>FileItem/SHA256</Context>
    <Content>a1b2c3...</Content>
  </IndicatorItem>
  <IndicatorItem id="file_path" condition="contains">
    <Context>FileItem/FullPath</Context>
    <Content>AppData\Roaming\</Content>
  </IndicatorItem>
</Indicator>
```

```json
// STIX 2.1 Pattern
"pattern": "[file:hashes.'SHA-256' = 'a1b2c3...' AND file:parent_directory_ref.name = 'AppData']"
```

## Heuristic Engine Design

### Static Features (PE/ELF)
```python
# Feature vector for ML classifier
features = {
    # Header features
    "machine_type": pe.FILE_HEADER.Machine,
    "num_sections": pe.FILE_HEADER.NumberOfSections,
    "timestamp": pe.FILE_HEADER.TimeDateStamp,
    "characteristics": pe.FILE_HEADER.Characteristics,
    
    # Optional header
    "subsystem": pe.OPTIONAL_HEADER.Subsystem,
    "dll_characteristics": pe.OPTIONAL_HEADER.DllCharacteristics,
    "size_of_image": pe.OPTIONAL_HEADER.SizeOfImage,
    "entry_point": pe.OPTIONAL_HEADER.AddressOfEntryPoint,
    
    # Section features
    "section_entropies": [s.entropy for s in pe.sections],
    "section_names": [s.Name.decode().rstrip('\x00') for s in pe.sections],
    "section_characteristics": [s.Characteristics for s in pe.sections],
    
    # Import features
    "imports_count": len(pe.DIRECTORY_ENTRY_IMPORT),
    "suspicious_imports": count_suspicious(pe.imports),
    "import_hash": pe.get_imphash(),
    
    # Export features
    "exports_count": len(pe.DIRECTORY_ENTRY_EXPORT) if hasattr(pe, 'DIRECTORY_ENTRY_EXPORT') else 0,
    
    # Resource features
    "resources_count": count_resources(pe),
    "resource_entropies": [r.entropy for r in pe.resources],
    
    # String features
    "string_count": len(strings),
    "suspicious_strings": count_suspicious_strings(strings),
    "base64_strings": count_base64(strings),
    
    # Crypto features
    "crypto_constants": detect_crypto_constants(bytes),
}
```

### Behavioral Rules (Sigma/EDR)
```yaml
# Sigma rule for behavioral detection
title: Suspicious Process Execution Chain
id: <uuid>
status: stable
description: Detects trojan download/execute chain
logsource:
  product: windows
  service: sysmon
detection:
  selection_download:
    EventID: 1  # Process Creation
    Image|endswith: 
      - '\powershell.exe'
      - '\cmd.exe'
      - '\wscript.exe'
      - '\cscript.exe'
      - '\mshta.exe'
      - '\rundll32.exe'
      - '\regsvr32.exe'
    CommandLine|contains:
      - 'DownloadFile'
      - 'DownloadString'
      - 'Invoke-WebRequest'
      - 'Invoke-Expression'
      - 'IEX'
      - 'curl'
      - 'wget'
      - 'bitsadmin'
      - 'certutil'
  selection_execute:
    EventID: 1
    ParentImage|endswith:
      - '\powershell.exe'
      - '\cmd.exe'
      - '\wscript.exe'
      - '\mshta.exe'
    Image|endswith:
      - '\powershell.exe'
      - '\cmd.exe'
      - '\rundll32.exe'
      - '\regsvr32.exe'
      - '\wscript.exe'
  timeframe: 60s
condition: selection_download and selection_execute
level: high
tags:
  - attack.t1059
  - attack.t1105
  - attack.t1204
```

## Scanning Engine Architecture

### File System Minifilter (Windows)
```c
// Key callbacks for real-time scanning
FLT_PREOP_CALLBACK_STATUS PreCreate(
    PFLT_CALLBACK_DATA Data,
    PCFLT_RELATED_OBJECTS FltObjects,
    PVOID* CompletionContext
) {
    // Check file extension, path, process context
    // Issue scan request to user-mode engine
    // Return FLT_PREOP_COMPLETE with block/allow
}

FLT_POSTOP_CALLBACK_STATUS PostCreate(
    PFLT_CALLBACK_DATA Data,
    PCFLT_RELATED_OBJECTS FltObjects,
    PVOID CompletionContext,
    FLT_POST_OPERATION_FLAGS Flags
) {
    // Handle scan results, quarantine if needed
}
```

### Linux Fanotify / eBPF
```c
// Fanotify for file access monitoring
int fanotify_fd = fanotify_init(FAN_CLASS_CONTENT | FAN_REPORT_FID, O_RDONLY);
fanotify_mark(fanotify_fd, FAN_MARK_ADD | FAN_MARK_MOUNT, 
              FAN_OPEN | FAN_CLOSE_WRITE | FAN_ACCESS, 
              AT_FDCWD, "/");

// eBPF LSM for finer-grained control
SEC("lsm/file_open")
int BPF_PROG(file_open_hook, struct file *file, int flags) {
    // Check path, process, credentials
    // Return 0 (allow) or -EPERM (deny)
}
```

## Performance Optimization

### Multi-Layer Scanning
```
Layer 1: Fast Pre-filter (10-50ms)
  - Hash lookup (local + cloud)
  - Extension/allowlist check
  - Quick entropy/size heuristics

Layer 2: Signature Scan (50-200ms)
  - YARA/ClamAV pattern matching
  - Multi-threaded, SIMD-optimized

Layer 3: Heuristic/ML (200-500ms)
  - Feature extraction
  - Model inference (ONNX/TensorRT)
  - Behavioral emulation (lightweight)

Layer 4: Deep Analysis (async, seconds)
  - Sandbox detonation
  - Full static analysis
  - Cloud ML ensemble
```

### Optimization Techniques
- **Aho-Corasick** for multi-pattern string matching
- **SIMD** (AVX2/AVX-512) for entropy, hash computation
- **Memory-mapped I/O** for large files
- **Thread pool** with work-stealing for concurrent scans
- **Cache-friendly** data structures (robin-hood hashing for hash sets)
- **Async I/O** (IOCP on Windows, io_uring on Linux)

## False Positive Reduction

### Allowlist Management
- **Microsoft/OS binaries**: Signed, known paths, catalog-signed
- **Enterprise apps**: Custom allowlist with hash + path + publisher
- **Developer tools**: Compiler outputs, build artifacts (configurable)

### Context-Aware Decisions
- **Process reputation**: Signed vs unsigned, prevalence, age
- **File provenance**: Download zone identifier, email attachment, USB
- **User behavior**: Admin vs standard, interactive vs service

### Feedback Loop
```python
# Telemetry collection for FP reduction
telemetry = {
    "file_hash": sha256,
    "detection_name": "Heuristic.Suspicious",
    "action_taken": "quarantined",
    "user_action": "restored",  # FP indicator
    "file_path": path,
    "process_path": proc_path,
    "signer": cert_info,
    "prevalence": cloud_reputation,
    "timestamp": now
}
```

## Tooling & Frameworks

### Open Source Engines
- **ClamAV**: Mature signature engine, daemon + library
- **YARA**: Pattern matching, embeddable library
- **OpenEDR**: Open-source EDR framework (Wazuh, LimaCharlie)
- **Velociraptor**: Endpoint visibility, artifact collection
- **GRR**: Remote live forensics

### Commercial SDKs
- **Bitdefender SDK**: Scanning engine + signatures
- **Kaspersky SDK**: Multi-layer scanning
- **Sophos Intercept X API**: Behavioral + ML
- **CrowdStrike Falcon API**: Cloud-native EDR

### Development Tools
- **YARA-Rules**: Community rule repository
- **MalwareBazaar / VirusShare**: Sample feeds
- **VT / Hybrid Analysis / Joe Sandbox**: Dynamic analysis APIs
- **MISP / OpenCTI**: Threat intel platforms

## Output Formats

### Scan Result
```json
{
  "scan_id": "uuid",
  "timestamp": "ISO8601",
  "file": {
    "path": "/path/to/file.exe",
    "size": 123456,
    "sha256": "a1b2c3...",
    "mime": "application/x-dosexec"
  },
  "engine_version": "1.2.3",
  "signatures_version": "2024.01.15",
  "results": [
    {
      "layer": "signature",
      "engine": "yara",
      "rule": "Trojan_Emotet_Loader",
      "severity": "high",
      "matches": ["$s1", "$h2"]
    },
    {
      "layer": "heuristic",
      "engine": "ml_classifier",
      "score": 0.94,
      "verdict": "malicious",
      "family": "Emotet"
    }
  ],
  "final_verdict": "malicious",
  "action": "quarantined",
  "quarantine_path": "/quarantine/a1b2c3..."
}
```

### Performance Metrics
```json
{
  "scan_time_ms": 142,
  "layers": {
    "prefilter": 3,
    "signature": 45,
    "heuristic": 89,
    "deep": 0
  },
  "files_scanned": 15000,
  "detections": 3,
  "false_positives": 0,
  "throughput_mb_s": 850
}
```

## Trigger Phrases
Use this skill when user mentions:
- "antivirus development" / "AV engine"
- "EDR development" / "XDR rules"
- "YARA rules" / "ClamAV signatures"
- "heuristic engine" / "behavioral detection"
- "real-time protection" / "on-access scanning"
- "file system filter driver" / "minifilter"
- "quarantine" / "remediation" / "rollback"
- "false positive reduction"
- "AV performance optimization"
- "signature development"
- "malware classification"
- "ML malware detection"
