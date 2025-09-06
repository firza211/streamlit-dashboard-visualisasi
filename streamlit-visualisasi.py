import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Atur tema plotting untuk grafik yang lebih menarik
sns.set_theme(style="whitegrid")

# Nama file excel
FILE_NAME = "data_kuisioner.xlsx"

# Fungsi untuk memuat data
def load_data():
    if os.path.exists(FILE_NAME):
        return pd.read_excel(FILE_NAME)
    else:
        # Membuat DataFrame kosong dengan struktur kolom yang benar
        columns = ["Nama", "Jenis Kelamin", "Umur", "Sudah Pernah"] + \
                  [f"P{i}" for i in range(1, 5)] + \
                  [f"Q{i}" for i in range(1, 5)] + \
                  [f"R{i}" for i in range(1, 5)] + \
                  [f"S{i}" for i in range(1, 5)] + \
                  [f"T{i}" for i in range(1, 5)] + \
                  [f"U{i}" for i in range(1, 5)]
        return pd.DataFrame(columns=columns)

# Fungsi interpretasi skor
def interpretasi_skor(rk):
    if 1.00 <= rk <= 1.80:
        return "Sangat Tidak Puas"
    elif 1.81 <= rk <= 2.60:
        return "Tidak Puas"
    elif 2.61 <= rk <= 3.40:
        return "Cukup Puas"
    elif 3.41 <= rk <= 4.20:
        return "Puas"
    else:
        return "Sangat Puas"

# Muat data di awal
df = load_data()

# ---------------- SIDEBAR MENU ----------------
st.sidebar.title("📌 Menu")
menu = st.sidebar.radio("Pilih Halaman:", ["📝 Isi Kuisioner", "📊 Analisis Data"])

