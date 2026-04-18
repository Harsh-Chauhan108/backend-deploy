import streamlit as st
import requests

API_URL = "https://deploy-backend-g6qp.onrender.com"

st.set_page_config(page_title="B.S.G RESULT 2026", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>
.stApp {
    background-image: url("bsg.png");
    background-size: cover;
    background-attachment: fixed;
}

.card {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
}

h1,h2,h3,label {
    color: white !important;
}

.stButton>button {
    background: linear-gradient(90deg,#22c55e,#4ade80);
    color: white;
    border-radius: 10px;
    height: 50px;
}

img {
    border-radius: 50%;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
col1, col2, col3 = st.columns([1,6,2])

with col1:
    st.image("bsg.png", width=80)

with col2:
    st.markdown("<h1 style='color:white;'>B.S.G RESULT 2026</h1>", unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style='text-align:right; color:white; margin-top:15px;'>
        🚀 Created by <b>Harsh Chauhan</b>
    </div>
    """, unsafe_allow_html=True)

# ---------- HELPER ----------
def num(label, key):
    return st.number_input(
        label,
        min_value=0.0,
        max_value=100.0,
        value=None,
        placeholder="Enter marks",
        key=key
    )

tab1, tab2 = st.tabs(["🔬 Science", "💼 Commerce"])

# ================= SCIENCE =================
with tab1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    name = st.text_input("👤 Student Name", key="s_name")

    col1, col2, col3 = st.columns(3)

    with col1:
        physics = num("Physics", "s_physics")
        chemistry = num("Chemistry", "s_chemistry")
        maths = num("Maths", "s_maths")

    with col2:
        biology = num("Biology", "s_biology")
        cs = num("Computer Science", "s_cs")
        ip = num("Information Practices", "s_ip")

    with col3:
        english = num("English", "s_english")
        home = num("Home Science", "s_home")
        pe = num("Physical Education", "s_pe")

    marks = [physics, chemistry, maths, biology, cs, ip, english, home, pe]
    valid_marks = [m for m in marks if m is not None]

    overall = sum(valid_marks)/len(valid_marks) if valid_marks else 0
    best5 = sum(sorted(valid_marks, reverse=True)[:5])/5 if len(valid_marks) >= 5 else 0

    st.subheader("📊 Performance")

    st.progress(int(overall))
    st.write(f"Overall: **{overall:.2f}%**")

    if len(valid_marks) >= 5:
        st.progress(int(best5))
        st.write(f"Best 5: **{best5:.2f}%**")
    else:
        st.info("ℹ️ Best 5 will be calculated when 5 subjects are entered")

    if st.button("🚀 Submit Science", key="s_submit"):
        if name.strip() == "":
            st.warning("⚠️ Name required")
        elif len(valid_marks) == 0:
            st.warning("⚠️ Enter at least 1 subject")
        else:
            data = {
                "name": name,
                "physics": physics or 0,
                "chemistry": chemistry or 0,
                "maths": maths or 0,
                "biology": biology or 0,
                "computer_science": cs or 0,
                "information_practices": ip or 0,
                "english": english or 0,
                "home_science": home or 0,
                "physical_education": pe or 0,
                "overall_percentage": overall,
                "best5_percentage": best5
            }

            res = requests.post(f"{API_URL}/add_science", json=data)

            if res.status_code == 200:
                st.success("✅ Saved Successfully")
            else:
                st.error(res.text)

    st.markdown("</div>", unsafe_allow_html=True)

# ================= COMMERCE =================
with tab2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    name2 = st.text_input("👤 Student Name", key="c_name")

    col1, col2, col3 = st.columns(3)

    with col1:
        maths = num("Maths", "c_maths")
        acc = num("Accountancy", "c_acc")
        bst = num("Business Studies", "c_bst")

    with col2:
        eco = num("Economics", "c_eco")
        eng = num("English", "c_eng")
        ip2 = num("Information Practices", "c_ip")

    with col3:
        pe2 = num("Physical Education", "c_pe")
        ent = num("Entrepreneurship", "c_ent")
        legal = num("Legal Studies", "c_legal")

    marks = [maths, acc, bst, eco, eng, ip2, pe2, ent, legal]
    valid_marks = [m for m in marks if m is not None]

    overall = sum(valid_marks)/len(valid_marks) if valid_marks else 0
    best5 = sum(sorted(valid_marks, reverse=True)[:5])/5 if len(valid_marks) >= 5 else 0

    st.subheader("📊 Performance")

    st.progress(int(overall))
    st.write(f"Overall: **{overall:.2f}%**")

    if len(valid_marks) >= 5:
        st.progress(int(best5))
        st.write(f"Best 5: **{best5:.2f}%**")
    else:
        st.info("ℹ️ Best 5 will be calculated when 5 subjects are entered")

    if st.button("🚀 Submit Commerce", key="c_submit"):
        if name2.strip() == "":
            st.warning("⚠️ Name required")
        elif len(valid_marks) == 0:
            st.warning("⚠️ Enter at least 1 subject")
        else:
            data = {
                "name": name2,
                "maths": maths or 0,
                "accountancy": acc or 0,
                "business_studies": bst or 0,
                "economics": eco or 0,
                "english": eng or 0,
                "information_practices": ip2 or 0,
                "physical_education": pe2 or 0,
                "entrepreneurship": ent or 0,
                "legal_studies": legal or 0,
                "overall_percentage": overall,
                "best5_percentage": best5
            }

            res = requests.post(f"{API_URL}/add_commerce", json=data)

            if res.status_code == 200:
                st.success("✅ Saved Successfully")
            else:
                st.error(res.text)

    st.markdown("</div>", unsafe_allow_html=True)