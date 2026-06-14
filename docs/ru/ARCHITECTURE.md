# Архитектура

Обезличенный финальный публичный alpha-архив

Этот локализованный пакет содержит локальный несетевой анализатор SIMA и документацию для BOIS/BORIS под управлением человека. Он выдаёт кандидатные реконструкции, а не окончательную истину и не полевую валидацию.

Человек-рецензент задаёт область, ценностный интерфейс, допустимый риск и стоп-условия.

Не используйте этот alpha-пакет для автономного принудительного управления, медицинских/юридических/финансовых/военных решений или скрытого управления институтами.

Layer map:

- BOIS: grammar for incomplete knowledge, protocols, instructions, experience, physiology, and attention.
- SIMA: analytic layer for candidate reconstruction from substrate and observed opers.
- BORIS: human-led implementation layer for a specific domain.
- Tests: validation, self-check, stress cases, risk gates, and rollback.

Data flow: JSON object -> validation -> opers -> operome -> candidate M=<O,E,A,V,R,C,T> -> limits and next step.
