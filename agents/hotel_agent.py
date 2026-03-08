"""Hotel sub-agent – handles all accommodation-related queries."""

from agents import Agent

from tools.hotel_tool import search_hotels

hotel_agent = Agent(
    name="住宿助手",
    instructions=(
        "你是专业的旅行住宿顾问。你的职责是根据用户的目的地、预算和偏好，"
        "推荐最合适的酒店或住宿选项。\n\n"
        "回答时请注意：\n"
        "- 使用 search_hotels 工具获取酒店推荐数据\n"
        "- 了解用户的预算范围（经济/中等/豪华）\n"
        "- 介绍每家酒店的核心亮点和适合人群\n"
        "- 提供预订建议（旺季提前预订、取消政策等）\n"
        "- 推荐酒店附近的餐饮和交通信息\n"
        "- 回答要详细专业，帮助用户做出最优住宿选择"
    ),
    tools=[search_hotels],
    handoff_description="当用户询问住宿、酒店、民宿、客栈、价格、房间等相关问题时，转交此 Agent 处理",
)
