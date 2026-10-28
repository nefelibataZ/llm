"""Run with python -m eduagent or the eduagent command."""

import argparse

from eduagent.qa import answer


def main() -> None:
    parser = argparse.ArgumentParser(description="EduAgent 离线课程答疑")
    parser.add_argument("question", nargs="?", default="RAG 是什么？")
    args = parser.parse_args()
    try:
        result = answer(args.question)
    except ValueError as exc:
        parser.error(str(exc))
    print("模式：offline-extractive")
    print("回答：" + result.text)
    for source in result.sources:
        print(f"来源：{source['id']} | {source['title']}")


if __name__ == "__main__":
    main()
