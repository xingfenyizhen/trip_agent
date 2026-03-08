"""Streamlit Web UI for the AI Travel Planner (Trip Agent)."""

import asyncio
import os

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="智行旅游助手 – AI Travel Planner",
    page_icon="🌍",
    layout="wide",
)

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("⚙️ 设置")
    st.markdown("---")

    api_key_input = st.text_input(
        "🔑 OpenAI API Key",
        value=os.getenv("OPENAI_API_KEY", ""),
        type="password",
        placeholder="sk-...",
        help="输入你的 OpenAI API Key，或在 .env 文件中配置",
    )
    if api_key_input:
        os.environ["OPENAI_API_KEY"] = api_key_input

    model_choice = st.selectbox(
        "🤖 选择模型",
        options=["gpt-4o-mini", "gpt-4o"],
        index=0,
        help="gpt-4o-mini 速度快、成本低；gpt-4o 能力更强",
    )
    os.environ["OPENAI_MODEL"] = model_choice

    st.markdown("---")
    st.subheader("💡 快捷问题")

    quick_questions = [
        "帮我规划 3 天东京之旅",
        "查一下巴黎的天气",
        "推荐北京的文化景点",
        "推荐上海中等预算的酒店",
        "500 美元换成日元是多少？",
        "帮我规划 5 天巴黎行程",
        "查询新加坡的天气",
        "推荐东京豪华酒店",
    ]
    for q in quick_questions:
        if st.button(q, key=f"quick_{q}", use_container_width=True):
            st.session_state.pending_input = q

    st.markdown("---")
    st.markdown(
        "**🛠️ 技术栈**\n"
        "- OpenAI Agents SDK\n"
        "- Tool Calling\n"
        "- Agent Handoff\n"
        "- Streamlit\n"
        "- Python 3.10+"
    )

# ── Session state initialisation ───────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pending_input" not in st.session_state:
    st.session_state.pending_input = None

# ── Main area ──────────────────────────────────────────────────────────────────
st.title("🌍 智行旅游助手 – AI Travel Planner")
st.caption("基于 OpenAI Agents SDK 构建 · 支持多 Agent 协作 · Tool Calling · Agent Handoff")

# Render existing chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


async def run_agent(user_message: str) -> str:
    """Run the travel agent and return the final output."""
    # These imports are deferred so that environment variables (API key, model)
    # are fully configured before the SDK and agent definitions are loaded.
    from agents import Runner  # noqa: PLC0415
    from agents.travel_agent import travel_agent  # noqa: PLC0415

    result = await Runner.run(travel_agent, input=user_message)
    return result.final_output


def get_agent_response(user_message: str) -> str:
    """Synchronous wrapper around the async agent runner."""
    return asyncio.run(run_agent(user_message))


# Handle quick-question button clicks (inject as user message)
if st.session_state.pending_input:
    pending = st.session_state.pending_input
    st.session_state.pending_input = None
    st.session_state.messages.append({"role": "user", "content": pending})
    with st.chat_message("user"):
        st.markdown(pending)

    if not os.environ.get("OPENAI_API_KEY"):
        with st.chat_message("assistant"):
            st.error("❌ 请先在侧边栏输入 OpenAI API Key！")
        st.session_state.messages.append(
            {"role": "assistant", "content": "❌ 请先在侧边栏输入 OpenAI API Key！"}
        )
    else:
        with st.chat_message("assistant"):
            with st.spinner("🤔 思考中…"):
                try:
                    response = get_agent_response(pending)
                    st.markdown(response)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": response}
                    )
                except Exception as exc:  # pylint: disable=broad-except
                    err_msg = f"❌ 出现错误：{exc}"
                    st.error(err_msg)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": err_msg}
                    )
    st.rerun()

# Normal chat input
if prompt := st.chat_input("✈️ 问我任何旅行相关的问题…"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if not os.environ.get("OPENAI_API_KEY"):
        with st.chat_message("assistant"):
            st.error("❌ 请先在侧边栏输入 OpenAI API Key！")
        st.session_state.messages.append(
            {"role": "assistant", "content": "❌ 请先在侧边栏输入 OpenAI API Key！"}
        )
    else:
        with st.chat_message("assistant"):
            with st.spinner("🤔 思考中…"):
                try:
                    response = get_agent_response(prompt)
                    st.markdown(response)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": response}
                    )
                except Exception as exc:  # pylint: disable=broad-except
                    err_msg = f"❌ 出现错误：{exc}"
                    st.error(err_msg)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": err_msg}
                    )
