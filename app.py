import streamlit as st

# ==================================
# KONFIGURASI HALAMAN
# ==================================

st.set_page_config(
    page_title="Kalkulator FPB & KPK",
    page_icon="🧮",
    layout="wide"
)

# ==================================
# TEMA COLORFUL
# ==================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #ff9a9e,
        #fad0c4,
        #a18cd1,
        #84fab0,
        #8fd3f4
    );
}

h1{
    text-align:center;
    color:#4a148c;
}

h2,h3{
    color:#1565c0;
}

.stButton > button{
    width:100%;
    height:55px;
    border-radius:15px;
    border:none;
    background:linear-gradient(
        90deg,
        #ff6ec4,
        #7873f5
    );
    color:white;
    font-size:18px;
    font-weight:bold;
}

[data-testid="stSidebar"]{
    background:#ffffff;
}

</style>
""", unsafe_allow_html=True)

# ==================================
# SIDEBAR
# ==================================

with st.sidebar:

    st.title("📚 Menu")

    st.success("""
Materi yang digunakan:

✅ FPB

✅ KPK

✅ Algoritma Euclid

✅ Relatif Prima
""")

# ==================================
# JUDUL
# ==================================

st.title("🧮 KALKULATOR FPB & KPK")

st.markdown("""
### Menggunakan Algoritma Euclid

Masukkan dua bilangan.
""")

# ==================================
# FUNGSI FPB
# ==================================

def hitung_fpb(a, b):

    langkah = []

    while b != 0:

        q = a // b
        r = a % b

        langkah.append({
            "a": a,
            "b": b,
            "q": q,
            "r": r
        })

        a, b = b, r

    return a, langkah

# ==================================
# INPUT
# ==================================

col1, col2 = st.columns(2)

with col1:
    a = st.number_input(
        "Bilangan Pertama",
        min_value=1,
        step=1
    )

with col2:
    b = st.number_input(
        "Bilangan Kedua",
        min_value=1,
        step=1
    )

# ==================================
# PROSES
# ==================================

if st.button("🧮 Hitung"):

    fpb, langkah = hitung_fpb(int(a), int(b))

    kpk = abs(int(a) * int(b)) // fpb

    st.markdown("---")

    st.subheader("📊 Hasil Perhitungan")

    st.success(f"FPB = {fpb}")
    st.success(f"KPK = {kpk}")

    if fpb == 1:
        st.success(
            "✨ Kedua bilangan relatif prima karena FPB = 1."
        )
    else:
        st.warning(
            "⚠️ Kedua bilangan tidak relatif prima karena FPB ≠ 1."
        )

    st.markdown("---")

    st.subheader("📖 Langkah Algoritma Euclid")

    for i, item in enumerate(langkah, start=1):

        st.markdown(f"### Langkah {i}")

        st.write(
            f"Bilangan yang dibagi = {item['a']}"
        )

        st.write(
            f"Bilangan pembagi = {item['b']}"
        )

        st.write(
            f"Hasil bagi = {item['q']}"
        )

        st.write(
            f"Sisa = {item['r']}"
        )

        st.latex(
            f"{item['a']} = {item['q']} \\times {item['b']} + {item['r']}"
        )

        if item['r'] != 0:

            st.info(
                f"Karena sisa ≠ 0, maka perhitungan dilanjutkan menggunakan pasangan bilangan ({item['b']}, {item['r']})."
            )

        else:

            st.success(
                "Karena sisa = 0, proses berhenti. FPB diperoleh dari pembagi terakhir yang bukan nol."
            )

        st.markdown("---")

    st.subheader("🎯 Menentukan FPB")

    st.write(
        "Menurut Algoritma Euclid, FPB diperoleh ketika sisa pembagian sudah bernilai 0."
    )

    x = int(a)
    y = int(b)

    while y != 0:

        st.write(
            f"FPB({x},{y}) → FPB({y},{x % y})"
        )

        x, y = y, x % y

    st.success(
        f"Jadi FPB({int(a)},{int(b)}) = {fpb}"
    )

    st.markdown("---")

    st.subheader("🎯 Menentukan KPK")

    st.write(
        "Setelah memperoleh FPB, KPK dapat dihitung menggunakan rumus berikut."
    )

    st.latex(
        r"KPK(a,b)=\frac{a\times b}{FPB(a,b)}"
    )

    st.write("Substitusi nilai:")

    st.latex(
        rf"KPK({int(a)},{int(b)})=\frac{{{int(a)} \times {int(b)}}}{{{fpb}}}"
    )

    st.latex(
        rf"=\frac{{{int(a)*int(b)}}}{{{fpb}}}"
    )

    st.latex(
        rf"={kpk}"
    )

    st.success(
        f"Jadi KPK({int(a)},{int(b)}) = {kpk}"
    )

    st.markdown("---")

    st.subheader("🧠 Fakta Bilangan")

    if int(a) % 2 == 0:
        st.write(f"🔵 {int(a)} adalah bilangan genap")
    else:
        st.write(f"🟠 {int(a)} adalah bilangan ganjil")

    if int(b) % 2 == 0:
        st.write(f"🔵 {int(b)} adalah bilangan genap")
    else:
        st.write(f"🟠 {int(b)} adalah bilangan ganjil")

    st.info(
        f"⭐ Faktor Persekutuan Terbesar (FPB) dari kedua bilangan adalah {fpb}"
    )

    st.info(
        f"🌟 Kelipatan Persekutuan Terkecil (KPK) dari kedua bilangan adalah {kpk}"
    )
