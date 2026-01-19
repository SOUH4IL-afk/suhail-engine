import streamlit as st
import datetime
import json
import random

# --- 1. القواعد والبيانات الأساسية ---
ABJAD = {'أ': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'و': 6, 'ز': 7, 'ح': 8, 'ط': 9, 'ي': 10, 'ك': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80, 'ص': 90, 'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600, 'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000}
ALPHABET = "أبجد هوز حطي كلمن سعفص قرشت ثخذ ضظغ".replace(" ", "")

# ملوك الأيام المؤتمتة (رصد النظام)
WEEKDAY_KINGS = {
    "Sunday": ("الأحد (روقيائيل)", 352),
    "Monday": ("الاثنين (جبرائيل)", 245),
    "Tuesday": ("الثلاثاء (سمسمائيل)", 441),
    "Wednesday": ("الأربعاء (ميكائيل)", 851),
    "Thursday": ("الخميس (صرفيائيل)", 912),
    "Friday": ("الجمعة (عنيائيل)", 255),
    "Saturday": ("السبت (كسفيائيل)", 102)
}

# --- 2. محرك الأتمتة الفلكية ---

def get_auto_zodiac():
    """تحديد البرج الشمسي (الأس) تلقائياً بناءً على تاريخ اليوم"""
    now = datetime.datetime.now()
    m, d = now.month, now.day
    if (m == 3 and d >= 21) or (m == 4 and d <= 19): return "الحمل", 12
    if (m == 4 and d >= 20) or (m == 5 and d <= 20): return "الثور", 7
    if (m == 5 and d >= 21) or (m == 6 and d <= 20): return "الجوزاء", 15
    if (m == 6 and d >= 21) or (m == 7 and d <= 22): return "السرطان", 4
    if (m == 7 and d >= 23) or (m == 8 and d <= 22): return "الأسد", 10
    if (m == 8 and d >= 23) or (m == 9 and d <= 22): return "العذراء", 5
    if (m == 9 and d >= 23) or (m == 10 and d <= 22): return "الميزان", 8
    if (m == 10 and d >= 23) or (m == 11 and d <= 21): return "العقرب", 9
    if (m == 11 and d >= 22) or (m == 12 and d <= 21): return "القوس", 11
    if (m == 12 and d >= 22) or (m == 1 and d <= 19): return "الجدي", 3
    if (m == 1 and d >= 20) or (m == 2 and d <= 18): return "الدلو", 6
    return "الحوت", 14

def jabr_logic(number):
    """استنطاق الحروف من الأرقام (قاعدة النطق)"""
    chars = ""
    temp_num = number
    for val in sorted(ABJAD.values(), reverse=True):
        while temp_num >= val:
            for char, v in ABJAD.items():
                if v == val:
                    chars += char
                    temp_num -= val
                    break
    return chars

def generate_4x4_wafq(total_sum):
    """توليد الوفق الرباعي الممتزج آلياً"""
    base = (total_sum - 30) // 4
    remainder = (total_sum - 30) % 4
    wafq = [
        [base + 8, base + 11, base + 14, base + 1],
        [base + 13, base + 2, base + 7, base + 12],
        [base + 3, base + 16, base + 9, base + 6],
        [base + 10, base + 5, base + 4, base + 15]
    ]
    if remainder >= 1: wafq[3][0] += 1
    if remainder >= 2: wafq[2][1] += 1
    if remainder >= 3: wafq[1][2] += 1
    return wafq

# --- 3. واجهة البرنامج الذكية ---

st.set_page_config(page_title="الزايرجة الآلية الشاملة", layout="wide")
st.title("📜 المنظومة الآلية للزايرجة والاستنطاق")

# الرصد الأوتوماتيكي في الخلفية
current_time = datetime.datetime.now()
day_en = current_time.strftime("%A")
king_name, king_val = WEEKDAY_KINGS[day_en]
zodiac_name, zodiac_ass = get_auto_zodiac()
# قوة الوتر مرتبطة بيوم الشهر (ديناميكية)
auto_jump = (current_time.day % 7) + 1

with st.sidebar:
    st.header("📡 مرصد الوقت الحقيقي")
    st.success(f"تم تحديث الرصد: {current_time.strftime('%H:%M:%S')}")
    st.write(f"📅 **الملك الحاكم:** {king_name}")
    st.write(f"♈ **البرج الفلكي:** {zodiac_name}")
    st.write(f"🌊 **الوتر الحالي:** {auto_jump}")
    st.divider()
    st.caption("يعمل النظام وفق توقيتك المحلي لضبط ميزان الحروف.")

# إدخال البيانات الشخصية
with st.expander("👤 بيانات السائل (تستخدم في ضبط الميزان)", expanded=True):
    c1, c2 = st.columns(2)
    with c1:
        person_name = st.text_input("اسم الشخص:")
    with c2:
        mother_name = st.text_input("اسم الأم:")
    question = st.text_input("📝 اكتب سؤالك بوضوح:")

if st.button("🚀 استنطاق الكشف"):
    if not (question and person_name and mother_name):
        st.warning("يرجى ملء كافة البيانات لبدء الحساب.")
    else:
        # حساب الجمل الكلي (السؤال + السائل + الأم)
        q_val = sum(ABJAD.get(c, 0) for c in question if c in ABJAD)
        p_val = sum(ABJAD.get(c, 0) for c in person_name if c in ABJAD)
        m_val = sum(ABJAD.get(c, 0) for c in mother_name if c in ABJAD)
        total_sum = q_val + p_val + m_val
        
        # استخراج المستحصلة (المحرك الداخلي)
        mustahsila = ""
        combined = (question + person_name).replace(" ", "")
        for i, char in enumerate(combined):
            idx = (total_sum + i - zodiac_ass) % 28
            opp_char = ALPHABET[(idx + 14) % 28]
            final_char = ALPHABET[(ALPHABET.index(opp_char) + auto_jump) % 28]
            mustahsila += final_char
            
        # عرض النتائج النهائية
        st.markdown("---")
        st.subheader("🔮 النتيجة الروحانية المستنطقة")
        st.success(f"حروف الإجابة: {' . '.join(mustahsila[:12])}")
        
        res1, res2 = st.columns(2)
        with res1:
            st.info(f"👼 خادم الوقت الموكل: **{jabr_logic(total_sum % 1000)}ائيل**")
            st.metric("المجموع الرقمي للعمل", total_sum)
        
        with res2:
            st.subheader("🔢 الوفق الرباعي المحصن")
            
            wafq = generate_4x4_wafq(total_sum)
            for row in wafq:
                cols = st.columns(4)
                for idx, val in enumerate(row):
                    cols[idx].code(val)

st.divider()
st.caption("نظام مؤتمت يدمج أسرار 'ابن خلدون' مع الرصد الزمني الآلي.")