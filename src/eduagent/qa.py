"""Small deterministic retrieval baseline; no model inference is performed."""

import json
from dataclasses import dataclass
from importlib.resources import files


@dataclass(frozen=True)
class Answer:
    text: str
    sources: tuple[dict[str, str], ...]


def retrieve(question: str) -> list[dict]:
    """Rank lessons by matched keywords; preserve dataset order for ties."""
    query = question.strip().casefold()
    if not query:
        raise ValueError("问题不能为空")
    lessons = json.loads(
        files("eduagent").joinpath("data/lessons.json").read_text(encoding="utf-8")
    )
    ranked = []
    for lesson in lessons:
        score = sum(keyword.casefold() in query for keyword in lesson["keywords"])
        if score:
            ranked.append((score, lesson))
    ranked.sort(key=lambda item: item[0], reverse=True)
    return [lesson for _, lesson in ranked[:2]]


def answer(question: str) -> Answer:
    lessons = retrieve(question)
    if not lessons:
        return Answer("课程知识库中没有足够证据，请补充课程资料或联系老师。", ())
    return Answer(
        text="\n".join(lesson["content"] for lesson in lessons),
        sources=tuple(
            {"id": lesson["id"], "title": lesson["title"]} for lesson in lessons
        ),
    )
