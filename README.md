# Captcha Toolkit 🛠️

> 通用验证码识别工具包 | Universal CAPTCHA Recognition Toolkit

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

## ✨ Features

- ✅ **OCR识别** - 数字 + 字母 + 中文验证码
- ✅ **滑块验证码** - 缺口位置检测
- ✅ **批量处理** - 支持多线程并发
- ✅ **API服务** - 开箱即用的REST API
- ✅ **多种输入** - 文件 / Base64 / DataURI

## 🚀 Quick Start

```python
from captcha_toolkit import CaptchaSolver

solver = CaptchaSolver()

# OCR识别
result = solver.solve('captcha.png')
print(result)  # "aB3x7"

# 滑块识别
result = solver.solve_slide('bg.jpg', 'slice.png')
print(result)  # {"target": [120, 45, 50, 50]}
```

## 📦 Install

```bash
pip install ddddocr pillow
```

## 🎯 Use Cases

- 自动化注册/登录
- 爬虫验证码绕过
- 批量数据处理
- RPA自动化流程

## 💎 Support

If this toolkit helps you, consider supporting:

**USDT (ETH):** `0xAfe9B67B1DF618FAeD32dC71E3458cf549f26697`

---

*Made with ❤️ by K2st0r*
