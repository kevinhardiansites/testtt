#import libraries
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import altair as alt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

#interface
st.set_page_config(
    page_title="5 Juta Bayi Meninggal Setiap Tahun",
    layout="centered"
)

#Header
ct1 = st.container()
with ct1:
    st.header('**5 Juta Bayi Meninggal Setiap Tahun** : Apa Penyebabnya?')
    st.markdown('[Muhamad Faridi Dahlan] --- [TETRIS Program Batch IV]')
st.markdown('\n')

# Page of my web
def on_change(key):
    selection = st.session_state[key]
#Navigation bar
selected5 = option_menu(None, ["Pendahuluan", "Data & Metode","Analisa", "Diskusi"],
                        icons=['journal', 'file-spreadsheet', 'graph-up', "chat-left-text"],
                        on_change=on_change, key='menu_5', orientation="vertical")
#Pendahuluan page
if selected5 == 'Pendahuluan':
    #section latar belakang
    st.markdown("## Latar Belakang")
    # Buat kolom
    col1, col2, col3 = st.columns(3)
    # Tampilkan gambar di kolom tengah
    with col1:
        image = r'image/anak percaya diri.jpg'
        st.image(image,caption='Gambar 1. Anak Indonesia',width=500)
    st.write("""**Kematian  atau  mortalitas**  adalah  salah  satu  dari  tiga komponen proses demografi yang berpengaruh terhadap struktur penduduk. Tinggi rendahnya tingkat mortalitas pendudukan di suatu daerah tidak hanya mempengaruhi pertumbuhan penduduk, tetapi juga merupakan barometer dari tinggi rendahnya tingkat kesehatan masyarakat di daerah tersebut ([**Ibrahim,2023**](https://www.researchgate.net/publication/368642648_MORTALITAS))""")
    st.write("""Angka kematian anak menggambarkan kualitas pelayanan kesehatan sebagai indikator kesejahteraan negara 
    khususnya di Indonesia. Beberapa faktor yang berperan sebagai penyebab utama kematian adalah angka kemiskinan, remaja yang hamil, dan pendidikan ([**Sani,2020**](https://ejournal.fkm.unsri.ac.id/index.php/jikm/article/view/445))""")
    st.write("""Tingkat kematian anak-anak di bawah usia lima tahun atau balita secara global telah turun drastis hingga 61% sejak tahun 1990. Tingkat kematian pada balita kerap terjadi di negara yang memiliki penghasilan rendah.
    Menurut laporan UNICEF, terdapat **37 kematian anak usia di bawah lima tahun dari 1.000 kelahiran pada 2020**. Angka tersebut turun dibandingkan tahun 2015 yang sebanyak 43 kematian ([**Katadata,2020**](https://databoks.katadata.co.id/datapublish/2021/12/21/unicef-tingkat-kematian-anak-di-bawah-5-tahun-secara-global-turun-drastis))""")
    st.write("""Update terbaru dari UNICEF juga melaporkan, sekitar total **5 juta anak balita meninggal pada tahun 2021 di dunia** ([**UNICEF,2023**](https://data.unicef.org/topic/child-survival/under-five-mortality/))""")
    st.write("""Inilah yang menjadi alasan penulis ingin melakukan analisa lebih lanjut. Adapun tujuan dari analisa adalah untuk melihat apakah ada keterkaitan antara faktor-faktor (korelasi pendidikan, fertilitas remaja, kesenjangan kemiskinan) tersebut dengan mortalitas anak balita terkhusus di Indonesia. Semoga dengan project ini bisa menjadi pertimbangan bagi stakeholders maupun pemerintah untuk mengurangi mortalitas balita di Indonesia""")
    st.write('-'*100)
    #Section Kondisi Mortalitas Anak Dunia
    st.markdown("## Kondisi Mortalitas Anak Dunia")
    st.write("""Berdasarkan jurnal WHO, Kematian balita semakin terkonsentrasi di Afrika sub-Sahara dan Asia Selatan, sementara proporsi di 
di seluruh dunia turun dari 32% pada tahun 1990 menjadi 18% pada tahun 2013. Anak-anak berisiko lebih besar meninggal sebelum usia 5 tahun jika mereka 
lahir di daerah pedesaan, rumah tangga miskin, atau dari ibu yang 
tidak mendapatkan pendidikan dasar ([**WHO Journal,2014**](https://apps.who.int/iris/bitstream/handle/10665/242265/WER8938_418-420.PDF))""")
    st.write("")
    #inputting grafik
    st.write("""Grafik di bawah ini menunjukkan mortalitas balita (dibawah 5 tahun) per 1000 kelahiran dari tahun ke tahun diseluruh dunia""")
    #olah data csv
    df_year = pd.read_csv(r'dataset-streamlit/yoy_mortality.csv')
    fig = px.line(data_frame=df_year,x=df_year['Year(s)'],y=df_year['mortality'])
    fig.update_layout(title="Grafik 1  Median Mortalitas Balita Dibawah 5 Tahun (per 1000 kelahiran)")
    st.plotly_chart(fig)
    st.write("Dari grafik menunjukkan adanya tanda positif bagi seluruh dunia, dikarenakan semakin menurunnya angka mortalitas balita")
    st.write('-'*100)
    #section rumusan masalah
    st.markdown("## Rumusan Masalah")
    st.write("1. Bagaimana capaian parameter mortalitas balita di Indonesia saat ini dan pada masa lalu jika dibandingkan dengan negara lain di ASEAN?")
    st.write("2. Bagaimana korelasi pendidikan, fertilitas remaja, kesenjangan kemiskinan terhadap mortalitas balita di Indonesia?")
    st.write('-'*100)
    #section batasan masalah
    st.markdown("## Batasan Masalah")
    st.write("1. Data yang akan dibandingkan adalah antara data mortalitas balita Indonesia dengan negara ASEAN lain")
    st.write("2. Tahun pada grafik yang disajikan akan menyesuaikan ketersediaan data dari sumber")
