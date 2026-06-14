# نموذج البيانات والمخططات

أرشيف ألفا عام نهائي مجهول الهوية

توفر هذه الحزمة المحلية محلل SIMA يعمل محلياً من دون شبكة، مع وثائق لاستخدام BOIS/BORIS بقيادة بشرية. وهي تنتج إعادة بناء مرشحة، لا حقيقة نهائية ولا تحققاً ميدانياً.

يجب على المراجع البشري تحديد المجال وواجهة القيم والمخاطر المقبولة وشروط التوقف.

لا تستخدم حزمة ألفا هذه للحكم القسري الذاتي، أو القرارات الطبية/القانونية/المالية/العسكرية، أو التحكم المؤسسي الخفي.

Required top-level JSON keys: `object_id`, `object_type`, `domain`, `value_interface`, `substrate`, `observations`.

Required substrate fields: `units`, `channels`, `memory`, `costs`, `failure_modes`, `stop_authority`.

Required value-interface fields: `goals`, `constraints`, `forbidden_losses`.

Observation fields become opers: `trigger`, `distinction`, `evidence`, `carrier`, `authority`, `value_risk_gate`, `transformation`, `memory_write`, `closure_signal`, `transition_residue`, `cost`, `confidence`.
