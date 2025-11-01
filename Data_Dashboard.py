import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from io import StringIO


def inject_dynamic_css():
    theme = st.session_state.theme
    if theme == "Dark":
        css = """
        <style>
            :root {
                --main-bg: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
                --text: #e2e8f0;
                --card-bg: #1e293b;
                --card-border: #334155;
                --sidebar-bg: #0f172a;
                --sidebar-text: #e2e8f0;
                --accent: #818cf8;
                --button-primary: #6366f1;
                --button-hover: #4f46e5;
                --button-success: #10b981;
                --radio-bg: #1e293b;
                --radio-border: #4c5670;
                --radio-selected: #6366f1;
                --radio-text: #e2e8f0;
                --metric: #a5b4fc;
                --hr: #334155;
                --logo-filter: invert(1);
            }
        </style>
        """
    else:
        css = """
        <style>
            :root {
                --main-bg: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
                --text: #1e293b;
                --card-bg: white;
                --card-border: #cbd5e1;
                --sidebar-bg: white;
                --sidebar-text: #1e293b;
                --accent: #3b82f6;
                --button-primary: #2563eb;
                --button-hover: #1d4ed8;
                --button-success: #059669;
                --radio-bg: #f8fafc;
                --radio-border: #dbeafe;
                --radio-selected: #2563eb;
                --radio-text: #1e293b;
                --metric: #3b82f6;
                --hr: #cbd5e1;
                --logo-filter: none;
            }
        </style>
        """
    
    st.markdown(css + """
    <style>
        .main {
            background: var(--main-bg);
            padding-top: 1.5rem;
            color: var(--text);
        }
        h1, h2, h3, p, li, div {
            color: var(--text) !important;
        }
        h1 {
            text-align: center;
            font-weight: 800;
            font-size: 2.4rem;
            margin-bottom: 0.2rem;
            background: linear-gradient(90deg, var(--accent), #ec4899);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        h2 {
            color: var(--accent);
            margin-top: 1.5rem;
            border-left: 2px solid var(--accent);
            padding-left: 12px;
        }
        
        /* BEAUTIFUL RADIO BUTTONS */
        .stRadio > div {
            background: var(--radio-bg);
            padding: 1rem;
            border-radius: 16px;
            border: 1px solid var(--radio-border);
            margin: 0.8rem 0;
            transition: all 0.3s ease;
        }
        .stRadio > div:hover {
            border-color: var(--accent);
            box-shadow: 0 6px 16px rgba(99, 102, 241, 0.2);
            transform: translateY(-2px);
        }
        .stRadio label {
            color: var(--radio-text) !important;
            font-weight: 600;
            font-size: 1.05rem;
            padding: 6px 0;
        }
        .stRadio input:checked + div {
            background: var(--radio-selected) !important;
            border-color: var(--radio-selected) !important;
        }
        .stRadio input:checked + div label {
            color: white !important;
            font-weight: 700;
        }

        /* CARDS */
        .stDataFrame, .stPyplot {
            background: var(--card-bg);
            border-radius: 18px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.12);
            padding: 1.4rem;
            margin: 1.3rem 0;
            border: 1px solid var(--card-border);
            transition: transform 0.2s ease;
        }
        .stDataFrame:hover, .stPyplot:hover {
            transform: translateY(-3px);
        }
        
        /* SIDEBAR */
        [data-testid="stSidebar"] {
            background: var(--sidebar-bg);
            border-right: 1px solid var(--hr);
        }
        [data-testid="stSidebar"] * {
            color: var(--sidebar-text) !important;
        }
        [data-testid="stSidebar"] h2 {
            color: var(--accent) !important;
            text-align: left;
            margin: 1.2rem 0 0.8rem 0.8rem;
            font-size: 1.3rem;
        }
        .sidebar-section {
            margin: 1.2rem 0;
            padding: 0 0.8rem;
        }
        .sidebar-divider {
            height: 1px;
            background: var(--hr);
            margin: 1.2rem 0;
        }
        
        /* BUTTONS */
        .stButton>button {
            background: var(--button-primary);
            color: white;
            border: none;
            border-radius: 14px;
            font-weight: 700;
            padding: 0.65rem 1.3rem;
            width: 100%;
            margin-top: 0.7rem;
            transition: all 0.3s ease;
            font-size: 1.05rem;
        }
        .stButton>button:hover {
            background: var(--button-hover);
            transform: translateY(-3px);
            box-shadow: 0 6px 18px rgba(37, 99, 235, 0.4);
        }
        .stDownloadButton>button {
            background: var(--button-success);
            color: white;
            border-radius: 14px;
            font-weight: 700;
            width: 100%;
            padding: 0.65rem;
            font-size: 1.05rem;
        }
        
        /* METRICS */
        [data-testid="stMetricValue"] {
            color: var(--metric) !important;
            font-size: 1.4rem !important;
            font-weight: 700;
        }
        
        hr {
            border-color: var(--hr) !important;
        }
        footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)


if 'df' not in st.session_state:
    st.session_state.df = None
if 'theme' not in st.session_state:
    st.session_state.theme = "Light"
if 'uploaded_file_name' not in st.session_state:
    st.session_state.uploaded_file_name = None


inject_dynamic_css()


st.markdown("<h1>✨ Data Visualization Dashboard</h1>", unsafe_allow_html=True)
subtitle_color = "#e2e8f0" if st.session_state.theme == "Dark" else "#1e293b"
st.markdown(f"<p style='text-align:center; color:{subtitle_color}; font-size:1.1rem;'>Upload • Explore • Visualize • Clean • Export</p>", unsafe_allow_html=True)


with st.sidebar:
    
    st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
    st.markdown("<h2> Theme</h2>", unsafe_allow_html=True)
    new_theme = "Dark" if st.button(" Dark Mode", use_container_width=True) else None
    if new_theme is None:
        new_theme = "Light" if st.button(" Light Mode", use_container_width=True) else st.session_state.theme
    
    if new_theme != st.session_state.theme:
        st.session_state.theme = new_theme
        
    
    st.markdown('</div><div class="sidebar-divider"></div>', unsafe_allow_html=True)
    

    st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
    st.markdown("<h2> Navigation</h2>", unsafe_allow_html=True)
    page = st.radio(
        "Go to",
        [" Upload Data", " Summary", " Visualize", " Missing Data", " Export Report", " Advanced", "ℹ About"],
        index=0
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Info
    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
    st.caption(" Your data never leaves your device")
    st.caption(" Built with Streamlit + Python")


def load_data_from_session():
    if st.session_state.df is not None:
        return st.session_state.df.copy()
    st.info("⬆ Please upload a dataset first.")
    st.stop()

if page == " Upload Data":
    st.subheader(" Upload Your CSV File")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv", label_visibility="collapsed")
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            if df.empty:
                st.error(" Uploaded file is empty.")
            else:
                st.session_state.df = df
                st.session_state.uploaded_file_name = uploaded_file.name
                st.success(f" Loaded **{df.shape[0]:,} rows** and **{df.shape[1]} columns** from `{uploaded_file.name}`")
                st.dataframe(df.head(), use_container_width=True)
        except Exception as e:
            st.error(f" Error: {e}")
    elif st.session_state.df is not None:
        st.success(f" Dataset already loaded: `{st.session_state.uploaded_file_name}`")
        st.dataframe(st.session_state.df.head(), use_container_width=True)
    else:
        st.info(" Upload a CSV file to begin analysis.")


elif page == " Summary":
    df = load_data_from_session()
    st.subheader(" Dataset Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Rows", f"{df.shape[0]:,}")
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing", f"{df.isnull().sum().sum():,}")
    col4.metric("Memory", f"{df.memory_usage(deep=True).sum() / 1024:.1f} KB")
    
    st.write("**Column Data Types:**")
    st.dataframe(df.dtypes.to_frame("Type").T, use_container_width=True)
    
    num_df = df.select_dtypes(np.number)
    if not num_df.empty:
        st.write("**Numeric Summary Statistics:**")
        stats = pd.DataFrame({
            'Mean': num_df.mean(),
            'Median': num_df.median(),
            'Std Dev': num_df.std(ddof=1),
            'Min': num_df.min(),
            'Max': num_df.max()
        }).round(3)
        st.dataframe(stats, use_container_width=True)


elif page == " Visualize":
    df = load_data_from_session()
    st.subheader(" Choose a Visualization")
    
    num_cols = df.select_dtypes(np.number).columns.tolist()
    cat_cols = df.select_dtypes('object').columns.tolist()
    
    plot_options = []
    if num_cols: plot_options += ["Histogram", "Box Plot"]
    if cat_cols: plot_options.append("Bar Chart")
    if len(num_cols) > 1: plot_options += ["Correlation Heatmap", "Scatter Plot"]
    
    if not plot_options:
        st.warning(" No suitable columns for visualization.")
        st.stop()
    
    plot_type = st.radio("Select chart type:", plot_options, horizontal=True)
    
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(10, 5))
    
    if plot_type == "Histogram" and num_cols:
        col = st.radio("Select column:", num_cols, horizontal=True) if len(num_cols) <= 6 else st.selectbox("Select column:", num_cols)
        sns.histplot(df[col].dropna(), kde=True, ax=ax, color="#8b5cf6")
    elif plot_type == "Bar Chart" and cat_cols:
        col = st.radio("Select column:", cat_cols, horizontal=True) if len(cat_cols) <= 6 else st.selectbox("Select column:", cat_cols)
        df[col].value_counts().head(10).plot(kind='bar', ax=ax, color="#10b981")
        plt.xticks(rotation=30, ha='right')
    elif plot_type == "Box Plot" and num_cols:
        col = st.radio("Select column:", num_cols, horizontal=True) if len(num_cols) <= 6 else st.selectbox("Select column:", num_cols)
        sns.boxplot(y=df[col], ax=ax, color="#f59e0b")
    elif plot_type == "Correlation Heatmap" and len(num_cols) > 1:
        sns.heatmap(df[num_cols].corr(), annot=True, cmap="viridis", center=0, ax=ax)
    elif plot_type == "Scatter Plot" and len(num_cols) > 1:
        x_col = st.radio("X-axis:", num_cols, horizontal=True)
        y_col = st.radio("Y-axis:", [c for c in num_cols if c != x_col] or num_cols, horizontal=True)
        sns.scatterplot(data=df, x=x_col, y=y_col, alpha=0.7, ax=ax, color="#ef4444")
    
    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)


elif page == " Missing Data":
    df = load_data_from_session()
    st.subheader(" Missing Value Report")
    
    missing = df.isnull().sum()
    total_missing = missing.sum()
    if total_missing == 0:
        st.success(" No missing values!")
    else:
        st.info(f" Total missing cells: **{total_missing:,}**")
        st.bar_chart(missing[missing > 0])
        
        action = st.radio("Choose cleaning method:", 
                         ["Do nothing", "Drop rows", "Fill numeric with mean", "Fill numeric with median", "Fill categorical with mode"])
        
        if action == "Drop rows" and st.button(" Apply"):
            st.session_state.df = df.dropna()
            st.success(" Rows dropped!")
        elif action == "Fill numeric with mean" and st.button(" Apply Mean"):
            num_cols = df.select_dtypes(np.number).columns
            if len(num_cols) == 0:
                st.error(" No numeric columns.")
            else:
                df_filled = df.copy()
                df_filled[num_cols] = df_filled[num_cols].fillna(df_filled[num_cols].mean())
                st.session_state.df = df_filled
                st.success(" Filled with mean!")
        elif action == "Fill numeric with median" and st.button(" Apply Median"):
            num_cols = df.select_dtypes(np.number).columns
            if len(num_cols) == 0:
                st.error(" No numeric columns.")
            else:
                df_filled = df.copy()
                df_filled[num_cols] = df_filled[num_cols].fillna(df_filled[num_cols].median())
                st.session_state.df = df_filled
                st.success(" Filled with median!")
        elif action == "Fill categorical with mode" and st.button(" Apply Mode"):
            cat_cols = df.select_dtypes('object').columns
            if len(cat_cols) == 0:
                st.error(" No categorical columns.")
            else:
                df_filled = df.copy()
                for col in cat_cols:
                    if df_filled[col].isnull().sum() > 0:
                        mode_val = df_filled[col].mode()
                        if not mode_val.empty:
                            df_filled[col].fillna(mode_val[0], inplace=True)
                st.session_state.df = df_filled
                st.success(" Filled with mode!")


elif page == " Export Report":
    df = load_data_from_session()
    num_df = df.select_dtypes(np.number)
    if num_df.empty:
        st.warning(" No numeric data to export.")
    else:
        report = pd.DataFrame({
            'Mean': num_df.mean(),
            'Median': num_df.median(),
            'Std Dev': num_df.std(ddof=1),
            'Missing %': (num_df.isnull().mean() * 100).round(2)
        }).round(3)
        st.subheader(" Summary Report")
        st.dataframe(report, use_container_width=True)
        csv = report.to_csv().encode('utf-8')
        st.download_button("⬇ Download Report (CSV)", csv, "data_summary_report.csv", "text/csv")


elif page == " Advanced":
    df = load_data_from_session()
    st.subheader(" Advanced Analysis")
    
    if st.checkbox("Show Duplicate Rows"):
        dupes = df.duplicated().sum()
        st.metric("Duplicate Rows", dupes)
        if dupes > 0:
            st.dataframe(df[df.duplicated()].head(), use_container_width=True)
    
    if st.checkbox("Show Outliers (IQR Method)"):
        num_cols = df.select_dtypes(np.number).columns.tolist()
        if num_cols:
            col = st.radio("Select column for outlier detection:", num_cols, horizontal=True)
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            outliers = df[(df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))]
            st.metric("Outliers Found", len(outliers))
            if len(outliers) > 0:
                st.dataframe(outliers.head(), use_container_width=True)
        else:
            st.warning("No numeric columns for outlier detection.")


else:
    st.subheader(" About This Dashboard")
    st.markdown("""
    A **vibrant, interactive EDA tool** built with:
    - **Python**: pandas, numpy, seaborn, matplotlib
    - **Streamlit**: for instant web UI
    - **Zero data upload** — everything runs locally
    
     **Features**:
    - Light/Dark mode (no refresh!)
    - File persists across theme changes
    - Advanced analysis (duplicates, outliers)
    - Beautiful, animated UI
    
    **Developed by:-**  **Muhammad Noman Shaikh**!
    """)
    logo_filter = "invert(1)" if st.session_state.theme == "Dark" else "none"