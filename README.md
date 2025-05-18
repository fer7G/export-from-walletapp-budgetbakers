# Export transactions from WalletApp by BudgetBakers
[![es](https://img.shields.io/badge/language-es-yellow.svg)](README.es.md)

Since WalletApp by BudgetBakers does *not* include a feature to export your transaction records, this script provides a workaround to export them into a `.csv` file in the most effective way possible using the `.html` version of the web app.

## Requirements

The script has been developed and tested with **Python 3.12**. To install the required libraries, run `pip install -r requirements.txt`.

## Usage

1. Log into your account on the [web version](https://web.budgetbakers.com/) and go to the “Records” section.

2. Select the time range you want to export. Then, scroll all the way down so that the full list of transactions is loaded in the `.html`. If you have many records, it’s recommended to do it year by year. This is also a good practice for making regular exports instead of downloading everything each time.

3. Save the page with a name like `registros` in the same folder where this repository is located. You should end up with the `.html` file and a folder like this:

```
├── README.md
├── registros_files
├── registros.html
├── requirements.txt
├── script.py
└── venv
```

4. Make sure the filename matches the variable inside the script (`html_path = "registros.html"`), and then run `python3 script.py`.

5. The transactions will be exported to a dataset called `transacciones_exportadas.csv`, with the following columns:

   * Date
   * Amount
   * Description
   * Category
   * Payer/Payee
   * Tags
   * Account

⚠️ **Note**: This script is designed to extract data from an `.html` file in Spanish. Since WalletApp doesn't allow changing the language, it hasn't been tested with English exports. The script parses dates like "17 de septiembre de 2024" and converts them to 2024/09/17, so if you're working with an `.html` file in another language, you'll need to adapt the date parsing lines accordingly. It's a simple change.

## Limitations

The script extracts as much information as possible from the `.html`, but some data is not available in the downloaded page. These fields **cannot** be exported:

* Time of transaction
* Full description (if it’s longer than 40 characters)
* Payment method (cash, debit card, etc.)
* Payment type (income, transfer...) – although this can be inferred from the amount sign
* Payment status
* Location