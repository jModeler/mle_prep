# Tubi ML Breadth & Depth — 27-Day Prep Plan

**Interview date:** ~2026-06-20 (two days after the coding round)
**Format:** 60 min, **verbal only**, no coding, with a Tubi MLE
**Daily budget:** ~30 min in parallel with `PREP_PLAN.md` (coding prep), bumping to a full day on 2026-06-19
**Goal:** show **breadth** across all the PDF's focus areas, with **depth in 1–2 specialties** + production-grounded stories from your real work.

---

## Strategy in one paragraph

You already have production ML intuition; the round will test whether you can **articulate it under pressure with trade-offs and follow-ups**. Most candidates regurgitate definitions. Staff signal = "we hit X in production, here's why we chose Y over Z, here's what we'd change at 10× scale." Spend ~30 min/day building short verbal notes per topic, drill the two depth specialties harder, and finish with two verbal mocks the day before. **Talk out loud during prep. Don't just read.**

---

## Depth specialty recommendation (pick & commit by Day 7)

1. **Recommendation systems & ranking** (primary) — Tubi is a content platform, this is the highest-leverage depth. Cover: collaborative filtering → matrix factorization → two-tower neural retrieval → ranking funnel → learning-to-rank → cold start → exploration. Have a story.
2. **ML in production / model lifecycle** (secondary) — leverages your day job. Cover: feature stores, online vs batch inference, monitoring/drift, retraining cadence, A/B testing & off-policy eval, staged rollouts. Have a story.

If your production background is in something else (search, fraud, NLP), swap (2) accordingly — but keep recsys as (1) given Tubi's domain.

---

## Tubi-relevant ML/DL applications — frame answers around these

Staff MLEs at a Netflix-like platform are typically thinking about:

- **Homepage personalization** — row/shelf selection, ordering within a row, real-time signals
- **Candidate generation → ranking funnel** — millions of titles, two-stage system (recall then precision)
- **Two-tower embeddings** — user tower + item tower, ANN serving (FAISS / ScaNN), trained with in-batch negatives
- **Sequential / session-based recsys** — what you watched in this session matters; SASRec, BERT4Rec, Transformer-based next-item
- **Cold start** — new titles, new users, region launches (Tubi is FAST-ad-supported, lots of catalog churn)
- **Search** — query understanding, semantic search (embed query + title), hybrid retrieval
- **Content understanding** — video/audio embeddings, metadata enrichment, auto-tagging, NSFW/safety
- **Ads** (Tubi is AVOD) — CTR prediction, pacing, frequency capping, ad-pod assembly, bid optimization
- **Exploration** — contextual bandits for new content surfacing, Thompson sampling
- **Causal & A/B** — interleaving for ranking eval, CUPED for variance reduction, off-policy evaluation when bandits/RL are involved
- **MLOps** — feature stores (online + offline parity), drift detection, retraining triggers, shadow/canary deploys

When asked about almost any topic, **anchor at least one example to a Tubi-like use case.** Reviewers love this.

---

## Staff-level verbal habits — drill before every mock

1. **Structure your answer.** "Two-sentence definition → when used → 2 trade-offs → 1 production gotcha → ask if they want depth." 30–60 seconds total.
2. **Use the language of trade-offs.** "X is better when you have lots of data; Y wins when labels are scarce." Always name two alternatives.
3. **Reach for production stories.** "We deployed model X for problem Y. The interesting part was Z." One per topic minimum.
4. **Bridge to scale.** "At Tubi-scale, this would need..." even if not asked. Free staff-signal.
5. **Anticipate the follow-up.** When you finish an answer, the interviewer is choosing a probe. Pre-empt it: "I should note one nuance..."
6. **Comfortable with 'I don't know'.** Better to say "I haven't worked with X; here's what I'd read first and how I'd reason from first principles" than to bluff. Bluffing is the fastest way to a no-hire.
7. **Math sketch, not derivation.** Know the formula and what each term means. Don't try to derive on a whiteboard verbally — it kills your time.

---

## How to use this plan

