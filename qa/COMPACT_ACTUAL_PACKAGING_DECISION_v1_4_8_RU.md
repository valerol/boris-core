# Compact actual packaging decision [решение о компактной актуальной упаковке] v1.4.8

Operator [оператор] selected Method 3 [метод 3], Method 6 [метод 6] and Method 7 [метод 7].

Applied rules [применённые правила]:

- BR-113 — Manifest-Only History Reference Rule [правило ссылочной истории только через манифест].
- BR-114 — Canonical Copy Packaging Rule [правило упаковки с единственной канонической копией].
- BR-115 — Archive Role Separation Rule [правило разделения ролей архивов].
- BR-116 — Public Release + Full Actual Companion Rule [правило пары публичного релиза и полной актуальной версии].

Conclusion [вывод]: historical versions [исторические версии] remain in local storage [локальное хранение] and chat histories [истории чатов]. Working full archive [рабочий полный архив] must be compact [компактный], below 200 MB [МБ], and must not recursively include old full binary archives [старые полные бинарные архивы].
