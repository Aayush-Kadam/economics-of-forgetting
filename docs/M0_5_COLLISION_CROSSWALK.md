# M0.5 Proposition-Level Collision Crosswalk

**Audit date:** 2026-09-19  
**Purpose:** close the two mandatory M0 collision risks and test the five-ingredient mechanism for economic, not notational, equivalence.

## Evidence standard and limitations

Hamilton and Cui were checked against the public SSRN record, the authors' 35-slide MSOM presentation, the authors' public theorem-verification code, and the matching dissertation chapter record. The slides state the model, Theorem 1, Lemma 2, and Theorem 3. The SSRN PDF itself was blocked by an automated access challenge in this environment; this is therefore a proposition-level check using author-provided substitutes, not a claim that every appendix line was inspected.

For Paulson Gjerde and Slotnick, the publisher's extended article page exposed the introduction, model description, qualitative comparative statics, and computational conclusions. A legally accessible full manuscript was not found. The crosswalk therefore distinguishes directly observed results from inferences and does not claim appendix-level verification.

For the other high-risk papers, accessible full text or detailed publisher versions from M0 were revisited where available.

## Five-ingredient test

| Paper | A: explicit record persistence | B: pre-event misconduct | C: productive post-event rehabilitation | D: reputation-dependent opportunity | E: institution-produced future-quality predictiveness | Entire mechanism? |
|---|---:|---:|---:|---:|---:|---:|
| Hamilton & Cui (2024) | Yes | Partial: disintermediation | No; provider quality is fixed | Yes | No | **No** |
| Paulson Gjerde & Slotnick (2004) | Yes | No | Partial: persistent quality investment, not adverse-history rehabilitation | Yes, through price/revenue | Partial feedback, no predictive decomposition | **No** |
| Bohren (2024) | Partial: persistent payoff state/rating interpretation | No lifecycle misconduct stage | Quality investment, not adverse-record rehabilitation | Yes | Yes in broad effort-to-state sense | **No** |
| Board & Meyer-ter-Vehn (2013) | Bayesian belief persistence, not chosen record decay | No | Quality investment/rebuilding | Yes | Yes in broad sense | **No** |
| Hauser (2024) | Bayesian decay/renewal | No | Quality investment and renewal | Yes | Yes in broad sense | **No** |
| Sperisen (2018) | Yes: bounded/fading memory | Strategic service action | No persistent rehabilitable state | Yes: hiring | No | **No** |
| Elul & Gottardi (2015) | Yes: access to default records | Repayment/default moral hazard | No persistent productive state | Yes: credit access | No | **No** |
| Mungan (2017) | Yes: expungement | Crime | Behavior after expungement, but no continuous productive rehabilitation stock | Informal sanctions | Not the proposed structural channel | **No** |

No checked paper contains all five ingredients. The closest economic union is obtained only by combining results from several papers.

## 1. Hamilton and Cui (2024), *Fresh Rating Systems: Structure, Incentives, and Fees*

1. **State variable:** an aggregate rating `R_t`; in the incentive model, provider quality `q` and a disintermediation rate `p` also matter.
2. **Quality:** the distribution generating transaction reviews; in the platform game each provider has true quality `q`.
3. **Fixed/endogenous:** adversarially switching across fixed distributions in the freshness problem; fixed provider quality in the platform-incentive problem.
4. **Effort changes future quality:** no.
5. **Current versus persistent effort effect:** disintermediation affects whether a review is generated, not a productive state.
6. **Separate public reputation:** yes, `R_t`.
7. **Evolution:** moving average, stated in slides as `R_t=(1-alpha)R_{t-1}+alpha g(s_t or NR)`.
8. **Explicit forgetting:** yes, an alpha-moving average and comparisons with sliding windows.
9. **Persistence exogenous:** the aggregation weight is a design choice.
10. **Chosen by platform:** yes; penalty review and fee are optimized, while moving-average weights solve a freshness objective.
11. **Analog of phi:** `1-alpha`.
12. **Analog of rho:** no intrinsic productive-state persistence parameter.
13. **phi/rho distinct:** no rho object exists.
14. **Reputation affects opportunity:** yes, hiring probability `h(R_t)`.
15. **Opportunity affects action:** yes, it disciplines on- versus off-platform transactions.
16. **Initial misconduct:** not in the proposed lifecycle sense; disintermediation is repeated platform avoidance.
17. **Persistence deters misconduct:** the paper studies penalties and fees, not a comparative static of record persistence on an initial harmful act.
18. **Post-adverse rehabilitation:** no.
19. **Long memory reduces rehabilitation:** no.
20. **Reduced rehabilitation worsens quality:** no; true provider quality is fixed.
21. **History causes predicted quality:** no.
22. **Predictiveness decomposition:** no.
23. **Hysteresis:** no productive-state hysteresis.
24. **Multiple regimes:** provider types separate at a quality threshold relative to penalty plus fee.
25. **Optimal memory:** moving average is asymptotically min-max for freshness; the platform chooses penalty and fee for revenue. This is not a welfare-optimal rehabilitation half-life.
26. **Lifecycle asymmetry:** no.
27. **Earned forgetting:** no; penalty reviews address inactivity.
28. **Main results observed:** Theorem 1 gives asymptotic convergence of myopically min-max oblivious weights to moving or simple averaging; Lemma 2 characterizes disintermediation by `q < beta+f`; Theorem 3 gives a tight 3/4 prior-free revenue approximation for penalty and fee.
29. **Duplicated proposed results:** age-weighted ratings; moving-average implementation; platform-chosen rating persistence as such.
30. **Distinct results:** productive rehabilitation, separate state persistence, lifecycle asymmetry, and institution-produced quality predictiveness.