- Each day below is **~30 min** in parallel with the coding plan. Hit it before or after your coding block.
- Per day: write a **short note** in `bd_notes/<topic>.md` (or a personal doc) using this template:
  - **What it is** (1 sentence)
  - **When/why used** (2–3 bullets)
  - **Trade-offs** vs nearest alternative
  - **Math sketch** (formula + what each term means)
  - **Production gotcha** (1 bullet)
  - **Tubi/recsys connection** (1 bullet)
  - **My story** (1 paragraph from your real work)
  - **Likely follow-ups** (3 bullets)
- The note is your **verbal script**. Practice saying it out loud, with a timer, in 60 seconds.

---

## Phase 1 — Foundations & classical ML (Days 1–7)

Your coursework is reinforcing these. Make these the "easy fluency" portion — drill articulation, not learning new material.

### Day 1 — Sun 2026-05-24 — Major categories of ML
- [ ] Supervised, unsupervised, semi-supervised, self-supervised, reinforcement, anomaly. One Tubi example per category (e.g., SSL pretraining of content embeddings).
- [ ] Verbal drill: "Walk me through the major flavors of ML and when you'd use each" — 90 seconds.

### Day 2 — Mon 2026-05-25 — Bias-variance + regularization
- [ ] Bias-variance trade-off in one sentence; L1 vs L2 (sparsity vs shrinkage); dropout; early stopping; data augmentation.
- [ ] Tubi angle: how does this show up in CTR models with very wide feature spaces?

### Day 3 — Tue 2026-05-26 — Decision trees & ensembles
- [ ] Single tree → bagging (RF) → boosting (GBM, XGBoost, LightGBM). When to pick each. Feature importance methods (gain, SHAP).
- [ ] Tubi angle: ranking with GBM (LambdaMART) is still a strong baseline. Why? When would you move off it?

### Day 4 — Wed 2026-05-27 — ML statistics & metrics
- [ ] Classification: precision/recall/F1, ROC-AUC vs PR-AUC, calibration (Platt, isotonic).
- [ ] Ranking: **nDCG, MAP, MRR, Hit@K, Recall@K** — know which to use when.
- [ ] Tubi angle: offline metric vs online metric divergence — when nDCG goes up but watch-time doesn't. Why?

### Day 5 — Thu 2026-05-28 — Imbalanced data, missing data, outliers
- [ ] Class imbalance: SMOTE, class weights, focal loss, threshold tuning, stratified sampling.
- [ ] Missing data: drop / mean-impute / model-based / "missing is informative" flag.
- [ ] Outliers: detection (isolation forest, LOF) vs handling (clip, winsorize, robust loss).

### Day 6 — Fri 2026-05-29 — Clustering
- [ ] K-Means (parametric, spherical), hierarchical (dendrogram, no K needed), DBSCAN (density, handles noise), GMM (soft).
- [ ] How to choose K: elbow, silhouette, gap statistic. When clustering is the wrong tool.
- [ ] Tubi angle: user segmentation vs personalization — when do you cluster vs use per-user embeddings?

### Day 7 — Sat 2026-05-30 — Hyperparameter optimization + algorithm selection
- [ ] Grid → random → Bayesian (Optuna, Hyperopt) → BOHB / Hyperband.
- [ ] No Free Lunch theorem — what it actually means in practice.
- [ ] **End of Phase 1 verbal mock (15 min):** pick 3 random topics from this week, give a 60-sec answer + answer one follow-up per topic. Record yourself.

---

## Phase 2 — Recsys + ranking + embeddings (Days 8–14) ⭐ DEPTH FOCUS

This is the week to **go deep**. Tubi is asking you about its core problem.

### Day 8 — Sun 2026-05-31 — Embeddings (what & how)
- [ ] One-hot vs dense embeddings; word2vec (skip-gram, CBOW); contrastive learning (SimCLR, in-batch negatives); BERT-style.
- [ ] Properties: similarity preservation, transferability, dimensionality choice.
- [ ] Tubi angle: title embeddings from co-watch graph vs from metadata vs from content (video/audio).

### Day 9 — Mon 2026-06-01 — Recsys foundations
- [ ] Content-based vs collaborative; user-user CF, item-item CF; matrix factorization (SVD, ALS); implicit feedback (Hu, Koren, Volinsky).
- [ ] Why MF dominated for a decade; why it lost to neural models.
- [ ] **My story slot:** which recsys flavor have you worked with? Have the story ready.