#data and metode page
elif selected5 == 'Data & Metode':
    #sumber data section
    st.markdown("## Sumber Data")
    st.write("Sumber dataset yang saya dapatkan adalah sebagai berikut :")
    #input sumber dataset web
    st.write("1. [**Under-five mortality, for both sexes combined (deaths under age five per 1,000 live births)**](https://data.un.org/Data.aspx?d=PopDiv&f=variableID%3A80)")
    st.write("2. [**Adolescent fertility rate (births per 1,000 women ages 15-19)**](https://data.worldbank.org/indicator/SP.ADO.TFRT)")
    st.write("3. [**Poverty gap at $2.15 a day (2017 PPP) (%)**](https://data.worldbank.org/indicator/SI.POV.GAPS)")
    st.write("4. [**School life expectancy (years). Primary to secondary education (ISCED 1 to 3)**](https://data.un.org/Data.aspx?d=UNESCO&f=series:SLE_123)")
    st.write('-'*100)
    #penjelasan dataset section
    st.markdown("## Penjelasan Dataset")
    st.write("""1. **Under-five mortality, for both sexes combined (deaths under age five per 1,000 live births)** : Probabilitas kematian antara kelahiran dan usia 5 tahun. Dinyatakan sebagai kematian per 1.000 kelahiran. Semakin tinggi mortality,menandakan semakin tinggi angka kematian balita""")
    st.write("""2. **Adolescent fertility rate (births per 1,000 women ages 15-19)** : Tingkat kesuburan spesifik usia yang memberikan ukuran dasar kesehatan reproduksi yang berfokus pada kelompok perempuan remaja yang rentan. Semakin tinggi fertility,menandakan semakin tinggi angka kehamilan pada usia 15-19 tahun""")
    st.write("""3. **Poverty gap at \$2.15 a day (2017 PPP) (%)** : Ukuran yang mencerminkan kedalaman kemiskinan serta kejadiannya.Ukuran ini menunjukkan rata−rata kekurangan pendapatan atau konsumsi dari garis kemiskinan sebesar 2,15 dollar per hari, yang dinyatakan sebagai persentase dari garis kemiskinan tersebut. Semakin tinggi poverty, semakin dalam kemiskinan di negara tersebut""")
    st.write("""4. **School life expectancy (years). Primary to secondary education (ISCED 1 to 3)** : Jumlah total tahun sekolah yang dapat diharapkan diterima oleh seorang anak, yang mencakup pendidikan dasar hingga menengah (ISCED 1 hingga 3). [ISCED : 1 Primary Education , 2 Lower Secondary Education , 3 Upper Secondary Education]""")
    st.write('-'*100)
    #tahap pengerjaan project section
    st.markdown("## Tahap Pengerjaan Project")
    st.image('image/Mencari Dataset Trekait.png', caption='Gambar 2. Proses Tahapan Pengerjaan' )