**Classification: PARTIAL COLLISION.**

## 2. Paulson Gjerde and Slotnick (2004), *Quality and Reputation: The Effects of External and Internal Factors over Time*

1. **State variable:** installed long-term quality effort, quality outcomes, production/quantity, price, and reputation-relevant history.
2. **Quality:** product performance, affected by adverse quality and improvement activities.
3. **Fixed/endogenous:** endogenous.
4. **Effort changes future quality:** yes; long-term recruitment/training/process improvement persists.
5. **Current versus persistent effect:** explicitly separates short-term and long-term quality effort.
6. **Separate public reputation:** yes in the economic description; price depends on past and current quality.
7. **Evolution:** exponential-smoothing/half-life formulation according to the article and later technical summaries.
8. **Explicit forgetting:** yes.
9. **Persistence exogenous:** treated as a market-environment parameter.
10. **Chosen by planner/platform:** no.
11. **Analog of phi:** reputation half-life.
12. **Analog of rho:** persistence/half-life of long-term quality effort.
13. **phi/rho distinct:** yes. This distinction is prior art and cannot be claimed as new by itself.
14. **Reputation affects opportunity:** yes, via price and revenue.
15. **Opportunity affects effort:** yes, the firm optimizes quality expenditure.
16. **Initial misconduct:** no.
17. **Persistence deters misconduct:** no misconduct stage.
18. **Post-adverse rehabilitation:** no explicit adverse-record lifecycle stage.
19. **Long memory reduces rehabilitation:** persistent reputation can induce lower quality investment because the firm relies on past reputation, but this is not a post-adverse-history recovery theorem.
20. **Reduced effort worsens future state:** long-term effort can affect later quality; the reported comparative statics include deterioration under some persistence changes.
21. **History causes predicted quality:** a broad feedback exists through investment, but the paper does not frame or decompose predictive validity.
22. **Predictiveness decomposition:** no.
23. **Hysteresis:** not an identified central theorem.
24. **Multiple regimes:** comparative outcomes differ with quality versus price competition and persistence parameters.
25. **Optimal memory:** no institutional optimum over memory duration.
26. **Lifecycle asymmetry:** no.
27. **Earned forgetting:** no.
28. **Main results observed:** qualitative sufficient conditions for changing quality/quantity expenditures; computational comparative statics across market competition, reputation persistence, efficacy, and persistence of quality effort.
29. **Duplicated proposed results:** separating record and quality persistence; reputation persistence affects productive effort; half-life terminology.
30. **Distinct results:** common-policy pre-event deterrence/post-event discouragement, adverse-record recovery threshold, and predictiveness decomposition.

**Classification: HIGH COLLISION on primitives; PARTIAL COLLISION on the surviving mechanism. Overall: HIGH COLLISION.**

## 3. Bohren (2024), *Persistence in a Dynamic Moral Hazard Game*

