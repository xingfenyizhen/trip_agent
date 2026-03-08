"""Itinerary tool – generates detailed day-by-day travel itineraries."""

from agents import function_tool

# Sample itinerary templates per city (up to 5 days worth of content)
_ITINERARY_TEMPLATES: dict[str, list[dict]] = {
    "东京": [
        {
            "morning": "浅草寺参拜 → 仲见世通购物街闲逛 → 浅草文化观光中心俯瞰雷门",
            "afternoon": "秋叶原电器街 & 动漫文化探索 → 上野公园散步 → 东京国立博物馆",
            "evening": "上野アメ横商店街晚餐，品尝烤串和章鱼烧",
            "restaurant": "推荐：天すし（天妇罗寿司）或 炉端焼き居酒屋",
            "transport": "建议购买Suica卡，乘坐JR山手线在各站之间移动，方便快捷",
        },
        {
            "morning": "新宿御苑早晨漫步 → 东京都厅免费展望台俯瞰全景",
            "afternoon": "原宿竹下通潮流街区 → 表参道高端购物 → 涩谷十字路口打卡",
            "evening": "涩谷 Scramble Square 楼顶观景台夜景 → 居酒屋晚餐",
            "restaurant": "推荐：涩谷 SHIBUYA SKY 附近的和牛烧肉或寿司店",
            "transport": "步行+地铁，JR涩谷站换乘方便",
        },
        {
            "morning": "筑地市场外市场早餐（新鲜海鲜） → 筑地本愿寺参拜",
            "afternoon": "银座奢侈品购物街 → 东京国立近代美术馆",
            "evening": "六本木 Hills 夜景 → Tokyo Midtown高档餐厅晚餐",
            "restaurant": "推荐：六本木高级日料割烹或法餐",
            "transport": "地铁日比谷线、大江户线",
        },
        {
            "morning": "乘JR到镰仓（约1小时），游览高德院大佛、长谷寺",
            "afternoon": "小町通商店街午餐 → 鹤冈八幡宫参拜 → 海岸步道散步",
            "evening": "返回东京，新宿或池袋晚餐",
            "restaurant": "推荐：镰仓小町通的抹茶甜品店",
            "transport": "JR横须贺线往返镰仓",
        },
        {
            "morning": "东京晴空塔登顶观景 → 押上周边商场购物",
            "afternoon": "台场海滨公园 → 富士电视台 → 调色板城购物",
            "evening": "台场夜景与彩虹桥灯光 → 回程前最后一顿日料",
            "restaurant": "推荐：台场 Aqua City 内的各式日式料理",
            "transport": "乘坐百合海鸥号无人驾驶单轨列车前往台场",
        },
    ],
    "北京": [
        {
            "morning": "天安门广场观升旗（需提前查询时间） → 天安门城楼 → 故宫前三殿",
            "afternoon": "故宫后宫区域（御花园、珍宝馆） → 景山公园登高俯瞰故宫全貌",
            "evening": "南锣鼓巷胡同探访 → 什刹海酒吧街体验北京夜生活",
            "restaurant": "推荐：四季民福烤鸭（故宫附近）或 老北京炸酱面馆",
            "transport": "地铁1号线天安门站下车，景山步行可达",
        },
        {
            "morning": "颐和园开园即入，游览长廊、排云殿",
            "afternoon": "乘船游昆明湖 → 十七孔桥打卡 → 北京大学未名湖散步",
            "evening": "五道口商圈晚餐，北京大学周边咖啡馆",
            "restaurant": "推荐：颐和园附近的江南厨子或石锅鱼",
            "transport": "地铁4号线颐和园站",
        },
        {
            "morning": "长城（慕田峪或八达岭），建议提前预约",
            "afternoon": "长城游览 → 附近明十三陵参观",
            "evening": "返回市区，王府井步行街购物",
            "restaurant": "推荐：全聚德烤鸭（王府井店）",
            "transport": "建议包车或参加小团游前往长城",
        },
    ],
    "巴黎": [
        {
            "morning": "早起参观埃菲尔铁塔（预约开门时段，人少） → 战神广场野餐",
            "afternoon": "塞纳河游船 → 圣母院（外观，内部修缮中） → 西岱岛漫步",
            "evening": "蒙马特高地 → 圣心堂俯瞰巴黎夜景 → 蒙马特小酒馆晚餐",
            "restaurant": "推荐：蒙马特的 La Maison Rose 或 Chez Plumeau",
            "transport": "步行+地铁1号线，建议购买Navigo周票",
        },
        {
            "morning": "罗浮宫（预留4小时，重点：蒙娜丽莎、胜利女神、维纳斯）",
            "afternoon": "杜伊勒利花园漫步 → 奥赛博物馆（印象派名作）",
            "evening": "香榭丽舍大街漫步 → 凯旋门登顶夜景",
            "restaurant": "推荐：Café de Flore 或 Les Deux Magots 感受巴黎咖啡文化",
            "transport": "地铁1号线贯穿香榭丽舍全线",
        },
        {
            "morning": "凡尔赛宫（乘RER C，全天游览）",
            "afternoon": "凡尔赛花园 → 大特里亚农宫",
            "evening": "返回巴黎，玛黑区漫步 → 犹太区享用晚餐",
            "restaurant": "推荐：玛黑区的 L'As du Fallafel 或时尚法式小酒馆",
            "transport": "RER C线，约40分钟",
        },
    ],
}