### Day 10 — Tue 2026-06-02 — Modern neural recsys
- [ ] Two-tower architecture (user tower + item tower, dot product at top, in-batch negatives for training, ANN at serving).
- [ ] Candidate generation vs ranking — the **funnel** (retrieve thousands → rank hundreds → re-rank/business rules → present dozens).
- [ ] Wide-and-deep, DeepFM, DCN for ranking.

### Day 11 — Wed 2026-06-03 — Sequential / session-based recsys
- [ ] Why sequence matters (recent watches >> historical preferences for streaming).
- [ ] GRU4Rec → SASRec (self-attention) → BERT4Rec (masked). How they differ from collaborative filtering conceptually.
- [ ] Tubi angle: a session-aware model for "what to autoplay next" vs a session-agnostic homepage model.

### Day 12 — Thu 2026-06-04 — Learning to rank
- [ ] **Pointwise** (regression on relevance score), **pairwise** (RankNet, LambdaRank), **listwise** (ListNet, LambdaMART surrogates for nDCG).
- [ ] Why pairwise beats pointwise; why listwise beats pairwise (sometimes).
- [ ] Loss functions that are differentiable surrogates for nDCG.

### Day 13 — Fri 2026-06-05 — Cold start
- [ ] **New user**: content-based fallback, demographic/contextual priors, onboarding signals, contextual bandits.
- [ ] **New item**: content embedding fallback (use side-features in the item tower), forced exploration ("introduce new titles" slot), Thompson sampling.
- [ ] Tubi angle: new-title launches are constant — how does the system surface them without nuking metrics?

### Day 14 — Sat 2026-06-06 — Exploration / bandits / RL
- [ ] Multi-armed bandits: ε-greedy, UCB, **Thompson sampling**. When to prefer each.
- [ ] Contextual bandits: LinUCB, neural bandits.
- [ ] RL framing of recsys: state (user history), action (item), reward (engagement) — and why pure RL hasn't taken over (off-policy issues, reward hacking, evaluation hard).
- [ ] **End of Phase 2 verbal mock (20 min):** 5-min deep dive on "design a recommendation system for Tubi's homepage," then 10 min of follow-ups (cold start, evaluation, scale).

---

## Phase 3 — Deep learning, modern, & Tubi-applied (Days 15–21)

DL fundamentals you need to articulate; modern arch you should at least have a working mental model of.

### Day 15 — Sun 2026-06-07 — Deep learning basics
- [ ] Backprop in one sentence (chain rule, reverse-mode autodiff); SGD vs momentum vs **Adam** (adaptive learning rates per param).
- [ ] Vanishing/exploding gradients; batch norm vs layer norm vs no norm; weight init (Xavier, He).
- [ ] When DL beats GBM and when it doesn't.

### Day 16 — Mon 2026-06-08 — Attention & Transformers
- [ ] **Self-attention** formula (QK^T / sqrt(d), softmax, weight V). What Q/K/V represent intuitively.
- [ ] Multi-head: why multiple heads (different relationship types).
- [ ] Positional encoding (sinusoidal vs learned vs RoPE).
- [ ] Encoder-only (BERT) vs decoder-only (GPT) vs encoder-decoder (T5).

### Day 17 — Tue 2026-06-09 — LLMs
- [ ] Pre-training (next-token prediction at scale), instruction fine-tuning (SFT), RLHF (reward model + PPO), DPO (no RL).
- [ ] **RAG** — when LLM weights aren't enough; retriever + generator; chunking + embedding strategies.
- [ ] Hallucinations (causes + mitigations: RAG, citations, lower temperature, constrained decoding).
- [ ] Tubi angle: where could LLMs realistically fit? Content metadata enrichment, search query understanding, synopsis generation.

### Day 18 — Wed 2026-06-10 — Reinforcement learning (high level)
- [ ] Policy vs value function; on-policy vs off-policy; Q-learning vs policy gradients vs actor-critic.
- [ ] RLHF connection: reward model is a learned value function; PPO is the policy update.
- [ ] Why pure RL is rare in production recsys.

### Day 19 — Thu 2026-06-11 — A/B testing, causal inference, off-policy eval
- [ ] A/B testing pitfalls: SRM, peeking, novelty effects, network effects.
- [ ] **Interleaving** for ranking (TDI) — why it's higher-power than A/B for ranking.
- [ ] **CUPED** — variance reduction with pre-period covariates.
- [ ] **Off-policy evaluation** — IPS, doubly robust, when needed (bandits/RL).
- [ ] **Uplift modeling** — meta-learners (T, S, X-learner) for treatment effects.

