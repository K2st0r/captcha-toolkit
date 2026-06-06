# Captcha Toolkit 🛠️

> 通用验证码识别工具包 | Universal CAPTCHA Recognition Toolkit

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

## ✨ 功能特性

- ✅ **OCR文字识别** - 数字 + 字母 + 中文验证码
- ✅ **滑块验证码** - 缺口位置检测
- ✅ **批量处理** - 多图片并发识别
- ✅ **多种输入** - 文件 / Base64 / DataURI
- ✅ **API服务** - 开箱即用的REST接口

## 🚀 快速开始

```bash
pip install ddddocr pillow
```

```python
from captcha_toolkit import CaptchaSolver

solver = CaptchaSolver()

# 识别验证码
result = solver.solve('captcha.png')
print(result)  # 输出: "aB3x7"

# 滑块验证码
pos = solver.solve_slide('bg.jpg', 'slice.png')
print(pos)  # 输出: {"target": [x, y, w, h]}

# 批量识别
results = solver.solve_batch(['img1.png', 'img2.png', 'img3.png'])
```

## 📦 项目结构

```
captcha-toolkit/
├── captcha_toolkit.py    # 核心库
├── README.md             # 本文件
└── LICENSE               # MIT License
```

## 🎯 适用场景

- Web自动化 / 爬虫
- 批量注册 / 登录
- RPA流程自动化
- 测试环境验证码处理

## 💎 支持项目

如果这个工具帮到了你，欢迎打赏支持持续开发！

**USDT (ERC20):** `0xAfe9B67B1DF618FAeD32dC71E3458cf549f26697`

---

*Made with ❤️ by [K2st0r](https://github.com/K2st0r)*
