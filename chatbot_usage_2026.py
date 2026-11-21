"""Столбчатая диаграмма по файлу «Все разборы за 2026 год.md»."""

from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


# Число самостоятельных работ, в которых можно установить название сервиса.
# Один сервис учитывается один раз на работу в рамках задания.
by_assignment = {
    # Включены ответы из приложения с критериями и упоминание «дипсика».
    "Промпт-инжиниринг": {
        "ChatGPT": 2, "DeepSeek": 2, "Grok": 1, "Perplexity": 1,
    },
    "Паспорт специальности": {
        "Qwen": 6, "DeepSeek": 4, "GigaChat": 3, "Gemini": 2, "ChatGPT": 2,
        "Алиса": 1, "Gemma": 1, "Claude": 1, "Kimi": 1, "Perplexity": 1,
    },
    "Ядро исследования": {
        "Qwen": 3, "DeepSeek": 3, "GigaChat": 2, "Алиса": 1,
        "Gemma": 1, "Claude": 1, "Gemini": 1, "Perplexity": 1,
    },
    # Учтены все явно опробованные модели, включая Alice AI под именем «Алиса».
    "Перевод": {
        "Qwen": 4, "ChatGPT": 3, "Gemini": 2, "Алиса": 1,
        "DeepSeek": 1, "Gemma": 1, "GigaChat": 1,
    },
    # В работе с Qwen также пробовали исправить график с Алисой и GigaChat.
    "Визуализация": {"Claude": 1, "Qwen": 1, "Алиса": 1, "GigaChat": 1},
}


def main():
    totals = Counter()
    for counts in by_assignment.values():
        totals.update(counts)
    ranked = sorted(totals, key=lambda name: (-totals[name], name))
    values = [totals[name] for name in ranked]

    fig, ax = plt.subplots(figsize=(10, 6.8))
    fig.subplots_adjust(left=0.16, right=0.94, top=0.87, bottom=0.10)
    ax.set_title("Какими чат-ботами пользовались слушатели в 2026 году",
                 loc="left", fontsize=16, pad=16)
    bars = ax.barh(ranked, values, color="#246A84", height=0.68)
    ax.invert_yaxis()
    ax.bar_label(bars, padding=5)
    ax.set_xlim(0, max(values) + 1)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_xlabel("Число работ, в которых использовали сервис")
    ax.set_axisbelow(True)
    ax.grid(axis="x", alpha=0.2)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0)

    output = Path(__file__).with_suffix(".jpg")
    fig.savefig(output, dpi=300, facecolor="white", pil_kwargs={"quality": 95, "subsampling": 0})
    plt.close(fig)
    print(output)


if __name__ == "__main__":
    main()
