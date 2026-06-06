#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Captcha Toolkit Pro v1.0 - 通用验证码识别工具包
==============================================
功能: OCR识别、滑块识别、批量处理、API服务、中文支持
价格: 20 USDT
购买: 0xAfe9B67B1DF618FAeD32dC71E3458cf549f26697 (ETH/USDT - ERC20)
==============================================
"""

import base64
import io
import os
import time
import json
from typing import Union, List, Optional

__version__ = "1.0.0"
__price__ = "20 USDT"
__wallet__ = "0xAfe9B67B1DF618FAeD32dC71E3458cf549f26697"

class CaptchaError(Exception):
    """验证码识别错误"""
    pass

class CaptchaSolver:
    """
    通用验证码识别器
    
    支持:
    - 数字+字母验证码
    - 中文验证码  
    - 滑块验证码缺口检测
    - 批量识别
    - 文件/base64/dataURI多种输入
    """
    
    def __init__(self, beta: bool = True, gpu: bool = False):
        """
        初始化验证码识别器
        
        Args:
            beta: 使用Beta模型(对复杂验证码效果更好)
            gpu: 启用GPU加速(需要CUDA)
        """
        try:
            import ddddocr
        except ImportError:
            raise CaptchaError("请先安装ddddocr: pip install ddddocr pillow")
        
        self.ocr = ddddocr.DdddOcr(show_ad=False, beta=beta)
        self.det = ddddocr.DdddOcr(det=True, ocr=False, show_ad=False)
    
    def _load_image(self, image_data: Union[str, bytes]) -> bytes:
        """统一图片加载: 支持文件路径/base64/dataURI/bytes"""
        if isinstance(image_data, bytes):
            return image_data
        
        if os.path.isfile(image_data):
            with open(image_data, 'rb') as f:
                return f.read()
        
        if image_data.startswith('data:'):
            image_data = image_data.split('base64,')[-1]
        
        try:
            return base64.b64decode(image_data)
        except:
            try:
                with open(image_data, 'rb') as f:
                    return f.read()
            except:
                raise CaptchaError(f"无法加载图片: {image_data[:50]}...")
    
    def solve(self, image_data: Union[str, bytes]) -> str:
        """
        识别验证码
        
        Args:
            image_data: 图片数据(文件路径/base64/dataURI/bytes)
            
        Returns:
            识别结果字符串
        
        Examples:
            >>> solver = CaptchaSolver()
            >>> solver.solve('captcha.png')      # 文件路径
            >>> solver.solve('iVBORw0KGgo...')   # base64
            >>> solver.solve(b'...')              # bytes
        """
        img_bytes = self._load_image(image_data)
        result = self.ocr.classification(img_bytes)
        return result.strip() if result else ""
    
    def solve_batch(self, images: List[Union[str, bytes]], workers: int = 1) -> List[str]:
        """
        批量识别验证码
        
        Args:
            images: 图片列表
            workers: 并发数(目前为顺序执行)
            
        Returns:
            识别结果列表
        """
        results = []
        total = len(images)
        for i, img in enumerate(images):
            result = self.solve(img)
            results.append(result)
            if (i + 1) % 10 == 0:
                print(f"  [进度] {i+1}/{total}")
        return results
    
    def solve_slide(self, bg_image: Union[str, bytes], slice_image: Union[str, bytes]) -> dict:
        """
        滑块验证码缺口检测
        
        Args:
            bg_image: 背景图(带缺口的完整图片)
            slice_image: 滑块图(可移动的小块)
            
        Returns:
            {"target": [x, y, w, h]} 缺口位置
        """
        bg = self._load_image(bg_image)
        sl = self._load_image(slice_image)
        result = self.det.slide_match(sl, bg, simple_target=True)
        return result


def quick_start():
    """快速上手示例"""
    print("""
╔══════════════════════════════════════════╗
║     Captcha Toolkit Pro v1.0            ║
║     通用验证码识别工具包                  ║
╠══════════════════════════════════════════╣
║ 使用方法:                                ║
║                                          ║
║  from captcha_toolkit import CaptchaSolver ║
║  solver = CaptchaSolver()                ║
║  result = solver.solve('captcha.png')    ║
║  print(result)  # 输出识别结果            ║
║                                          ║
║  # 滑块验证码                             ║
║  pos = solver.solve_slide('bg.jpg','slice.png') ║
║                                          ║
║ 价格: 20 USDT                            ║
║ 钱包: 0xAfe9B67B...f26697 (ETH/USDT)     ║
╚══════════════════════════════════════════╝
    """)


if __name__ == "__main__":
    quick_start()
    try:
        solver = CaptchaSolver()
        print("[OK] CaptchaSolver 初始化成功")
        print(f"[OK] 版本: v{__version__}")
        print(f"[OK] 价格: {__price__}")
        print(f"[OK] 钱包: {__wallet__}")
    except Exception as e:
        print(f"[Error] {e}")
