# بدء سريع

حزمة BOIS:SIMA&BORIS العامة v1.4.3 مع تكافؤ صارم للغات الأمم المتحدة وطبقة BORIS EGO v1.0.

توفر هذه الحزمة محلل SIMA محلياً من دون شبكة ووثائق لاستخدام BOIS/BORIS بقيادة بشرية. المخرجات هي إعادة بناء مرشحة، وليست حقيقة نهائية ولا تحققاً ميدانياً.

يجب على المراجع البشري تحديد المجال، وواجهة القيم، والمخاطر المقبولة، وشروط التوقف.

لا تستخدم هذه الحزمة للحكم القسري الذاتي، أو القرارات الطبية/القانونية/المالية/العسكرية، أو التحكم المؤسسي الخفي.

## المسار العملي المختصر

1. صِف الكائن في ملف JSON.
2. تحقّق من الملف.
3. شغّل التحليل.
4. اقرأ الآلة المرشحة، وإشارات المخاطر، والأوبروم، والحدود.
5. لا تحوّل المخرجات إلى تعليمات محلية قبل اختبار تجربة ومراجعة بشرية.

## الأوامر

```bash
python -m bois_sima_boris docs --lang ar
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
python -m bois_sima_boris self-check --root .
python -m pytest
```

## BORIS EGO والنواة النشطة

استخدم `BORIS_EGO_LAYER.md` في هذا المجلد كنواة عامة نشطة لـ BORIS EGO v1.0. المسار المختصر: اقرأ هذا الملف، ثم `QUICKSTART.md`، ثم شغّل `python -m bois_sima_boris docs --lang ar`، وراجع `../../START_HERE_UN.md` للوصول اللغوي المتكافئ.

ملاحظة: BORIS EGO v1.0 نشط افتراضياً كجزء من النواة؛ لا يلزم تفعيل Mode 10 [الوضع 10].
