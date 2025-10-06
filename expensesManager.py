import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class ExpensesManager:
    def __init__(self):
        # Initialize DataFrames for better data analytics
        self.expenses_df = pd.DataFrame(columns=['amount', 'description', 'date', 'currency', 'category', 'type'])
        self.incomes_df = pd.DataFrame(columns=['amount', 'description', 'date', 'currency', 'source', 'type'])
        
        # Currency conversion rates (simplified - in real app, use API)
        self.exchange_rates = {
            'COP_to_USD': 0.00025,
            'USD_to_COP': 4000,
            'COP_to_COP': 1,
            'USD_to_USD': 1
        }

# =======================================================================================

    def convert_currency(self, amount, from_currency, to_currency):
        """Convert currency using exchange rates"""
        if from_currency == to_currency:
            return amount
        
        rate_key = f"{from_currency}_to_{to_currency}"
        if rate_key in self.exchange_rates:
            return round(amount * self.exchange_rates[rate_key], 2)
        else:
            print(f"Exchange rate not available for {from_currency} to {to_currency}")
            return amount
        
# =======================================================================================

    def add_expense(self, amount=None, description=None, date=None, currency=None, category=None):
        """Add expense to DataFrame for analytics"""
        try:
            if amount is None:
                amount = float(input("Input the amount: "))
                
            if currency is None:
                print("In which currency is this?\n1) COP\n2) USD")
                currency_choice = int(input("Select a number: "))
                currency = 'COP' if currency_choice == 1 else 'USD'
            
            if description is None:
                description = input("Type a description: ")
            
            if category is None:
                print("Select category:\n1) Food\n2) Transportation\n3) Entertainment\n4) Bills\n5) Other")
                cat_choice = int(input("Select category: "))
                categories = {1: 'Food', 2: 'Transportation', 3: 'Entertainment', 4: 'Bills', 5: 'Other'}
                category = categories.get(cat_choice, 'Other')
            
            if date is None:
                date_input = input("Enter date (DD/MM/YYYY) or press Enter for today: ")
                if date_input:
                    date = pd.to_datetime(date_input, format='%d/%m/%Y')
                else:
                    date = pd.Timestamp.now()
            
            # Convert to USD for standardization
            amount_usd = self.convert_currency(amount, currency, 'USD')
            
            # Create new row
            new_expense = pd.DataFrame({
                'amount': [amount],
                'description': [description],
                'date': [date],
                'currency': [currency],
                'category': [category],
                'type': ['expense'],
                'amount_usd': [amount_usd]
            })
            
            # Add to DataFrame
            self.expenses_df = pd.concat([self.expenses_df, new_expense], ignore_index=True)
            print(f"✓ Expense added: {description} - {amount} {currency} ({amount_usd} USD)")
            
        except Exception as e:
            print(f"Error adding expense: {e}")

# =======================================================================================


    def add_income(self, amount=None, description=None, date=None, currency=None, source=None):
        """Add income to DataFrame for analytics"""
        try:
            if amount is None:
                amount = float(input("Input the amount: "))
                
            if currency is None:
                print("In which currency is this?\n1) COP\n2) USD")
                currency_choice = int(input("Select a number: "))
                currency = 'COP' if currency_choice == 1 else 'USD'
            
            if description is None:
                description = input("Type a description: ")
            
            if source is None:
                print("Select source:\n1) Salary\n2) Freelance\n3) Investment\n4) Gift\n5) Other")
                source_choice = int(input("Select source: "))
                sources = {1: 'Salary', 2: 'Freelance', 3: 'Investment', 4: 'Gift', 5: 'Other'}
                source = sources.get(source_choice, 'Other')
            
            if date is None:
                date_input = input("Enter date (DD/MM/YYYY) or press Enter for today: ")
                if date_input:
                    date = pd.to_datetime(date_input, format='%d/%m/%Y')
                else:
                    date = pd.Timestamp.now()
            
            # Convert to USD for standardization
            amount_usd = self.convert_currency(amount, currency, 'USD')
            
            # Create new row
            new_income = pd.DataFrame({
                'amount': [amount],
                'description': [description],
                'date': [date],
                'currency': [currency],
                'source': [source],
                'type': ['income'],
                'amount_usd': [amount_usd]
            })
            
            # Add to DataFrame
            self.incomes_df = pd.concat([self.incomes_df, new_income], ignore_index=True)
            print(f"✓ Income added: {description} - {amount} {currency} ({amount_usd} USD)")
            
        except Exception as e:
            print(f"Error adding income: {e}")