### Day 20 — Fri 2026-06-12 — Production ML & lifecycle ⭐ SECONDARY DEPTH
- [ ] **Feature stores** — offline/online parity, point-in-time correctness, why it matters.
- [ ] **Batch vs real-time inference** — when to pick which; latency budgets.
- [ ] **Monitoring** — feature drift, prediction drift, label drift, concept drift. Detection methods (KS test, PSI).
- [ ] **Retraining triggers** — calendar, drift, performance regression.
- [ ] **Deployment** — shadow → canary → ramped → full; rollback criteria.
- [ ] **My story slot:** the production lifecycle story you can tell in 3 minutes.

### Day 21 — Sat 2026-06-13 — Tubi end-to-end synthesis
- [ ] Pick 3 Tubi product surfaces and design the ML for each, verbally, 5 min each: (1) homepage personalization, (2) "Up Next" autoplay, (3) ad CTR prediction.
- [ ] For each: data, features, model choice, evaluation, scale concerns, cold start, A/B plan.
- [ ] **End of Phase 3 verbal mock (30 min):** mixed-topic free-form; cover at least 6 different topics, 1 deep dive, 2 production stories.

---

## Phase 4 — Coding-focus blackout (Days 22–25) + final push (Days 26–27)

### Days 22–25 (2026-06-14 to 2026-06-17) — **Coding-only.**
- [ ] No new B&D material. Optional: 10-min skim of one note before bed. Don't burn energy.

### Day 26 — Wed 2026-06-18 — Coding interview day
- [ ] Morning: coding interview. Afternoon: nap / decompress.
- [ ] **Evening (45 min max):** re-read the two depth specialty note bundles (recsys, prod ML). Nothing else.

### Day 27 — Thu 2026-06-19 — Dedicated B&D day ⭐
- [ ] **AM (90 min):** read all your topic notes. Mark any you can't explain in 60 seconds.
- [ ] **Mock #1 (45 min):** ask a friend (or use a self-prompt list) to fire 8 random questions across the PDF topics. Time each answer to 60–90 sec. Record. Listen back.
- [ ] **Lunch + break.**
- [ ] **PM (60 min):** address the weakest 2–3 topics from Mock #1.
- [ ] **Mock #2 (30 min):** "deep dive on recsys" — 10 min monologue, then 20 min of follow-ups.
- [ ] **Evening:** light dinner, no screens after 9 pm. Sleep 8 hr.

### Day 28 — Fri 2026-06-20 — B&D interview day
- [ ] AM: walk, light breakfast, scan your 1-page topic index (NOT all notes).
- [ ] **First 2 min of interview:** listen carefully. Repeat the question back if it's ambiguous.
- [ ] **Per topic:** structured 60-sec answer → pause → "want me to go deeper on X or Y?" — gives the interviewer agency, signals breadth.
- [ ] You've earned this.

---

## Anticipated question bank — add to this as you go

Use these as self-prompts during practice. Add your own as you spot patterns.

**Recsys / ranking (depth)**
- Design a recommendation system for Tubi's homepage. Walk me through the funnel.
- When would you use a two-tower model vs LambdaMART for ranking?
- How do you handle cold start for new content?
- Your nDCG went up 2% offline but watch-time is flat in A/B. What's going on?
- How would you evaluate a recommender system without an A/B test?

**Embeddings**
- How would you generate title embeddings at Tubi? Compare 3 approaches.
- Why dense embeddings beat one-hot for categorical features in deep models?
- How do you serve embeddings at low latency for millions of items?

**Classical ML**
- When does XGBoost beat a neural net? When does it lose?
- Walk me through bias-variance with a concrete example.
- Class imbalance in CTR prediction — what's your playbook?

**Deep learning / modern**
- Explain self-attention as if I'm a backend engineer.
- What does RLHF actually do? Why not just SFT?
- Where could RAG help at Tubi?

**Production / lifecycle**
- How do you detect model drift? What do you do about it?
- Walk me through how you'd ship a new ranking model from offline metric to full rollout.
- Tell me about a model you launched. What was the hardest part?

---

## Tracking notes

- Day 1:
- Day 2:
- ...
