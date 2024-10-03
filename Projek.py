import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np
from babel.numbers import format_currency
sns.set(style='dark')

st.title('Dashboard Projek Dicoding')
st.header('E-Commerce Public Data Analysis')
st.caption('By : Amanda Risky Allawiyah')

st.text('Halo, selamat datang di dashboard E-Commerce Analysis :)')


 # Load datasets
sellers_df = pd.read_csv("https://raw.githubusercontent.com/amandarisky25/Proyek-Analisis-Data/refs/heads/main/seller_olah.csv")
customers_df = pd.read_csv("https://raw.githubusercontent.com/amandarisky25/Proyek-Analisis-Data/refs/heads/main/customer_olah.csv")
order_items_df = pd.read_csv("https://raw.githubusercontent.com/amandarisky25/Proyek-Analisis-Data/refs/heads/main/order_items_olah.csv")
orders_df = pd.read_csv("https://raw.githubusercontent.com/amandarisky25/Proyek-Analisis-Data/refs/heads/main/order_olah.csv")


# Membuat Tabs untuk menampilkan analisis
tab1, tab2, tab3, tab4 = st.tabs(["Data Seller", "Data Customer", "Order", "Delivery Time"])

# Tab untuk Analisis Data Seller
with tab1:
    st.header("Analisis Data Seller")

    top_10_seller_city_counts = sellers_df.groupby(by="seller_city").seller_id.nunique().sort_values(ascending=False).head(10)
    
    # Visualisasi 10 Kota dengan Jumlah Seller Tertinggi
    st.write("### 10 Kota dengan Jumlah Seller Tertinggi")
    st.bar_chart(top_10_seller_city_counts)

    # Mengelompokkan data penjual per City dan mengurutkan
    seller_city_counts = sellers_df.groupby(by="seller_city").seller_id.nunique().sort_values(ascending=False).reset_index()

    # Streamlit Header
    st.header("Analisis Jumlah Seller Berdasarkan Kota")

    # Meminta input dari pengguna untuk memilih rentang data yang ingin ditampilkan
    start_index, end_index = st.slider(
        'Pilih Rentang Indeks City untuk Ditampilkan:',
        min_value=1,
        max_value=len(seller_city_counts),
        value=(1, 10),
        step=1
    )

    # Memilih data berdasarkan rentang input
    selected_data = seller_city_counts.iloc[start_index-1:end_index]

    # Membuat visualisasi bar chart menggunakan Matplotlib dan Seaborn
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='seller_city', y='seller_id', data=selected_data, palette='viridis', ax=ax)
    ax.set_title(f'Jumlah Seller per City dari Peringkat {start_index} hingga {end_index}')
    ax.set_xlabel('City')
    ax.set_ylabel('Jumlah Seller')
    ax.set_xticks(ax.get_xticks())
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Menampilkan grafik di Streamlit
    st.pyplot(fig)


    # Mengelompokkan data penjual per state
    seller_state_counts = sellers_df.groupby(by="seller_state").seller_id.nunique().sort_values(ascending=False).reset_index()

    # Visualisasi Jumlah Seller Berdasarkan State
    st.write("### Jumlah Seller Berdasarkan State")
    start_state, end_state = st.slider('Pilih Rentang Indeks State untuk Ditampilkan:', 1, len(seller_state_counts), (1, 10))
    selected_state_data = seller_state_counts.iloc[start_state-1:end_state]
    fig, ax = plt.subplots()
    sns.barplot(x='seller_state', y='seller_id', data=selected_state_data, palette='viridis', ax=ax)
    ax.set_title(f'Jumlah Seller per State dari Peringkat {start_state} hingga {end_state}')
    st.pyplot(fig)

# Tab untuk Analisis Data Customer
with tab2:
    st.header("Analisis Data Customer")
    top_10_customers_city_counts = customers_df.groupby(by="customer_city").customer_id.nunique().sort_values(ascending=False).head(10)
    
    # Visualisasi 10 Kota dengan Jumlah Seller Tertinggi
    st.write("### 10 Kota dengan Jumlah Seller Tertinggi")
    st.bar_chart(top_10_customers_city_counts)

    # Mengelompokkan data customer per City dan mengurutkan
    customer_city_counts = customers_df.groupby(by="customer_city").customer_id.nunique().sort_values(ascending=False).reset_index()
    # Visualisasi Jumlah Customer Berdasarkan City
    st.write("### Jumlah Customer Berdasarkan City")
    start_city, end_city = st.slider('Pilih Rentang Indeks City untuk Ditampilkan:', 1, len(customer_city_counts), (1, 10))
    selected_city_data = customer_city_counts.iloc[start_city-1:end_city]

    # Membuat visualisasi bar chart menggunakan Matplotlib dan Seaborn
    fig, ax = plt.subplots()
    sns.barplot(x='customer_city', y='customer_id', data=selected_city_data, palette='viridis', ax=ax)
    ax.set_title(f'Jumlah Customer per City dari Peringkat {start_city} hingga {end_city}')
    ax.set_xlabel('City')
    ax.set_ylabel('Jumlah Customer')
    plt.xticks(rotation=45)  # Memiringkan label di sumbu x agar tidak berhimpit
    plt.tight_layout()

    # Menampilkan grafik di Streamlit
    st.pyplot(fig)

    # Mengelompokkan data seller per state dan mengurutkan
    seller_state_counts = sellers_df.groupby(by="seller_state").seller_id.nunique().sort_values(ascending=False).reset_index()

    # Streamlit Header
    st.header("Analisis Jumlah Seller Berdasarkan State")

    # Meminta input dari pengguna untuk memilih rentang data yang ingin ditampilkan
    start_index, end_index = st.slider(
        'Pilih Rentang Indeks State untuk Ditampilkan:',
        min_value=1,
        max_value=len(seller_state_counts),
        value=(1, 10),
        step=1
    )

    # Memilih data berdasarkan rentang input
    selected_data = seller_state_counts.iloc[start_index-1:end_index]

    # Membuat visualisasi bar chart menggunakan Matplotlib dan Seaborn
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='seller_state', y='seller_id', data=selected_data, palette='viridis', ax=ax)
    ax.set_title(f'Jumlah Seller per State dari Peringkat {start_index} hingga {end_index}')
    ax.set_xlabel('State')
    ax.set_ylabel('Jumlah Seller')
    plt.xticks(rotation=45)  # Memiringkan label di sumbu x agar tidak berhimpit
    plt.tight_layout()

    # Menampilkan grafik di Streamlit
    st.pyplot(fig)

