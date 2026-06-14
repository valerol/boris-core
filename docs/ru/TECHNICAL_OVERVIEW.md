# Технический обзор

Обезличенный финальный публичный alpha-архив

Этот локализованный пакет содержит локальный несетевой анализатор SIMA и документацию для BOIS/BORIS под управлением человека. Он выдаёт кандидатные реконструкции, а не окончательную истину и не полевую валидацию.

Человек-рецензент задаёт область, ценностный интерфейс, допустимый риск и стоп-условия.

Не используйте этот alpha-пакет для автономного принудительного управления, медицинских/юридических/финансовых/военных решений или скрытого управления институтами.

The package contains a small Python CLI with no runtime dependencies. It reads local JSON, validates required fields, maps observations into opers, builds an operome, and returns a candidate philosophical-machine map.

Runtime boundaries: no network, no shell execution, no dynamic code execution, no autonomous action.
