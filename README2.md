# Data Collector Pro 🕷️

> 网页数据采集器 | Smart Web Scraper

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

## ✨ Features

- ✅ **CSS选择器** - 精准提取页面元素
- ✅ **正则匹配** - 灵活的数据抽取
- ✅ **自动翻页** - 批量采集多页数据
- ✅ **结构化输出** - 直接导出JSON
- ✅ **请求控制** - 限速/重试/Headers

## 🚀 Quick Start

```python
from data_collector import DataCollector

dc = DataCollector()

# 简单采集
data = dc.scrape(
    'https://example.com', 
    selector='h1.title, .price'
)

# 结构化采集
data = dc.scrape_to_json(
    'https://example.com/list?page={page}',
    fields={
        '_row': '.product-item',
        'title': '.product-name',
        'price': '.product-price',
    },
    pages=5
)

print(json.dumps(data, indent=2))
```

## 📦 Install

```bash
pip install requests beautifulsoup4 lxml
```

## 💎 Support

If this tool helps you, consider supporting:

**USDT (ETH):** `0xAfe9B67B1DF618FAeD32dC71E3458cf549f26697`

---

*Made with ❤️ by K2st0r*
