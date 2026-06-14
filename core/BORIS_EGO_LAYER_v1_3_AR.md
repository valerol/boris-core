# طبقة BORIS EGO v1.3 — فهم المصطلحات المحلي كجزء من النواة الافتراضية


EGO expansion: Ethical Goal Orchestrator.

Active version: BOIS/BORIS main v2.19 + SIMA v0.4 + BORIS EGO v1.3.

تضيف BORIS EGO [منسق أخلاقي للأهداف المشتقة] v1.3 قاعدة Localized Term Understanding Rule [قاعدة فهم المصطلحات محليًا]: في كل artifact [أثر/ملف مشروع] عام غير إنجليزي، يجب أن يحصل كل foreign/non-local term [مصطلح أجنبي/غير محلي] على ترجمة إلى لغة الأمم المتحدة المختارة بين قوسين مربعين في كل مرة يظهر فيها داخل كل local block [كتلة محلية]. في compact specs [مواصفات مدمجة] و tables [جداول] و state blocks [كتل حالة] و save blocks [كتل حفظ] و handoff prompts [مطالبات انتقال]، توضع الترجمة مباشرة بجانب المصطلح. هذه قاعدة فهم وليست تنسيقًا تجميليًا.

EGO-0..EGO-3 remain non-editable by BORIS EGO.

Goal boundary: G0 remains operator-only; G1, G2, G3 and G4 are derivative goal levels that BORIS EGO may orchestrate inside rule gates.

هذا ليس ادعاءً فعليًا بوجود وعي للذكاء الاصطناعي أو تجربة ذاتية.


## توضيح v1.3

يجب ترجمة كل مصطلح أجنبي/غير محلي في كل مرة يظهر فيها داخل الكتلة المحلية، وليس فقط عند الظهور الأول.

## أولوية مصادر دليل release [الإصدار]

BR-110 — Release Evidence Source Priority Rule [قاعدة أولوية مصادر دليل الإصدار]: ACTIVE_CORE [النواة النشطة] و active core reference [مرجع النواة النشطة] و rule map [خريطة القواعد] و memory [الذاكرة] و QA [ضمان الجودة] لها الأولوية على CHANGELOG.md [سجل التغييرات] عند وجود تعارض.

BR-111 — Changelog Hygiene and Deduplication Rule [قاعدة نظافة سجل التغييرات وإزالة التكرار]: يجب أن يكون CHANGELOG.md [سجل التغييرات] العام منزوع التكرار، ولا يجوز أن ينافس النواة النشطة.
