"""命令行交互入口 – 基于 OpenAI Agents SDK 的智能旅行规划助手。"""

import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

from agents import Runner  # noqa: E402 – load_dotenv must run first

from agents.travel_agent import travel_agent  # noqa: E402


_BANNER = r"""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║   🌍  智行旅游助手  AI Travel Planner  ✈️               ║
║                                                          ║
║   Powered by OpenAI Agents SDK  |  Multi-Agent System   ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
"""

_HELP_TEXT = """
💡 你可以问我：
   • 帮我规划 3 天东京之旅
   • 查一下巴黎的天气
   • 推荐北京的景点（文化类）
   • 帮我推荐上海中等预算的酒店
   • 500 美元换成日元是多少？

输入 quit / exit / q 退出程序
"""


async def chat_loop() -> None:
    """运行命令行对话循环。"""
    print(_BANNER)
    print(_HELP_TEXT)
    print("=" * 60)

    while True:
        try:
            user_input = input("\n👤 你：").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\n👋 感谢使用智行旅游助手，祝旅途愉快！")
            break

        if not user_input:
            continue

        if user_input.lower() in {"quit", "exit", "q", "退出"}:
            print("\n👋 感谢使用智行旅游助手，祝旅途愉快！")
            break

        print("\n🤖 助手：思考中…\n")
        try:
            result = await Runner.run(travel_agent, input=user_input)
            print(f"🤖 助手：{result.final_output}")
        except Exception as exc:  # pylint: disable=broad-except
            print(f"❌ 出现错误：{exc}")

        print("\n" + "─" * 60)


def main() -> None:
    """程序入口函数，检查环境变量并启动对话循环。"""
    api_key = os.getenv("OPENAI_API_KEY", "")
    if not api_key or api_key == "your_openai_api_key_here":
        print(
            "\n❌ 未检测到有效的 OPENAI_API_KEY！\n"
            "请按以下步骤配置：\n"
            "  1. 复制 .env.example 为 .env\n"
            "  2. 在 .env 中填入你的 OpenAI API Key\n"
            "  3. 重新运行程序\n"
        )
        return

    asyncio.run(chat_loop())


if __name__ == "__main__":
    main()
