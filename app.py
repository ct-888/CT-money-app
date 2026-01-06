import streamlit as st
import pandas as pd
from datetime import date

# --- 設定紅金風格 ---
st.set_page_config(page_title="168錢母營運系統", page_icon="💰", layout="wide")

st.markdown("""
    <style>
    /* 紅金配色主題 */
    .stApp { background-color: #FFF8E7; } /* 米黃底 */
    h1, h2, h3, h4, p, label, .stMarkdown { color: #8B0000 !important; } /* 深紅字 */
    [data-testid="stMetricValue"] { color: #D32F2F !important; } /* 亮紅數字 */
    
    /* 輸入框優化 */
    .stTextInput > div > div > input { color: #8B0000; }
    .stNumberInput > div > div > input { color: #8B0000; }
    
    /* 金色按鈕 */
    div.stButton > button {
        background-color: #D4AF37;
        color: #8B0000;
        border: none;
        font-weight: bold;
        width: 100%;
        padding: 10px;
        font-size: 18px;
    }
    div.stButton > button:hover { background-color: #C5A000; color: white; }
    
    /* 分頁標籤 */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { background-color: #FFF0F0; color: #8B0000; border-radius: 5px; }
    .stTabs [aria-selected="true"] { background-color: #D4AF37 !important; color: white !important; }
    </style>
""", unsafe_allow_html=True)

# --- 標題區 ---
st.title("🧧 168錢母 雲端營運系統")
st.markdown("### ✨ 財源廣進，日日見財 ✨")
st.divider()

# --- 分頁功能 ---
tab1, tab2 = st.tabs(["📅 每日流水帳 (Daily)", "📊 每月固定支出 (Monthly)"])

# === 分頁 1: 每日營運 ===
with tab1:
    st.subheader("📝 新增今日數據")
    with st.form("daily_form"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            entry_date = st.date_input("日期", value=date.today())
            revenue = st.number_input("當日營收", min_value=0, step=1000)
            fee_store = st.number_input("超商手續費", min_value=0)
            tx_count = st.number_input("交易總數", min_value=0)
            
        with col2:
            coin_in = st.number_input("收幣量", min_value=0, step=10000)
            coin_out = st.number_input("出幣量", min_value=0, step=10000)
            fee_coin_out = st.number_input("出幣手續費", min_value=0)
            coin_exchange = st.number_input("幣換台", min_value=0)

        with col3:
            loss_activity = st.number_input("活動損失", min_value=0)
            loss_discount = st.number_input("優惠損失", min_value=0)
            fee_transfer = st.number_input("轉帳手續費", min_value=0)
            total_assets = st.number_input("總資產 (驗算用)", min_value=0, step=10000)

        # 簡易淨利試算
        profit = revenue - fee_store - fee_coin_out - loss_activity - loss_discount - fee_transfer
        st.markdown(f"#### 💰 試算當日淨利: :red[${profit:,}]")

        submitted = st.form_submit_button("✅ 確認入帳 (金按鈕)")
        if submitted:
            st.balloons() # 放氣球慶祝
            st.success(f"{entry_date} 資料已送出！(目前為演示模式，尚未連結資料庫)")

# === 分頁 2: 每月支出 ===
with tab2:
    st.subheader("📉 月度成本登錄")
    with st.form("monthly_form"):
        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1:
            month_str = st.selectbox("月份", [f"{i}月" for i in range(1, 13)])
            cost_rent = st.number_input("房租", value=0, step=1000)
            cost_tax = st.number_input("稅務成本", value=0, step=1000)
        with m_col2:
            cost_water = st.number_input("水費", value=0)
            cost_electric = st.number_input("電費", value=0)
            cost_net = st.number_input("網路費", value=0)
        with m_col3:
            salary_base = st.number_input("員工薪資", value=0, step=1000)
            salary_bonus = st.number_input("業績/年終", value=0, step=1000)
            cost_phone = st.number_input("電話費", value=0)

        submitted_m = st.form_submit_button("✅ 確認支出 (金按鈕)")
        if submitted_m:
            st.success(f"{month_str} 支出已送出！")