#analisa page
elif selected5 == 'Analisa':
    #analisa 1 section
    st.markdown("## Analisa 1 : Perbandingan Mortalitas Balita di Indonesia Dengan Negara ASEAN")
    #olah data csv
    df_morasean_2022 = pd.read_csv('dataset-streamlit/mortality_2022.csv')
    colors = ['lightslategray',] * 10
    colors[5] = 'red'
    df_morasean_2022.rename(columns={'Country or Area': 'Country'}, inplace=True)
    #buat bar chart dengan plotly
    fig_indo = go.Figure(data=[go.Bar(
    x=df_morasean_2022['Value'],
    y=df_morasean_2022['Country'],
    orientation ='h',
    marker_color=colors # marker color can be a single color value or an iterable
    )])
    fig_asean = go.Figure(data=[go.Bar(
    x=df_morasean_2022['Value'],
    y=df_morasean_2022['Country'],
    orientation ='h'
    )])
    #dropdown menu
    negara = st.selectbox(
    "Pilihan Grafik 2 : Indonesia/ASEAN",
    ['ASEAN','Indonesia']
    )
    if negara == "Indonesia":
        fig_indo.update_layout(title_text="Grafik 2.1  Perbandingan Mortalitas Balita di Indonesia Dengan Negara ASEAN Lain (Tahun 2022)")
        st.plotly_chart(fig_indo)
    else :
        fig_asean.update_layout(title="Grafik 2.2  Perbandingan Mortalitas Balita diantara Negara ASEAN (Tahun 2022)")
        st.plotly_chart(fig_asean)
    st.write("""Berdasarkan grafik di atas,pada tahun 2022 kita masih memiliki nilai mortalitas yang cukup tinggi. Dengan angka 21 kematian balita per 1000 kelahiran (peringkat 5 di ASEAN). Hal ini tentu bisa menjadi sebuah evaluasi bagi kita agar bisa menurunkan angka tersebut di tahun kedepannya. Pemerintah ataupun stakeholders terkait perlu mengkaji mengenai isu yang berkaitan dengan kesejahteraan ini. Kita mungkin bisa belajar dari negara Singapura yang mampu menjadi terbaik dalam menekan angka mortalitas balita""")
    st.write('-'*100)
    #analisa 2 section
    st.markdown("## Analisa 2 : Perbandingan Trend Mortalitas Balita (YoY) di Indonesia Dengan Negara ASEAN")
    #olah data csv
    df_trends = pd.read_csv('dataset-streamlit/trends.csv')
    df_trends.rename(columns={'Country or Area': 'Country'}, inplace=True)
    #buat line chart dengan plotly
    fig_asean_trends = px.line(df_trends, x="Year(s)", y="Value", color='Country')
    indonesia = df_trends[df_trends['Country']=='indonesia']
    malaysia = df_trends[df_trends['Country']=='malaysia']
    singapore = df_trends[df_trends['Country']=='singapore']
    thailand = df_trends[df_trends['Country']=='thailand']
    philippines = df_trends[df_trends['Country']=='philippines']
    myanmar = df_trends[df_trends['Country']=='myanmar']
    cambodia = df_trends[df_trends['Country']=='cambodia']
    vietnam = df_trends[df_trends['Country']=='viet nam']
    brunei = df_trends[df_trends['Country']=='brunei darussalam']
    lao = df_trends[df_trends['Country']=='lao people\'s democratic republic']
    # Define your dataset
    data = {
        "Tahun": df_trends['Year(s)'].unique(),
        "Indonesia": np.array(indonesia['Value']),  # First line (Indonesia)
        "Malaysia": np.array(malaysia['Value']),  # Second line (Malaysia)
        "Singapore": np.array(singapore['Value']), 
        "Thailand": np.array(thailand['Value']),
        "Philippines": np.array(philippines['Value']),
        "Myanmar": np.array(myanmar['Value']),
        "Cambodia": np.array(cambodia['Value']),
        "Vietnam": np.array(vietnam['Value']),
        "Brunei": np.array(brunei['Value']),
        "Lao": np.array(lao['Value'])      
    }
    df = pd.DataFrame(data)
    #buat lineplot
    fig_indo_trends = px.line(
        df,
        x="Tahun",
        y=["Indonesia", "Malaysia","Singapore","Thailand","Philippines","Myanmar","Cambodia","Vietnam","Brunei","Lao"],
        color_discrete_sequence=["red", "grey","grey","grey","grey","grey","grey","grey","grey","grey"]
    )
    #dropdown menu
    negara_2 = st.selectbox(
    "Pilihan Grafik 3 : Indonesia/ASEAN",
    ['ASEAN','Indonesia']
    )
    if negara_2 == "ASEAN":
        fig_asean_trends.update_layout(title_text="Grafik 3.1  Perbandingan Mortalitas Balita (YoY) Antarnegara di ASEAN")
        st.plotly_chart(fig_asean_trends)
    else :
        fig_indo_trends.update_layout(title_text="Grafik 3.2  Perbandingan Mortalitas Balita di Indonesia Dengan Negara ASEAN Lain (YoY)")
        st.plotly_chart(fig_indo_trends)
    st.write("""Semua negara di ASEAN memiliki kecenderungan turun dari tahun ke tahun sejak 1950. Jika kita lihat pada tahun 1950 an, kita masih memiliki nilai mortalitas balita yang begitu tinggi (304 kematian balita dari 1000 kelahiran), bahkan dibanding dengan negara Filipina. Namun, hingga era sekarang justru kita memiliki angka yang dibawah Filipina. Tetapi, hal menarik justru terjadi pada tahun 1965 di Indonesia. Kenaikan mortalitas yang terjadi diperkirakan karena kejadian [**krisis ekonomi di Indonesia pada tahun 1965**](https://www.kompasiana.com/andriaditya4909/60c4d36e8ede486c184ad382/krisis-ekonomi-1965-inflansi-tersebar-dalam-sejarah-indonesia) """)
    st.write('-'*100)
    #analisa 3 section
    st.markdown("## Analisa 3 : Apakah Ada Perbedaan Signifikan Antara Negara ASEAN?")
    st.write("""Pada section analisa 3 ini, kita akan melakukan uji statistik ANOVA untuk melihat apakah ada perbedaan signifikan antar grup negara di ASEAN dengan hipotesa""")
    st.write("""**Hipotesa Nol (H0)** : Tidak ada perbedaan signifikan mortalitas balita antar negara ASEAN""")
    st.write("""**Hipotesa Alternatif (Ha)** : Ada perbedaan signifikan mortalitas balita antar negara ASEAN""")
    #buat boxplot
    fig_asean_boxplot = px.box(df_trends, x="Country", y="Value",title="Grafik 4  Perbandingan Mortalitas Balita Antar Negara ASEAN (Secara Uji Statistik)")
    st.plotly_chart(fig_asean_boxplot)
    st.write("Kalau berdasarkan grafik boxplot diatas, kita mungkin melihat adanay beberapa negara yang memiliki perbedaan (seperti Singapura dan Lao). Namun, kita akan coba menghitung berdasar uji ANOVA")
    #lakukan analisa anova
    indonesia = df_trends[df_trends['Country']=='indonesia']
    malaysia = df_trends[df_trends['Country']=='malaysia']
    singapore = df_trends[df_trends['Country']=='singapore']
    thailand = df_trends[df_trends['Country']=='thailand']
    philippines = df_trends[df_trends['Country']=='philippines']
    myanmar = df_trends[df_trends['Country']=='myanmar']
    cambodia = df_trends[df_trends['Country']=='cambodia']
    vietnam = df_trends[df_trends['Country']=='viet nam']
    brunei = df_trends[df_trends['Country']=='brunei darussalam']
    lao = df_trends[df_trends['Country']=='lao people\'s democratic republic']
    y1 = indonesia['Value']
    y2 = malaysia['Value']
    y3 = singapore['Value']
    y4 = thailand['Value']
    y5 = philippines['Value']
    y6 = myanmar['Value']
    y7 = cambodia['Value']
    y8 = vietnam['Value']
    y9 = brunei['Value']
    y10 = lao['Value']
    anova = stats.f_oneway(y1,y2,y3,y4,y5,y6,y7,y8,y9,y10)
    #hasil analisa uji anova
    st.write("Berikut merupakan hasil uji ANOVA :")
    st.write(anova)
    st.write("**Insight** : Berdasarkan hasil diatas, bisa diartikan bahwa ada perbedaan mortalitas yang signifikan (setidaknya antar 1 negara dengan negara lain)")
    st.write("**Possible Cause** : Kemungkinan adanya perbedaan permasalahan mortalitas. Perlu kita lakukan lebih lanjut mengenai faktor kemungkinan penyebabnya")
    st.write("Seperti yang telah disebutkan pada halaman pendahuluan, kita bisa mengira jika faktor-faktor tersebut antara lain : korelasi pendidikan, fertilitas remaja, kesenjangan kemiskinan")
    st.write('-'*100)
    #analisa 4 section
    st.markdown("## Analisa 4 : Apakah Faktor (pendidikan, fertilitas remaja, kesenjangan kemiskinan) memiliki korelasi dengan mortalitas balita?")
    st.write("Apakah faktor-faktor yang telah disebutkan di section analisa 3 itu memang memiliki korelasi dengan mortalitas balita? sehingga menyebabkan antar negara memiliki perbedaan nilai mortalitasnya")
    df_correl = pd.read_csv('dataset-streamlit/correlation.csv')
    df_correl = df_correl.loc[:,['school_years','mortality_5','poverty_percentage','ferr_rate']]
    custom_cmap = sns.color_palette("coolwarm", as_cmap=True)
    corr = df_correl.corr()
    fig_correl, ax = plt.subplots()
    sns.heatmap(data=corr,cmap=custom_cmap,annot=True)
    st.pyplot(fig_correl)
    st.write("Kalau kita lihat dari grafik heatmap, terjadi korelasi yang cukup kuat antar semua variabel yang ada. Ini bisa menjadi acuan bahwa kemungkinan antar variabel memiliki korelasi yang kuat. Grafik heatmap ini juga menjadi bukti yang memperkuat [**Jurnal WHO tahun 2014**](https://apps.who.int/iris/bitstream/handle/10665/242265/WER8938_418-420.PDF). Meskipun, tentu ada faktor lainnya yang menyebabkan tinggi/rendahnya mortalitas balita")
