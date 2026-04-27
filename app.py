import streamlit as st

st.set_page_config(page_title="Rental Deal Analyzer", page_icon="🏠")

st.title("🏠 3B Dih Analyzer")
st.write("Calculate the ROI and Cash Flow of a property to see if it's a good investment.")

# --- SIDEBAR INPUTS ---
with st.sidebar:
    st.header("1. Purchase Details")
    price = st.number_input("Purchase Price ($)", value=200000, step=5000)
    down_pct = st.slider("Down Payment %", 0, 100, 20)
    closing_costs = st.number_input("Closing Costs ($)", value=5000, step=500)
    
    st.header("2. Risk Factors")
    maint_pct = st.slider("Maintenance %", 0, 15, 5)
    vac_pct = st.slider("Vacancy %", 0, 15, 5)

# --- MAIN PANEL INPUTS ---
st.header("Monthly Financials")
col1, col2 = st.columns(2)

with col1:
    rent = st.number_input("Monthly Rent ($)", value=1500)
    loan_pmt = st.number_input("Monthly Loan Payment ($)", value=1000)

with col2:
    taxes_annual = st.number_input("Annual Property Taxes ($)", value=3000)
    ins_annual = st.number_input("Annual Insurance ($)", value=1200)
    hoa = st.number_input("Monthly HOA ($)", value=0)

# --- CALCULATIONS ---
down_dollars = price * (down_pct / 100)
total_cash_invested = down_dollars + closing_costs

m_taxes = taxes_annual / 12
m_ins = ins_annual / 12
m_maint = rent * (maint_pct / 100)
m_vac = rent * (vac_pct / 100)

total_monthly_out = loan_pmt + m_taxes + m_ins + hoa + m_maint + m_vac
cash_flow = rent - total_monthly_out
annual_roi = (cash_flow * 12 / total_cash_invested * 100) if total_cash_invested > 0 else 0

# --- DISPLAY RESULTS ---
st.divider()
res_col1, res_col2 = st.columns(2)
res_col1.metric("Monthly Cash Flow", f"${cash_flow:,.2f}")
res_col2.metric("Annual ROI", f"{annual_roi:.2f}%")

if annual_roi >= 13:
    st.success("💎 VERDICT: INVEST RARE DEAL!!")
elif annual_roi >= 8:
    st.info("✅ VERDICT: GOOD DEAL")
elif annual_roi >= 5:
    st.warning("⚖️ VERDICT: AVERAGE DEAL")
else:
    st.error("❌ VERDICT: NOT A GOOD DEAL")

st.info(f"Total Cash Out-of-Pocket: ${total_cash_invested:,.2f}")


