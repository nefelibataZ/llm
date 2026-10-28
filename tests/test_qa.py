import subprocess
import sys
import unittest

from eduagent.qa import answer


class QATests(unittest.TestCase):
    def test_supported_question_has_grounded_source(self):
        result = answer("RAG 是什么？")
        self.assertIn("检索增强生成", result.text)
        self.assertEqual(result.sources[0]["id"], "rag-intro")

    def test_case_insensitive_retrieval(self):
        self.assertEqual(answer("rag").sources[0]["id"], "rag-intro")

    def test_unknown_question_abstains(self):
        result = answer("明天天气怎么样？")
        self.assertIn("没有足够证据", result.text)
        self.assertEqual(result.sources, ())

    def test_empty_question_rejected(self):
        with self.assertRaises(ValueError):
            answer("  ")

    def test_cli(self):
        result = subprocess.run(
            [sys.executable, "-m", "eduagent", "RAG"],
            capture_output=True, text=True, encoding="utf-8",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("rag-intro", result.stdout)


if __name__ == "__main__":
    unittest.main()