else  :
    st.markdown("## Diskusi")
    st.image('image/nutritional-needs-child.jpg',caption="Gambar 3. Healthy Child", width=500)
    st.write("Sejauh ini, kita patut merasa senang. Dikarenakan mortalitas balita di Indonesia mengalami penurunan angka. Itu artinya kita sudah memilki fasilitas kesehatan yang baik dan pendidikan yang juga baik. Namun, kita tentu menginginkan trend ini terus menurun dari tahun ke tahun. Beberapa hal yang mungkin bisa kita lakukan adalah sebagai berikut :")
    st.write("**1. Memberikan pendidikan kelas pra nikah**")
    st.write("Ini berkaitan dengan pendidikan sebelum pernikahan. Penting bagi pasangan yang ingin melaksanakan pernikahan. Karena, paling tidak dengan memberi pendidikan kepada pasangan tersebut bisa mencegah dari hal-hal negatif yang mungkin akan ada dalam pernikahan. Bahkan, menurut sumber [**Kumparan**](https://kumparan.com/kumparannews/mengenal-kelas-pranikah-yang-akan-diwajibkan-bagi-pengantin-muslim-1sG8lRn2bgD/1) disebutkan bahwa akan kemungkinan diwajibkan untuk kelas pra nikah sebelum melaksanakan pernikahan")
    st.write("**2. Memberikan edukasi tentang bahaya kehamilan sebelum usia matang**")
    st.write("Kita sudah melihat dari korelasi antara fertilitas usia 15-19 tahun berbanding terbalik dengan mortalitas. Bisa dikatakan juga, bahwa semakin kecil fertilitas akan kemungkinan semakin kecil mortalitas. [**Alodokter**](https://www.alodokter.com/benarkah-hamil-di-usia-muda-dapat-membahayakan-kesehatan-ibu) menyebutkan ada 3 bahaya bagi ibu terkhusus jika hamil kurang dari usia matang menikah")
    st.write("**3. Meningkatkan kualitas pendidikan dan kesehatan**")
    st.write("Tidak hanya menyediakan akses ke pendidikan yang lebih baik, pemerintah juga harus meningkatkan kualitas pendidikan. Ini dapat dilakukan dengan mengembangkan kurikulum yang lebih baik, meningkatkan kualitas pengajaran, dan menyediakan fasilitas pendidikan yang memadai")
    st.write("Akses ke layanan kesehatan masih sangat terbatas di beberapa daerah di Indonesia. Pemerintah harus meningkatkan akses ke fasilitas kesehatan dengan membangun lebih banyak rumah sakit, puskesmas, dan klinik. Selain itu, pemerintah juga harus memperbaiki infrastruktur kesehatan yang sudah ada")
    st.write("**4. Memberikan edukasi seks kepada remaja dibangku sekolah**")
    st.write("Meskipun mungkin hal ini masih menjadi tabu di negara kita, namun hal ini diperlukan untuk mencegah hal negatif yang mungkin akan terjadi pada remaja. Penurunan tingkat kelahiran remaja dapat menunjukkan peningkatan akses remaja terhadap informasi dan layanan kesehatan reproduksi, serta peningkatan penggunaan kontrasepsi. Hal ini dapat mengurangi risiko komplikasi kehamilan yang berhubungan dengan kelahiran pada usia muda")
    st.write("")
    st.write("")
    st.write("")
    st.write("Itulah mungkin beberapa hal yang bisa kita telaah guna mengurangi mortalitas pada balita di Indonesia. Dengan adanya project ini, saya mengharapkan agar kita bisa terus mengurangi angka mortalitas, dan terus meningkatkan pendidikan dan fasilitas kesehatan.")
