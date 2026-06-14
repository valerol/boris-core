# الاختبارات والاختبارات الذاتية

أرشيف عام مرشح للإصدار

استخدم الاختبارات المحلية فقط. إنها تتحقق من البنية، والوثائق، وسلوك CLI، والوصول اللغوي، وحدود EGO، ونظافة الأرشيف، ومجاميع التحقق. وهي لا تثبت الموثوقية الميدانية ولا وعي الآلة.

الأوامر:

```bash
python -m pytest
python -m bois_sima_boris self-check --root .
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
```

مجموعات الاختبار: الاتساق الفلسفي، والمنطق، وبنية opers، وبنية الأرشيف، والتوطين، وخط أساس السلامة، وسلوك الضغط، ونظافة الإصدار، وتكامل EGO، والتوافق مع الفسيولوجيا المتطورة.