# =======================================================================================

    def show_expenses(self):
        """Display expenses with analytics"""
        if self.expenses_df.empty:
            print("No expenses recorded.")
            return
        
        print("\n=== EXPENSES SUMMARY ===")
        print(self.expenses_df[['date', 'description', 'amount', 'currency', 'category']].to_string(index=False))
        
        print(f"\nTotal Expenses: ${self.expenses_df['amount_usd'].sum():.2f} USD")
        print("\nExpenses by Category:")
        category_summary = self.expenses_df.groupby('category')['amount_usd'].sum().sort_values(ascending=False)
        for category, amount in category_summary.items():
            print(f"  {category}: ${amount:.2f}")

    def show_incomes(self):
        """Display incomes with analytics"""
        if self.incomes_df.empty:
            print("No incomes recorded.")
            return
        
        print("\n=== INCOMES SUMMARY ===")
        print(self.incomes_df[['date', 'description', 'amount', 'currency', 'source']].to_string(index=False))
        
        print(f"\nTotal Income: ${self.incomes_df['amount_usd'].sum():.2f} USD")
        print("\nIncome by Source:")
        source_summary = self.incomes_df.groupby('source')['amount_usd'].sum().sort_values(ascending=False)
        for source, amount in source_summary.items():
            print(f"  {source}: ${amount:.2f}")

# =======================================================================================


    def calculate_net_balance(self):
        """Calculate and display net balance with analytics"""
        total_income = self.incomes_df['amount_usd'].sum() if not self.incomes_df.empty else 0
        total_expenses = self.expenses_df['amount_usd'].sum() if not self.expenses_df.empty else 0
        net_balance = total_income - total_expenses
        
        print("\n=== FINANCIAL SUMMARY ===")
        print(f"Total Income:  ${total_income:.2f} USD")
        print(f"Total Expenses: ${total_expenses:.2f} USD")
        print(f"Net Balance:   ${net_balance:.2f} USD")
        
        if net_balance > 0:
            print("You're in the positive! Good financial health.")
        elif net_balance < 0:
            print("You're spending more than earning. Consider budgeting.")
        else:
            print("You're breaking even.")

        return net_balance
    
