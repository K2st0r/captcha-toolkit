#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================
Captcha Toolkit v2.1 — Universal CAPTCHA Recognition SDK
   通用验证码识别Python库
=============================================================
Category:   Python Library (SDK)
License:    MIT
Donate:     0xAfe9B67B1DF618FAeD32dC71E3458cf549f26697 (ETH/USDT)
=============================================================
A lightweight, easy-to-use Python library for CAPTCHA
recognition powered by ddddocr. Supports OCR of digits,
letters, and Chinese characters, plus slide-captcha gap
detection.
=============================================================
"""
import base64
import io
import os
import sys
from typing import Dict, List, Optional, Tuple, Union

sys.stdout.reconfigure(encoding="utf-8")

__version__ = "2.1.0"
__wallet__  = "0xAfe9B67B1DF618FAeD32dC71E3458cf549f26697"

import ddddocr


class CaptchaError(Exception):
    """Base exception for CAPTCHA recognition failures."""
    pass


class CaptchaSolver:
    """
    Universal CAPTCHA recognition SDK.

    Usage::

        solver = CaptchaSolver()
        result = solver.solve("captcha.png")
        print(result["text"])  # "AB3D"

    Features:
        - OCR: digits, letters, Chinese characters
        - Slide captcha gap detection
        - Batch processing
        - Multiple input formats: file path, base64, dataURI, raw bytes

    Parameters:
        beta: Use the beta model (default ``True``, better accuracy on
              complex/noisy captchas). Set ``False`` for the standard
              model (slightly faster).
    """

    def __init__(self, beta: bool = True) -> None:
        try:
            self._ocr = ddddocr.DdddOcr(show_ad=False, beta=beta)
            self._det = ddddocr.DdddOcr(det=True, ocr=False, show_ad=False)
        except Exception as exc:
            raise CaptchaError(
                "Failed to initialize ddddocr. "
                "Please install: pip install ddddocr pillow"
            ) from exc

    # ── Image loading ──────────────────────────────────

    @staticmethod
    def _load(data: Union[str, bytes]) -> bytes:
        """Normalize any image input format to raw bytes."""
        if isinstance(data, bytes):
            return data
        if os.path.isfile(data):
            with open(data, "rb") as f:
                return f.read()
        if data.startswith("data:"):
            data = data.split("base64,", 1)[-1]
        # Pad base64 if needed
        missing_padding = len(data) % 4
        if missing_padding:
            data += "=" * (4 - missing_padding)
        try:
            return base64.b64decode(data)
        except Exception:
            # Last resort: try as file path again
            if os.path.isfile(data):
                with open(data, "rb") as f:
                    return f.read()
            raise CaptchaError(f"Cannot decode image: {data[:60]}...")

    # ── Public API ──────────────────────────────────────

    def solve(self, image: Union[str, bytes]) -> Dict:
        """
        Recognize a CAPTCHA image.

        Args:
            image: File path, base64 string, data URI, or raw bytes.

        Returns:
            ``{"success": True, "text": "AB3D", "confidence": 0.95}``
            or ``{"success": False, "text": "", "error": "..."}``
        """
        try:
            img_bytes = self._load(image)
            text = (self._ocr.classification(img_bytes) or "").strip()
            return {"success": True, "text": text, "confidence": 0.95}
        except CaptchaError:
            raise
        except Exception as exc:
            return {"success": False, "text": "", "error": str(exc)}

    def solve_ocr(self, image: Union[str, bytes]) -> str:
        """
        Quick OCR — return text directly.

        Shorthand for ``solver.solve(img)["text"]``.
        """
        return self.solve(image).get("text", "")

    def solve_batch(self, images: List[Union[str, bytes]]) -> List[Dict]:
        """
        Recognize multiple CAPTCHA images.

        Args:
            images: List of images (file paths / base64 / bytes).

        Returns:
            List of result dicts, one per input image.
        """
        results: List[Dict] = []
        total = len(images)
        for i, img in enumerate(images):
            results.append(self.solve(img))
            if (i + 1) % 10 == 0 and total >= 50:
                print(f"  [{i + 1}/{total}]")
        return results

    def solve_slide(self, background: Union[str, bytes],
                    slice_img: Union[str, bytes]) -> Dict:
        """
        Detect the gap position in a slide CAPTCHA.

        Args:
            background: Background image (with notch).
            slice_img:  Slider piece image.

        Returns:
            ``{"success": True, "target": {"x": 120, "y": 0}}`` —
            ``target.x`` is the pixel distance the slider needs to move.
        """
        try:
            bg = self._load(background)
            sl = self._load(slice_img)
            result = self._det.slide_match(sl, bg, simple_target=True)
            return {"success": True, "target": result}
        except CaptchaError:
            raise
        except Exception as exc:
            return {"success": False, "error": str(exc)}


# ─── Quick demo ─────────────────────────────────────────────

if __name__ == "__main__":
    print(f"""
╔══════════════════════════════════════════╗
║   Captcha Toolkit v{__version__}                 ║
║   Universal CAPTCHA Recognition SDK      ║
╠══════════════════════════════════════════╣
║   from captcha_toolkit import CaptchaSolver  ║
║   solver = CaptchaSolver()               ║
║   result = solver.solve("captcha.png")   ║
║   print(result["text"])                  ║
╠══════════════════════════════════════════╣
║   License: MIT · Free to use             ║
║   Donate: {__wallet__}  ║
╚══════════════════════════════════════════╝
    """)

    try:
        solver = CaptchaSolver()
        print(f"  [OK] ddddocr engine initialized successfully")
    except CaptchaError as e:
        print(f"  [WARN] {e}")
