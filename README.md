# 🌍 智行旅游助手 (Trip Agent)

基于 **OpenAI Agents SDK** 构建的智能旅行规划 Agent 系统，支持多 Agent 协作、Tool Calling 和 Agent Handoff。

## ✨ 功能特性

- 🗺️ 个性化行程规划
- 🌤️ 实时天气查询（Weather Agent）
- 🏨 酒店住宿推荐（Hotel Agent）
- 🎯 景点推荐与介绍
- 💱 多货币换算
- 🤝 Agent Handoff 多智能体协作

## 🛠️ 技术栈

- **OpenAI Agents SDK** - Agent 编排框架
- **Tool Calling** - 工具函数调用
- **Agent Handoff** - 多 Agent 协作移交
- **Streamlit** - Web 可视化界面
- **Python 3.10+**

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/xingfenyizhen/trip_agent.git
cd trip_agent
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置环境变量

```bash
cp .env.example .env
# 编辑 .env，填入你的 OpenAI API Key
```

### 4. 运行

**命令行模式：**

```bash
python main.py
```

**Web UI 模式：**

```bash
streamlit run app.py
```

## 📐 架构设计

```
用户输入
   │
   ▼
travel_agent (主 Agent)
   ├── Tool: get_attractions()    景点推荐
   ├── Tool: create_itinerary()   行程规划
   ├── Tool: convert_currency()   货币换算
   ├── Handoff → weather_agent    天气查询
   │              └── Tool: get_weather()
   └── Handoff → hotel_agent      住宿推荐
                  └── Tool: search_hotels()
```

## 📁 项目结构

```
trip_agent/
├── README.md               # 项目说明（中英文）
├── requirements.txt        # 依赖列表
├── .env.example            # 环境变量示例
├── .gitignore              # 忽略 .env 等敏感文件
├── main.py                 # 程序入口，命令行交互
├── agents/
│   ├── __init__.py
│   ├── travel_agent.py     # 主 Agent 定义
│   ├── weather_agent.py    # 天气查询子 Agent
│   └── hotel_agent.py      # 酒店推荐子 Agent
├── tools/
│   ├── __init__.py
│   ├── weather_tool.py     # 天气工具函数
│   ├── hotel_tool.py       # 酒店推荐工具函数
│   ├── attraction_tool.py  # 景点推荐工具函数
│   ├── itinerary_tool.py   # 行程规划工具函数
│   └── currency_tool.py    # 货币换算工具函数
└── app.py                  # Streamlit 可视化 Web UI
```

## 💼 简历描述参考

> 基于 OpenAI Agents SDK 构建多智能体旅行规划系统，实现 Tool Calling、Agent Handoff 等核心 Agentic AI 设计模式；集成天气、住宿、景点、行程、货币换算五大工具模块，支持命令行与 Streamlit Web 双模式交互。

---

# 🌍 Trip Agent (English)

An intelligent travel planning system built with **OpenAI Agents SDK**, featuring multi-agent collaboration, Tool Calling, and Agent Handoff.

## ✨ Features

- 🗺️ Personalised itinerary planning
- 🌤️ Weather queries (Weather Agent)
- 🏨 Hotel recommendations (Hotel Agent)
- 🎯 Attraction recommendations
- 💱 Multi-currency conversion
- 🤝 Agent Handoff for multi-agent collaboration

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env   # then add your OpenAI API Key

# Run CLI
python main.py

# Run Web UI
streamlit run app.py
```