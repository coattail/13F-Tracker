# Mobile Change Table Width Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the mobile company column in Quarter-over-Quarter Position Changes readable by preventing the grid from collapsing below a usable width.

**Architecture:** Keep the existing rendered markup and grid layout. Add a mobile-only overflow boundary around the existing group container, then assign the header and row list a shared minimum width so they remain aligned and can scroll horizontally together when needed.

**Tech Stack:** Static HTML, CSS, vanilla JavaScript, Playwright/browser-based visual verification.

---

### Task 1: Capture the mobile regression

**Files:**
- Modify: `styles.css`
- Verify: browser viewport at approximately 390px wide

- [ ] **Step 1: Reproduce the issue before the fix**

Open the local site on a narrow mobile viewport, navigate to an institution with long company names, and confirm the company column collapses into near-character wrapping in the changes ranking table.

- [ ] **Step 2: Record the expected behavior**

Expected after the fix:
- the company column remains readable,
- the header and body columns stay aligned,
- horizontal overflow is contained within the ranking table area only.

### Task 2: Implement the minimum-width mobile table layout

**Files:**
- Modify: `styles.css`

- [ ] **Step 1: Add mobile-only scrolling behavior**

Inside the existing mobile media query, allow the change group to scroll horizontally only when needed.

- [ ] **Step 2: Give the header and body the same minimum width**

Apply a shared `min-width` to `.change-grid-head` and `.change-pro-list` so the company column has enough room and both structures stay aligned.

- [ ] **Step 3: Preserve the current wrapping and visual styling**

Do not alter the generated HTML or company-label content; the fix should come from layout constraints only.

### Task 3: Verify and ship

**Files:**
- Verify: `styles.css`, rendered local page, Git history

- [ ] **Step 1: Verify mobile rendering**

Use a narrow viewport and confirm long labels such as `Alphabet (GOOGL) · A` read normally rather than stacking one or two characters per line.

- [ ] **Step 2: Verify desktop rendering**

Open a desktop viewport and confirm the existing layout remains unchanged.

- [ ] **Step 3: Commit the focused fix**

Commit only the CSS change for the actual bug fix.

- [ ] **Step 4: Sync with the remote repository**

Reconcile the local branch with `origin/main` without discarding unrelated local work, then push the finished branch if repository state allows it.
