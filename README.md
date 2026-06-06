<div align="center">

# Captcha Toolkit

**Universal CAPTCHA Recognition SDK**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-2.1.0-purple.svg)](https://github.com/K2st0r/captcha-toolkit/releases)
[![Donate](https://img.shields.io/badge/Donate-USDT-red.svg)](#donate)

</div>

---

## Table of Contents

- [English](#english)
- [中文](#chinese)
- [Donate / 打赏](#donate--打赏)

---

## English

### What is Captcha Toolkit?

Captcha Toolkit is a **Python SDK** for CAPTCHA recognition, powered by [ddddocr](https://github.com/sml2h3/ddddocr). It provides a clean, requests-style API for OCR (digits, letters, Chinese) and slide-captcha gap detection. One-line setup, multiple input formats, batch processing support.

### Features

| Category | Description |
|----------|-------------|
| **OCR Recognition** | Digits, letters, Chinese characters — beta + standard models |
| **Slide Detection** | Auto-detect slider CAPTCHA gap position (pixel distance) |
| **Batch Processing** | Process multiple images at once |
| **Any Input Format** | File path, base64 string, data URI, or raw bytes |
| **Structured Response** | Each result includes success status and confidence |
| **Clean API** | `solver.solve()` for full result, `solver.solve_ocr()` for text-only |

### Installation

```bash
git clone https://github.com/K2st0r/captcha-toolkit.git
cd captcha-toolkit
pip install ddddocr pillow
```

### Quick Start

```python
from captcha_toolkit import CaptchaSolver

solver = CaptchaSolver()

# File path
result = solver.solve("captcha.png")
print(result)  # {"success": True, "text": "AB3D", "confidence": 0.95}

# Quick text-only
text = solver.solve_ocr("captcha.png")  # "AB3D"

# Base64
result = solver.solve("iVBORw0KGgoAAAA...")

# Data URI
result = solver.solve("data:image/png;base64,iVBOR...")

# Raw bytes
with open("captcha.png", "rb") as f:
    result = solver.solve(f.read())
```

### Batch Processing

```python
images = ["c1.png", "c2.png", "c3.png", "c4.png", "c5.png"]
results = solver.solve_batch(images)
for r in results:
    if r["success"]:
        print(f"→ {r['text']}")
```

### Slide CAPTCHA Detection

```python
position = solver.solve_slide("background_with_notch.png", "slider_piece.png")
print(position)
# {"success": True, "target": {"x": 120, "y": 0}}
# Move the slider 120 pixels to the right to solve
```

### Error Handling

```python
from captcha_toolkit import CaptchaSolver, CaptchaError

try:
    solver = CaptchaSolver()
    result = solver.solve("captcha.png")
    if result["success"]:
        print(f"Result: {result['text']}")
    else:
        print(f"Failed: {result.get('error')}")
except CaptchaError as e:
    print(f"Init error: {e}")
```

---

## 中文

### 概述

Captcha Toolkit 是一个基于 [ddddocr](https://github.com/sml2h3/ddddocr) 的 **Python 验证码识别 SDK**。提供简洁的 requests 风格 API，支持数字/字母/中文 OCR 和滑块验证码缺口检测。

### 安装

```bash
git clone https://github.com/K2st0r/captcha-toolkit.git
cd captcha-toolkit
pip install ddddocr pillow
```

### 快速上手

```python
from captcha_toolkit import CaptchaSolver

solver = CaptchaSolver()                      # 默认 Beta 模型
result = solver.solve("captcha.png")           # 文件路径
result = solver.solve("base64编码的图片")       # base64
result = solver.solve(b"raw_image_bytes")      # 原始字节
text = solver.solve_ocr("captcha.png")         # 直接返回文本 "AB3D"

# 批量识别
results = solver.solve_batch(["c1.png", "c2.png", "c3.png"])

# 滑块检测
pos = solver.solve_slide("背景图.png", "滑块图.png")
# -> {"success": True, "target": {"x": 120, "y": 0}}
```

### 返回格式

```python
# 成功 → {"success": True, "text": "AB3D", "confidence": 0.95}
# 失败 → {"success": False, "text": "", "error": "..."}
# 滑块 → {"success": True, "target": {"x": 120, "y": 0}}
```

### 模型选择

```python
solver = CaptchaSolver(beta=True)   # Beta模型：复杂验证码更好（默认）
solver = CaptchaSolver(beta=False)  # 标准模型：稍快一些
```

---

## Donate / 打赏

<div align="center">
<img src="https://raw.githubusercontent.com/K2st0r/captcha-toolkit/main/static/zan.png" width="200" alt="WeChat Pay">

📱 微信扫码赞赏

**USDT (ERC20):** `0xAfe9B67B1DF618FAeD32dC71E3458cf549f26697`

</div>

---

MIT License · Made with ❤️ by [K2st0r](https://github.com/K2st0r)
