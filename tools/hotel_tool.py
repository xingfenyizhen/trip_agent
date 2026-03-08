"""Hotel tool – provides mock hotel recommendations for popular travel destinations."""

from agents import function_tool

# Mock hotel data: city -> budget -> list of hotels
_HOTEL_DATA: dict[str, dict[str, list[dict]]] = {
    "北京": {
        "经济": [
            {
                "name": "北京青年驿站（天安门店）",
                "price": "¥180/晚",
                "rating": "4.2 ⭐",
                "address": "东城区前门大街附近",
                "highlight": "步行可达天安门，交通便利，提供免费早餐",
            },
            {
                "name": "如家快捷酒店（王府井店）",
                "price": "¥220/晚",
                "rating": "4.0 ⭐",
                "address": "东城区王府井大街",
                "highlight": "王府井商圈核心，购物餐饮极为方便",
            },
            {
                "name": "汉庭酒店（北京南站店）",
                "price": "¥200/晚",
                "rating": "4.1 ⭐",
                "address": "丰台区北京南站附近",
                "highlight": "临近高铁站，适合转乘旅客，性价比高",
            },
        ],
        "中等": [
            {
                "name": "北京王府半岛酒店（商务楼）",
                "price": "¥680/晚",
                "rating": "4.6 ⭐",
                "address": "东城区金宝街8号",
                "highlight": "商务设施完善，近王府井，含自助早餐",
            },
            {
                "name": "北京国际饭店",
                "price": "¥750/晚",
                "rating": "4.5 ⭐",
                "address": "东城区建国门内大街9号",
                "highlight": "老牌五星，地理位置优越，服务专业",
            },
            {
                "name": "北京SKY国际酒店",
                "price": "¥620/晚",
                "rating": "4.4 ⭐",
                "address": "朝阳区三里屯附近",
                "highlight": "三里屯时尚地标旁，夜生活丰富",
            },
        ],
        "豪华": [
            {
                "name": "北京华尔道夫酒店",
                "price": "¥2800/晚",
                "rating": "4.9 ⭐",
                "address": "东城区王府井大街5-15号",
                "highlight": "奢华五星，俯瞰故宫，无懈可击的管家服务",
            },
            {
                "name": "北京柏悦酒店",
                "price": "¥3200/晚",
                "rating": "4.9 ⭐",
                "address": "朝阳区工人体育场北路2号",
                "highlight": "顶层无边泳池，Michelin星级餐厅，极致奢华",
            },
            {
                "name": "北京东方君悦大酒店",
                "price": "¥2500/晚",
                "rating": "4.8 ⭐",
                "address": "东城区长安街1号",
                "highlight": "天安门正对面，无与伦比的历史景观",
            },
        ],
    },
    "东京": {
        "经济": [
            {
                "name": "Hostel 新宿青年旅舍",
                "price": "¥180/晚",
                "rating": "4.3 ⭐",
                "address": "新宿区歌舞伎町附近",
                "highlight": "交通枢纽旁，背包客聚集地，多语言员工",
            },
            {
                "name": "东横INN池袋东口",
                "price": "¥320/晚",
                "rating": "4.1 ⭐",
                "address": "豊島区池袋東口",
                "highlight": "含免费早餐，交通极便利，日式商务风格",
            },
            {
                "name": "Super Hotel 上野",
                "price": "¥280/晚",
                "rating": "4.2 ⭐",
                "address": "台東区上野",
                "highlight": "天然温泉，上野公园步行可达",
            },
        ],
        "中等": [
            {
                "name": "新宿华盛顿酒店",
                "price": "¥880/晚",
                "rating": "4.5 ⭐",
                "address": "新宿区西新宿3丁目",
                "highlight": "西新宿核心，富士山景观房，便捷购物",
            },
            {
                "name": "东京湾Intercontinental",
                "price": "¥1200/晚",
                "rating": "4.6 ⭐",
                "address": "港区台場",
                "highlight": "海湾全景，台场地标，近彩虹桥",
            },
            {
                "name": "浅草View Hotel",
                "price": "¥950/晚",
                "rating": "4.4 ⭐",
                "address": "台東区浅草",
                "highlight": "浅草寺正对面，传统江户风情",
            },
        ],
        "豪华": [
            {
                "name": "东京安缦酒店",
                "price": "¥8000/晚",
                "rating": "5.0 ⭐",
                "address": "千代田区大手町1-5-6",
                "highlight": "日本最奢华酒店之一，禅意设计，顶层SPA",
            },
            {
                "name": "东京半岛酒店",
                "price": "¥5500/晚",
                "rating": "4.9 ⭐",
                "address": "千代田区有楽町1-8-1",
                "highlight": "皇宫景观，Rolls-Royce接送，Michelin餐厅",
            },
            {
                "name": "东京柏悦酒店",
                "price": "¥6000/晚",
                "rating": "4.9 ⭐",
                "address": "新宿区西新宿3-7-1-2",
                "highlight": "52层全景，《迷失东京》拍摄地",
            },
        ],
    },
    "巴黎": {
        "经济": [
            {
                "name": "Generator Paris Hostel",
                "price": "¥200/晚",
                "rating": "4.2 ⭐",
                "address": "10区共和国广场附近",
                "highlight": "时尚设计青旅，酒吧社交氛围浓厚",
            },
            {
                "name": "ibis Paris Tour Eiffel",
                "price": "¥480/晚",
                "rating": "4.1 ⭐",
                "address": "15区艾菲尔铁塔附近",
                "highlight": "艾菲尔铁塔步行15分钟，价格实惠",
            },
            {
                "name": "Pullman Paris Montparnasse",
                "price": "¥550/晚",
                "rating": "4.0 ⭐",
                "address": "14区蒙帕纳斯",
                "highlight": "交通便利，近地铁站，法式早餐",
            },
        ],
        "中等": [
            {
                "name": "巴黎万豪香榭丽舍酒店",
                "price": "¥1800/晚",
                "rating": "4.6 ⭐",
                "address": "8区香榭丽舍大街70号",
                "highlight": "香榭丽舍正街，凯旋门步行可达",
            },
            {
                "name": "巴黎诺富特埃菲尔铁塔酒店",
                "price": "¥1600/晚",
                "rating": "4.5 ⭐",
                "address": "15区Quai de Grenelle",
                "highlight": "塞纳河畔，埃菲尔铁塔景观房",
            },
            {
                "name": "巴黎罗浮宫索菲特酒店",
                "price": "¥2000/晚",
                "rating": "4.7 ⭐",
                "address": "1区罗浮宫旁",
                "highlight": "罗浮宫对面，步行至主要博物馆",
            },
        ],
        "豪华": [
            {
                "name": "巴黎丽兹酒店",
                "price": "¥12000/晚",
                "rating": "5.0 ⭐",
                "address": "1区旺多姆广场15号",
                "highlight": "传奇奢华，海明威常驻，Coco Chanel曾居住于此",
            },
            {
                "name": "四季乔治五世酒店",
                "price": "¥9000/晚",
                "rating": "5.0 ⭐",
                "address": "8区乔治五世大道31号",
                "highlight": "巴黎最顶级酒店，三星Michelin餐厅",
            },
            {
                "name": "巴黎文华东方酒店",
                "price": "¥8500/晚",
                "rating": "4.9 ⭐",
                "address": "8区康朋街251号",
                "highlight": "旗舰SPA，顶层无边泳池，卓越法式服务",
            },
        ],
    },
}