# ---------------- HALAMAN FORM ----------------
if menu == "📝 Isi Kuisioner":
    st.title("Kuisioner Kepuasan Pengguna Website Codashop")
    st.subheader("Pendekatan Metode PIECES dan Visualisasi Data")
    st.write("---")


    st.markdown("""
    Assalamualaikum warahmatullahi wabarakatuh,

    Perkenalkan, saya **Muhammad Firza Nauvaldhi**, mahasiswa Program Studi Sistem Informasi, Fakultas Ilmu Komputer dan Teknologi Informasi, Universitas Gunadarma.

    Saat ini, saya sedang melakukan penelitian untuk tugas akhir (skripsi) dengan judul:
    **"Analisis Kepuasan Pengguna Website Codashop: Pendekatan Metode PIECES dan Visualisasi Data"**

    Penelitian ini bertujuan untuk menganalisis tingkat kepuasan Anda sebagai pengguna terhadap website Codashop berdasarkan kerangka PIECES (*Performance, Information, Economy, Control, Efficiency, Service*).
    > Link Website: [www.codashop.com](https://www.codashop.com)

    Sehubungan dengan hal tersebut, saya memohon kesediaan Bapak/Ibu/Saudara/i untuk meluangkan waktu sekitar 5-10 menit guna mengisi kuesioner ini. Seluruh data dan informasi yang Anda berikan akan **dijamin kerahasiaannya** dan hanya akan digunakan untuk kepentingan akademis.

    Atas bantuan, partisipasi, dan waktu yang telah diluangkan, saya ucapkan terima kasih yang sebesar-besarnya.

    Wassalamualaikum warahmatullahi wabarakatuh.
    """)
    st.write("---")

    # Data responden
    st.subheader("Data Responden")
    nama = st.text_input("Nama")
    jk = st.radio("Jenis Kelamin", ["Laki-Laki", "Perempuan"])
    umur = st.selectbox("Umur", ["12 - 16 Tahun", "17 - 25 Tahun", "26 - 35 Tahun", "35 - 45 Tahun"])
    pernah = st.radio("Apakah Anda sudah pernah menggunakan layanan Codashop sebelumnya?", ["Pernah", "Tidak Pernah"])

    st.markdown("""
    **Petunjuk Pengisian:**
    Pilihlah salah satu angka pada skala penilaian yang paling sesuai dengan pendapat Anda untuk setiap pernyataan di bawah ini.
    - **1 = Sangat Tidak Setuju**
    - **2 = Tidak Setuju**
    - **3 = Netral**
    - **4 = Setuju**
    - **5 = Sangat Setuju**
    """)

    # ---- Bagian Pertanyaan PIECES ----
    st.write("---")

    pertanyaan_P = [
        "Website Codashop dapat diakses dengan cepat.",
        "Proses pemrosesan transaksi (top-up) di Codashop berjalan dengan cepat.",
        "Navigasi antar halaman di website Codashop terasa lancar dan responsif.",
        "Website jarang mengalami error atau kegagalan sistem saat menggunakan Codashop."
    ]
    pertanyaan_Q = [
        "Informasi mengenai produk (item game, diamond, dll.) yang dijual disajikan secara jelas dan akurat.",
        "Daftar harga dan rincian metode pembayaran yang tersedia di Codashop mudah untuk dipahami.",
        "Instruksi atau langkah-langkah untuk melakukan top-up sangat jelas dan mudah diikuti.",
        "Informasi yang saya terima setelah transaksi berhasil (bukti pembayaran) sudah relevan dan memadai."
    ]
    pertanyaan_R = [
        "Harga yang ditawarkan oleh Codashop kompetitif jika dibandingkan dengan platform sejenis lainnya.",
        "Website Codashop memberikan manfaat ekonomi melalui berbagai promosi, diskon, atau cashback.",
        "Biaya yang saya keluarkan sepadan dengan kemudahan dan kecepatan layanan yang saya dapatkan.",
        "Menggunakan Codashop membantu saya menghemat waktu dan usaha dalam melakukan pembelian item digital."
    ]
    pertanyaan_S = [
        "Saya merasa data pribadi (seperti User ID Game) yang saya masukkan di website Codashop aman.",
        "Proses pembayaran yang terhubung dengan mitra (e-wallet, transfer bank, dll.) terasa aman dan terpercaya.",
        "Website Codashop memberikan kontrol yang baik bagi saya untuk memeriksa kembali pesanan sebelum membayar.",
        "Proses pembayaran di website Codashop memberikan saya rasa aman dari potensi transaksi yang tidak sah."
    ]
    pertanyaan_T = [
        "Langkah-langkah untuk melakukan top-up di Codashop sangat ringkas dan tidak berbelit-belit.",
        "Waktu yang saya butuhkan untuk menyelesaikan satu transaksi dari awal hingga akhir sangat singkat.",
        "Desain antarmuka (tampilan) website Codashop membuat proses top-up menjadi lebih efisien.",
        "Struktur dan navigasi website Codashop dirancang secara jelas sehingga saya tidak kesulitan mencari produk."
    ]
    pertanyaan_U = [
        "Website Codashop menyediakan layanan pelanggan (customer service) yang mudah untuk dihubungi jika terjadi masalah.",
        "Informasi bantuan atau FAQ (Frequently Asked Questions) yang tersedia di website cukup membantu.",
        "Kualitas penanganan keluhan atau masalah oleh tim layanan website Codashop sudah baik.",
        "Website Codashop memberikan kesan bahwa mereka akan merespons keluhan pelanggan dengan baik."
    ]

    st.subheader("Bagian P - Performance")
    P = [st.radio(pertanyaan, [1,2,3,4,5], key=pertanyaan, horizontal=True) for pertanyaan in pertanyaan_P]

    st.subheader("Bagian Q - Information")
    Q = [st.radio(pertanyaan, [1,2,3,4,5], key=pertanyaan, horizontal=True) for pertanyaan in pertanyaan_Q]

    st.subheader("Bagian R - Economy")
    R = [st.radio(pertanyaan, [1,2,3,4,5], key=pertanyaan, horizontal=True) for pertanyaan in pertanyaan_R]

    st.subheader("Bagian S - Control & Security")
    S = [st.radio(pertanyaan, [1,2,3,4,5], key=pertanyaan, horizontal=True) for pertanyaan in pertanyaan_S]

    st.subheader("Bagian T - Efficiency")
    T = [st.radio(pertanyaan, [1,2,3,4,5], key=pertanyaan, horizontal=True) for pertanyaan in pertanyaan_T]

    st.subheader("Bagian U - Service")
    U = [st.radio(pertanyaan, [1,2,3,4,5], key=pertanyaan, horizontal=True) for pertanyaan in pertanyaan_U]

    # Tombol simpan
    if st.button("💾 Simpan Jawaban"):
        if not nama:
            st.warning("Nama wajib diisi.")
        else:
            new_data = pd.DataFrame([[nama, jk, umur, pernah] + P + Q + R + S + T + U], columns=df.columns)
            df = pd.concat([df, new_data], ignore_index=True)
            df.to_excel(FILE_NAME, index=False)
            st.success("Jawaban Anda berhasil disimpan! Terima kasih telah berpartisipasi.")