1-5. The payoff-relevant state (e.g. product quality) is persistent and costly action changes its drift; this is genuine future-quality investment.  
6-13. The state may be interpreted as a rating, so the canonical application does not require a separate public record recursion and natural quality recursion; persistence can reflect technology or design.  
14-15. Small-player actions and firm revenue depend on the state, generating dynamic effort incentives.  
16-20. There is no initial-misconduct/post-record-rehabilitation lifecycle split or theorem that longer record retention discourages rehabilitation.  
21. Past incentives can affect future quality in the broad sense; this component is prior art.  
22-27. No informational-versus-produced predictiveness decomposition, chosen record half-life, or earned-forgetting mechanism. Recovery regions and multiple effort regimes occur.  
28. Main results characterize MPE/PPE, persistence as an incentive channel, and uniqueness conditions.  
29-30. Any claim that persistent ratings induce quality investment duplicates this paper; the separate-record lifecycle asymmetry remains distinct.

**Classification: HIGH COLLISION.**

## 4. Board and Meyer-ter-Vehn (2013, 2022) and Hauser (2024)

1-5. Hidden firm quality is endogenously managed by investment and may switch persistently.  
6-13. Public reputation is a Bayesian belief, not a mechanically chosen record with a distinct exponential retention parameter. Intrinsic quality transition rates are distinct from beliefs, but there is no planner choosing record memory.  
14-15. Reputation affects revenue and therefore investment.  
16-20. These models contain work/shirk cutoffs, low-reputation rebuilding, exit, and promotion, but not one initial misconduct decision followed by productive rehabilitation under the same retention rule.  
21. Beliefs influence investment and future quality, so the broad feedback is established prior art.  
22-27. No proposed predictiveness decomposition or deterrence-versus-rehabilitation comparative static in record persistence. Hauser has reputation cycles and endogenous renewal.  
28. Principal results characterize investment cutoffs, reputation dynamics, firm lifecycle, promotion, and reputation cycles.  
29-30. Reputation-induced quality and recovery cycles duplicate prior work; the record-policy lifecycle comparison remains distinct.

**Classification: HIGH COLLISION.**

## 5. Sperisen (2018)

The state is the observed record in the mechanic game; bounded memory observes recent periods while fading memory randomly samples past periods with declining probabilities. Hiring and signaling create reputational echoes. There is no separately accumulating productive quality stock, no rehabilitation technology `alpha`, and no pre/post lifecycle asymmetry. The main collision is design of fading memory and the claim that an intermediate memory technology can retain information while limiting harmful feedback.

**Classification: PARTIAL COLLISION.**

## 6. Elul and Gottardi (2015)

The relevant record is past default information; regulation restricts access. Repeated borrowing produces moral hazard, adverse selection, access effects, and a welfare comparison. Borrower actions do not build a distinct persistent human-capital/quality stock, and the paper does not derive post-record productive rehabilitation or institution-produced predictiveness.

**Classification: PARTIAL COLLISION.**

## 7. Mungan (2017)

The record is a criminal conviction that may be expunged at cost. The model explicitly studies general and specific deterrence and conditional second chances. It is therefore a serious collision for any generic “forgetting versus deterrence” claim. It does not model a continuous public-memory parameter separately from a productive state, opportunity-driven rehabilitation investment, or predictive decomposition.

**Classification: HIGH COLLISION for deterrence/expungement; PARTIAL COLLISION overall.**

## Endogenous-predictiveness terminology audit

Searches across “self-fulfilling reputation,” “belief-dependent investment,” “rating-dependent quality investment,” “reputational hysteresis,” “dynamic stigma and investment,” “policy-induced persistence,” and related terms locate many models in which reputation or beliefs change investment and therefore future quality. Board and Meyer-ter-Vehn, Bohren, Hauser, Ban-the-Box investment models, and models of national reputation already establish broad self-confirming or reputation-induced real outcomes. Accordingly:

- **Not novel:** reputation affects the future fundamental through investment.
- **Potentially distinct:** the retention rule itself changes the strength of this feedback, and the same retention increase has opposite pre-event and post-event incentive effects.
- **Unresolved until M3:** a structural decomposition of predictive power into signal persistence and institution-produced state persistence.

## Lifecycle-asymmetry verdict

No checked paper establishes the exact joint comparative static under one explicit record-memory parameter:

`d Pr(misconduct)/d phi < 0` before an adverse event and `d e_rehab/d phi < 0` after the event, with rehabilitation changing a distinct persistent state `x`.

The pieces exist separately, so novelty can attach only to the joint proposition and its conditions—not to either derivative, feedback from reputation to investment, or decay design alone.

## Final M0.5 verdict

**PROCEED TO M1 WITH FURTHER NARROWING**

