from src.dfc import register_proposal, simulate_flag_impact


def test_register_proposal():
    proposal = register_proposal({"flag": True}, "user1")
    assert proposal["status"] == "PENDING"
    assert proposal["user_id"] == "user1"


def test_simulate_flag_impact():
    proposal = {"data": {"flag": True}}
    impact = simulate_flag_impact(proposal)
    assert impact["score_shift"] == 1
