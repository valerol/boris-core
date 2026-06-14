# ابدأ هنا — BOIS:SIMA&BORIS v1.4.3

حزمة alpha عامة مع تكافؤ لغات الأمم المتحدة وطبقة BORIS EGO v1.0.

لا توجد لغة وصول عامة مفضلة. ترتيب اللغات في الفهارس ثابت فقط ولا يعني أولوية.

للبدء السريع: اقرأ هذا الملف، ثم `QUICKSTART.md`، ثم `USER_MANUAL_SHORT.md`. للعمل الكامل اقرأ `USER_MANUAL_FULL.md` و `BORIS_EGO_LAYER.md`.

## روابط المستخدم الأساسية

- بدء سريع: `QUICKSTART.md`
- تعليمات مستخدم قصيرة: `USER_MANUAL_SHORT.md`
- دليل مستخدم كامل: `USER_MANUAL_FULL.md`
- طبقة BORIS EGO: `BORIS_EGO_LAYER.md`
- حياد اللغة: `LANGUAGE_NEUTRALITY.md`

## BOIS/BORIS/SIMA/BORIS EGO

```text
BOIS/BORIS main v2.16 + SIMA v0.4 + BORIS EGO v1.0
```


## الأوامر

```bash
python -m pip install -e .
python -m bois_sima_boris docs --lang ar
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
python -m bois_sima_boris ego-status --lang ar
python -m bois_sima_boris self-check --root .
python -m pytest
```

ملاحظة: BORIS EGO v1.0 نشط افتراضياً كجزء من النواة؛ لا يلزم تفعيل Mode 10 [الوضع 10].
