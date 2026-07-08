"""
Baseline Opportunity Scoring Framework
FlyRank Search Intelligence Capstone
"""

def opportunity_score(impressions, position):
    if position <= 0:
        return 0

    return impressions / position


# Example Usage
if __name__ == "__main__":
    score = opportunity_score(10000, 10)
    print(f"Opportunity Score: {score}")