_DEFAULT_TEMPLATE = [
    {
        "morning": "参观城市地标建筑，了解当地历史文化",
        "afternoon": "游览自然风景区或主题公园",
        "evening": "探访当地美食街，品尝特色小吃",
        "restaurant": "推荐到当地评分最高的特色餐厅用餐",
        "transport": "建议使用当地公共交通或步行游览市区",
    },
    {
        "morning": "参观博物馆或画廊",
        "afternoon": "游览城市公园或滨水区",
        "evening": "夜市或文化演出体验",
        "restaurant": "推荐当地传统菜系餐厅",
        "transport": "可租用自行车或电动车探索城市",
    },
    {
        "morning": "郊区一日游（古镇、山景或海滨）",
        "afternoon": "购物或自由时间",
        "evening": "告别晚宴，品尝最具代表性的当地美食",
        "restaurant": "推荐城市内米其林推荐或本地人常去餐厅",
        "transport": "包车或参加当地半日游团",
    },
]

_STYLE_NOTES = {
    "文化": "以历史人文探索为主，深度体验当地传统文化、博物馆和古迹。",
    "休闲": "节奏轻松，避开热门景点高峰，多留白让自己充分放松。",
    "美食": "以美食为主线，每餐精心安排，探索当地最具特色的餐厅和市场。",
    "均衡": "兼顾文化、自然、美食，节奏适中，老少皆宜。",
}


@function_tool
def create_itinerary(city: str, days: int, style: str = "均衡") -> str:
    """为指定城市生成详细的逐日旅行行程。

    Args:
        city: 目标城市名称。
        days: 旅行天数（建议1-7天）。
        style: 行程风格，可选值为"文化"、"休闲"、"美食"、"均衡"，默认为"均衡"。

    Returns:
        格式化的逐日行程字符串。
    """
    days = max(1, min(days, 7))  # clamp to 1-7
    templates = _ITINERARY_TEMPLATES.get(city, _DEFAULT_TEMPLATE)
    style_note = _STYLE_NOTES.get(style, _STYLE_NOTES["均衡"])

    lines = [
        f"🗓️ {city} {days}日 {style}风格 行程规划",
        "=" * 40,
        f"📌 行程主题：{style_note}",
        "",
    ]
    for day in range(1, days + 1):
        tmpl = templates[(day - 1) % len(templates)]
        lines.append(f"【第 {day} 天】")
        lines.append(f"  🌅 上午：{tmpl['morning']}")
        lines.append(f"  ☀️  下午：{tmpl['afternoon']}")
        lines.append(f"  🌙 晚上：{tmpl['evening']}")
        lines.append(f"  🍽️  餐厅推荐：{tmpl['restaurant']}")
        lines.append(f"  🚇 交通建议：{tmpl['transport']}")
        lines.append("")

    lines.append("🌟 温馨提示：")
    lines.append("  • 行程仅供参考，请根据体力和兴趣灵活调整。")
    lines.append("  • 热门景点建议提前网上预约，避免现场排队。")
    lines.append("  • 保留一定自由时间，随机探索才是旅行的乐趣所在！")
    return "\n".join(lines)