# ---------------- HALAMAN ANALISIS ----------------
else:
    st.title("📊 Analisis Kepuasan Pengguna Website Codashop")
    st.subheader("Pendekatan Metode PIECES")

    if 'df' in locals() and not df.empty:
        df.columns = df.columns.str.strip()

        aspek = {
            "Performance": [f"P{i}" for i in range(1,5)],
            "Information": [f"Q{i}" for i in range(1,5)],
            "Economy": [f"R{i}" for i in range(1,5)],
            "Control & Security": [f"S{i}" for i in range(1,5)],
            "Efficiency": [f"T{i}" for i in range(1,5)],
            "Service": [f"U{i}" for i in range(1,5)],
        }

        hasil = []
        for asp, cols in aspek.items():
            valid_cols = [col for col in cols if col in df.columns]
            if not valid_cols:
                continue

            total_skor_jsk = df[valid_cols].sum().sum()
            rata_rata_skor_rk = df[valid_cols].mean(axis=1).mean()
            
            # Gunakan interpretasi skor, bukan persen puas
            keterangan = interpretasi_skor(rata_rata_skor_rk)

            hasil.append([asp, total_skor_jsk, rata_rata_skor_rk, keterangan])

        df_hasil = pd.DataFrame(hasil, columns=["Variabel", "Total Skor (JSK)", "Rata-rata Skor (RK)", "Keterangan"])

        st.subheader("📑 Tabel Ringkasan Hasil Analisis")
        st.dataframe(df_hasil.style.format({
            "Total Skor (JSK)": "{:d}",
            "Rata-rata Skor (RK)": "{:.3f}"
        }))

        st.subheader("📈 Rata-rata Skor Kepuasan per Variabel")
        df_hasil_sorted = df_hasil.sort_values("Rata-rata Skor (RK)", ascending=False)
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x="Rata-rata Skor (RK)", y="Variabel", data=df_hasil_sorted, palette="viridis", orient='h', ax=ax)
        ax.set_xlim(0,5)
        ax.set_ylabel("Variabel PIECES")
        ax.set_xlabel("Rata-rata Skor (Skala 1-5)")
        for container in ax.containers:
            ax.bar_label(container, fmt='%.3f')
        st.pyplot(fig)
        
        with st.expander("Lihat Interpretasi Skor"):
            st.info("""
            **Interpretasi Skor Rata-Rata:**
            - **1.00 - 1.80**: Sangat Tidak Puas
            - **1.81 - 2.60**: Tidak Puas
            - **2.61 - 3.40**: Cukup Puas
            - **3.41 - 4.20**: Puas
            - **4.21 - 5.00**: Sangat Puas
            """)

        st.subheader("📋 Daftar Jawaban Responden")
        with st.expander("Klik untuk melihat data mentah"):
            kolom_identitas = ["Nama", "Umur", "Jenis Kelamin", "Sudah Pernah"]
            valid_identitas = [col for col in kolom_identitas if col in df.columns]
            cols_ordered = valid_identitas + [col for col in df.columns if col not in valid_identitas]
            st.dataframe(df[cols_ordered], use_container_width=True)

    else:
        st.warning("Belum ada data responden. Silakan isi kuisioner terlebih dahulu pada halaman '📝 Isi Kuisioner'.")