_DEFAULT_HOTELS: dict[str, list[dict]] = {
    "经济": [
        {
            "name": "舒适快捷酒店",
            "price": "¥200-350/晚",
            "rating": "4.0 ⭐",
            "address": "市中心附近",
            "highlight": "性价比高，交通便利，干净整洁",
        },
        {
            "name": "城市商务旅馆",
            "price": "¥250-400/晚",
            "rating": "4.1 ⭐",
            "address": "商业区",
            "highlight": "含早餐，设施齐全，适合商务出行",
        },
        {
            "name": "背包客青年旅舍",
            "price": "¥150-250/晚",
            "rating": "4.2 ⭐",
            "address": "旅游景区附近",
            "highlight": "社交氛围好，适合独行旅客",
        },
    ],
    "中等": [
        {
            "name": "城市精品酒店",
            "price": "¥600-900/晚",
            "rating": "4.5 ⭐",
            "address": "市中心核心区",
            "highlight": "精致装修，优质服务，含丰盛早餐",
        },
        {
            "name": "四星商务酒店",
            "price": "¥700-1000/晚",
            "rating": "4.4 ⭐",
            "address": "商务区",
            "highlight": "商务设施齐全，健身房，游泳池",
        },
        {
            "name": "品牌连锁酒店",
            "price": "¥650-950/晚",
            "rating": "4.3 ⭐",
            "address": "交通枢纽附近",
            "highlight": "品质稳定，积分兑换，多语种服务",
        },
    ],
    "豪华": [
        {
            "name": "五星奢华酒店",
            "price": "¥2500-4000/晚",
            "rating": "4.9 ⭐",
            "address": "城市最佳地段",
            "highlight": "顶级设施，管家服务，Michelin餐厅",
        },
        {
            "name": "顶级度假酒店",
            "price": "¥3000-5000/晚",
            "rating": "4.9 ⭐",
            "address": "城市地标位置",
            "highlight": "无边泳池，豪华SPA，专属礼宾",
        },
        {
            "name": "历史精品奢华酒店",
            "price": "¥2800-4500/晚",
            "rating": "5.0 ⭐",
            "address": "历史文化中心",
            "highlight": "历史建筑改建，独特艺术氛围，极致体验",
        },
    ],
}


@function_tool
def search_hotels(city: str, budget: str = "中等") -> str:
    """根据城市和预算推荐酒店住宿选项。

    Args:
        city: 目标城市名称。
        budget: 预算档次，可选值为"经济"、"中等"、"豪华"，默认为"中等"。

    Returns:
        格式化的酒店推荐信息字符串。
    """
    city_data = _HOTEL_DATA.get(city, {})
    hotels = city_data.get(budget, _DEFAULT_HOTELS.get(budget, _DEFAULT_HOTELS["中等"]))

    lines = [
        f"🏨 {city} {budget}级酒店推荐",
        "=" * 35,
    ]
    for i, hotel in enumerate(hotels, 1):
        lines.append(
            f"\n{i}. {hotel['name']}\n"
            f"   💰 价格：{hotel['price']}\n"
            f"   ⭐ 评分：{hotel['rating']}\n"
            f"   📍 地址：{hotel['address']}\n"
            f"   ✨ 亮点：{hotel['highlight']}"
        )
    lines.append(
        f"\n📌 温馨提示：以上价格为参考价格，实际价格请以预订平台为准。"
        f"建议提前预订，旺季期间价格可能有所上涨。"
    )
    return "\n".join(lines)
