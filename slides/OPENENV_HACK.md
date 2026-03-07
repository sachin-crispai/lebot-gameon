# OpenEnv Hackathon SF — Participant Guide

## Event Overview
- **Event:** OpenEnv Hackathon SF
- **Host:** Cerebral Valley, in partnership with Shack15
- **Purpose:** Participants build RL environments and post-train a base model using OpenEnv.
- **Dates:** Saturday, March 7, 2026 to Sunday, March 8, 2026
- **Details Page:** https://cerebralvalley.ai/e/openenv-hackathon-sf/details
- **Submission Page:** https://cerebralvalley.ai/e/openenv-hackathon-sf/hackathon/submit

---

## 1. Join the Discord
### PyTorch Discord Server
- Join the **PyTorch Discord Server**: https://discord.gg/VBcf6VtfY6
- Participants will be given a **Hackathon Participant** role by an admin.
- This role grants access to the hackathon-specific channels.
- The Discord is used to:
  - interact with other hackers and sponsors,
  - introduce yourselves,
  - form teams.
- **Maximum team size:** 3
- If you do not receive your role within **24 hours** of joining, ping **@CV**.

### Discord username submission
- Participants must submit their Discord username here:
  - https://forms.gle/9K9uXZ26kjqGR8BA8
- The page notes that the hackathon will use the **OpenEnv Discord Channel**:
  - https://discord.gg/CN66NtjFVz
- Access to the hackathon channels is granted by assigning a role to the submitted Discord username.

---

## 2. Location
- **Venue:** Shack15
- **Address:** 1 Ferry Building, Suite 201, San Francisco, CA 94111

### Venue access
- Shack15 is on the **2nd floor** of the Ferry Building.
- Go up the Ferry Building elevator to the second floor.
- Turn left.
- The main entrance to Shack15 will be there.

### Parking
- Parking near the Ferry Building is **extremely limited**.
- Recommended alternatives:
  - Uber
  - Lyft
  - Public transportation
  - parking farther away

---

## 3. WiFi Information
- WiFi details removed for security. Ask organizers onsite.

---

## 4. Hackathon Schedule
### Saturday, March 7
- **9:00 AM:** Doors open, breakfast served, team formation
- **10:00 AM – 11:30 AM:** Kick-off presentations with:
  - Meta
  - Hugging Face
  - UC Berkeley
  - CoreWeave
  - OpenPipe
  - Unsloth AI
  - Fleet AI
  - Mercor
  - Scaler AI Labs
  - Snorkel AI
  - Patronus AI
  - Halluminate
  - Scale AI
- **11:30 AM:** Hacking begins
- **1:00 PM:** Lunch served
- **6:00 PM:** Dinner served
- **10:00 PM:** Doors close; re-entry not permitted

### Sunday, March 8
- **9:00 AM:** Doors open, breakfast served
- **1:00 PM:** Hacking stops; submissions due
- **1:15 PM:** First round judging begins
- **2:00 PM:** Lunch served
- **3:00 PM:** Final round judging begins
- **4:00 PM:** Winners announced and closing
- **5:00 PM:** Doors close

### Opening slides
- **OpenEnv Opening Slides.pdf**
- https://drive.google.com/file/d/1Ip-NnoIAnpTH7Mup5LKhriNhqriglpKr/view?usp=drive_link

---

## 5. Hackathon and Submission Rules
- **Open Source:** Repository must be public.
- **New Work Only:** Projects must be started from scratch during the hackathon.
- **No previous work** is allowed.
- **Team size:** Up to 3 members.
- **Banned projects:** Projects will be disqualified if they:
  - violate legal, ethical, or platform policies,
  - use code, data, or assets you do not have the rights to.
- Your project **must use OpenEnv** (**stable release 0.2.1**) deployed on **HF Spaces**.
- You **must show a minimal training script** for your environment using **Unsloth** or **HF TRL** in **Colab**.
- You **must upload a one-minute demo video to YouTube** talking about your submission.

