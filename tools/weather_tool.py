"""Weather tool – provides mock weather data for popular travel destinations."""

from agents import function_tool

# Mock weather data for common travel cities
_WEATHER_DATA: dict[str, dict] = {
    "北京": {
        "temp": "18°C",
        "feels_like": "16°C",
        "condition": "晴转多云",
        "humidity": "45%",
        "wind": "东北风 3级",
        "advice": "早晚温差较大，建议携带外套；防晒指数高，记得涂抹防晒霜。",
        "outfit": "白天穿薄外套或毛衣，晚上需加厚外套。",
    },
    "上海": {
        "temp": "22°C",
        "feels_like": "21°C",
        "condition": "多云",
        "humidity": "68%",
        "wind": "东南风 2级",
        "advice": "天气舒适，适合外出游玩；有轻微降雨可能，建议备伞。",
        "outfit": "穿着轻薄外套或衬衫即可，雨天注意防潮。",
    },
    "东京": {
        "temp": "14°C",
        "feels_like": "12°C",
        "condition": "小雨",
        "humidity": "75%",
        "wind": "北风 2级",
        "advice": "今日有小雨，建议携带雨伞；气温偏低，注意保暖。",
        "outfit": "建议穿着厚外套或风衣，内搭毛衣，务必带伞。",
    },
    "巴黎": {
        "temp": "12°C",
        "feels_like": "10°C",
        "condition": "多云转晴",
        "humidity": "60%",
        "wind": "西风 3级",
        "advice": "天气凉爽，适合步行游览；午后阳光充足，可享受露天咖啡。",
        "outfit": "穿着风衣或中厚外套，搭配围巾，建议穿舒适步行鞋。",
    },
    "纽约": {
        "temp": "8°C",
        "feels_like": "5°C",
        "condition": "晴",
        "humidity": "50%",
        "wind": "西北风 4级",
        "advice": "天气晴朗但寒冷，户外活动注意保暖；适合参观博物馆和室内景点。",
        "outfit": "需穿厚外套或羽绒服，戴手套和帽子，洋葱式穿法最佳。",
    },
    "伦敦": {
        "temp": "10°C",
        "feels_like": "8°C",
        "condition": "阴有小雨",
        "humidity": "80%",
        "wind": "西风 3级",
        "advice": "典型伦敦天气，随时备伞；适合游览室内博物馆和画廊。",
        "outfit": "穿着防水外套，内搭毛衣，必备雨伞。",
    },
    "悉尼": {
        "temp": "26°C",
        "feels_like": "28°C",
        "condition": "晴",
        "humidity": "55%",
        "wind": "东北风 2级",
        "advice": "阳光明媚，适合海滩活动；紫外线较强，做好防晒工作。",
        "outfit": "穿着轻便夏装，备好防晒霜和泳装，可带薄外套备用。",
    },
    "迪拜": {
        "temp": "35°C",
        "feels_like": "40°C",
        "condition": "晴，高温",
        "humidity": "30%",
        "wind": "西风 2级",
        "advice": "天气酷热，建议避开正午室外活动；多补充水分，做好防晒。",
        "outfit": "穿着透气轻薄衣物，进入室内场所需备外套（空调较强）。",
    },
    "新加坡": {
        "temp": "30°C",
        "feels_like": "34°C",
        "condition": "多云，午后有雷阵雨",
        "humidity": "85%",
        "wind": "东南风 1级",
        "advice": "高温高湿，午后常有雷阵雨，建议随身携带雨具和水瓶。",
        "outfit": "穿着轻薄透气衣物，携带折叠伞，进入商场需备薄外套。",
    },
    "曼谷": {
        "temp": "33°C",
        "feels_like": "38°C",
        "condition": "晴转多云",
        "humidity": "78%",
        "wind": "南风 1级",
        "advice": "炎热潮湿，注意防暑；寺庙参观需注意着装规范（遮肩盖膝）。",
        "outfit": "穿着轻薄宽松衣物，访寺庙时需准备遮蔽衣物。",
    },
}

_DEFAULT_WEATHER = {
    "temp": "20°C",
    "feels_like": "19°C",
    "condition": "晴",
    "humidity": "55%",
    "wind": "微风",
    "advice": "天气良好，适合外出游玩，注意随时关注当地天气变化。",
    "outfit": "根据当地季节选择合适衣物。",
}


@function_tool
def get_weather(city: str) -> str:
    """查询指定城市的天气信息，包含温度、天气状况和穿衣建议。

    Args:
        city: 城市名称，例如"北京"、"东京"、"巴黎"。

    Returns:
        格式化的天气信息字符串。
    """
    data = _WEATHER_DATA.get(city, _DEFAULT_WEATHER)
    return (
        f"🌤️ {city} 实时天气\n"
        f"{'=' * 30}\n"
        f"🌡️  当前温度：{data['temp']}（体感 {data['feels_like']}）\n"
        f"☁️  天气状况：{data['condition']}\n"
        f"💧 相对湿度：{data['humidity']}\n"
        f"🌬️  风向风力：{data['wind']}\n"
        f"\n💡 出行建议：{data['advice']}\n"
        f"👗 穿衣指南：{data['outfit']}"
    )
