import streamlit as st
import datetime
import random

# --- 1. الأصول والقواعد الحرفية (قاعدة الجفر) ---
ABJAD = {'أ': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'و': 6, 'ز': 7, 'ح': 8, 'ط': 9, 'ي': 10, 'ك': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80, 'ص': 90, 'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600, 'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000}
ALPHABET = "أبجد هوز حطي كلمن سعفص قرشت ثخذ ضظغ".replace(" ", "")
NATURES = {"ناري": "أهطمدشذ", "ترابي": "بويصتض", "هوائي": "جزكفسظ", "مائي": "دحلعقخغ"}

# --- 2. محرك القواعد السبع المدمج ---

def get_astrological_axis():
    """القاعدة 1: التدوير والأس الفلكي"""
    now = datetime.datetime.now()
    zodiacs = [
        ("الحمل", 12), ("الثور", 7), ("الجوزاء", 15), ("السرطان", 4),
        ("الأسد", 10), ("العذراء", 5), ("الميزان", 8), ("العقرب", 9),
        ("القوس", 11), ("الجدي", 3), ("الدلو", 6), ("الحوت", 14)
    ]
    # حساب البرج بناءً على المسار الشمسي الحالي
    m, d = now.month, now.day
    if (m == 3 and d >= 21) or (m == 4 and d <= 19): return zodiacs[0]
    elif (m == 4 and d >= 20) or (m == 5 and d <= 20): return zodiacs[1]
    elif (m == 5 and d >= 21) or (m == 6 and d <= 20): return zodiacs[2]
    elif (m == 6 and d >= 21) or (m == 7 and d <= 22): return zodiacs[3]
    elif (m == 7 and d >= 23) or (m == 8 and d <= 22): return zodiacs[4]
    elif (m == 8 and d >= 23) or (m == 9 and d <= 22): return zodiacs[5]
    elif (m == 9 and d >= 23) or (m == 10 and d <= 22): return zodiacs[6]
    elif (m == 10 and d >= 23) or (m == 11 and d <= 21): return zodiacs[7]
    elif (m == 11 and d >= 22) or (m == 12 and d <= 21): return zodiacs[8]
    elif (m == 12 and d >= 22) or (m == 1 and d <= 19): return zodiacs[9]
    elif (m == 1 and d >= 20) or (m == 2 and d <= 18): return zodiacs[10]
    else: return zodiacs[11]

def get_dominant_nature(text):
    """القاعدة 2: الميزان والطبائع"""
    scores = {"ناري": 0, "ترابي": 0, "هوائي": 0, "مائي": 0}
    for char in text:
        for nature, chars in NATURES.items():
            if char in chars: scores[nature] += 1
    return max(scores, key=scores.get)

def synthesize_answer(mustahsila_chars, total_sum, nature, category):
    """القاعدة 3 & 4: التوليف والاستنطاق اللغوي"""
    engines = {
        "رزق": {
            "ناري": "فتح قريب في الرزق ونيل رفعة", "ترابي": "بركة ثابتة تأتيك بالصبر والتؤدة",
            "هوائي": "تغير مبارك في المال وبشرى سارة", "مائي": "سعة في الحال ورزق جارٍ بغير تعب"
        },
        "عام": {
            "ناري": "تنال الظفر بمرادك بقوة التأييد", "ترابي": "أساس مقصدك ثابت والنجاح حليفك",
            "هوائي": "خبر يسرك يغير مجرى الأمور سريعة", "مائي": "تيسير شامل وصفاء في الوقت الحالي"
        }
    }
    base_msg = engines.get(category, engines["عام"])[nature]
    # القاعدة 5: استخراج "كلمة النطق" من المستحصلة
    speech_core = "".join(mustahsila_chars[:4])
    return f"{base_msg}. (إشارة النطق: {speech_core})"

# --- 3. واجهة المنظومة السباعية ---

st.set_page_config(page_title="الزايرجة السباعية الكبرى", layout="wide")
st.title("📜 منظومة الزايرجة السباعية الكبرى (تطوير ابن خلدون)")

with st.sidebar:
    st.header("⚙️ رصد القواعد السبع")
    q_category = st.selectbox("نوع الكشف:", ["عام", "رزق", "سفر", "صحة"])
    now = datetime.datetime.now()
    z_name, z_ass = get_astrological_axis()
    st.info(f"♈ البرج الحالي: {z_name}")
    st.info(f"🕒 رصد الدقيقة: {now.minute}")

col1, col2 = st.columns(2)
with col1:
    p_name = st.text_input("اسم الشخص:")
    m_name = st.text_input("اسم الأم:")
with col2:
    question = st.text_input("نص السؤال:")

if st.button("🚀 تشغيل محرك الاستنطاق"):
    if p_name and m_name and question:
        # القاعدة 6: حساب الجمل الكبير (الجفر)
        full_identity = p_name + m_name
        total_sum = sum(ABJAD.get(c, 0) for c in (question + full_identity) if c in ABJAD)
        dominant_nature = get_dominant_nature(question + full_identity)
        
        # القاعدة 7: السقوط والنظائر (توليد المستحصلة)
        mustahsila = []
        combined_text = (question + p_name).replace(" ", "")
        for i, char in enumerate(combined_text[:12]):
            # معادلة الزايرجة المركبة (المجموع + الرصد الزمني + الأس الفلكي)
            idx = (total_sum + i + now.minute + z_ass) % 28
            # استخدام نظيرة الحرف لضبط النطق
            antonym_idx = (idx + 14) % 28
            mustahsila.append(ALPHABET[antonym_idx])
            
        # إنتاج الجواب النهائي
        final_answer = synthesize_answer(mustahsila, total_sum, dominant_nature, q_category)
        
        st.markdown("---")
        st.subheader("🔮 الجواب المستنطق النهائي")
        st.success(f"**{final_answer}**")
        
        # عرض البيانات الفنية للتثبيت
        c1, c2, c3 = st.columns(3)
        with c1: st.metric("الطبع الغالب", dominant_nature)
        with c2: st.metric("المجموع العددي", total_sum)
        with c3: st.write("📝 الحروف المستحصلة:", " . ".join(mustahsila[:6]))

        st.subheader("🔢 الوفق الجامع (للتثبيت الروحاني)")
        base_wafq = (total_sum - 30) // 4
        # بناء الوفق الرباعي الشهير
        wafq = [[base_wafq+8, base_wafq+11, base_wafq+14, base_wafq+1], [base_wafq+13, base_wafq+2, base_wafq+7, base_wafq+12], [base_wafq+3, base_wafq+16, base_wafq+9, base_wafq+6], [base_wafq+10, base_wafq+5, base_wafq+4, base_wafq+15]]
        for row in wafq:
            cols = st.columns(4)
            for i, v in enumerate(row): cols[i].code(v)
    else:
        st.error("يرجى إكمال البيانات لبدء عملية الاستنطاق.")