---

## 6. Hackathon Problem Statements
Your project must address **at least one** of the **five required problem statements**.

Some problem statements also include **optional partner-sponsored sub-problem statements**.
- These are additional focus areas related to the main theme.
- A project may align with **multiple** partner sub-problem statements.
- However, a team can only be **judged for a maximum of two** partner sub-problem statements.
- Teams should **select up to two** when submitting.
- Matching projects are eligible for **extra partner prizes**, judged separately from the main track winners.
- **Each partner sub-problem statement prize:** **$10,000 USD**

### Statement 1: Multi-Agent Interactions
- Focus: cooperation, competition, negotiation, and coalition formation.
- Goal: train agents to model beliefs and incentives of others in partially observable settings.
- This supports theory-of-mind reasoning and emergent strategic behavior.

**Expected outcome:**
- An environment that can be used to train multi-agent task handling in an LLM.

**Example environments:**
- Market simulations
- Compute-allocation negotiations
- Collaborative puzzle worlds
- Mixed cooperative/competitive strategy games

**Partner sub-themes:**
- **Fleet AI — Scalable Oversight:** Environments that train oversight agents to monitor, analyze, and explain the behavior of other AI agents operating in complex, multi-agent settings.
- **Halluminate — Multi-Actor Environments:** Build a realistic environment where an agent interacts with and manages multiple actors (agents) to discover and achieve the task.

### Statement 2: (Super) Long-Horizon Planning & Instruction Following
- Focus: environments requiring deep, multi-step reasoning with sparse or delayed rewards.
- Goal: enable agents to decompose goals, track state over extended trajectories, and recover from early mistakes.
- Objective: push beyond shallow next-token reasoning toward structured planning and durable internal representations.

**Expected outcome:**
- An environment that can capture and improve LLM behavior on challenging long-horizon tasks that need long-running sessions beyond context memory limits.

**Example environments:**
- Research-planning simulators
- Large-scale codebase refactoring tasks
- Strategic resource management worlds
- Long-horizon logistics optimization
- Extremely complicated long-horizon instruction following (for example, 300 scattered instructions)

**Partner sub-themes:**
- **Mercor:** Make an environment with capped/uncapped rewards where frontier model rewards scale with token output.
- **Scale AI:** Environments for long-horizon workflows for non-code business use cases, focusing on Sales, Project Management, or HR & IT.

### Statement 3: World Modeling
#### Statement 3.1: Professional Tasks
- Focus: environments that require real interaction with tools, APIs, or dynamic systems where the model is expected to do real hard work instead of exploiting shortcuts.
- Goal: enable agents to maintain consistent internal state, update beliefs based on outcomes, and orchestrate multi-step workflows.
- Objective: strengthen causal reasoning and persistent world models.

**Expected outcome:**
- An environment capturing nuances of a defined partially observable world and improving LLM interaction with it.

**Example environments:**
- Dynamic browser/API ecosystems
- Enterprise applications
- Scientific workflow loops (papers -> code -> experiments)
- Economic simulations with feedback
- Tool-discovery benchmarks

**Partner sub-theme:**
- **Scaler AI Labs:** Multi-App RL Environment for Enterprise Workflows — create RL environments to demonstrate complex workflows, business rule nuances, etc. in a large enterprise.

#### Statement 3.2: Personalized Tasks
- Focus: environments for real personalized task handling, such as replying to personal messages or handling dinner conflicts due to work conflicts.
- Think personal assistant tasks.

**Expected outcome:**
- An environment that gives the model a realistic simulation of handling personal tasks, conflicts, and delegations.

**Example environments:**
- Executive assistant meeting planner
- Dinner and drive planning
- Email and message replying

**Partner sub-theme:**
- **Patronus AI:** Consumer Workflows with Schema Drift — multi-step consumer workflow environments where the underlying data schemas, API contracts, terms and conditions, policies, and rules change.

