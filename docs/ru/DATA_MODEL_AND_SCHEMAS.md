# Модель данных и схемы

Обезличенный финальный публичный alpha-архив

Этот локализованный пакет содержит локальный несетевой анализатор SIMA и документацию для BOIS/BORIS под управлением человека. Он выдаёт кандидатные реконструкции, а не окончательную истину и не полевую валидацию.

Человек-рецензент задаёт область, ценностный интерфейс, допустимый риск и стоп-условия.

Не используйте этот alpha-пакет для автономного принудительного управления, медицинских/юридических/финансовых/военных решений или скрытого управления институтами.

Required top-level JSON keys: `object_id`, `object_type`, `domain`, `value_interface`, `substrate`, `observations`.

Required substrate fields: `units`, `channels`, `memory`, `costs`, `failure_modes`, `stop_authority`.

Required value-interface fields: `goals`, `constraints`, `forbidden_losses`.

Observation fields become opers: `trigger`, `distinction`, `evidence`, `carrier`, `authority`, `value_risk_gate`, `transformation`, `memory_write`, `closure_signal`, `transition_residue`, `cost`, `confidence`.
