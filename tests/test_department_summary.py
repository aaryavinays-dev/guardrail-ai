from types import SimpleNamespace

from audit_repository import get_department_summary


class FakeQuery:
    def all(self):
        return [
            SimpleNamespace(
                department="Finance",
                action="BLOCK",
                risk_level="CRITICAL",
                risk_reasons="ssn detected, password detected",
            ),
            SimpleNamespace(
                department="Finance",
                action="ALLOW",
                risk_level="LOW",
                risk_reasons="",
            ),
            SimpleNamespace(
                department="Engineering",
                action="BLOCK",
                risk_level="HIGH",
                risk_reasons="api_key detected",
            ),
        ]


class FakeDB:
    def query(self, model):
        return FakeQuery()


def test_department_summary_groups_logs_by_department():
    summary = get_department_summary(FakeDB())

    departments = {
        item["department"]: item
        for item in summary["departments"]
    }

    assert departments["Finance"]["total_requests"] == 2
    assert departments["Finance"]["blocked_count"] == 1
    assert departments["Finance"]["critical_count"] == 1
    assert departments["Finance"]["top_risk_reasons"]["ssn detected"] == 1
    assert departments["Finance"]["top_risk_reasons"]["password detected"] == 1

    assert departments["Engineering"]["total_requests"] == 1
    assert departments["Engineering"]["blocked_count"] == 1
    assert departments["Engineering"]["critical_count"] == 0
    assert departments["Engineering"]["top_risk_reasons"]["api_key detected"] == 1