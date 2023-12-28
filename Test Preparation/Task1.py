import pandas as pd


ecom = pd.read_csv('Ecommerce_Purchases.csv')


print("Head of the DataFrame:")
print(ecom.head())


print(f"Number of rows: {ecom.shape[0]}, Number of columns: {ecom.shape[1]}")


average_purchase_price = ecom['Purchase Price'].mean()
print("Average Purchase Price:", f'${average_purchase_price:.2f}')


highest_purchase_price = max(ecom['Purchase Price'])
lowest_purchase_price = min(ecom['Purchase Price'])
print("Highest Purchase Price:", f"${highest_purchase_price}")
print("Lowest Purchase Price:", f"${lowest_purchase_price}")


num_english_speakers = sum(ecom['Language'] == 'en')
print(f"\nNumber of people with English as their language: {num_english_speakers}")


num_lawyers = sum(ecom['Job'] == 'Lawyer')
print(f"\nNumber of people with the job title 'Lawyer': {num_lawyers}")


num_am_purchases = sum(ecom['AM or PM'] == 'AM')
num_pm_purchases = sum(ecom['AM or PM'] == 'PM')
print(f"\nNumber of purchases during AM: {num_am_purchases}")
print(f"Number of purchases during PM: {num_pm_purchases}")


common_job_titles = ecom['Job'].value_counts().head(5)
print("\n5 most common Job Titles:")
print(common_job_titles)


purchase_price_90WT = ecom.loc[ecom['Lot'] == '90 WT', 'Purchase Price'].iloc[0]
print(f"\nPurchase Price for Lot '90 WT': ${purchase_price_90WT:.2f}")


email_credit_card_number = ecom.loc[ecom['Credit Card'] == 4926535242672853, 'Email'].iloc[0]
print(f"\nEmail of the person with Credit Card Number 4926535242672853: {email_credit_card_number}")


amex_above_95 = ecom.query("`CC Provider` == 'American Express' and `Purchase Price` > 95")
num_amex_above_95 = len(amex_above_95)
print(f"\nNumber of people with American Express and purchase above $95: {num_amex_above_95}")


exp_2025 = ecom[ecom['CC Exp Date'].str.split('/').str[1] == '25']
num_exp_2025 = len(exp_2025)
print(f"\nNumber of people with a credit card expiring in 2025: {num_exp_2025}")


top_email_providers = ecom['Email'].str.split('@').str[1].value_counts().nlargest(5)
print(f"\nTop 5 most popular email providers/hosts: {top_email_providers}")
