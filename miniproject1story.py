import csv

def load_work_orders_csv(filename):
    work_orders = []
    with open(filename, "r", newline = "", encoding = "utf-8-sig") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if not row or row.get("id") is None or row["id"].strip() == "":
                continue
            row["id"] = int(row["id"])
            row["hours"] = int(row["hours"])
            work_orders.append(row)

    return work_orders
def status_summary(work_orders):
    summary = {}

    for wo in work_orders:
        status = wo["status"]
        summary[status] = summary.get(status, 0) + 1
    return summary
def priority_summary(work_orders):
    summary = {}
    for wo in work_orders:
        priority = wo["priority"]
        summary[priority] = summary.get(priority, 0) + 1
    return summary
def tech_summary(work_orders):
    
    summary = {}
    for wo in work_orders:
        tech = wo["tech"]
        status = wo["status"]
        summary[tech] = summary.get(tech, {})
        summary[tech][status] = summary[tech].get(status, 0) + 1
    return summary

def dashbaord(work_orders):
    print("Total Number of Workorders", len(work_orders))
    total_hours, avg_hours = total_and_average_hours(work_orders)
    print("Total Hours : ", total_hours)
    print("Average Hours :", avg_hours)

    print("\nSTATUS SUMMARY")
    for status, count in status_summary(work_orders).items():
        print(f"{status : >7} : {count}")
    print("\nPRIORITY SUMMARY")
    for priority, count in priority_summary(work_orders).items():
        print(f"{priority : >7} : {count}")
    print("\nTECHNICIAN DASHBOARD")
    for tech, statuses in tech_summary(work_orders).items():
        details = ",".join(f"{s} : {c}" for s,c in statuses.items())
        print(f"{tech} -> {details}")

def total_and_average_hours(work_orders):
    total_hours = sum(wo["hours"] for wo in work_orders)
    avg_hours = total_hours/len(work_orders) if work_orders else 0
    return total_hours, round(avg_hours, 2)


work_orders = load_work_orders_csv("work_orders.csv")
dashbaord(work_orders)

# update test 2026-01-02














































































































































    

       






    


