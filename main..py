import streamlit as st

# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="◎",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Styles ────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

*, *::before, *::after { box-sizing: border-box; }

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Background */
.stApp { background: #07080f; }

/* Remove Streamlit UI clutter */
#MainMenu, footer, header, .stDeployButton { visibility: hidden !important; }
.block-container {
    padding: 3rem 1.5rem 3rem !important;
    max-width: 600px !important;
}

/* ─── Hero ─────────────────────────────── */
.hero {
    text-align: center;
    padding: 1.5rem 0 3rem;
}
.hero-pill {
    display: inline-block;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #818cf8;
    background: rgba(99,102,241,0.1);
    border: 1px solid rgba(99,102,241,0.25);
    border-radius: 100px;
    padding: 0.3rem 0.9rem;
    margin-bottom: 1.4rem;
}
.hero-h1 {
    font-size: 3rem;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -0.04em;
    line-height: 1.1;
    margin-bottom: 1rem;
}
.hero-h1 em {
    font-style: normal;
    background: linear-gradient(130deg, #818cf8, #c084fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-p {
    font-size: 0.95rem;
    color: #4b5563;
    line-height: 1.65;
    max-width: 380px;
    margin: 0 auto;
}

/* ─── Card ─────────────────────────────── */
.card {
    background: #10111a;
    border: 1px solid #1c1e2d;
    border-radius: 20px;
    padding: 1.75rem;
    margin-bottom: 0.875rem;
}
.card-label {
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.13em;
    text-transform: uppercase;
    color: #374151;
    margin-bottom: 1.25rem;
}

/* ─── Number Input ─────────────────────── */
.stNumberInput label {
    color: #6b7280 !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
}
.stNumberInput input {
    background: #07080f !important;
    border: 1px solid #1c1e2d !important;
    border-radius: 12px !important;
    color: #ffffff !important;
    font-size: 1.6rem !important;
    font-weight: 700 !important;
    letter-spacing: -0.02em !important;
    padding: 0.75rem 1rem !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
}
.stNumberInput input:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 3px rgba(99,102,241,0.12) !important;
    outline: none !important;
}
/* Stepper buttons */
.stNumberInput > div > div > button {
    background: #1c1e2d !important;
    border: none !important;
    border-radius: 8px !important;
    color: #6b7280 !important;
}
.stNumberInput > div > div > button:hover {
    background: #252840 !important;
    color: #ffffff !important;
}

/* ─── CTA Button ───────────────────────── */
.stButton > button {
    width: 100% !important;
    background: #6366f1 !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 0.95rem 1.5rem !important;
    font-size: 0.88rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.04em !important;
    transition: background 0.2s, box-shadow 0.2s, transform 0.15s !important;
}
.stButton > button:hover {
    background: #4f46e5 !important;
    box-shadow: 0 6px 20px rgba(99,102,241,0.4) !important;
    transform: translateY(-1px) !important;
}
.stButton > button:active {
    transform: translateY(0) !important;
    box-shadow: none !important;
}

/* ─── Results ──────────────────────────── */
.results {
    animation: slideUp 0.45s cubic-bezier(.22,1,.36,1);
}
@keyframes slideUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* Result hero card */
.r-card {
    border-radius: 24px;
    padding: 3rem 2rem 2.5rem;
    text-align: center;
    margin-bottom: 0.875rem;
    position: relative;
    overflow: hidden;
}
.r-card::after {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at 50% 0%, rgba(255,255,255,0.06) 0%, transparent 65%);
    pointer-events: none;
}
.r-eyebrow {
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.35);
    margin-bottom: 1rem;
}
.r-num {
    font-size: 7rem;
    font-weight: 800;
    letter-spacing: -0.05em;
    line-height: 1;
    margin-bottom: 1rem;
}
.r-badge {
    display: inline-block;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 0.45rem 1.3rem;
    border-radius: 100px;
}

