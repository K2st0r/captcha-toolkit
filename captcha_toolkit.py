#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Captcha Toolkit v1.0 - 通用验证码识别工具包
价格: 20 USDT
购买后发送至: 0xAfe9B67B1DF618FAeD32dC71E3458cf549f26697 (ETH/USDT)
功能: OCR识别、滑块识别、批量处理、API服务
"""
import base64, json, os, sys, time, io
from PIL import Image

__version__ = "1.0.0"
__price__ = "20 USDT"
__wallet__ = "0xAfe9B67B1DF618FAeD32dC71E3458cf549f26697"

class CaptchaSolver:
    """通用验证码识别器"""
    
    def __init__(self, beta=True, gpu=False):
        import ddddocr
        self.ocr = ddddocr.DdddOcr(show_ad=False, beta=beta)
        self.det = ddddocr.DdddOcr(det=True, ocr=False, show_ad=False)
        print(f"[CaptchaSolver] Loaded (beta={beta}, gpu={gpu})")
    
    def solve(self, image_data):
        """识别图片验证码
        Args:
            image_data: bytes/str (文件路径/base64/dataURI)
        Returns:
            str: 识别结果
        """
        if isinstance(image_data, str):
            if os.path.isfile(image_data):
                with open(image_data, 'rb') as f:
                    image_data = f.read()
            elif image_data.startswith('data:'):
                image_data = base64.b64decode(image_data.split('base64,')[1])
            else:
                try:
                    image_data = base64.b64decode(image_data)
                except:
                    with open(image_data, 'rb') as f:
                        image_data = f.read()
        return self.ocr.classification(image_data)
    
    def solve_batch(self, images, workers=4):
        """批量识别"""
        results = []
        for img in images:
            results.append(self.solve(img))
        return results
    
    def solve_slide(self, bg_img, slice_img):
        """滑块验证码 - 返回缺口位置"""
        if isinstance(bg_img, str):
            if bg_img.startswith('data:'):
                bg_img = base64.b64decode(bg_img.split('base64,')[1])
            else:
                with open(bg_img, 'rb') as f:
                    bg_img = f.read()
        if isinstance(slice_img, str):
            if slice_img.startswith('data:'):
                slice_img = base64.b64decode(slice_img.split('base64,')[1])
            else:
                with open(slice_img, 'rb') as f:
                    slice_img = f.read()
        return self.det.slide_match(slice_img, bg_img, simple_target=True)


def demo():
    """演示使用方法"""
    solver = CaptchaSolver()
    
    # 从文件识别
    # result = solver.solve('captcha.png')
    # print(f'识别结果: {result}')
    
    # 从base64识别
    # result = solver.solve('iVBORw0KGgo...')
    # print(f'识别结果: {result}')
    
    # 滑块识别
    # result = solver.solve_slide('bg.jpg', 'slice.png')
    # print(f'滑块位置: {result}')
    
    print("\n[Demo] CaptchaSolver ready!")
    print(f"  版本: v{__version__}")
    print(f"  价格: {__price__}")
    print(f"  钱包: {__wallet__}")


if __name__ == "__main__":
    demo()
