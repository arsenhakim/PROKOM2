import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats

# Mengatur tema Streamlit
st.set_page_config(layout="wide")
st.header('Website Pengujian Korelasi')

# Fungsi untuk menghasilkan data acak
def generate_data(n):
    np.random.seed(0)
    data1 = np.random.randn(n)
    data2 = np.random.randn(n)
    df = pd.DataFrame({'Data1': data1, 'Data2': data2})
    return df

# Memuat data dari file CSV
def load_data(file):
    try:
        data = pd.read_csv(file)
        return data
    except:
        st.error("Gagal memuat file. Pastikan format file adalah CSV.")

# Pilihan untuk mengunggah data atau menghasilkan data acak
data_option = st.radio('Pilih sumber data:', ('Upload File', 'Generate Random Data'))

# Inisialisasi variabel data
data = pd.DataFrame()

# Jika memilih 'Upload File'
if data_option == 'Upload File':
    file = st.file_uploader('Unggah file CSV', type=['csv'])
    if file is not None:
        data = load_data(file)

# Jika memilih 'Generate Random Data'
else:
    n = st.number_input('Jumlah data:', min_value=10, max_value=1000, step=10, value=100)
    data = generate_data(n)

# Menampilkan data jika data tersedia
if not data.empty:
    # Menampilkan data
    st.title('Pengujian Korelasi')
    st.subheader('Data')
    st.dataframe(data)

    # Menentukan hipotesis
    st.subheader('Hipotesis')
    st.write('H0: Tidak terdapat korelasi antara Data1 dan Data2')
    st.write('H1: Terdapat korelasi antara Data1 dan Data2')

    # Uji Korelasi (Pearson's correlation)
    st.subheader('Uji Korelasi')
    corr_coef, p_value = stats.pearsonr(data['Data1'], data['Data2'])
    st.write(f"Koefisien Korelasi: {corr_coef}")
    st.write(f"P-Value: {p_value}")
    alpha = 0.05
    st.write("Tingkat signifikansi: ", str(alpha))
    # Menarik kesimpulan
    
    st.subheader('Kesimpulan')
    if p_value < alpha:
        st.write("Tolak H0 karena p-value < alpha")
        st.write("Terdapat korelasi yang signifikan antara Data1 dan Data2.")
    else:
        st.write("Gagal tolak H0 karena p-value >= alpha")
        st.write("""Dengan menggunakan tingkat kepercayaan sebesar 95% didapatkan hasil pengujian korelasi
        tidak terdapat korelasi yang signifikan antara Data1 dan Data2.
        """)
else:
    st.info("Upload File anda terlebih dahulu untuk melanjutkan (disarankan file yang akan diupload hanya berisi data variabel X dan variabel Y)")