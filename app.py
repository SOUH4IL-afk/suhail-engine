import streamlit as st
import datetime
import random

# --- 1. الثوابت والقواعد الجفرية ---
ABJAD = {'أ': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'و': 6, 'ز': 7, 'ح': 8, 'ط': 9, 'ي': 10, 'ك': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80, 'ص': 90, 'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600, 'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000}
ALPHABET = "أبجد هوز حطي كلمن سعفص قرشت ثخذ ضظغ".replace(" ", "")

WEEKDAY_KINGS = {
    "Sunday": ("الأحد (روقيائيل)", 352),
    "Monday": ("الاثنين (جبرائيل)", 245),
    "Tuesday": ("الثلاثاء (سمسمائيل)", 441),
    "Wednesday": ("الأربعاء (ميكائيل)", 851),
    "Thursday": ("الخميس (صرفيائيل)", 912),
    "Friday": ("الجمعة (عنيائيل)", 255),
    "Saturday": ("السبت (كسفيائيل)", 102)
}

# --- 2. المحركات الذكية ---

def get_auto_zodiac():
    now = datetime.datetime.now()
    m, d = now.month, now.day
    # تحديد البرج والأس آلياً
    if (m == 3 and d >= 21) or (m == 4 and d <= 19): return "الحمل", 12
    elif (m == 4 and d >= 20) or (m == 5 and d <= 20): return "الثور", 7
    elif (m == 5 and d >= 21) or (m == 6 and d <= 20): return "الجوزاء", 15
    elif (m == 6 and d >= 21) or (m == 7 and d <= 22): return "السرطان", 4
    elif (m == 7 and d >= 23) or (m == 8 and d <= 22): return "الأسد", 10
    elif (m == 8 and d >= 23) or (m == 9 and d <= 22): return "العذراء", 5
    elif (m == 9 and d >= 23) or (m == 10 and d <= 22): return "الميزان", 8
    elif (m == 10 and d >= 23) or (m == 11 and d <= 21): return "العقرب", 9
    elif (m == 11 and d >= 22) or (m == 12 and d <= 21): return "القوس", 11
    elif (m == 12 and d >= 22) or (m == 1 and d <= 19): return "الجدي", 3
    elif (m == 1 and d >= 20) or (m == 2 and d <= 18): return "الدلو", 6
    else: return "الحوت", 14

def construct_prose_answer(mustahsila_chars, total_sum):
    """تحويل حروف المستحصلة إلى جملة مقروءة مباشرة"""
    # تصنيف الأجوبة حسب طبائع الحساب (نار، تراب، هواء، ماء)
    keys = {
        0: ["الظفر بالمراد قريب والوقت مناسب", "نور التأييد يسطع في هذا الأمر"],
        1: ["ثبات السعي يورث النجاح الأكيد", "تمسك بالصبر فالنتيجة محمودة جداً"],
        2: ["بشرى سارة تأتيك مع هبوب رياح التغيير", "انفراج في الضيق ونبأ يسر الخاطر"],
        3: ["في هذا المسعى رزق مبارك وصفاء"، "تيسير في الخطى وبركة في النتائج"]
    }
    element_index = total_sum % 4
    base_sentence = random.choice(keys[element_index])
    
    # دمج حروف المستحصلة بشكل مقروء في سياق الجواب
    readable_part = "".join(mustahsila_chars[:4]) # نأخذ أول 4 حروف ككلمة سرية
    return f"{base_sentence}.. (إشارة النطق: {readable_part})"

def generate_4x4_wafq(total_sum):
    if total_sum < 30: total_sum += 360
    base = (total_sum - 30) // 4
    remainder = (total_sum - 30) % 4
    wafq = [[base+8, base+11, base+14, base+1], [base+13, base+2, base+7, base+12], [base+3, base+16, base+9, base+6], [base+10, base+5, base+4, base+15]]
    if remainder >= 1: wafq[3][0] += 1
    if remainder >= 2: wafq[2][1] += 1
    if remainder >= 3: wafq[1][2] += 1
    return wafq

# --- 3. واجهة المستخدم ---

st.set_page_config(page_title="منظومة الزايرجة الناطقة", layout="wide")
st.title("📜 استنطاق الزايرجة الكبرى (نطق الحروف)")

# الرصد الآلي اللحظي
current_time = datetime.datetime.now()
king_name, king_val = WEEKDAY_KINGS[current_time.strftime("%A")]
zodiac_name, zodiac_ass = get_auto_zodiac()
auto_jump = (current_time.day % 7) + 1

with st.sidebar:
    st.header("📡 الرصد الفلكي")
    st.success(f"اليوم: {king_name}")
    st.info(f"البرج: {zodiac_name}")
    st.warning(f"قوة الوتر: {auto_jump}")

with st.expander("👤 مدخلات الكشف", expanded=True):
    c1, c2 = st.columns(2)
    with c1:
        p_name = st.text_input("اسم السائل:")
        m_name = st.text_input("اسم الأم:")
    with c2:
        question = st.text_input("اكتب سؤالك:")

if st.button("🚀 استنطاق الجواب المقروء"):
    if p_name and m_name and question:
        # حساب الجمل
        q_sum = sum(ABJAD.get(c, 0) for c in question if c in ABJAD)
        p_sum = sum(ABJAD.get(c, 0) for c in p_name if c in ABJAD)
        m_sum = sum(ABJAD.get(c, 0) for c in m_name if c in ABJAD)
        total_sum = q_sum + p_sum + m_sum
        
        # استخراج حروف المستحصلة
        mustahsila_chars = []
        combined = (question + p_name).replace(" ", "")
        for i, char in enumerate(combined):
            idx = (total_sum + i - zodiac_ass) % 28
            opp = ALPHABET[(idx + 14) % 28]
            final_char = ALPHABET[(ALPHABET.index(opp) + auto_jump) % 28]
            mustahsila_chars.append(final_char)
        
        # عرض الجواب النثري المباشر
        st.markdown("---")
        st.subheader("📝 الجواب المنطوق")
        final_answer = construct_prose_answer(mustahsila_chars, total_sum)
        st.success(f"**{final_answer}**")
        
        # التفاصيل التقنية
        res1, res2 = st.columns(2)
        with res1:
            st.write(f"🔢 المجموع الكلي: **{total_sum}**")
            st.write(f"🔮 الحروف المستحصلة (نطقاً): `{''.join(mustahsila_chars[:8])}`")
        with res2:
            st.subheader("🔢 الوفق الرباعي (سر التثبيت)")
            wafq = generate_4x4_wafq(total_sum)
            for row in wafq:
                cols = st.columns(4)
                for idx, val in enumerate(row):
                    cols[idx].code(val)
    else:
        st.error("يرجى إكمال البيانات.")