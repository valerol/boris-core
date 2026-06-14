# مرجع واجهة الأوامر

أرشيف ألفا عام نهائي مجهول الهوية

توفر هذه الحزمة المحلية محلل SIMA يعمل محلياً من دون شبكة، مع وثائق لاستخدام BOIS/BORIS بقيادة بشرية. وهي تنتج إعادة بناء مرشحة، لا حقيقة نهائية ولا تحققاً ميدانياً.

يجب على المراجع البشري تحديد المجال وواجهة القيم والمخاطر المقبولة وشروط التوقف.

لا تستخدم حزمة ألفا هذه للحكم القسري الذاتي، أو القرارات الطبية/القانونية/المالية/العسكرية، أو التحكم المؤسسي الخفي.

## الأوامر

```bash
python -m bois_sima_boris docs --lang ar
python -m bois_sima_boris ego-status
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
python -m bois_sima_boris self-check --root .
python -m pytest
```
