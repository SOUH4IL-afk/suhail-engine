import streamlit as st
import datetime
import json
import random

# --- 1. القواعد والبيانات الأساسية ---
ABJAD = {'أ': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'و': 6, 'ز': 7, 'ح': 8, 'ط': 9, 'ي': 10, 'ك': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80, 'ص': 90, 'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600, 'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000}
ALPHABET = "أبجد هوز حطي كلمن سعفص قرشت ثخذ ضظغ".replace(" ", "")
ZODIAC_ROOTS = {"الحمل": 12, "الثور": 7, "الجوزاء": 15, "السرطان": 4, "الأسد": 10, "العذراء": 5, "الميزان": 8, "العقرب": 9, "القوس": 11, "الجدي": 3, "الدلو": 6, "الحوت": 14}
DAY_KINGS = {"الأحد (روقيائيل)": 352, "الاثنين (جبرائيل)": 245, "الثلاثاء (سمسمائيل)": 441, "الأربعاء (ميكائيل)": 851, "الخميس (صرفيائيل)": 912, "الجمعة (عنيائيل)": 255, "السبت (كسفيائيل)": 102}

# --- 2. محرك العمليات المتقدمة ---

def calculate_gematria(text):
    """حساب جمل النص بناءً على جدول أبجد الكبير"""
    return sum(ABJAD.get(c, 0) for c in text if c in ABJAD)

def jabr_logic(number):
    """استنطاق الحروف من الأعداد (قاعدة النطق الجفري)"""
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
    """توليد الوفق الرباعي الممتزج"""
    if total_sum < 30: total_sum += 280 # تعديل لضمان عدم وجود أرقام سالبة
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

# --- 3. واجهة البرنامج ---

st.set_page_config(page_title="الزايرجة الجامعة الكبرى", layout="wide")
st.title("📜 المنظومة الكبرى لاستنطاق الزايرجة والأوفاق")

with st.sidebar:
    st.header("⚙️ إعدادات الرصد")
    zodiac_name = st.selectbox("برج الطالع:", list(ZODIAC_ROOTS.keys()))
    day_king = st.selectbox("ملك اليوم الحالي:", list(DAY_KINGS.keys()))
    jump_val = st.slider("قوة الوتر (القفز):", 1, 7, 3)

# حقول بيانات السائل والسؤال
with st.expander("👤 بيانات السائل والسؤال (سرية تامة)", expanded=True):
    col_a, col_b = st.columns(2)
    with col_a:
        person_name = st.text_input("اسم السائل:")
        mother_name = st.text_input("اسم الأم:")
    with col_b:
        question = st.text_input("نص السؤال:")

if st.button("🚀 بدء الاستنطاق الجامع"):
    if not (question and person_name and mother_name):
        st.error("يرجى إكمال كافة البيانات (الاسم، اسم الأم، السؤال).")
    else:
        # أ. الحسابات العددية
        q_sum = calculate_gematria(question)
        p_sum = calculate_gematria(person_name)
        m_sum = calculate_gematria(mother_name)
        total_sum = q_sum + p_sum + m_sum
        
        # ب. استخراج المستحصلة الحرفية
        mustahsila = ""
        ass = ZODIAC_ROOTS[zodiac_name]
        king_val = DAY_KINGS[day_king]
        
        # دمج السؤال مع الاسم في مصفوفة واحدة للاستنطاق
        combined_text = (question + person_name).replace(" ", "")
        for i, char in enumerate(combined_text):
            # معادلة المستحصلة: (المجموع الكلي + رتبة الحرف - الأس)
            idx = (total_sum + i - ass) % 28
            # تطبيق النظيرة والقفز
            opp_char = ALPHABET[(idx + 14) % 28]
            final_char = ALPHABET[(ALPHABET.index(opp_char) + jump_val) % 28]
            mustahsila += final_char
        
        # ج. عرض النتائج
        st.markdown("---")
        st.subheader("🔮 كشف المستحصلة الحرفية")
        st.success(f"الحروف المستنطقة: {' . '.join(mustahsila[:15])}") # عرض أول 15 حرف لجمالية النظم
        
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"👼 الملك الموكل بالإجابة والسائل: **{jabr_logic(total_sum % 1000)}ائيل**")
            st.metric("المجموع العددي الكلي", total_sum)
        
        with col2:
            st.subheader("🟦 الوفق الرباعي المخصص (4x4)")
            
            wafq_4 = generate_4x4_wafq(total_sum)
            for row in wafq_4:
                cols = st.columns(4)
                for idx, val in enumerate(row):
                    cols[idx].code(val)
            st.caption("هذا الوفق ممتزج بطبائع السائل وسر السؤال.")

st.markdown("---")
st.caption("تمت البرمجة بناءً على دمج أصول ابن خلدون، الرزواوي، ومخطوطات الجفر.")