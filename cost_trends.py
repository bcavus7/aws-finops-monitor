import boto3
from datetime import date, timedelta
from cost_analysis import compare_costs

today = date.today()
this_month = today.replace(day=1)
last_month = (this_month - timedelta(days=1)).replace(day=1)
two_months_ago = (last_month - timedelta(days=1)).replace(day=1)

client = boto3.client("ce", region_name="us-east-1")

response = client.get_cost_and_usage(
    TimePeriod={
        "Start": two_months_ago.isoformat(),
        "End": this_month.isoformat()
    },
    Granularity="MONTHLY",
    Metrics=["UnblendedCost"],
    GroupBy=[{"Type": "DIMENSION", "Key": "SERVICE"}]
)

monthly_costs = {}

for period in response["ResultsByTime"]:
    month = period["TimePeriod"]["Start"]
    monthly_costs[month] = {
        item["Keys"][0]: float(
            item["Metrics"]["UnblendedCost"]["Amount"]
        )
        for item in period["Groups"]
    }

previous = monthly_costs.get(two_months_ago.isoformat(), {})
current = monthly_costs.get(last_month.isoformat(), {})

print(f"Comparing {two_months_ago:%B} vs {last_month:%B}")

if not previous and not current:
    print("No billing history available yet.")
else:
    for item in compare_costs(previous, current):
        print(
            f"{item['service']}: "
            f"${item['previous']:.2f} -> "
            f"${item['current']:.2f} | "
            f"{item['status']}"
        )
