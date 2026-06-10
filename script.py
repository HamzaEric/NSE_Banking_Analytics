import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from pathlib import Path

st.set_page_config(
    layout="wide"
)
# def main():
st.header("Quantitative Analysis of Banking Stocks in the Kenyan Equity Market(NSE)")
st.markdown("---")
col1,col2 = st.columns(2)
with col1:
    st.image("Pulsar Vexline Legit.jpg",width = 600)
with col2:
    data = {
        "Technical Indicators Used": [
            "Volume Weighted Average Price",
            "Static Volatility",
            "Dynamic Volatility",
            "Beta",
            "Moving Average Convergence Divergence",
        ]
    }
    df = pd.DataFrame(data)
    st.dataframe(df,use_container_width=True)
    df_one = pd.DataFrame({
        "Stocks Analysed": ["Diamond Trust Bank Kenya Limited (DTB)","Equity Group Holdings PLC (EQTY)","I&M Group PLC (IMH)","KCB Group PLC (KCB)","NCBA Group PLC (NCBA)","Stanbic Holdings PLC (SBIC)","Standard Chartered Bank Kenya Limited (SCBK)","Co-operative Bank of Kenya Limited (COOP)","ABSA Bank Kenya PLC"]})
    df_one = pd.DataFrame(df_one)
    st.dataframe(df_one,use_container_width=True)
st.markdown("---")
st.link_button("Get the Colab Notebook","https://colab.research.google.com/drive/1F8uQiN4jgXw5PWNVULd5eDe6Qz168b3R?usp=drive_link")
st.markdown("---")
st.subheader("The Analysis")
html_file = Path(r"NSE_Banking_Sector_Analysis.html")
components.html(html_file.read_text(encoding="utf-8"),height= 1000 ,scrolling=True)
# if __name__ == "__main__":
#     st.set_page_config(layout="wide")