/* Underweight */
.t-uw { background: linear-gradient(160deg, #0c1220 0%, #0f2447 100%); border: 1px solid rgba(59,130,246,0.2); }
.t-uw .r-num   { color: #93c5fd; }
.t-uw .r-badge { background: rgba(59,130,246,0.12); color: #93c5fd; border: 1px solid rgba(59,130,246,0.25); }

/* Normal */
.t-nm { background: linear-gradient(160deg, #0c1220 0%, #052e1c 100%); border: 1px solid rgba(34,197,94,0.2); }
.t-nm .r-num   { color: #86efac; }
.t-nm .r-badge { background: rgba(34,197,94,0.12); color: #86efac; border: 1px solid rgba(34,197,94,0.25); }

/* Overweight */
.t-ow { background: linear-gradient(160deg, #0c1220 0%, #2d1b00 100%); border: 1px solid rgba(245,158,11,0.2); }
.t-ow .r-num   { color: #fcd34d; }
.t-ow .r-badge { background: rgba(245,158,11,0.12); color: #fcd34d; border: 1px solid rgba(245,158,11,0.25); }

/* Obese */
.t-ob { background: linear-gradient(160deg, #0c1220 0%, #2d0808 100%); border: 1px solid rgba(239,68,68,0.2); }
.t-ob .r-num   { color: #fca5a5; }
.t-ob .r-badge { background: rgba(239,68,68,0.12); color: #fca5a5; border: 1px solid rgba(239,68,68,0.25); }

/* ─── Stats Row ────────────────────────── */
.stats {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0.6rem;
    margin-bottom: 0.875rem;
}
.stat-box {
    background: #10111a;
    border: 1px solid #1c1e2d;
    border-radius: 16px;
    padding: 1.1rem 0.75rem;
    text-align: center;
}
.stat-n {
    display: block;
    font-size: 1.35rem;
    font-weight: 700;
    color: #f9fafb;
    letter-spacing: -0.02em;
    line-height: 1;
    margin-bottom: 0.35rem;
}
.stat-l {
    display: block;
    font-size: 0.62rem;
    font-weight: 600;
    color: #374151;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}

/* ─── Scale ────────────────────────────── */
.scale-bar {
    width: 100%;
    height: 6px;
    border-radius: 3px;
    background: linear-gradient(90deg,
        #3b82f6 0%,  #3b82f6 30%,
        #22c55e 30%, #22c55e 55%,
        #f59e0b 55%, #f59e0b 75%,
        #ef4444 75%, #ef4444 100%);
    position: relative;
    margin: 1rem 0 0.6rem;
}
.scale-dot {
    position: absolute;
    top: 50%;
    transform: translate(-50%, -50%);
    width: 18px;
    height: 18px;
    background: #fff;
    border-radius: 50%;
    border: 3px solid #07080f;
    box-shadow: 0 0 0 3px rgba(255,255,255,0.18);
}
.scale-tags {
    display: flex;
    justify-content: space-between;
    margin-top: 0.4rem;
}
.s-tag {
    font-size: 0.6rem;
    font-weight: 500;
    color: #374151;
}

/* ─── Ideal block ──────────────────────── */
.ideal-row {
    display: flex;
    align-items: center;
    gap: 0.875rem;
    background: rgba(34,197,94,0.05);
    border: 1px solid rgba(34,197,94,0.12);
    border-radius: 14px;
    padding: 1rem 1.25rem;
    margin-top: 1.25rem;
}
.ideal-icon { font-size: 1.3rem; flex-shrink: 0; }
.ideal-text {
    font-size: 0.88rem;
    color: #6b7280;
    line-height: 1.55;
}
.ideal-text b { color: #4ade80; font-weight: 600; }

/* ─── Tips ─────────────────────────────── */
.tip-list { display: flex; flex-direction: column; gap: 0.5rem; }
.tip-row {
    display: flex;
    align-items: flex-start;
    gap: 0.875rem;
    padding: 1rem 1.1rem;
    background: #07080f;
    border: 1px solid #1c1e2d;
    border-radius: 14px;
}
.tip-dot {
    width: 7px; height: 7px;
    border-radius: 50%;
    background: #6366f1;
    flex-shrink: 0;
    margin-top: 0.42rem;
}
.tip-text {
    font-size: 0.88rem;
    color: #6b7280;
    line-height: 1.6;
}

/* ─── Footer ───────────────────────────── */
.foot {
    text-align: center;
    padding: 2.5rem 0 0;
    font-size: 0.72rem;
    color: #1f2937;
    letter-spacing: 0.04em;
}
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-pill">◎ Health Tool</div>
    <div class="hero-h1">Kalkulator <em>BMI</em></div>
    <div class="hero-p">
        Hitung Indeks Massa Tubuh Anda dan dapatkan gambaran kondisi kesehatan secara instan.
    </div>
</div>
""", unsafe_allow_html=True)

# ── Inputs ────────────────────────────────────────────────────────────────────
st.markdown('<div class="card"><div class="card-label">Data Anda</div>', unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    berat  = st.number_input("Berat Badan (kg)",  min_value=10.0,  max_value=300.0, value=65.0,  step=0.5, format="%.1f")
with c2:
    tinggi = st.number_input("Tinggi Badan (cm)", min_value=50.0,  max_value=280.0, value=170.0, step=0.5, format="%.1f")
st.markdown("</div>", unsafe_allow_html=True)

# ── Calculation ───────────────────────────────────────────────────────────────
bmi       = berat / ((tinggi / 100) ** 2)
bmi_r     = round(bmi, 1)
bmi_pos   = round(min(max((bmi - 10) / 30 * 100, 1), 99), 1)
ideal_min = round(18.5  * ((tinggi / 100) ** 2), 1)
ideal_max = round(24.99 * ((tinggi / 100) ** 2), 1)

if bmi < 18.5:
    theme, status = "t-uw", "Kekurangan Berat Badan"
    tips = [
        "Tambah kalori dari sumber bergizi: telur, alpukat, kacang-kacangan, dan daging tanpa lemak.",
        "Makan 5–6 kali sehari dengan porsi lebih kecil agar lebih mudah dicerna tubuh.",
        "Latihan beban ringan 2–3 kali seminggu untuk membangun massa otot secara bertahap.",
        "Diskusikan program penambahan berat badan Anda bersama dokter atau ahli gizi.",
    ]
elif bmi <= 24.99:
    theme, status = "t-nm", "Berat Badan Ideal"
    tips = [
        "Pertahankan pola makan seimbang: protein berkualitas, serat, dan karbohidrat kompleks.",
        "Olahraga rutin minimal 150 menit per minggu — jalan, lari, bersepeda, atau renang.",
        "Tidur 7–9 jam per malam untuk mendukung pemulihan dan keseimbangan hormon.",
        "Pantau berat badan tiap 2–4 minggu agar tetap berada di rentang sehat.",
    ]
elif bmi <= 29.99:
    theme, status = "t-ow", "Kelebihan Berat Badan"
    tips = [
        "Kurangi gula tambahan dan makanan ultra-proses secara bertahap, bukan sekaligus.",
        "Ganti camilan dengan buah, kacang, atau yogurt rendah lemak untuk kontrol kalori.",
        "Jalan cepat 30 menit setiap hari adalah langkah awal yang sangat efektif.",
        "Catat asupan makanan harian — kesadaran adalah kunci perubahan kebiasaan.",
    ]
else:
    theme, status = "t-ob", "Obesitas"
    tips = [
        "Konsultasikan dengan dokter terlebih dahulu untuk penanganan yang tepat dan aman.",
        "Terapkan defisit kalori bertahap di bawah pengawasan profesional — jangan terburu-buru.",
        "Mulai berjalan 10–15 menit per hari dan tingkatkan secara perlahan seiring waktu.",
        "Pantau tekanan darah, gula darah, dan kolesterol secara rutin bersama tenaga medis.",
    ]

# gap
if berat < ideal_min:
    gap_str, gap_lbl = f"−{round(ideal_min - berat, 1)}", "Kurang (kg)"
elif berat > ideal_max:
    gap_str, gap_lbl = f"+{round(berat - ideal_max, 1)}", "Lebih (kg)"
else:
    gap_str, gap_lbl = "±0", "Dalam Ideal"

# ── Button ────────────────────────────────────────────────────────────────────
go = st.button("Hitung BMI Saya →", use_container_width=True)

if go:
    if theme == "t-nm":
        st.balloons()

    st.markdown('<div class="results">', unsafe_allow_html=True)

    # ── Result hero card
    st.markdown(f"""
    <div class="r-card {theme}">
        <div class="r-eyebrow">Indeks Massa Tubuh</div>
        <div class="r-num">{bmi_r}</div>
        <span class="r-badge">{status}</span>
    </div>
    """, unsafe_allow_html=True)

    # ── Stats
    st.markdown(f"""
    <div class="stats">
        <div class="stat-box">
            <span class="stat-n">{bmi_r}</span>
            <span class="stat-l">Nilai BMI</span>
        </div>
        <div class="stat-box">
            <span class="stat-n" style="font-size:1.05rem">{ideal_min}–{ideal_max}</span>
            <span class="stat-l">Rentang Ideal</span>
        </div>
        <div class="stat-box">
            <span class="stat-n">{gap_str}</span>
            <span class="stat-l">{gap_lbl}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Scale card
    st.markdown(f"""
    <div class="card">
        <div class="card-label">Posisi di Skala BMI</div>
        <div class="scale-bar">
            <div class="scale-dot" style="left:{bmi_pos}%"></div>
        </div>
        <div class="scale-tags">
            <span class="s-tag">Kurus &lt;18.5</span>
            <span class="s-tag">Normal 18.5–24.9</span>
            <span class="s-tag">Gemuk 25–29.9</span>
            <span class="s-tag">Obesitas ≥30</span>
        </div>
        <div class="ideal-row">
            <div class="ideal-icon">⚖</div>
            <div class="ideal-text">
                Untuk tinggi <b>{tinggi} cm</b>, berat badan ideal Anda
                berada di <b>{ideal_min} – {ideal_max} kg</b>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Tips card
    tips_html = "".join(
        f'<div class="tip-row"><div class="tip-dot"></div><div class="tip-text">{t}</div></div>'
        for t in tips
    )
    st.markdown(f"""
    <div class="card">
        <div class="card-label">Rekomendasi</div>
        <div class="tip-list">{tips_html}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown('<div class="foot">BMI Calculator &nbsp;·&nbsp; Dibuat dengan Streamlit</div>', unsafe_allow_html=True)