### Statement 4: Self-Improvement
- Focus: environments where agents learn to generate new challenges, escalate difficulty, and improve through self-play or adaptive curricula.
- Goal: recursive skill amplification rather than optimizing fixed tasks.

**Expected outcome:**
- An environment for improving self-play of an LLM over a defined set of tasks.

**Example environments:**
- Self-play negotiation arenas
- Auto-generated math/proof tasks
- Evolving coding competitions
- Adaptive RL curricula

**Partner sub-theme:**
- **Snorkel AI:** Simulated Experts-in-the-Loop — an environment that simulates interactions with real subject-matter experts, with changing requirements and preferences.

### Statement 5: Wild Card — Impress Us!
- The organizers do not want to limit ideas that do not fit the named categories.
- They explicitly want creative, out-of-the-box tasks that meaningfully add value to LLM training on a certain task.

### Challenge document
- **Hackathon Challenge.pdf**
- https://drive.google.com/file/d/1L-wXy0-WX63_lvVPOTFpsy5j5Kn9zs8T/view?usp=drive_link

---

## 7. CV Hackathon Winners
- Winners page:
  - https://cv.inc/hackathons
- The linked site describes Cerebral Valley as:
  - “The premier ecosystem for AI builders, researchers, and founders. Join thousands of ML engineers and entrepreneurs shaping the future of artificial intelligence.”

---

## 8. OpenEnv Provided Resources
Participants are told to read the full slideshow, which includes:
- OpenEnv fundamentals and architecture
- Local development, Docker, and HF Spaces deployment
- OpenEnv in practice
- Training (TRL & Unsloth)
- How to access infrastructure, including the GPU request form

### Technical content PDF
- **OpenEnv Hackathon Technical content.pdf**
- https://drive.google.com/file/d/1oXW4l7BJgaUQ8wj8vAFYWqPUnwzT52-A/view?usp=sharing

---

## 9. Partner Provided Resources
### Unsloth AI
- Unsloth notebooks and GRPO reasoning RL notebooks:
  - https://unsloth.ai/docs/get-started/unsloth-notebooks#grpo-reasoning-rl-notebooks

### Mercor
- Dataset:
  - https://huggingface.co/datasets/mercor/apex-agents
- Archipelago repo for running the eval:
  - https://github.com/Mercor-Intelligence/archipelago
- APEX-Agents paper:
  - https://arxiv.org/abs/2601.14242

### Hugging Face
- **$30 in compute and inference credits**
- Set up a Hugging Face account here:
  - https://huggingface.co/join
- Then follow:
  - https://huggingface.co/openenv-community
- The page states that you will be granted **$30 of compute and inference credits**.

### Northflank
- **Each team gets an H100**
- Northflank instructions:
  - https://northflank.notion.site/Northflank-Docs-OpenEnv-Hackathon-2496d14c785180c6a595e6776e3118ba
- Northflank GPU/deployment request form:
  - https://docs.google.com/forms/d/e/1FAIpQLSd2bxx5jAXE8D3FjF7OVekSxwpDVMf1LWE3Z-g4FZoDJ4W6xg/viewform
- The form is described as being for access to H100 capacity and deployment infrastructure once the team is formed.
- The page also says to join the **NorthFlank Discord channel** for questions, but no direct Discord link is shown in the extracted page text.

### Cursor
- **$50 in Cursor credits**
- Apply here:
  - https://forms.gle/2L86ksEa7uFxNdoT8
- The page says to fill out the form to receive **$50 in Cursor Credits** on the day of the OpenEnv Hackathon.

---

## 10. Judging & Submissions
- Judging takes place on **Sunday, March 8**.
- Judges evaluate **technical demos**.
- Teams are asked to show what they built to solve the problem statements.
- **Do not show a presentation.**
- Organizers will check that the project was built entirely during the event.
- No previous work is allowed.