# Tab untuk Analisis Order
with tab3:
    st.header("Analisis Order")

    # Mengubah kolom shipping_limit_date menjadi datetime
    order_items_df['shipping_limit_date'] = pd.to_datetime(order_items_df['shipping_limit_date'])
    order_items_df['shipping_month'] = order_items_df['shipping_limit_date'].dt.month
    order_items_df['shipping_year'] = order_items_df['shipping_limit_date'].dt.year
    shipping_limit_count = order_items_df.groupby(['shipping_year', 'shipping_month'])['order_id'].count().reset_index()

    # Visualisasi Jumlah Order
    fig, ax = plt.subplots()
    sns.lineplot(
        x='shipping_month', y='order_id', hue='shipping_year', data=shipping_limit_count,
        palette='tab10', marker='o', ax=ax
    )
    ax.set_title('Jumlah Order per Bulan dan Tahun')
    st.pyplot(fig)

    #COBA
    # Mengubah kolom shipping_limit_date menjadi datetime
    order_items_df['shipping_limit_date'] = pd.to_datetime(order_items_df['shipping_limit_date'])
    order_items_df['shipping_month'] = order_items_df['shipping_limit_date'].dt.month
    order_items_df['shipping_year'] = order_items_df['shipping_limit_date'].dt.year
    shipping_limit_count = order_items_df.groupby(['shipping_year', 'shipping_month'])['order_id'].count().reset_index()

    # Pilihan Tahun
    st.write("### Pilih Tahun untuk Melihat Jumlah Order per Bulan")
    selected_year = st.selectbox('Pilih Tahun:', shipping_limit_count['shipping_year'].unique())

    # Filter data berdasarkan tahun yang dipilih
    filtered_data = shipping_limit_count[shipping_limit_count['shipping_year'] == selected_year]

    # Visualisasi Jumlah Order untuk Tahun yang Dipilih
    fig, ax = plt.subplots()
    sns.lineplot(
        x='shipping_month', y='order_id', data=filtered_data,
        palette='tab10', marker='o', ax=ax
    )
    ax.set_title(f'Jumlah Order per Bulan untuk Tahun {selected_year}')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Order')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Menampilkan grafik di Streamlit
    st.pyplot(fig)



# Tab untuk Analisis Delivery Time
with tab4:
    st.header("Analisis Delivery Time")

    orders_df["order_delivered_customer_date"] = pd.to_datetime(orders_df["order_delivered_customer_date"])
    orders_df["order_purchase_timestamp"] = pd.to_datetime(orders_df["order_purchase_timestamp"])
    delivery_time = orders_df["order_delivered_customer_date"] - orders_df["order_purchase_timestamp"]
    delivery_time = delivery_time.apply(lambda x: x.total_seconds())
    orders_df["delivery_time"] = round(delivery_time / 86400)

    # Statistik Waktu Pengiriman
    delivery_time_stats = orders_df['delivery_time'].describe()
    st.write("### Statistik Waktu Pengiriman")
    st.write(delivery_time_stats)

    # Visualisasi Distribusi Waktu Pengiriman
    fig, ax = plt.subplots()
    sns.histplot(orders_df['delivery_time'], bins=20, kde=True, color='green', ax=ax)
    ax.set_title('Distribusi Waktu Pengiriman (Delivery Time)')
    st.pyplot(fig)

    # Kategori Waktu Pengiriman
    orders_df['delivery_time_category'] = pd.cut(orders_df['delivery_time'], bins=[-np.inf, 3, 6, np.inf], labels=['Cepat', 'Sedang', 'Lama'])
    delivery_time_category_counts = orders_df['delivery_time_category'].value_counts().reset_index()
    delivery_time_category_counts.columns = ['delivery_time_category', 'order_count']

    # Visualisasi Kategori Waktu Pengiriman
    fig, ax = plt.subplots()
    sns.barplot(x='delivery_time_category', y='order_count', data=delivery_time_category_counts, palette='magma', ax=ax)
    ax.set_title('Jumlah Pesanan Berdasarkan Kategori Waktu Pengiriman')
    st.pyplot(fig)
