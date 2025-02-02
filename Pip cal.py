# Updated pip value definition
pip_value = 0.1  # 1 pip = 0.1 price movement in this broker

# Calculate the dollar value of 1 pip for 20 lots
value_per_pip = lot_size * pip_value  # USD per pip for 1 lot
value_per_pip_for_20_lots = value_per_pip * number_of_lots

# Calculate total loss for 40 pips
total_loss = value_per_pip_for_20_lots * 40

# Recalculate total balance required
total_balance_required = required_margin + total_loss

value_per_pip_for_20_lots, total_loss, total_balance_required
