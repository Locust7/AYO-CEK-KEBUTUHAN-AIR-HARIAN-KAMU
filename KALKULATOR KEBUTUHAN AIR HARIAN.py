import streamlit as st

st.set_page_config(page_title="💧 Kalkulator Kebutuhan Air Harian", layout="centered")

# HEADER
st.markdown("<h1 style='text-align: center; color: #00BFFF;'>💧 Kalkulator Kebutuhan Air Harian</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Tentukan berapa liter air yang kamu butuhkan setiap hari agar tetap sehat dan bertenaga!</p>", unsafe_allow_html=True)

st.markdown("""
<style>
    .big-font {
        font-size:20px !important;
        color: #4B0082;
    }
    .highlight-box {
        background-color: #f0f9ff;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #add8e6;
    }
</style>
""", unsafe_allow_html=True)

# INPUT FORM
st.markdown("<div class='highlight-box'><b>Masukkan data pribadi kamu untuk menghitung kebutuhan air harian:</b></div>", unsafe_allow_html=True)
berat = st.number_input("⚖ Berat badan kamu (kg):", min_value=1.0, step=0.5)
aktivitas = st.selectbox("🏃 Tingkat aktivitas:", ["Ringan", "Sedang", "Berat"])
cuaca = st.selectbox("🌦 Kondisi cuaca saat ini:", ["Dingin", "Normal", "Panas"])
jenis_kelamin = st.selectbox("🚻 Jenis kelamin:", ["Pria", "Wanita"])
usia = st.number_input("🎂 Usia kamu:", min_value=1, max_value=120, step=1)

# PERHITUNGAN
def hitung_air(berat, aktivitas, cuaca, jenis_kelamin, usia):
    dasar = berat * 30  # WHO: 30 ml per kg

    if aktivitas == "Sedang":
        dasar += 300
    elif aktivitas == "Berat":
        dasar += 600

    if cuaca == "Panas":
        dasar += 400
    elif cuaca == "Dingin":
        dasar -= 200

    if jenis_kelamin == "Pria":
        dasar += 200
    else:
        dasar -= 100

    if usia < 18:
        dasar -= 300

    return dasar / 1000  # Konversi ke liter

# HASIL
if st.button("💦 Hitung Kebutuhan Air"):
    if berat > 0:
        total = hitung_air(berat, aktivitas, cuaca, jenis_kelamin, usia)
        st.markdown(f"<h3 style='color: #007ACC;'>🌊 Kamu butuh sekitar <span style='color:#FF4500;'>{total:.2f} liter</span> air per hari!</h3>", unsafe_allow_html=True)

       # KATEGORI REKOMENDASI
if total < 1.5:
    st.markdown("<div class='highlight-box' style='background-color:#fff8f0; border-color:#f0cba8;'>⚠ <b>Rendah:</b> Tambahkan lebih banyak air saat beraktivitas.</div>", unsafe_allow_html=True)
elif total >= 1.5 and total < 2.5:
    st.markdown("<div class='highlight-box' style='background-color:#f0fff0; border-color:#a0d6b4;'>✅ <b>Cukup:</b> Pertahankan kebiasaan hidrasi kamu.</div>", unsafe_allow_html=True)
else:
    st.markdown("<div class='highlight-box' style='background-color:#e6f7ff; border-color:#8acde3;'>💪 <b>Tinggi:</b> Sangat aktif? Pastikan kamu bawa botol ke mana pun!</div>", unsafe_allow_html=True)

       # INFO ILMIAH
st.markdown("<h4 style='color:#20B2AA;'>📘 Dasar Ilmiah:</h4>", unsafe_allow_html=True)
st.markdown("""
<div class='highlight-box'>
    <ul>
        <li>Rata-rata kebutuhan air: <b>30–35 ml/kg berat badan per hari</b> (sumber: WHO & EFSA).</li>
        <li><b>Cuaca panas</b> dan <b>aktivitas fisik tinggi</b> meningkatkan kehilangan cairan lewat keringat.</li>
        <li><b>Pria</b> cenderung membutuhkan lebih banyak air karena proporsi massa otot yang lebih tinggi.</li>
        <li><b>Anak-anak</b> butuh lebih sedikit air, kecuali mereka sangat aktif.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

      # TIPS
st.markdown("<h4 style='color:#FF69B4;'>✨ Tips Hidrasi Sehat:</h4>", unsafe_allow_html=True)
st.markdown("""
<div class='highlight-box'>
    <ul>
        <li>🕗 Minum segelas air segera setelah bangun tidur.</li>
        <li>🥗 Konsumsi buah tinggi air seperti <b>semangka, melon, dan jeruk</b>.</li>
        <li>⏰ Gunakan aplikasi pengingat minum secara berkala.</li>
        <li>🧊 Minum air dingin saat cuaca panas untuk menyegarkan tubuh.</li>
        <li>🚰 Selalu bawa <b>tumbler</b> ke mana pun kamu pergi.</li>
    </ul>
</div>
""", unsafe_allow_html=True)
 else:
    st.warning("Masukkan berat badan yang valid terlebih dahulu.")
# FOOTER
st.markdown("---")
st.markdown("<p style='text-align: center; color: grey;'>Proyek Streamlit oleh: <b>IFTA, NADILA, VANIA, DAVIONA, SULTHAN</b></p>", unsafe_allow_html=True)            st.markdown("<div class='highlight-box' style='background-color:#fff8f0; border-color:#f0cba8;'>⚠ <b>Rendah:</b> Tambahkan lebih banyak air saat beraktivitas.</div>", unsafe_allow_html=True)
