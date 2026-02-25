# Sample Conversation Threads for Demo

## Scenario 1: Risk/Compliance Decision
"""
From: Sarah Chen <s.chen@wealthsimple.com>
To: Risk Committee <risk@wealthsimple.com>
Subject: New crypto trading feature - compliance review

Hey team,

We're looking to launch crypto trading for our premium users by Q2. Marketing is pushing hard for this given competitor pressure.

Key considerations:
- Regulatory landscape is still evolving in Canada
- We'd need additional KYC procedures for crypto trades
- Potential AML implications with large crypto positions
- Our current infrastructure can handle it technically

I'm leaning toward a phased rollout - start with BTC/ETH only, $10K daily limits, enhanced monitoring.

Thoughts? We need to decide by Friday to hit the Q2 timeline.

Sarah

---

From: Mike Rodriguez <m.rodriguez@wealthsimple.com>
Reply: I'm concerned about the regulatory risk. FINTRAC guidance on crypto reporting is still unclear. Can we get legal sign-off first?

---

From: Legal Team <legal@wealthsimple.com>
Reply: We can proceed with enhanced due diligence but recommend starting even smaller - $5K limits and BTC only initially.

---

From: Sarah Chen
Reply: Agreed. Let's go with BTC only, $5K daily limits, and full rollout pending regulatory clarity. I'll own the implementation timeline.
"""

## Scenario 2: Product Launch Decision  
"""
Slack conversation - #product-launch channel

Alex Kim: Folks, we have a problem. The new portfolio rebalancing feature has a bug that affects users with >$500K portfolios. It's calculating tax efficiency incorrectly.

Jamie Walsh: How bad is the impact?

Alex Kim: About 3% of users could see suboptimal tax outcomes. Not huge dollar amounts but not great either.

Jamie Walsh: Options?
1. Delay launch by 2 weeks to fix
2. Launch with known issue, fix in patch
3. Launch but exclude high-net-worth users temporarily

Sarah Liu: Marketing has already announced the March 15 launch date. Delay would be embarrassing.

Alex Kim: I vote for option 3. We can enable the feature for <$500K users immediately, fix the bug, then roll out to everyone.

Jamie Walsh: Risk is that HNW users might feel excluded. But I agree - better than broken functionality.

Alex Kim: I'll handle the communication to affected users. Timeline: launch March 15 for most users, full rollout by March 30.

Sarah Liu: Approved. I'll update marketing materials to reflect phased rollout.
"""

## Scenario 3: Customer Incident Escalation
"""
From: Customer Success <cs@wealthsimple.com>
To: Product Team <product@wealthsimple.com>
Subject: URGENT - Trading halt affecting 50+ users

Team,

We have a critical issue. Our trading system is rejecting orders for about 50 users who have perfectly valid accounts. They're seeing "insufficient funds" errors even with adequate cash balances.

Customer impact:
- Users missing market opportunities
- Multiple complaints on social media  
- Some threatening to leave platform

Technical team says it's a caching issue that could take 6-8 hours to fully resolve.

Options:
1. Wait for full technical fix (6-8 hours)
2. Manual override for affected users (30 min per user)
3. Offer trading fee credits as compensation

I recommend option 2 + 3. We manually enable trading for these users immediately AND offer compensation.

This needs executive approval given the manual override process.

Who can authorize this approach?

Mike Chen - Customer Success Lead

---

From: Head of Product
Reply: Approved for manual override. I'll personally authorize each one. Also approved for trading fee credits for affected users.

---

From: Mike Chen  
Reply: Perfect. I'll coordinate with ops team. Should have everyone back online within 2 hours.
"""