# =======================================================================================

    def generate_analytics_report(self):
        """Generate comprehensive analytics report"""
        print("\n" + "="*50)
        print("           ANALYTICS REPORT")
        print("="*50)
        
        if self.expenses_df.empty and self.incomes_df.empty:
            print("No data available for analysis.")
            return
        
        # Basic statistics
        if not self.expenses_df.empty:
            print(f"\n📊 EXPENSE ANALYTICS:")
            print(f"   • Average expense: ${self.expenses_df['amount_usd'].mean():.2f}")
            print(f"   • Largest expense: ${self.expenses_df['amount_usd'].max():.2f}")
            print(f"   • Smallest expense: ${self.expenses_df['amount_usd'].min():.2f}")
            print(f"   • Total transactions: {len(self.expenses_df)}")
            
        if not self.incomes_df.empty:
            print(f"\n💰 INCOME ANALYTICS:")
            print(f"   • Average income: ${self.incomes_df['amount_usd'].mean():.2f}")
            print(f"   • Largest income: ${self.incomes_df['amount_usd'].max():.2f}")
            print(f"   • Smallest income: ${self.incomes_df['amount_usd'].min():.2f}")
            print(f"   • Total transactions: {len(self.incomes_df)}")

    def create_visualizations(self):
        """Create graphs for data visualization"""
        try:
            if self.expenses_df.empty and self.incomes_df.empty:
                print("No data available for visualization.")
                return
            
            fig, axes = plt.subplots(2, 2, figsize=(15, 10))
            fig.suptitle('Financial Analytics Dashboard', fontsize=16)
            
            # Expenses by category (pie chart)
            if not self.expenses_df.empty:
                category_data = self.expenses_df.groupby('category')['amount_usd'].sum()
                axes[0,0].pie(category_data.values, labels=category_data.index, autopct='%1.1f%%')
                axes[0,0].set_title('Expenses by Category')
            
            # Income vs Expenses comparison
            if not self.expenses_df.empty or not self.incomes_df.empty:
                total_income = self.incomes_df['amount_usd'].sum() if not self.incomes_df.empty else 0
                total_expenses = self.expenses_df['amount_usd'].sum() if not self.expenses_df.empty else 0
                
                axes[0,1].bar(['Income', 'Expenses'], [total_income, total_expenses], 
                             color=['green', 'red'], alpha=0.7)
                axes[0,1].set_title('Income vs Expenses')
                axes[0,1].set_ylabel('Amount (USD)')
            
            # Monthly trend (if we have date data)
            if not self.expenses_df.empty:
                monthly_expenses = self.expenses_df.copy()
                monthly_expenses['month'] = pd.to_datetime(monthly_expenses['date']).dt.to_period('M')
                monthly_trend = monthly_expenses.groupby('month')['amount_usd'].sum()
                
                axes[1,0].plot(monthly_trend.index.astype(str), monthly_trend.values, marker='o')
                axes[1,0].set_title('Monthly Expenses Trend')
                axes[1,0].set_ylabel('Amount (USD)')
                axes[1,0].tick_params(axis='x', rotation=45)
            
            # Income sources distribution
            if not self.incomes_df.empty:
                source_data = self.incomes_df.groupby('source')['amount_usd'].sum()
                axes[1,1].bar(source_data.index, source_data.values, color='lightblue')
                axes[1,1].set_title('Income by Source')
                axes[1,1].set_ylabel('Amount (USD)')
                axes[1,1].tick_params(axis='x', rotation=45)
            
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Error creating visualizations: {e}")
            print("Make sure you have matplotlib and seaborn installed:")
            print("pip install matplotlib seaborn")

    def export_to_csv(self):
        """Export data to CSV files for external analysis"""
        try:
            if not self.expenses_df.empty:
                self.expenses_df.to_csv('expenses_data.csv', index=False)
                print("✓ Expenses exported to 'expenses_data.csv'")
            
            if not self.incomes_df.empty:
                self.incomes_df.to_csv('incomes_data.csv', index=False)
                print("✓ Incomes exported to 'incomes_data.csv'")
                
            # Combined dataset
            if not self.expenses_df.empty or not self.incomes_df.empty:
                combined_df = pd.concat([
                    self.expenses_df.assign(transaction_type='expense'),
                    self.incomes_df.assign(transaction_type='income')
                ], ignore_index=True)
                combined_df.to_csv('financial_data.csv', index=False)
                print("✓ Combined data exported to 'financial_data.csv'")
                
        except Exception as e:
            print(f"Error exporting data: {e}")

    def get_spending_insights(self):
        """Provide AI-like insights based on spending patterns"""
        if self.expenses_df.empty:
            print("No expense data available for insights.")
            return
        
        print("\n🔍 SPENDING INSIGHTS:")
        
        # Top spending category
        top_category = self.expenses_df.groupby('category')['amount_usd'].sum().idxmax()
        top_amount = self.expenses_df.groupby('category')['amount_usd'].sum().max()
        print(f"• Your biggest spending category is '{top_category}' (${top_amount:.2f})")
        
        # Recent spending trend
        if len(self.expenses_df) >= 5:
            recent_avg = self.expenses_df.tail(5)['amount_usd'].mean()
            overall_avg = self.expenses_df['amount_usd'].mean()
            
            if recent_avg > overall_avg * 1.2:
                print("• ⚠ Your recent spending is 20% higher than average")
            elif recent_avg < overall_avg * 0.8:
                print("• ✓ Your recent spending is lower than average - good job!")
        
        # Frequency analysis
        most_frequent = self.expenses_df['category'].mode()[0]
        freq_count = (self.expenses_df['category'] == most_frequent).sum()
        print(f"• You spend most frequently on '{most_frequent}' ({freq_count} transactions)")

    def selectOption(self):
        """Main menu with enhanced options"""
        while True:
            print("""
    ╔══════════════════════════════════════╗
    ║         EXPENSES MANAGER             ║
    ║          (Analytics Ready)           ║
    ╚══════════════════════════════════════╝
    
    Select one option:
            1) Add expense
            2) Add income
            ----------------
            3) Show expenses
            4) Show incomes
            ----------------
            5) Calculate net balance
            6) Analytics report
            7) Create visualizations
            8) Export to CSV
            9) Get spending insights
            ----------------
            0) Exit""")

            try:
                option = int(input("Select an Option: "))
                
                if option == 1:
                    self.add_expense()
                elif option == 2:
                    self.add_income()
                elif option == 3:
                    self.show_expenses()
                elif option == 4:
                    self.show_incomes()
                elif option == 5:
                    self.calculate_net_balance()
                elif option == 6:
                    self.generate_analytics_report()
                elif option == 7:
                    self.create_visualizations()
                elif option == 8:
                    self.export_to_csv()
                elif option == 9:
                    self.get_spending_insights()
                elif option == 0:
                    print("Thank you for using Expenses Manager!")
                    break
                else:
                    print("Invalid option. Please try again.")
                    
            except ValueError:
                print("Please enter a valid number.")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    manager = ExpensesManager()
    manager.selectOption()