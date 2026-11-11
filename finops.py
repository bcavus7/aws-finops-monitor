import boto3
from budget_logic import analyze_budget

account = boto3.client("sts").get_caller_identity()["Account"]
client = boto3.client("budgets", region_name="us-east-1")

budget = client.describe_budget(
    AccountId=account,
    BudgetName="My Monthly Cost Budget"
)["Budget"]

limit = float(budget["BudgetLimit"]["Amount"])
spent = float(budget["CalculatedSpend"]["ActualSpend"]["Amount"])

remaining, usage_percent, warning = analyze_budget(limit, spent)

print(f"Monthly Budget: ${limit:.2f}")
print(f"Actual Spending: ${spent:.2f}")
print(f"Remaining Budget: ${remaining:.2f}")
print(f"Budget Used: {usage_percent:.1f}%")

if warning:
    print("WARNING: Budget threshold reached!")
else:
    print("Status: Within budget")

alerts = client.describe_notifications_for_budget(
    AccountId=account,
    BudgetName="My Monthly Cost Budget"
)["Notifications"]

print("\nAWS Budget Alerts:")
for alert in alerts:
    print(f"{alert['NotificationType']}: {alert['Threshold']}% - {alert['NotificationState']}")

from datetime import datetime, timedelta, timezone

today = datetime.now(timezone.utc).date()
start = today.replace(day=1).isoformat()
end = (today + timedelta(days=1)).isoformat()

ce = boto3.client("ce", region_name="us-east-1")

response = ce.get_cost_and_usage(
    TimePeriod={"Start": start, "End": end},
    Granularity="MONTHLY",
    Metrics=["UnblendedCost"],
    GroupBy=[{"Type": "DIMENSION", "Key": "SERVICE"}]
)

print("\nAWS Spending by Service:")

groups = response["ResultsByTime"][0]["Groups"]

if not groups:
    print("No spending data available yet.")
else:
    for item in groups:
        service = item["Keys"][0]
        cost = float(item["Metrics"]["UnblendedCost"]["Amount"])
        print(f"{service}: ${cost:.2f}")
