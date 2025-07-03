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

    st.subheader("✅ Rekomendasi Push Rank")
    for _, row in df.iterrows():
        hero = row['Hero']
        win_rate = row['Win Rate (%)']
        match_count = row['Match Count']

        if match_count < 5:
            status = "⚪ Data tidak cukup (mainkan lagi)"
        elif win_rate >= 55:
            status = "🟢 Sangat disarankan untuk push"
        elif win_rate >= 50:
            status = "🟡 Coba rotasi untuk push"
        elif win_rate >= 40:
            status = "🔸 Perlu hati-hati, evaluasi lebih lanjut"
        else:
            status = "🔴 Hindari push dengan hero ini"

        st.write(f"**{hero}** — {win_rate:.1f}% win rate dari {match_count} match → {status}")

    st.markdown("---")
    st.markdown("Made with ❤️ for solo rankers")