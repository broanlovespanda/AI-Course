from production import AND, OR, NOT, PASS, FAIL, IF, THEN, \
     match, populate, simplify, variables
from zookeeper import ZOOKEEPER_RULES

# This function, which you need to write, takes in a hypothesis
# that can be determined using a set of rules, and outputs a goal
# tree of which statements it would need to test to prove that
# hypothesis. Refer to the problem set (section 2) for more
# detailed specifications and examples.

# Note that this function is supposed to be a general
# backchainer.  You should not hard-code anything that is
# specific to a particular rule set.  The backchainer will be
# tested on things other than ZOOKEEPER_RULES.


def backchain_to_goal_tree(rules, hypothesis):
    matching_rules = []
    runningOR = OR()
    for rule in rules:
        match_result = match(rule._action[0], hypothesis)
        if match_result != None:
            runningOR.append(populate(rule._action[0], match_result))
            conditional = rule._conditional
            runningCondition = AND()
            for condition in range(0, len(conditional)):
                condition2 = populate(conditional[condition], match_result)
                runningCondition.append(backchain_to_goal_tree(rules, condition2))
            runningOR.append(runningCondition)
    if len(runningOR) != 0:
        return simplify(runningOR)
    else:
        return hypothesis
# Here's an example of running the backward chainer - uncomment
# it to see it work:
print backchain_to_goal_tree(ZOOKEEPER_RULES, 'opus is a penguin')
