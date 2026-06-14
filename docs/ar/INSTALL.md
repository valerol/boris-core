# التثبيت

## التثبيت والتشغيل من دون تثبيت

1. ثبّت Python 3.9 أو أحدث.
2. فك ضغط الحزمة.
3. يمكن التشغيل مباشرة قبل التثبيت:

```bash
python -m bois_sima_boris docs --lang ar
python -m bois_sima_boris ego-status
```

4. تثبيت محلي اختياري في نمط قابل للتحرير:

```bash
python -m pip install --no-index -e .
```

تتضمن الحزمة آلية بناء محلية بلا تبعيات خارجية لهذا المسار غير المتصل.

## أوامر مشتركة

```bash
python -m bois_sima_boris docs --lang ar
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
python -m bois_sima_boris self-check --root .
python -m pytest
```