### Submission requirements
- Submit here:
  - https://cerebralvalley.ai/e/openenv-hackathon-sf/hackathon/submit
- In the submission form, teams must:
  - upload a **one-minute demo video on YouTube** talking about the submission,
  - show a **minimal training script** for the environment using **Unsloth** or **HF TRL** in **Colab**.
- Projects must use **OpenEnv stable release 0.2.1** deployed on **HF Spaces**.

### Judging criteria
- **Environment Innovation (40%)**
  - Is the environment novel, creative, or challenging?
  - Does it meaningfully test the agent’s behavior?
- **Storytelling (30%)**
  - Does the team clearly explain the problem, environment, and agent behavior?
  - Is the demo engaging and easy to follow?
- **Training Script Showing Improvement in Rewards (20%)**
  - Does the demo provide observable evidence of training progress, such as reward curves, metrics, or before/after behavior?
- **Reward and Training Pipeline Setup (10%)**
  - Is the reward logic coherent, and does the pipeline produce meaningful improvement in the agent’s inference and behavior?

### Judging process
Judging proceeds in **two rounds**:
1. Hackers are assigned groups of judges.
   - Approximately **3 minutes** to pitch
   - Followed by **1–2 minutes** of Q&A
2. The **top six teams** advance to demo on stage to a panel of judges.
   - Approximately **3 minutes** to pitch
   - Followed by **2–3 minutes** of Q&A

---

## 11. Prizes
- **1st Place:** $15,000 USD cash
- **2nd Place:** $9,000 USD cash
- **3rd Place:** $6,000 USD cash

---

## Contact
- Email: wania@cerebralvalley.ai
- Or message on Discord

---

## Quick Links
- Event details: https://cerebralvalley.ai/e/openenv-hackathon-sf/details
- Submission page: https://cerebralvalley.ai/e/openenv-hackathon-sf/hackathon/submit
- PyTorch Discord: https://discord.gg/VBcf6VtfY6
- OpenEnv Discord channel: https://discord.gg/CN66NtjFVz
- Discord username form: https://forms.gle/9K9uXZ26kjqGR8BA8
- Opening slides: https://drive.google.com/file/d/1Ip-NnoIAnpTH7Mup5LKhriNhqriglpKr/view?usp=drive_link
- Challenge PDF: https://drive.google.com/file/d/1L-wXy0-WX63_lvVPOTFpsy5j5Kn9zs8T/view?usp=drive_link
- Technical content PDF: https://drive.google.com/file/d/1oXW4l7BJgaUQ8wj8vAFYWqPUnwzT52-A/view?usp=sharing
- CV hackathons: https://cv.inc/hackathons
- Unsloth docs: https://unsloth.ai/docs/get-started/unsloth-notebooks#grpo-reasoning-rl-notebooks
- Mercor dataset: https://huggingface.co/datasets/mercor/apex-agents
- Archipelago repo: https://github.com/Mercor-Intelligence/archipelago
- APEX-Agents paper: https://arxiv.org/abs/2601.14242
- Hugging Face signup: https://huggingface.co/join
- OpenEnv community on Hugging Face: https://huggingface.co/openenv-community
- Northflank docs: https://northflank.notion.site/Northflank-Docs-OpenEnv-Hackathon-2496d14c785180c6a595e6776e3118ba
- Northflank GPU request form: https://docs.google.com/forms/d/e/1FAIpQLSd2bxx5jAXE8D3FjF7OVekSxwpDVMf1LWE3Z-g4FZoDJ4W6xg/viewform
- Cursor credits form: https://forms.gle/2L86ksEa7uFxNdoT8

---

## Notes
- The page includes a standalone selected string: `4RGvhbN2$E`. It is not explained anywhere in the visible extracted content.
- The page also contains a generated table of contents mirroring the main sections.
- The extracted page text includes some duplicated markup artifacts from the browser capture.
