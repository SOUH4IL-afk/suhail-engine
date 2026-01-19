import streamlit as st
import datetime
import json
import random

# --- 1. القواعد الجفرية والبيانات الأساسية ---
ABJAD = {'أ': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'و': 6, 'ز': 7, 'ح': 8, 'ط': 9, 'ي': 10, 'ك': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80, 'ص': 90, 'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600, 'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000}
ALPHABET = "أبجد هوز حطي كلمن سعفص قرشت ثخذ ضظغ".replace(" ", "")
ZODIAC_ROOTS = {"الحمل": 12, "الثور": 7, "الجوزاء": 15, "السرطان": 4, "الأسد": 10, "العذراء": 5, "الميزان": 8, "العقرب": 9, "القوس": 11, "الجدي": 3, "الدلو": 6, "الحوت": 14}
DAY_KINGS = {"الأحد (روقيائيل)": 352, "الاثنين (جبرائيل)": 245, "الثلاثاء (سمسمائيل)": 441, "الأربعاء (ميكائيل)": 851, "الخميس (صرفيائيل)": 912, "الجمعة (عنيائيل)": 255, "السبت (كسفيائيل)": 102}

# --- 2. محرك الجبر والوفق المتطور ---

def jabr_logic(number):
    """تحويل الأرقام إلى حروف ناطقة (قاعدة النطق)"""
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

def get_angel_name(total_sum):
    """استخراج اسم الملك الروحاني الموكل بالسؤال"""
    letters = jabr_logic(total_sum % 1000)
    return letters + "ائيل"

def generate_4x4_wafq(total_sum):
    """توليد الوفق الرباعي (الممتزج) لحفظ سر السؤال"""
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

# --- 3. واجهة المستخدم ---

st.set_page_config(page_title="الزايرجة الكبرى الجامعة", layout="wide")
st.title("📜 المنظومة الجامعة للزايرجة والأوفاق")

with st.sidebar:
    st.header("⚙️ معايير الكشف")
    zodiac_name = st.selectbox("برج الطالع:", list(ZODIAC_ROOTS.keys()))
    day_king = st.selectbox("ملك اليوم الحالي:", list(DAY_KINGS.keys()))
    jump_val = st.slider("قوة الوتر (القفز الحرفي):", 1, 7, 3)

question = st.text_input("📝 اكتب سؤالك بوضوح:")

if st.button("بدء عملية الاستنطاق الكبرى"):
    if question:
        # حساب جمل السؤال
        q_sum = sum(ABJAD.get(c, 0) for c in question if c in ABJAD)
        
        # استخراج المستحصلة
        mustahsila = ""
        ass = ZODIAC_ROOTS[zodiac_name]
        king_val = DAY_KINGS[day_king]
        for i, char in enumerate(question.replace(" ", "")):
            idx = (q_sum + king_val + i - ass) % 28
            # تطبيق النظيرة
            opp_char = ALPHABET[(idx + 14) % 28]
            # تطبيق القفز
            mustahsila += ALPHABET[(ALPHABET.index(opp_char) + jump_val) % 28]
        
        # عرض النتائج
        st.subheader("🔮 المستحصلة الروحانية")
        st.success(f"الحروف المستنطقة: {' . '.join(mustahsila)}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"👼 الملك الموكل بالإجابة: **{get_angel_name(q_sum)}**")
            st.info(f"🔢 مجموع جمل السؤال: {q_sum}")
        
        with col2:
            st.subheader("🟦 الوفق الرباعي (4x4)")
            wafq_4 = generate_4x4_wafq(q_sum)
            for row in wafq_4:
                cols = st.columns(4)
                for idx, val in enumerate(row):
                    cols[idx].code(val)
    else:
        st.error("يرجى إدخال السؤال.")