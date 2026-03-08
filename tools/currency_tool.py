"""Currency tool – provides mock currency conversion for common travel currencies."""

from agents import function_tool

# Mock exchange rates relative to CNY (Chinese Yuan) – as of early 2025 (mock data)
# 1 CNY = X foreign currency
_RATES_FROM_CNY: dict[str, float] = {
    "CNY": 1.0,
    "USD": 0.1379,
    "EUR": 0.1271,
    "JPY": 20.83,
    "GBP": 0.1089,
    "HKD": 1.0779,
    "AUD": 0.2134,
    "CAD": 0.1884,
    "SGD": 0.1852,
    "THB": 4.9856,
    "KRW": 182.35,
}

_CURRENCY_NAMES: dict[str, str] = {
    "CNY": "人民币",
    "USD": "美元",
    "EUR": "欧元",
    "JPY": "日元",
    "GBP": "英镑",
    "HKD": "港币",
    "AUD": "澳元",
    "CAD": "加拿大元",
    "SGD": "新加坡元",
    "THB": "泰铢",
    "KRW": "韩元",
}

_CURRENCY_SYMBOLS: dict[str, str] = {
    "CNY": "¥",
    "USD": "$",
    "EUR": "€",
    "JPY": "¥",
    "GBP": "£",
    "HKD": "HK$",
    "AUD": "A$",
    "CAD": "C$",
    "SGD": "S$",
    "THB": "฿",
    "KRW": "₩",
}


@function_tool
def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
    """模拟货币换算，支持主流旅行货币之间的相互换算。

    支持的货币：CNY（人民币）、USD（美元）、EUR（欧元）、JPY（日元）、
    GBP（英镑）、HKD（港币）、AUD（澳元）、CAD（加拿大元）、
    SGD（新加坡元）、THB（泰铢）、KRW（韩元）。

    Args:
        amount: 待换算的金额。
        from_currency: 源货币代码（如"CNY"、"USD"）。
        to_currency: 目标货币代码（如"JPY"、"EUR"）。

    Returns:
        格式化的换算结果字符串。
    """
    from_currency = from_currency.upper().strip()
    to_currency = to_currency.upper().strip()

    supported = list(_RATES_FROM_CNY.keys())

    if from_currency not in _RATES_FROM_CNY:
        return (
            f"❌ 不支持的源货币：{from_currency}。\n"
            f"✅ 目前支持的货币：{', '.join(supported)}"
        )
    if to_currency not in _RATES_FROM_CNY:
        return (
            f"❌ 不支持的目标货币：{to_currency}。\n"
            f"✅ 目前支持的货币：{', '.join(supported)}"
        )

    # Convert: source -> CNY -> target
    amount_in_cny = amount / _RATES_FROM_CNY[from_currency]
    result = amount_in_cny * _RATES_FROM_CNY[to_currency]

    # Cross rate
    cross_rate = _RATES_FROM_CNY[to_currency] / _RATES_FROM_CNY[from_currency]

    from_sym = _CURRENCY_SYMBOLS.get(from_currency, from_currency)
    to_sym = _CURRENCY_SYMBOLS.get(to_currency, to_currency)
    from_name = _CURRENCY_NAMES.get(from_currency, from_currency)
    to_name = _CURRENCY_NAMES.get(to_currency, to_currency)

    return (
        f"💱 货币换算结果\n"
        f"{'=' * 30}\n"
        f"  {from_sym}{amount:,.2f} {from_currency}（{from_name}）\n"
        f"  ≈  {to_sym}{result:,.2f} {to_currency}（{to_name}）\n\n"
        f"📊 当前汇率：1 {from_currency} = {cross_rate:.4f} {to_currency}\n"
        f"⚠️  注意：以上汇率为参考汇率（模拟数据），实际换汇请以银行或正规换汇平台为准。\n"
        f"💡 旅行换汇建议：机场汇率通常不佳，建议在银行或使用境外信用卡刷卡消费。"
    )
