def calculate_roi(initial_investment, final_value):

    return ((final_value - initial_investment) / initial_investment) * 100
def calculate_npv(initial_investment, cash_flows, discount_rate):

    npv = -initial_investment
    for i, cash_flow in enumerate(cash_flows):
        npv += cash_flow / ((1 + discount_rate) ** (i + 1))
    return npv

initial_investment = 10000
final_value = 15000
cash_flows = [-10000, 3000, 4000, 5000, 6000]
discount_rate = 0.1

roi = calculate_roi(initial_investment, final_value)
print("ROI: {:.2f}%".format(roi))

npv = calculate_npv(initial_investment, cash_flows, discount_rate)
print("NPV: {:.2f}".format(npv))
