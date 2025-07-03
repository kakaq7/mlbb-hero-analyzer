import pandas as pd
import streamlit as st

st.title("📊 MLBB Hero Win Rate Analyzer")
st.markdown("Analisis hero berdasarkan win rate dan jumlah match untuk push rank solo.")

# Input data manual
hero_data = st.text_area("Masukkan data hero (format: Hero, Win Rate %, Match Count):", 
"""Irithel, 44.5, 155
Popol & Kupa, 23.1, 13
Lesley, 36.4, 11
Wanwan, 50.0, 10
Layla, 100.0, 1""")

if hero_data:
    lines = hero_data.strip().split("\n")
    data = []
    for line in lines:
        try:
            hero, win_rate, match_count = [x.strip() for x in line.split(",")]
            data.append({
                'Hero': hero,
                'Win Rate (%)': float(win_rate),
                'Match Count': int(match_count)
            })
        except:
            st.error(f"Format salah di baris: {line}")

    df = pd.DataFrame(data)

    st.subheader("📈 Data Hero")
    st.dataframe(df.sort_values(by='Win Rate (%)', ascending=False), use_container_width=True)

    st.subheader("✅ Rekomendasi Push Rank (Detail)")
    for _, row in df.iterrows():
        hero = row['Hero']
        win_rate = row['Win Rate (%)']
        match_count = row['Match Count']

        if match_count < 5:
            status = "⚪ Data tidak cukup (mainkan lagi)"
            insight = f"{hero} baru dimainkan {match_count} kali. Perlu lebih banyak data untuk memastikan apakah hero ini cocok untuk push."
        elif win_rate >= 55:
            status = "🟢 Sangat disarankan untuk push"
            insight = f"{hero} memiliki win rate tinggi ({win_rate:.1f}%) dari {match_count} match. Cocok dijadikan andalan untuk push solo."
        elif win_rate >= 50:
            status = "🟡 Coba rotasi untuk push"
            insight = f"{hero} cukup seimbang dengan win rate {win_rate:.1f}%. Masih bisa diandalkan, tapi perlu hati-hati."
        elif win_rate >= 40:
            status = "🔸 Perlu evaluasi lebih lanjut"
            insight = f"{hero} berada di bawah win rate ideal. Sebaiknya uji kembali atau evaluasi gaya main."
        else:
            status = "🔴 Hindari push dengan hero ini"
            insight = f"{hero} punya win rate rendah ({win_rate:.1f}%). Tidak disarankan untuk push, kecuali kamu yakin dengan performanya."

        st.markdown(f"### {hero} — {status}")
        st.markdown(insight)
        st.markdown("---")

    st.markdown("Made with ❤️ for solo rankers")
￼Enter
