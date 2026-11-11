from cost_analysis import compare_costs

def test_cost_spike():
    result = compare_costs({"EC2": 100}, {"EC2": 140})
    assert result[0]["status"] == "COST SPIKE"
    assert result[0]["percent"] == 40

def test_new_service():
    result = compare_costs({}, {"RDS": 30})
    assert result[0]["status"] == "NEW SERVICE"

def test_cost_decrease():
    result = compare_costs({"S3": 20}, {"S3": 18})
    assert result[0]["status"] == "OK"
    assert result[0]["difference"] == -2

def test_no_change():
    result = compare_costs({"EC2": 100}, {"EC2": 100})
    assert result[0]["status"] == "OK"
