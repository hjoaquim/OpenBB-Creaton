# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import streamlit as st
from openbb_terminal.sdk import openbb

# IMPORTATION INTERNAL
from config import PORTFOLIO_FILE, DASHBOARD_TITLE

st.title(f"# {DASHBOARD_TITLE}")

# Load portfolio
p = openbb.portfolio.load(PORTFOLIO_FILE)

# asset allocation
alloc_assets = openbb.portfolio.alloc.assets(p)
st.write("### Asset allocation", alloc_assets)

# Get holdings of assets
st.write("### Holdings of assets")

holdp = openbb.portfolio.holdp(p)
st.write("##### Holdings of assets (in percentage)", holdp.tail(5))

holdv = openbb.portfolio.holdv(p)
st.write("##### Holdings of assets (absolute value)")
st.area_chart(holdv)

# summary
summary = openbb.portfolio.summary(p)
st.write("### Summary", summary)

# asset allocation per sector
alloc_sectors = openbb.portfolio.alloc.sectors(p)
st.write("### Asset allocation per sector", alloc_sectors)

# Get yearly returns
yearly_returns = openbb.portfolio.yret(p)
st.write("### Yearly returns", yearly_returns)
st.bar_chart(yearly_returns)

# Get monthly returns
monthly_returns = openbb.portfolio.mret(p)
st.write("### Monthly returns", monthly_returns[-1])
st.bar_chart(monthly_returns[-1])

# Display daily returns
daily_returns = openbb.portfolio.distr(p)
st.write("### Daily returns", daily_returns.tail(30))
st.bar_chart(daily_returns.tail(30))

# Get portfolio expected shortfall
expected_shortfall = openbb.portfolio.es(p)
st.write("### Expected shortfall", expected_shortfall)
es_button = st.button(
    label="Expected shortfall info",
    help="**Expected shortfall**, also known as conditional value-at-risk (CVaR), is a measure of risk that estimates the average loss an investor can expect to incur over a given time period if a portfolio falls within a certain level of the distribution of its returns. It is similar to value-at-risk (VaR), but instead of estimating the maximum loss that is expected to occur with a certain probability, it estimates the average loss that is expected to occur beyond a certain level of the distribution of returns.\nFor example, if a portfolio has a 1% expected shortfall, it means that there is a 1% probability that the portfolio will lose more than the estimated average loss. Expected shortfall is typically used as a risk measure for portfolios with non-normal return distributions, such as those with fat tails or skew. It is used in the fields of finance and investment to help investors and portfolio managers understand and manage the risk of their portfolios.",
    disabled=True,
)
st.write(es_button)

# Get portfolio VaR
var = openbb.portfolio.var(p)
st.write("### Value at risk", var)
var_button = st.button(
    label="Value-at-risk (VaR)",
    help="**Value-at-risk (VaR)** is a measure of the risk of loss for an investment or portfolio. It estimates the maximum loss that an investor can expect to incur over a given time period with a certain level of confidence. For example, a portfolio with a 5% VaR over a one-year time horizon means that there is a 5% probability that the portfolio will lose more than the estimated maximum loss over the next year.\nVaR is typically calculated using statistical methods that involve modeling the distribution of returns for an investment or portfolio. It can be expressed in absolute terms, such as dollars or euros, or as a percentage of the portfolio's value.\nVaR is a widely used risk measure in the fields of finance and investment. It is used by investors and portfolio managers to understand and manage the risk of their portfolios, as well as by regulators to set risk-based capital requirements for financial institutions.",
    disabled=True,
)
st.write(var_button)

# Calculate the drawdown (MDD) of historical series
mdd = openbb.portfolio.maxdd(p)
st.write("### Maximum drawdown")
mdd_button = st.button(
    label="Maximum drawdown (MDD)",
    help="**Drawdown**, also known as **maximum drawdown (MDD)**, is a measure of the decline in value of an investment or portfolio from its peak to its trough. It is typically expressed as a percentage of the peak value and is used to assess the risk of an investment or portfolio.\nFor example, if an investment has a peak value of $100 and a trough value of $80, its drawdown would be 20%. This means that the investment lost 20% of its value from its peak to its trough.\nIn a historical series, the maximum drawdown (MDD) is the largest drawdown that has occurred over a certain time period. It is a measure of the maximum loss that an investor could have experienced during that time period.\nMDD is often used by investors and portfolio managers to assess the risk of an investment or portfolio and to compare the risk of different investments or portfolios. It can be calculated using the following formula:\nMDD = (Peak Value - Trough Value) / Peak Value",
    disabled=True,
)
st.write(mdd_button)
st.write("##### Holdings")
st.area_chart(mdd[0])
st.write("##### Portfolio Drawdown")
st.area_chart(mdd[1])

# Get portfolio performance vs the benchmark
perf = openbb.portfolio.perf(p)
st.write("### Performance vs the benchmark", perf)
